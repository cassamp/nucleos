# -*- coding:utf-8 -*-
from invoicexpress import api, errors, settings
import re
from xml.parsers.expat import ExpatError
import xml.sax.saxutils

import requests
import xmltodict

from requests import Request, Session
import logging

log = logging.getLogger(__name__)

### CONFIG ###


# enspired by http://stackoverflow.com/questions/30259452/proper-way-to-consume-data-from-restful-api-in-django
# def get_books(year, author):
#     url = 'http://api.example.com/books'
#     params = {'year': year, 'author': author}
#     r = requests.get('http://api.example.com/books', params)
#     books = r.json()
#     books_list = {'books':books['results']}

# xml = """<?xml version='1.0' encoding='utf-8'?>
# <a>б</a>"""
# headers = {'Content-Type': 'application/xml'} # set what your server accepts
# print requests.post('http://httpbin.org/post', data=xml, headers=headers).text

context = {
    'account_name': settings.ACCOUNT_NAME,
}


def get_keys(keys_list, obj):
    """
            Returns obj with keys_list 
            And obj with all other keys (if any)
    """

    new_obj = {}
    for key in keys_list:
        if key in obj:
            new_obj[key] = obj[key]
            del obj[key]

    return new_obj, obj


def tune_dict(method, xml_params):
    """
            Changes dict to conform Invoicexpress API 
    """
    # import pdb
    # pdb.set_trace()
    if 'items' in xml_params:
        if 'item' in xml_params['items']:
            if type(xml_params['items']['item']) == type([]):
                xml_params['items']['@type'] = 'array'

    if method == 'invoice-receipts.email-document':
        if 'body' in xml_params:
            xml_params['body'] = xml.sax.saxutils.escape(xml_params['body'])
    return xml_params


def ask_api(method, xml_params={}):
    """ this function will do all  requests 
            to Invocexpress API

    :param action: 			api call name (e.g. users.accouts , invoices.get)
    :param xml_params: 	params, that should specified in xml body long list of additional arguments;


    :returns:		API answer as python dict 
    """

    action = api.method[method]

    # find all params in brackets
    url = action['url']
    keys_in_url = re.findall('\{(.[^\}]+)\}', url)

    # sort parameters into 2 groups xml parameters
    # and url parameters
    addr_params, xml_params = get_keys(keys_in_url, xml_params)
    addr_params['account-name'] = settings.ACCOUNT_NAME

    # now compile urls using settings
    url = action['url'].format(**addr_params)

    out = []
    for key in xml_params.keys():
        if key[-2:] == '[]':
            out += [key+"="+x for x in xml_params.pop(key)]

    if len(out) > 0:
        url = url+'?'+'&'.join(out)

    if 'url_params' in action:
        url_params, xml_params = get_keys(action['url_params'], xml_params)
    else:
        url_params = {}

    headers = {'Content-Type': 'application/xml; charset=utf-8'}
    url_params['api_key'] = settings.API_KEY

    request_args = {}
    if xml_params != {}:

        if not ('root_tag_name' in action):
            raise errors.WrongParams('This call must have root_tag_name')

        # need to "tune" dict due to API
        xml_params = tune_dict(method, xml_params)
        # wrap xml_params in root_tag
        xml_params = {action['root_tag_name']: xml_params}
        request_args['data'] = xmltodict.unparse(xml_params).encode('utf8')

    print(url)
    print(headers)
    print(url_params)
    print(request_args)
    # TODO: use one session for many requests
    s = Session()
    req = Request(action['method'],
                  url=url,
                  headers=headers,
                  params=url_params,
                  **request_args
                  )
    prepared = req.prepare()
    # TODO: connection error handling
    resp = s.send(prepared)

    print(resp)

    if resp.status_code == 200 or resp.status_code == 201:
        try:
            out = xmltodict.parse(resp.text)
            if len(out.keys()) > 1:
                raise errors.ApiUnimplemented('Have more then 1 key')
            # out = out[out.keys()[0]]
        except ExpatError:
            out = resp.text
        return out
    elif resp.status_code == 202:
        return 202
    else:
        error_message = str(resp.status_code)+': '+resp.text

        if resp.status_code == 404:
            raise errors.Error404(error_message)
        else:
            raise errors.ApiCallError(error_message)


# TODO: remove items special handling
