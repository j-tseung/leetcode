'''
Helper function to make folder names from LeetCode problem titles.
'''
def convert_snakecase(string):
    converted = ''.join([ch if ch.isdigit() or ch.isalpha() else '_' for ch in string if ch != '.'])
    print(converted)

string = input("Convert string: ")
convert_snakecase(string)