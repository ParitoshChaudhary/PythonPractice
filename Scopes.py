# x = 'outside'
#
# def report():
#     x = 'inside'
#     return x
#
# print(report())
# print(x)

# =================== LEGB =======================

x = 'THIS IS THE GLOBAL LEVEL'

# def enclosing():
#     # x = 'THHIS IS THE ENCLOSING LEVEL'
#     # LEGB
#     def inside():
#         # x = 'THIS IS THE LOCAL LEVEL'
#         print(x)
#
#     inside()
# enclosing()

# ====================== FOR GLOBL USE ===================

x = 'outside'

def report():
    # GRAB THE LOCAL LEVEL x VARIABLE !!
    global x
    # REASSIGN THE x VALUE
    x = 'inside'
    return x

print(report())
print(x)
