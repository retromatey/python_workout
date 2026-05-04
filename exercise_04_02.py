def name_triangle(name: str) -> None:
    line = ""
    for ch in name:
        line += ch
        print(line)

def main() -> None:
    tests = [
        "Harry",
        "Ronald",
        "Draco",
        "Hermione",
        "Voldemort",
    ]
    for test_set in tests:
        name_triangle(test_set)

if __name__ == "__main__":
    main()
