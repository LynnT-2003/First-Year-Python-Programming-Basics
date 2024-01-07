#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

'NUMBER 3 IN PROGRESS'

data.sort(reverse=True)
seen = set()

#print out data using the first row
print(f"Semester {data[0][1]}/{data[0][0]}") #Latest semester of first year
print(f"{data[0][2]}\t({data[0][3]})\t{data[0][4]}") #Course code, section and grade
seen.add(str(data[0][0]) + str(data[0][1])) #Latest semester of first year added to seen

#print out data starting from second row
for i in range(1,len(data)):
    temp = str(data[i][0]) + str(data[i][1])
    if temp not in seen: 
        seen.add(temp) #Add semester of the year to seen...
        print (f"\nSemester {temp[4:5]}/{temp[0:4]}") #... so that a semester of a year will only be printed once
    print(f"{data[i][2]}\t({data[i][3]})\t{data[i][4]}") #Course code, section and grade



        
    
