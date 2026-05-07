def ubbi_dubbi(original_word: str) -> str:
    result_list = []
    for letter in original_word:
        if letter in "aeiou":
            result_list.append("ub")
        result_list.append(letter)
    return "".join(result_list)

def test(expected: str, arg: str) -> None:
    actual = ubbi_dubbi(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["wubatuber", "water"],
        ["trubuck", "truck"],
        ["cubat", "cat"],
        ["cubompubutuber", "computer"],
        ["pythubon", "python"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()

