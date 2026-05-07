def sort_words(unsorted: str) -> str:
    return ",".join(sorted(unsorted.split()))

def test(expected: str, arg: str) -> None:
    actual = sort_words(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["one,two,three", "three two one"],
        ["apple,banana,orange", "banana orange apple"],
        ["car,motorcycle,truck", "motorcycle car truck"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()



