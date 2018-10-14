"""
1. Write a function that returns the sum of n numbers.
"""


def count_sum(numbers_array, count_to_sum: int) -> int:
    if not numbers_array:
        return 0
    tmp_array = numbers_array[0:count_to_sum]
    res_sum = sum(i for i in tmp_array)
    return res_sum

"""
2. Write a function that returns the odd numbers from a given interval. 
The default interval is 0-100. The interval is given from standard input
"""


def find_odd(start: int = 0, end: int = 100):
    out_num_array = []
    for num in range(start, (end + 1)):
        if num % 2 != 0:
            out_num_array.append(num)
    return out_num_array

"""
3. Write a function that builds html tags. Apply html escaping for html special chars.
The function will receive 2 parameters – tag type and tag content. 
It will return the generated html as text.
-
eg: f(‘b’, ‘Ham&Eggs’) returns “<b>Ham&amp;Eggs</b>”
-
HTML char escaping:
 < == &lt;
 > == &gt;
 “ == &quot;
 & == &amp;
"""


def build_html_tag(tag_type, tag_content):
    tag_dict = {'<': "&lt;", '>': "&gt;", '"': "&quot;", '&': "&amp;"}
    tag_type_dict = {'open': "<", 'close': ">", 'open-close': "</"}
    out_html = r""
    out_html += tag_type_dict['open'] + tag_type + tag_type_dict['close']
    updated_content = tag_content
    for tag_key in tag_dict:
        updated_content = updated_content.replace(tag_key, tag_dict[tag_key])

    out_html += updated_content + tag_type_dict['open-close'] + tag_type + tag_type_dict['close']
    return out_html

"""
4. Given following data structure:
[
{'first_name': 'John', 'last_name': 'Cornwell', 'net_worth': 2632.345},
{'first_name': 'Emily', 'last_name': 'Alton', 'net_worth': -4578.234},
{'first_name': 'James', 'last_name': 'Bond', 'net_worth': 1000.07},
]
Generate an output formatted like:
------------------------------------
| Cornwell J. | +2632.34 |
| Alton E. | -4578.23 |
| Bond J. | +1000.07 |
------------------------------------
-
Last names are left aligned with padding to 15 chars
-
From first name display only first letter right aligned with padding, total width 2 chars, followed by ‘.’
-
Net worth column width is 10 chars, we display only first two decimals, and also sign for both positive and negative numbers
-
Data is wrapped up between ‘|’ and ‘-’ ASCII chars to print similar to a table
"""


def print_dict(input_dict):
    print('{:-<36s}'.format(''))
    for item in input_dict:
        print('| {:<15s} {:>2}.|{:^10.2f}|'.format(item['last_name'],
                                                item['first_name'][0],
                                                item['net_worth']))
    print('{:-<36s}'.format(''))


def main():
    # Task 1
    num_array = [1, 7, 9, 10, 15]
    num_sum = count_sum(num_array, 3)
    print("num_sum: ", num_sum)

    # Task 3
    gen_html = build_html_tag('b', 'Ham&Eggs')
    print("gen_html: ", gen_html)

    # Task 2
    test_str = input("Enter the interval of numbers, like 1-100: ")
    intervals = test_str.split("-")
    if intervals[0].isdigit() and intervals[1].isdigit():
        odd_nums = find_odd(int(intervals[0]), int(intervals[1]))
        print("odd_nums: ", odd_nums)
    else:
        print("Invalid interval")

    # Task 4
    users_data = [
        {'first_name': 'John', 'last_name': 'Cornwell', 'net_worth': 2632.345},
        {'first_name': 'Emily', 'last_name': 'Alton', 'net_worth': -4578.234},
        {'first_name': 'James', 'last_name': 'Bond', 'net_worth': 1000.07},
    ]
    print_dict(users_data)


if __name__ == '__main__':
    main()
