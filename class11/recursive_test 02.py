def list_sum(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + list_sum(num_list[1:])

List = [1,2,3,4]
print (list_sum(List))

