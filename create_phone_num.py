"""
create ph no: ([1,2,3,4,5,6,7,8,9,0])
return (123) 456-7890
"""

def create_phone_num(list):
    #ph_no = '({}{}{}) {}{}{}-{}{}{}{}'.format(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],)
    ph_no = '({}{}{}) {}{}{}-{}{}{}{}'.format(*list)
    return ph_no
print(create_phone_num([1,2,3,4,5,6,7,8,9,0]))

"""
def my_sum(*num):           #num will be received as turple
    return sum(num)         #sum function is used to get sum in the turple

print(my_sum(1,2,3,4,5,6))  
"""
