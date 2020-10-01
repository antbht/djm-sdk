
class UserNotFoundError(KeyError):
    """ Raised when using a user which is not existing.""" 

class BackendError(RuntimeError):
    """ Raised if calls to backend raises errors."""