def new_decorator(func):

    def wrap_func():
        print("This is the First code to run.")

        func()

        print("This is the code that runs after the func() is executed")

    return wrap_func

@new_decorator
def func_needs_dec():
    print("Please use this to decorate !!")

# ================= IF WE DON'T USE A DECORATOR ===========
# func_dec = new_decorator(func_needs_dec)
# func_dec()

# =================== IF WE USE A DECORATOR ================
func_needs_dec()
