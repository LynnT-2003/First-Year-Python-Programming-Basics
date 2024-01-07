def binary(x):
    n = len(str(x))
    temp = []
    _bin = []
    result = 0
    for i in range (n):
        temp.append(2 ** i)
        temp.sort(reverse = True)
    for each in str(x):
        each = int(each)
        _bin.append(each)
    for z in range (n):
        mul = temp[z] * _bin[z]
        result += mul
    return result

UInput = int(input("Enter a binary number: "))
denary = (binary(UInput))
print(denary)
