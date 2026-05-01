from decimal import Decimal, InvalidOperation

def get_decimal_input(prompt: str) -> Decimal:
    result = Decimal(0.0)
    while True:
        try:
            num_str = input(f"{prompt}: ")
            result = Decimal(num_str)
            break
        except InvalidOperation:
            pass
    return result

def sum_nums() -> None:
    x = get_decimal_input("Enter the first number")
    y = get_decimal_input("Enter the second number")
    result = x + y
    print(f"{x} + {y} = {result}")

def main() -> None:
    sum_nums()

if __name__ == "__main__":
    main()
