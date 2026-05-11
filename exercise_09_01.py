def even_odd_sums(sequence):
    evens = sum(sequence[::2])
    odds = sum(sequence[1::2])
    return [evens, odds]

def test(expected, arg):
    actual = even_odd_sums(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main():
    tests = [
        [[90, 120], [10, 20, 30, 40, 50, 60]],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()
