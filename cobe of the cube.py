def cube(number):
    return number**3
def bythree(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(bythree(4))
print(bythree(12))