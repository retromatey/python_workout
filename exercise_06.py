def pl_sentence(words: str) -> str:
    pl_words = []
    for word in words.split():
        pl_words.append(pig_latin(word))
    return " ".join(pl_words)

def pig_latin(word: str) -> str:
    first_letter = word[0]
    if first_letter in "aeiou":
        return f"{word}way"
    return f"{word[1:]}{first_letter}ay"

def test(expected: str, arg: str) -> None:
    actual = pl_sentence(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["ellohay orldway", "hello world"],
        ["erehay areway omesay ordsway", "here are some words"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()

