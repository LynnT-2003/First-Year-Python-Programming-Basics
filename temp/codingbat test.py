def front_back(str):
  List = []
  for each in str:
    List.append(each)
  n = len(List)-1
  for i in range (n, -1, -1):
    return List[i]

print (front_back('chocolate'))
