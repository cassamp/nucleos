# -*-  coding:utf-8 -*-

import unittest
import uuid
import importlib
from . import errors
from . import helpers
from .services import ask_api


class ClientsApi(unittest.TestCase):
    def test_crud(self):

        result = ask_api('clients.create', {
            'name': 'Pedro',
            'code': uuid.uuid4(),
        })
        self.assertTrue('name' in result)
        self.assertEqual('Pedro', result['name'])

        new_user_id = result['id']
        print(new_user_id)

        # Listing all users
        result = ask_api('clients.list', {
            'per_page': 50,
        })
        print(result)
        self.assertTrue('client' in result)

        # search for new user
        # find_it = False
        # for u in result['clients']['client']:
        # 	print u['id']
        # 	if u['id'] == new_user_id:
        # 		find_it = True
        # self.assertTrue ( find_it )

        # updating user
        result = ask_api('clients.update', {
            'name': "Adam",
            'client-id': new_user_id,
        },
        )

        print("Update result: ", result)

        # searching for new

        # for u in result['clients']['client']:
        # print "ID: {id}, Name: {name}, Code: {code}".format(**u)


class InvoiceReceiptsApi(unittest.TestCase):
    def test_crud(self):
        # imitate error 422
        with self.assertRaises(errors.ApiCallError):

            result = ask_api('invoice-receipts.create', {
                'date': '01/01/2014',
                'due_date': '01/02/2014',
                            'client': {
                                'name': 'Ricardo Pereira',
                                'code': 100,
                            },
                'items': {'item': [
                    {
                        'name': 'Product 1',
                        'description': "Cleaning product",
                        'unit_price': 12.0,
                        'quantity': 2.0,
                    },
                    {
                        'name': 'Product 2',
                        'description': "Beauty product",
                        'unit_price': 123.0,
                        'quantity': 'bla bla',
                    },
                ]},


            })
        # now get normall call
        result = ask_api('invoice-receipts.create', {
            'date': '01/01/2014',
            'due_date': '01/02/2014',
            'client': {
                    'name': 'Ricardo Pereira',
                        'code': 100,
            },
            'items': {'item': [
                {
                    'name': 'Product 1',
                    'description': "Cleaning product",
                    'unit_price': 12.0,
                    'quantity': 2.0,
                },
                {
                    'name': 'Product 2',
                    'description': "Beauty product",
                    'unit_price': 123.0,
                    'quantity': 1.0,
                },
            ]},


        })
        print('ID:', result['id'])
        print('Link:', result['permalink'])

        one_receipt = ask_api('invoice-receipts.get', {
            'invoice-receipt-id': result['id']
        })

        self.assertEqual(one_receipt['permalink'], result['permalink'])
        print('Getted: ', one_receipt['permalink'])

        res = ask_api('invoice-receipts.update', {
            'invoice-receipt-id': one_receipt['id'],
            'due_date': one_receipt['due_date'],
            'date': one_receipt['date'],
            'client': {
                'name': 'Ricardo Ferrera',
                'code': '122'
            },
            'items': one_receipt['items']
        })
        print(res)

    def test_pdf_email(self):
        # list all and print

        result = ask_api('invoice-receipts.list', {
            'per_page': 7,
            'page': 1
        })

        print("Current page:", result['current_page'])
        for r in result['invoice_receipt']:
            print(
                'Id: {} Client: {}'.format(r['id'], r['client']['name'])
            )

        a, b = result['invoice_receipt'][0], result['invoice_receipt'][1]

        # make finalize
        with self.assertRaises(errors.ApiCallError):
            result = ask_api('invoice-receipts.change-state', {
                'invoice-receipt-id': a['id'],
                'state': 'cancelled',
            })

        with self.assertRaises(errors.ApiCallError):
            result = ask_api('invoice-receipts.email-document', {
                'invoice-receipt-id': b['id'],

                'client': {
                    'email': '???',
                    'save': 0,
                },

                'subject': 'The Html Letter',
                'body': 'This <b>is Plain</b> text'
            })

        result = ask_api('invoice-receipts.related_documents', {
            'invoice-receipt-id': a['id']

        })
        print(result)


class InvoiceReceiptsGeneratepdf(unittest.TestCase):
    def test_generate_pdf(self):
        result = ask_api('invoice-receipts.list', {
            'per_page': 7,
            'page': 1
        })
        print(result['invoice_receipt'][3]['id'])
        # print result
        while True:
            result = ask_api('invoice-receipts.pdf', {
                'invoice-receipt-id': result['invoice_receipt'][3]['id'],
            })
            if (result != 202):
                break

        print(result['pdfUrl'])

        # res = ask_api('invoice-receipts.create',{
  #           'date': '25/02/2016',
  #           'due_date': '25/02/2016',
  #           'client' : {
  #               'name' : 'bla-bal',
  #               'code' : 2333,
  #           },
  #           'items': { 'item' : [
  #           	{
  #           		'quantity': 1,
  #           		'description': u"Revista do Instituto do Direito Brasileiro, Vol. 3 (2014), No. 4, 2449-2521",
  #           		'unit_price': 4.00,
  #           		'name': u"Как дела",
  #           	},
  #           ]},
  #       })


create_array_good = {
    'date': '01/01/2014',
    'due_date': '01/02/2014',
    'client': {
            'name': 'Ricardo Pereira',
                'code': 100,
    },
    'items': {'item': [
        {
            'name': 'Product 1',
            'description': "Cleaning product",
            'unit_price': 12.0,
            'quantity': 2.0,
        },
        {
            'name': 'Product 2',
            'description': "Beauty product",
            'unit_price': 123.0,
            'quantity': 5,
        },
    ]}
}

create_array_bad = {
    'date': '01/01/2014',
    'due_date': '01/02/2014',
    'client': {
            'name': 'Ricardo Pereira',
                'code': 100,
    },
    'items': {'item': [
        {
            'name': 'Product 1',
            'description': "Cleaning product",
            'unit_price': 12.0,
            'quantity': 2.0,
        },
        {
            'name': 'Product 2',
            'description': "Beauty product",
            'unit_price': 123.0,
            'quantity': 'bla bla',
        },
    ]},
}


class Invoices(unittest.TestCase):
    def test_create_get(self):

        with self.assertRaises(errors.ApiCallError):
            result = ask_api('invoices.create', create_array_bad)

        result = ask_api('invoices.create', create_array_good)

        print(result['permalink'])

        self.assertTrue('permalink' in result)

        result = ask_api('invoices.get', {
            'invoice-id': result['id'],
        })
        self.assertTrue('permalink' in result)

        print(result['permalink'])

        res = ask_api('invoices.update', {
            'invoice-id': result['id'],
            'due_date': result['due_date'],
            'date': result['date'],
            'client': {
                'name': 'Ricardo Ferrera',
                'code': '122'
            },
            'items': result['items']
        })
        print(res)


class InvoicesList(unittest.TestCase):

    def test_list(self):
        res = ask_api('invoices.list', {
            'status[]': ['settled', 'draft'],
            'type[]': ['Invoice', ],
            'non_archived': True}
        )

        if 'invoice' in res:
            for inv in res['invoice']:
                print("{type} : {status} : {permalink}"
                      .format(**inv))
        else:
            print(res)

        with self.assertRaises(errors.Error404):
            result = ask_api('invoices.change-state', {
                'invoice-id': 0000000,
                'state': 'cancelled',
            })


class InvoiceReceiptsHelper(unittest.TestCase):
    def test_helper(self):
        inv_list = helpers.InvoiceReceipts(10)
        print(inv_list[:10])
        print(inv_list[10:20])


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(InvoiceReceiptsGeneratepdf)
    unittest.TextTestRunner(verbosity=2).run(suite)
# unittest.main()
