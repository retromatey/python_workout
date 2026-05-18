
def main() -> None:
    unsorted_list = [-1, -2, -3, 3,2,1]
    sorted_list = sorted(unsorted_list, key=lambda x: abs(x))
    print(sorted_list)

if __name__ == "__main__":
    main()
