def nonsense(filename: str) -> str:
    line_num = 0
    word_list = []
    max_line = 10
    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline()
        while line != "" and line_num < max_line:
            line = line.strip()
            if line != "": # ignoring blank lines
                words = line.split()
                if len(words) > line_num:
                    word_list.append(words[line_num])
                line_num += 1
            line = file.readline()
    return " ".join(word_list)

def test(expected: str, arg: str) -> None:
    actual = nonsense(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        ["Python high-level object-oriented with rapid standard all pointers",
         "sample.txt"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()
