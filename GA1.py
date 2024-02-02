'''
This file contains the template for Assignment1. For testing it, I will place
it
in a different directory, call the function <number_of_allowable_intervals>,
and check
its output. So, you can add/remove whatever you want to/from this file. But,
don't
change the name of the file or the name/signature of the following function.
Also, I will use <python3> to run this code.
'''
def number_of_allowable_intervals(input_file_path, output_file_path):
    file_in = open(input_file_path)
    file_out = open(output_file_path, 'w')
    input = file_in.read().replace(",","\n").split()
    input1 = [eval(i) for i in input]
    file_out.write(str(count_subarrays_within_range(input1[3:], input1[1], input1[2])))
'''
This function will contain your code. It wil read from the file
<input_file_path>,
and will write its output to the file <output_file_path>.
'''


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


def count_subarrays_within_range(A, t_min, t_max):
    def count_subarrays_with_sum_in_range(prefix_sums, start, end):
        if start == end:
            return 0
        
        mid = (start + end) // 2
        count = count_subarrays_with_sum_in_range(prefix_sums, start, mid) + \
                count_subarrays_with_sum_in_range(prefix_sums, mid + 1, end)
        
        # Count sub arrays where the sum falls within the range [t_min, t_max]
        i = j = mid + 1
        for left_sum in prefix_sums[start:mid+1]:
            while i <= end and prefix_sums[i] - left_sum < t_min:
                i += 1
            while j <= end and prefix_sums[j] - left_sum <= t_max:
                j += 1
            count += j - i
        
        # Merge the two sorted halves
        temp = [0] * (end - start + 1)
        i = start
        j = mid + 1
        k = 0
        while i <= mid and j <= end:
            if prefix_sums[i] < prefix_sums[j]:
                temp[k] = prefix_sums[i]
                i += 1
            else:
                temp[k] = prefix_sums[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = prefix_sums[i]
            i += 1
            k += 1
        while j <= end:
            temp[k] = prefix_sums[j]
            j += 1
            k += 1
        for idx in range(start, end + 1):
            prefix_sums[idx] = temp[idx - start]
        
        return count
    
    # Compute prefix sums
    prefix_sums = [0]
    for num in A:
        prefix_sums.append(prefix_sums[-1] + num)
    
    # Call the recursive function
    return count_subarrays_with_sum_in_range(prefix_sums, 0, len(prefix_sums) - 1)


number_of_allowable_intervals('output.txt', 'input.txt')
