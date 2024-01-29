'''
This file contains the template for Assignment1. For testing it, I will place
it
in a different directory, call the function <number_of_allowable_intervals>,
and check
its output. So, you can add/remove whatever you want to/from this file. But,
don't
change the name of the file or the name/signature of the following function.
Also, I will use <python3> to run this code.

def number_of_allowable_intervals(input_file_path, output_file_path):
    
    This function will contain your code. It wil read from the file
    <input_file_path>,
    and will write its output to the file <output_file_path>.
    
    pass '''



def number_of_allowable_intervals(input_file_path, output_file_path):
    '''
    Read the input file containing intervals and calculate the number of allowable intervals.

    Parameters:
        input_file_path (str): Path to the input file containing intervals.
        output_file_path (str): Path to the output file to write the result.

    Returns:
        None
    '''
    # Read input file
    with open(input_file_path, 'r') as input_file:
        intervals = input_file.readlines()

    #our input consists of (i) two arrays A[1, . . . , m] and B[1, . . . , n] of integers
    # (ii) a target value range denoted by [tmin, tmax].



    # Write result to output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(str(num_allowable_intervals))

# Example usage:
# number_of_allowable_intervals('input.txt', 'output.txt')