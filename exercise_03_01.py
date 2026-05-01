def convert_num(start: float, before: int, after: int) -> float:
    # Parse out the value before the decimal point.
    start_int = int(start)
    result_int = start_int % pow(10, before)

    # Parse out the value after the decimal point.
    start_decimal = start - start_int
    result_decimal = int(start_decimal * pow(10, after)) / pow(10, after)

    return result_int + result_decimal

def test(expected: float, start: float, before: int, after: int) -> None:
    actual = convert_num(start, before, after)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        [34.567, 1234.5678, 2, 3]
    ]
    for test_set in tests:
        test(test_set[0], test_set[1], test_set[2], test_set[3])

if __name__ == "__main__":
    main()
