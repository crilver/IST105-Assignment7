import sys
import re

# Assignment 7 - Cristobal Lara
a = sys.argv[1]
b = sys.argv[2]

int_list = a.split(',')
threshold = int(b)

def is_integer_regex(input):
    return bool(re.match(r'^-?\d+$', str(input)))

def all_entries_are_numbers(entryList):
    for val in entryList:
        if not is_integer_regex(val):
            return False
    return True

def bitwise_and(nums):
    result = nums[0]
    for num in nums[1:]:
        result &= num
    return result

def bitwise_or(nums):
    result = nums[0]
    for num in nums[1:]:
        result |= num
    return result

def bitwise_xor(nums):
    result = nums[0]
    for num in nums[1:]:
        result ^= num
    return result

def list_greater_than(nums, threshold):
    new_list = []
    for num in nums:
        if num > threshold:
            new_list.append(num)
    return new_list

if not all_entries_are_numbers(int_list):
    print("<h2>Error: All values in the list must be integers</h2>")
else:
    print(f"<h2>Integers separated by commas: {int_list}</h2>")
    print(f"<h2>Threshold: {threshold}</h2>")
    int_list = list(map(int, int_list))
    and_result = bitwise_and(int_list)
    or_result = bitwise_or(int_list)
    xor_result = bitwise_xor(int_list)
    print("<br>")
    print(f"<h2>Bitwise AND: {and_result}</h2>")
    print(f"<h2>Bitwise OR: {or_result}</h2>")
    print(f"<h2>Bitwise XOR: {xor_result}</h2>")
    filtered_list = list_greater_than(int_list, threshold)
    print(f"<h2>Numbers greater than threshold: {filtered_list}</h2>")