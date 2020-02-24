#
 

# error during call
class ApiCallError(Exception):
	pass

class ApiUninmplemented(Exception):
	pass

class WrongParams(Exception):
	pass

#need this class, as Not found are used during searching
class Error404(ApiCallError):
	pass