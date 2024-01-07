lst=list((input("Enter Words:").split()))
count=0

for c in lst:
    if c[0]==c[-1] or c[0]==c[-2] or c[1]==c[-1] or c[1]==c[-2]:
        count=count+1

print(f"Number of words that meet the requirements: {count}")
