def SplitType(numlist):
    output_splittype = [[],[]]
    for each in numlist:
        if isinstance(each,int) == True:
            output_splittype[0].append(each)
        elif isinstance (each,float) == True:
            output_splittype[1].append(each)
    return output_splittype

def KeepTwoDup(numlist):
    newli= []
    seen = set()
    seen2 = set()
    for item in numlist:
        if item not in seen:
            seen.add(item)
            newli.append(item)
        elif item in seen:
            if item not in seen2:
                seen2.add(item)
                newli.append(item)
    return newli

outlist = []
def ListofOdd(numlist): 
    if len(numlist) == 1:
        if numlist[0] % 2 != 0:
            outlist.append(numlist[0])
            return outlist
        else:
            return outlist
    else:
        if numlist[0] % 2 != 0:
            outlist.append(numlist[0])
            return ListofOdd(numlist[1:])
        else:
            return ListofOdd(numlist[1:])

'''print (KeepTwoDup([1,2,2,2,3,4,5,5,5,1,2,3,3]))

outlist = []
print (ListofOdd([1,2,2,2,3,4,5,5,5,1,2,3,3]))

print (SplitType([1,2,3,1.1,1.2,1.3]))'''
