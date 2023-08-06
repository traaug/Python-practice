def high_low(str):
    int_list = [int(str) for str in str.split()]
    return max(int_list),min(int_list)

max_num, min_num = high_low("1 2 3 4 5")
print("max num:",max_num)
print("mini num:",min_num)
