def removeDup(lst):
    noDupli = []
    seen = set()

    for each in lst:
        if each not in seen:
            seen.add(each)
            noDupli.append(each)
    return noDupli

def keep1Dup(lst):
    oneDupli = []
    seen1 = set()
    seen2 = set()

    for each in lst:
        if each not in seen1:
            seen1.add(each)
            oneDupli.append(each)
        elif each in seen1:
            if each not in seen2:
                oneDupli.append(each)
                seen2.add(each)
    return oneDupli

li = [1,1,3,5,4,5,5,9,4,8,6]
print(removeDup(li))
print(keep1Dup(li))            
    

