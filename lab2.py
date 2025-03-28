import time
import random

# Function to calculate average execution time
def time_average(func, iterations=50):
    time_list = []
    for _ in range(iterations):
        test_time = func()
        time_list.append(test_time)
    average_time = sum(time_list) / len(time_list)
    return average_time

# Add 1 number to the beginning of a list that already has 10 numbers in it
def add_one_to_ten():
    data = list(range(10))
    start = time.perf_counter()
    data.insert(0, 9)
    end = time.perf_counter()
    return (end - start) * 1e6

# Add 1 number to the beginning of a list that already has 1,000,000 numbers in it
def add_one_to_million():
    data = list(range(1_000_000))
    start = time.perf_counter()
    data.insert(0, 9)
    end = time.perf_counter()
    return (end - start) * 1e6

# Add 1 number to the end of a list that already has 10 numbers in it
def add_one_to_end_ten():
    data = list(range(10))
    start = time.perf_counter()
    data.append(9)
    end = time.perf_counter()
    return (end - start) * 1e6

# Add 1 number to the end of a list that already has 1,000,000 numbers in it
def add_one_to_end_million():
    data = list(range(1_000_000))
    start = time.perf_counter()
    data.append(9)
    end = time.perf_counter()
    return (end - start) * 1e6

# Remove 1 number from the beginning of a list that already has 10 numbers in it
def remove_one_from_start_ten():
    data = list(range(10))
    start = time.perf_counter()
    data.pop(0)
    end = time.perf_counter()
    return (end - start) * 1e6

# Remove 1 number from the beginning of a list that already has 1,000,000 numbers in it
def remove_one_from_start_million():
    data = list(range(1_000_000))
    start = time.perf_counter()
    data.pop(0)
    end = time.perf_counter()
    return (end - start) * 1e6

# Remove 1 number from the end of a list that already has 10 numbers in it
def remove_one_from_end_ten():
    data = list(range(10))
    start = time.perf_counter()
    data.pop()
    end = time.perf_counter()
    return (end - start) * 1e6

# Remove 1 number from the end of a list that already has 1,000,000 numbers in it
def remove_one_from_end_million():
    data = list(range(1_000_000))
    start = time.perf_counter()
    data.pop()
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a number in a list of 10 numbers (present)
def check_presence_ten_present():
    data = list(range(10))
    start = time.perf_counter()
    5 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a number in a list of 1,000,000 numbers (present)
def check_presence_million_present():
    data = list(range(1_000_000))
    start = time.perf_counter()
    500_000 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a number in a list of 10 numbers (absent)
def check_presence_ten_absent():
    data = list(range(10))
    start = time.perf_counter()
    -1 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a number in a list of 1,000,000 numbers (absent)
def check_presence_million_absent():
    data = list(range(1_000_000))
    start = time.perf_counter()
    -1 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a key in a dict of 10 key-value pairs (present)
def check_dict_ten_present():
    data = {i: i for i in range(10)}
    start = time.perf_counter()
    5 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a key in a dict of 1,000,000 key-value pairs (present)
def check_dict_million_present():
    data = {i: i for i in range(1_000_000)}
    start = time.perf_counter()
    500_000 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a key in a dict of 10 key-value pairs (absent)
def check_dict_ten_absent():
    data = {i: i for i in range(10)}
    start = time.perf_counter()
    -1 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Check for presence of a key in a dict of 1,000,000 key-value pairs (absent)
def check_dict_million_absent():
    data = {i: i for i in range(1_000_000)}
    start = time.perf_counter()
    -1 in data
    end = time.perf_counter()
    return (end - start) * 1e6

# Call all functions and display average results
if __name__ == "__main__":
    print(time_average(add_one_to_ten))
    print(time_average(add_one_to_million))
    print(time_average(add_one_to_end_ten))
    print(time_average(add_one_to_end_million))
    print(time_average(remove_one_from_start_ten))
    print(time_average(remove_one_from_start_million))
    print(time_average(remove_one_from_end_ten))
    print(time_average(remove_one_from_end_million))
    print(time_average(check_presence_ten_present))
    print(time_average(check_presence_million_present))
    print(time_average(check_presence_ten_absent))
    print(time_average(check_presence_million_absent))
    print(time_average(check_dict_ten_present))
    print(time_average(check_dict_million_present))
    print(time_average(check_dict_ten_absent))
    print(time_average(check_dict_million_absent))
