class SimpleExample:
    """A simple example class"""
    max = 256

    def message(self):
        return 'Hello, Classes!'

# Driver
simpleObj = SimpleExample() # make a class object
print(simpleObj.max)        # access class definition
print(simpleObj.message())  # call class method

del simpleObj               # clean up objects by deletion
