def run_time() -> None:
    times: list[float] = []
    end = False

    while not end:
        time_str = input("Enter 10 km run time: ")
        if time_str.isdigit():
            times.append(float(time_str))
        elif time_str == "":
            end = True
    
    times_len = len(times)
    total = sum(times)
    avg = total / times_len
    print(f"Average of {avg:.2f}, over {times_len} runs")

def test() -> None:
    run_time()

if __name__ == "__main__":
    test()
