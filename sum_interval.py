"""
calculate length between them
sum_interval = [[1,4],[7,10],[3,5]]
"""

def sum_interval(interval_list):
    num_set = set()
    for start,stop in interval_list:  #unpacking the list[1,4] to 1 and 4
        for i in range(start,stop):
            num_set.add(i)
    return len(num_set)

print(sum_interval([[1,4],[7,10],[3,5]]))
