def positive_sum(arr):
    if arr:
        sorted_nums = [x for x in arr if x > 0]
        return sum(sorted_nums)
    return 0


# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.
