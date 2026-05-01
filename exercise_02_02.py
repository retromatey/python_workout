from statistics import mean

def avg(num_list):
    result = 0
    total = 0
    for num in num_list:
        total += num
    result = total / len(num_list)
    return result

def compare(num_list):
    lib_result = mean(num_list)
    my_result = avg(num_list)
    correct = lib_result == my_result
    print(f"Expected: {lib_result}, Actual: {my_result}, Pass? {correct}")

compare([1,2,3,4])
compare([2,4,6,8])
