import MyOwnFunctions as MyFuncs

numlist = [1,2,2,2,3,4,5,5,5,1,2,3,3,1.1,1.2,1.3,4]

print (f"Split list into integers and float:\n{MyFuncs.SplitType(numlist)}\n")
print (f"Keep two duplicates:\n{MyFuncs.KeepTwoDup(numlist)}\n")

int_only = MyFuncs.SplitType(numlist)[0]
print (f"Odd numbers only list (using recursive function):\n{MyFuncs.ListofOdd(int_only)}")
