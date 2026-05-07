def strsort(unsorted: str) -> str:
    result_list = []
    for letter in unsorted:
        if len(result_list) == 0:
            result_list.append(letter)
        else:
            for i, ch in enumerate(result_list):
                if ord(letter) <= ord(ch):
                    result_list.insert(i, letter)
                    break
                elif i == len(result_list)-1:
                    result_list.append(letter)
                    break
    return "".join(result_list)

def test(expected: str, arg: str) -> None:
    actual = strsort(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["".join(sorted("water")), "water"],
        ["".join(sorted("truck")), "truck"],
        ["".join(sorted("computer")), "computer"],
        ["".join(sorted("python")), "python"],
        ["".join(sorted("dictionary")), "dictionary"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()


