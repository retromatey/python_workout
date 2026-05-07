def last_word(filename: str) -> str:
    result = ""

    with open(filename, "r", encoding="utf-8") as file:
        words = []
        line = file.readline()
        while line != "":
            for word in line.split():
                words.append(word)
            line = file.readline()
        result = sorted(words)[-1]

    return result

def test(expected: str, arg: str) -> None:
    actual = last_word(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["you", "sample.txt"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()




