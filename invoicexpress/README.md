python-invocexpress -  Python wrapper over Invocexpress (https://invoicexpress.com) API

Installation
------------------

Clone repository with 
```shell
    git clone https://github.com/blook-io/python-invoicexpress.git invoicexpress
```

Somewhere in your project settings (or Django settings)
```python
    import invoicexpress.settings
    invoicexpress.settings.ACCOUNT_NAME = 'xxxxxxxxx'
    invoicexpress.settings.API_KEY = 'xxxxxxxxxxxxxxxxxxxxx'
```

Use it.
```python
    from invoicexpress.services import ask_api

    result = ask_api( ... )
```

Docs
------------------
http://python-invoicexpress.readthedocs.org/en/latest/



