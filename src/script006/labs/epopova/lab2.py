"""
1.Write a python program that removes duplicates from a list
"""


def remove_duplicate(input_list):
    out_list = []
    for elem in input_list:
        if elem not in out_list:
            out_list.append(elem)
    return out_list


def remove_duplicates1(input_list):
    return list(set(input_list))


"""
2.Write a python program to convert a list of characters into a string
"""


def list_to_str(ch_list):
    return "".join(ch_list)


"""
3.Write a python program to flatten a nested list.
Hint: use ‘types’ https://docs.python.org/2/library/types.html
"""


def flatten_nested_list(input_list):
    if not input_list:
        return input_list
    if isinstance(input_list[0], list):
        return flatten_nested_list(input_list[0]) + flatten_nested_list(input_list[1:])
    return input_list[:1] + flatten_nested_list(input_list[1:])


"""
4. Write a python program to map two lists into a dictionary
"""


def lists_to_dict(list1, list2):
    return dict(zip(list1, list2))


"""
5. Write a python function to print a dictionary where the keys are numbers between 1 and n (both included) 
and the values are square of keys. “n” is passed as function parameter.
"""


def print_dict(dict_max_key):
    key_vals = [x for x in range(1, (dict_max_key + 1))]
    vals = [(x * x) for x in range(1, (dict_max_key + 1))]
    dict_for_print = lists_to_dict(key_vals, vals)
    print(dict_for_print)


"""
6. Write a Python program which takes two digits m (row) and n (column) 
as arguments(given from command line) and generates a two dimensional array. 
The element value in the i-throw and j-thcolumn of the array should be i*j.
"""


def gen_matrix(m, n):
    matrix_mxn = [[i * j for j in range(1, n + 1)] for i in range(1, m + 1)]
    return matrix_mxn


"""
7. Write a generator that implements the Fibonacci algorithm
"""


def fib_numbers(end_number):
    a, b = 0, 1
    while a <= end_number:
        yield a
        a, b = b, a + b


"""
8. Write a Python method that appends text given as input parameter to the beginning of a predefined file
"""


def append_to_file_bg(filename, text_to_append):
    with open(filename, 'r+') as file:
        file_data = file.read()
        file.seek(0, 0)
        file.write(text_to_append + '\n' + file_data)


"""
9. Write a Python program that reads file content and displays the number of lines that were read
"""


def read_file_count_lines(filename):
    num_lines = 0
    file_data = ""
    with open(filename, 'r') as file:
        for line in file:
            file_data += line
            num_lines += 1
    print("Read {} lines".format(num_lines))
    print(file_data)


"""
10. Write a Python program to append text into a file and displays the new content
"""


def append_to_file_end(filename, text_to_append):
    with open(filename, 'a+') as file:
        file.seek(0, 2)
        new_data_start = file.tell()
        file.writelines("\n" + text_to_append)
    return new_data_start


"""
11. Write a Python method that reads bytes from a specific range from a file. 
Range min and max values are sent as input parameters
"""


def bytes_from_file(filename, start, end):
    chunk_size = end - start;
    with open(filename, "rb") as file:
        file.seek(0, 2)
        file_size = file.tell()
        print("file_size: ", file_size)
        if (start < file_size) and (end < file_size):
            file.seek(start)
            chunk = file.read(chunk_size)
            print(chunk)


"""
12. Write a python program to find the longest words in a file
"""
"""
13. Write a Python program that prints all ‘.txt’ files from a directory.
Give the file extension as a parameter.
You can use the Python installation directory (e.gC:\Python27)
"""
"""
14. Write a Python program that pings localhost. 
Use osand subprocessmodules. Save command output.
Command: ‘ping localhost’ or ‘ping 127.0.0.1’
"""


def main():
    # Task 1
    test_list = [2, 4, 10, 40, 50, 1, 2, 4, 2, 5, 2, 20, 40, 35]
    print(remove_duplicate(test_list))
    print(remove_duplicates1(test_list))
    # Task 2
    ch_input_list = ['l', 'i', 's', 't', ' ', 'o', 'f', ' ', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's']
    print(list_to_str(ch_input_list))
    # Task 3
    test_nested_list = [[1, 3, 3, 5, 7], [2, 4, 4, 9, 6]]
    print("Flattened list: ", flatten_nested_list(test_nested_list))
    # Task 4
    list_key = [7, 5, 8, 2]
    list_value = ["aaa", "bbb", "ccc", "ddd"]
    print(lists_to_dict(list_key, list_value))
    # Task 5
    print_dict(25)
    # Task 6
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    res_matrix = gen_matrix(int(rows), int(columns))
    for row in res_matrix:
        print(' '.join([str(elem) for elem in row]))
    # Task 7
    end_number = int(input("Fib numbers: enter the end number here: "))
    fib_result = fib_numbers(end_number)
    while True:
        try:
            print(next(fib_result))
        except StopIteration:
            break
    # Task 8
    fl_name = "test-file.txt"
    append_to_file_bg(fl_name, "Python method that appends text given as input")
    with open(fl_name, "r+") as file:
        print(file.read())
    # Task 9
    read_file_count_lines(fl_name)
    # Task 10
    file_pos = append_to_file_end(fl_name, "Python method that appends text given as input")
    with open(fl_name, "r+") as file:
        file.seek(file_pos)
        print(file.read())
    # Task 11
    start_read = int(input("Enter start byte num for reading: "))
    end_read = int(input("Enter end byte num for reading: "))
    bytes_from_file(fl_name, start_read, end_read)


if __name__ == '__main__':
    main()