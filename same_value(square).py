"""
compare the lists and see if
[a2,b2] = [a,b] regardless of order
"""

def comp(list1,list2):
    squared_list = {x ** 2 for x in list1}    #it is a set()
    if set(list2) == squared_list:
        print("it is true")
    else:
        print("it is false")
    #return comp()

comp([1,3,2],[1,4,9])
