def str_stats(str_list):
    result = (0,0,0)
    shortest = len(str_list[0])
    longest = 0
    total = 0
    avg = 0
    for text in str_list:
        length = len(text)
        shortest = length if length < shortest else shortest
        longest = length if length > longest else longest
        total += length
    avg = round(total / len(str_list), 2)
    result = (shortest, longest, avg)
    return result

def test(str_list, expected):
    actual = str_stats(str_list)
    correct = actual[0] == expected[0] and \
              actual[1] == expected[1] and \
              actual[2] == expected[2]
    print(f"Expected: {expected}, Actual: {actual}, Pass {correct}")

test(["one", "two", "three"], (3, 5, round(11/3, 2)))
