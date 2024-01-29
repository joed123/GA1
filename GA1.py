

# Example usage:
# number_of_allowable_intervals('input.txt', 'output.txt')
        


# Returns the amount of numbers between the min and max values
def find_values_between(arr, min_val, max_val):
    # Check if max is less than all values in array
    if max_val < arr[0]:
        return 0

    # Check if min is greater than all values in array
    elif min_val > arr[len(arr) - 1]:
        return 0

    min_idx = find_closest(arr, min_val)
    # Check if we are including a value below the min value
    if arr[min_idx] < min_val:
        min_idx += 1

    max_idx = find_closest(arr, max_val)

    # return the number of values between max and min
    return max_idx - min_idx + 1

# Returns element index of target in arr[] or index of the value below where target would be
# Runs in O(lg(n)) time
def find_closest(arr, target):

    n = len(arr)
    if target <= arr[0]:
        return 0
    if target >= arr[n - 1]:
        return n - 1

    # Doing binary search to find closest value lg(n) time
    i = 0
    j = n
    mid = 0
    while i < j:
        mid = (i + j) // 2

        if arr[mid] == target:
            return mid

        if target < arr[mid]:

            # If target is greater than previous
            # return previous index
            if mid > 0 and target > arr[mid - 1]:
                return mid - 1

            # Repeat for other half
            j = mid

        # If target is greater than mid
        else:
            if mid < n - 1 and target < arr[mid + 1]:
                return mid

            # update i
            i = mid + 1

    return mid


# Finds possible pairs in O(nlg(n) + mlg(n)) time
def possible_pairs(A, B, t_min, t_max):

    # Sorts A in nlg(n) time
    A.sort()

    total = 0
    # Loops through B and finds pairs in mlg(n) time
    for x in B:
        temp_min = t_min - x
        temp_max = t_max - x
        # Finds values between min and max in lg(n) time
        total += find_values_between(A, temp_min, temp_max)

    return total


print(possible_pairs([0, 2, 1, 0, 0, 5, 17, 0], [-3, 10, 0], -3, 20))