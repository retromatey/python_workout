PEOPLE = [
    {"first":"Reuven", "last":"Lerner", "email":"reuven@lerner.co.il"},
    {"first":"Melania", "last":"Trump", "email":"flotus@whitehouse.gov"},
    {"first":"Donald", "last":"Trump", "email":"president@whitehouse.gov"},
    {"first":"Vladimir", "last":"Putin", "email":"president@kremvax.ru"},
]

def alphabetize_names():
    PEOPLE.sort(key=lambda x: [x["last"], x["first"]])
    return PEOPLE

def main():
    sorted_list = alphabetize_names()
    print(sorted_list)

if __name__ == "__main__":
    main()


