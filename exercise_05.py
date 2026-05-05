def pig_latin(word: str) -> str:
    first_letter = word[0]
    if first_letter in "aeiou":
        return f"{word}way"
    return f"{word[1:]}{first_letter}ay"

def test(expected: str, arg: str) -> None:
    actual = pig_latin(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["appleway", "apple"],
        ["ananabay", "banana"],
        ["rucktay", "truck"],
        ["omputercay", "computer"],
        ["iglooway", "igloo"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()
