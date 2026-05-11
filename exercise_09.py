# I'm not even bothering with typing in this file

def firstlast(sequence):
    return sequence[:1] + sequence[-1:]

def test(expected, arg):
    actual = firstlast(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main():
    tests = [
        [(1,3), (1,2,3)],
        [[1,3], [1,2,3]],
        ["ac", "abc"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()






