# =================== RETURNING A FUNCTION =============
def Hello(name = 'Jose'):
    print("Hello from main!!")

    def greet():
        return "This is the greet function!!"

    def welcome():
        return "This is the welcome function!!"

    # print(greet())
    # print(welcome())

    if name == 'Jose':
        return greet
    else:
        return welcome


x = Hello(name = 'Sam')
print(x())

# ===================== PASSING A FUNCTION AS AN ARGUMWNT ================

def hello():
    return "Hello from Jose!!"

def other(func):
    print("Hello FUNC")
    # Passing the function here
    print(func())

other(hello)
