# def find_duplicate(nums):
#     # """
#     # This function finds the first duplicate number in a list of integers.
#     # If no duplicates are found, it returns None.
    
#     # :param nums: List of integers
#     # :return: The first duplicate integer or None if no duplicates exist
#     # """
#     # seen = set()
#     # for num in nums:
#     #     if num in seen:
#     #         return num
#     #     seen.add(num)
#     # return None

def find_duplicates(nums):
    frequency = {}
    result = []

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    for key in frequency:
        if frequency[key] > 1:
            result.append(key)

    return result

print(find_duplicates([1, 2, 3, 2, 3, 4, 5, 1]))

    