def checkauth(callback): # decorator function
    def inner_function(): 
        # write code to extend the behavior of some_function()
        print('we check his email')
        callback() # call some_function
        # write code to extend the behavior of some_function()

    return inner_function # return a wrapper function

@checkauth
def printUser():
    print('Todo something with user')

printUser()
