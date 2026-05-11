def plus_minus(sequence):
    result = 0
    for i, val in enumerate(sequence):
        if i == 0:
            result = val
        elif i % 2 == 0:
            result -= val
        else:
            result += val
    return result

def test(expected, arg):
    actual = plus_minus(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main():
    tests = [
        [50, [10, 20, 30, 40, 50, 60]],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()

