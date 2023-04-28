from typing import List

# Two values in the array called nums, that equal to the target
# Find a way to store the values
# Returns a list with the indexes of the values

def two_sum(nums: List[int], target: int) -> List[int]:
    values_dictionary = {}

    for current_index, current_value in enumerate(nums):
        # I iterate through every value
        # I check against each stored value against the current_value

        current_difference = target - current_value

        # Returns a list in the order of their indexes
        if current_difference in values_dictionary:
            return [values_dictionary[current_difference], current_index]

        # If we don't have a match == target, we can add/update this value in our dictionary
        values_dictionary[current_value] = current_index