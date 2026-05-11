def my_zip(seq1, seq2):
    return [(seq1[x], seq2[x]) for x in range(0, len(seq1))]

def test(expected, arg1, arg2):
    actual = my_zip(arg1, arg2)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main():
    tests = [
        [[(10, "a"), (20, "b"), (30, "c")], [10, 20, 30], "abc"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1], test_set[2])

if __name__ == "__main__":
    main()


