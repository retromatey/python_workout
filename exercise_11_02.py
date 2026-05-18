
sample_str = [
    "This tutorial introduces the reader informally to the basic concepts and", 
    "features of the Python language and system. Be aware that it expects you to", 
    "have a basic understanding of programming in general.  It helps to have a", 
    "Python interpreter handy for hands-on experience, but all examples are", 
    "self-contained, so the tutorial can be read off- line as well.", 
]

def custom_length(word: str) -> int:
    count = 0
    for char in word:
        if char in "aeiou":
            count += 1
    return count

def sort_by_vowels(unsorted_str: str, desc: bool = True) -> list[str]:
    result = sorted(unsorted_str.split(" "), key=custom_length)
    if desc:
        result.reverse()
    return result

def main() -> None:
    for unsorted_str in sample_str:
        result = sort_by_vowels(unsorted_str)
        print(result)

if __name__ == "__main__":
    main()
