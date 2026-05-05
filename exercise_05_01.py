def pig_latin(word: str) -> str:
    translated = ""
    
    sanitized = word
    first_letter = word[0]
    is_upper = first_letter.isupper()
    has_punc = not word[-1].isalpha()

    if is_upper:
        first_letter = first_letter.lower()
    
    if has_punc:
        sanitized = sanitized[:-1]
    
    if first_letter in "aeiou":
        translated = f"{sanitized}way"
    else:
        translated = f"{sanitized[1:]}{first_letter}ay"

    if is_upper:
        translated = f"{translated[0].upper()}{translated[1:]}"

    if has_punc:
        translated = f"{translated}{word[-1]}"

    return translated

def test(expected: str, arg: str) -> None:
    actual = pig_latin(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["appleway", "apple"],
        ["Appleway", "Apple"],
        ["appleway.", "apple."],
        ["Appleway.", "Apple."],
        ["ananabay", "banana"],
        ["Ananabay", "Banana"],
        ["ananabay.", "banana."],
        ["Ananabay.", "Banana."],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()

