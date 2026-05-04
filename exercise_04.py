def hex_output(hex_val: str) -> int:
    total = 0
    for i, x in enumerate(reversed(hex_val)):
        total += (16 ** i) * int(x, 16)
    return total

def test(expected: int, arg: str) -> None:
    actual = hex_output(arg)
    result = actual == expected
    print(f"Expected: {expected}, Actual: {actual}, Pass: {result}")

def main() -> None:
    tests = [
        [int(0x0),   "0"],
        [int(0x1),   "1"],
        [int(0xa),   "a"],
        [int(0xb),   "b"],
        [int(0x10), "10"],
        [int(0x11), "11"],
        [int(0x19), "19"],
    ]
    for test_set in tests:
        test(test_set[0], test_set[1])

if __name__ == "__main__":
    main()
