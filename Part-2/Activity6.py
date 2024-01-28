def fac(no):
    result = 1
    while no >= 1:
        result = result * no
        no = no - 1
    return result

print(fac(5))