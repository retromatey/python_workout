def my_sum(*args):
    if not args:
        return args
    output = args[0]
    for arg in args[1:]:
        output += arg
    return output

def test(expected, *args):
    actual = my_sum(*args)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main():
    tests = [
        [(), ()],
        ["abc", ["a", "b", "c"]],
        ["abcdef", ["abc", "def"]],
        [[1,2,3,4,5,6], [[1,2,3], [4,5,6]]],
        [6, [1, 2, 3]],
    ]
    for test_set in tests:
        test(test_set[0], *test_set[1])

if __name__ == "__main__":
    main()

