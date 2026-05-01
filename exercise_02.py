# https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

# Note that the types of the args tuple don't have to be the same.
# How does mypy treat this?
def mysum(*args):
    result = 0
    for x in args:
        result += x
    return result


total = mysum(1, 2, 3)
real_total = sum([1, 2, 3])
print(f"total should be {real_total} - {total} - {total == real_total}")

print("==================================================================")

print("Here's a neat trick, we'll prefix the list with * to pass all the")
print("elements to the function.")

total = mysum(*[1,2,3]) # prefixing the list with "*"
real_total = sum([1, 2, 3])
print(f"total should be {real_total} - {total} - {total == real_total}")
