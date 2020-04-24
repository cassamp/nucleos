Installation
****************

1. Clone repository with 

.. code-block:: shell

    git clone https://github.com/blook-io/python-invoicexpress.git invoicexpress

2. somewhere in your project settings (or Django settings)

.. code-block:: python

    import invoicexpress.settings
    invoicexpress.settings.ACCOUNT_NAME = 'xxxxxxxxx'
    invoicexpress.settings.API_KEY = 'xxxxxxxxxxxxxxxxxxxxx'

3. Use it.

.. code-block:: python

    from invoicexpress.services import ask_api

    result = ask_api( ... )


