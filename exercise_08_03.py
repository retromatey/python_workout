def longest_word(filename: str) -> str:
    longest = ""

    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline()
        while line != "":
            for word in line.split():
                if len(word) > len(longest):
                    longest = word
            line = file.readline()

    return longest

def test(expected: str, arg: str) -> None:
    actual = longest_word(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["xxx", "sample.txt"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()





