from .services import ask_api
from  . import errors

# import pdb
class InvoiceReceipts(list):
    """InvoiceReceipts list for Paginated ! output"""
    def __init__(self, paginate_by):
        super(InvoiceReceipts, self).__init__()
        self.paginate_by = paginate_by

        # now getting total count
        res = ask_api('invoice-receipts.list',{
            'page': '1',
            })
        self.total_entries = int(res['total_entries'])

    def __len__(self):
        return self.total_entries

    def __getitem__(self,key):
        """ here we making paginated access """
        # pdb.set_trace()
        if isinstance(key, slice):
            if key.start%self.paginate_by != 0 or (key.stop-key.start) > self.paginate_by :
                raise errors.ApiUninmplemented('Sorry, accessing not by page not Implemented')

            res = ask_api('invoice-receipts.list',{
                'page': key.start/self.paginate_by + 1,
                'per_page': self.paginate_by,
            })
            return res['invoice_receipt']
        else :
            raise errors.ApiUninmplemented("Sorry, accessing not by slice not Implemented")

    def __getslice__(self,i,j):
        return self.__getitem__(slice(i,j))
        
        