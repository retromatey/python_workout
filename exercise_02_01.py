
def mysum(*args, start=0):
    result = start
    for x in args:
        result += x
    return result


total = mysum(1, 2, 3, start=10)
real_total = sum([1, 2, 3], 10)
print(f"total should be {real_total} - {total} - {total == real_total}")
