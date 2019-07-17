class MyCustomException(Exception):
    def __init__(self, errors):
        #self.errors = errors


try:
    raise (MyCustomException(10))
except MyCustomException as errors:
    print('A New Exception occurred:', errors)

'''

class MyCustomException(Exception):

    def __init__(self, message, errors):

    super().__init__(message)
        self.errors = errors

'''
