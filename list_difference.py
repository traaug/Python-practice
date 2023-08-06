"""
array_diff([1,2],[1]) == [2]
array_diff([1,2,2,2,3],[2]) == [1,3]
array_diff([1,2,2],[]) == [1,2,2]
"""

def list_difference(list1,list2):
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    return result
print(list_difference([1,2],[1]))
