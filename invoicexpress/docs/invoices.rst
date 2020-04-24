Invoices 
----------------

API Docs: https://invoicexpress.com/api/invoices/create

Please see :doc:`invoice-receipt` for usage examples of:

 - invoices.create
 - invoices.get
 - invoices.update

invoices.list
*************

Note that for parameters with *[]* (like *type[]*) you should provide *list*

Usage:

.. code-block:: python 

	res = ask_api('invoices.list',{
		'status[]': [ 'settled', 'draft' ],
		'type[]' : [ 'Invoice', 'InvoiceReceipt'], 
		'non_archived':True}
	)

	if 'invoice' in res:
		for inv in res['invoice'] :
			print ("{type} : {status} : {permalink}"
				.format ( **inv))
	else : print (res)










