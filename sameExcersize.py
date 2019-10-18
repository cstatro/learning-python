def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    elif array1.count(0) or array2.count(0):
        return False
    elif len(array1) is not 0 and len(array2) is not 0:
        val = all([any(x % i is 0 or i % x is 0 for x in array2)
                   for i in array1])
        return val
    else:
        return False


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [2]

comp(a, b)
