# functions my want to achieve
# 1.you can selected symbols on/off in 11/25
# 2.you can selected numbers on/off in 11/25
# 3.you can selected alphabet on/off in 11/25
# 4.auto copy , achieved in 11/24
# 5.make a error if use -l more 74 and -ed in 11/24

import argparse  # to work with the arguments
import string
import secrets
import pyperclip                # auto copy moduel


# function to generate the password
def get_password(length: int) -> str:
    # creating data
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    numbers = [str(a) for a in range(10)]
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase

    # variable to hold the password
    password = ''

    # if you want to more safety to 5 lower 
    # if length < 5:
    #     # adding one symbol
    #     password += secrets.choice(symbols)
    #     # adding one number
    #     password += secrets.choice(numbers)
    #     # adding one lowercase character
    #     password += secrets.choice(lowercase_characters)
    #     # adding one uppercase character
    #     password += secrets.choice(uppercase_characters)

    # now run a for loop starting from the current length of the password
    # all the way to the maxium length to fill in the remaining data
    while len(password) < length:
        # adding all the data together into a one list
        characters = lowercase_characters + uppercase_characters
        if args.excludesymbols:
            data = numbers + list(characters)
        elif args.excludenumbers:
            data = symbols + list(characters)
        elif args.excludealphabet:
            data = symbols + numbers
        else: 
            data = symbols + numbers + list(characters)

        # getting a random character from the list
        random_char = secrets.choice(data)

        # if asked to exclude duplicates
        if args.excludeduplicates:
            # if character not already inside the password
            # then add it into the password
            if random_char not in password:
                password += random_char
        else:  # if not asked to exclude duplicates
            # then just add the character without checking
            password += random_char

    # create a list of the password
    password_list = list(password)
    # shuffle the list into random sequence
    password = shuffle(password_list)

    # returning the password
    return password


# shuffle function based on Fisher–Yates shuffle using secrets.choice()
# as the integer selector
def shuffle(password: list):
    # n used to determine range of loop
    n = len(password)
    for x in range(n - 1, 0, -1):
        # set new variable y to random int within needed index
        y = secrets.choice(range(0, x + 1))
        # swap elements at index x and index y
        password[x], password[y] = password[y], password[x]
    # return concatenated password
    return ''.join(password)

# main method


def main(args: argparse.Namespace) -> None:
    # storing the length in a variable
    length = args.length

    # if the value is out of range then inform the user and exit
    # if length < 6 or length > 20:
    #   print('ERROR: -l/--length should be in the range of 6 - 20')
    #  exit(0)

    # added
    if (length > 74 and args.excludeduplicates) or (length > 62 and args.excludesymbols) or (length > 64 and args.excludenumbers) or (length > 22 and args.excludealphabet):
        print("ERROR: its too many length")
        exit(0)

    # this will hold the final password
    password = get_password(length)

    # printing the password to the user
    print(f'PASSWORD: {password}')
    pyperclip.copy(password)


if __name__ == '__main__':
    # creating the argparse object
    parser = argparse.ArgumentParser()

    # adding the length argument
    parser.add_argument(
        '-l', '--length',
        help='Length of the password. [MIN=1], [DEFAULT=6],[MAX= basic(infinity), -ed(74), -ed+(-es(62), -en(64), -ea(22)), more combinations will result in  shorter length.]',
        metavar='',
        default=6,
        type=int
    )

    # adding the exclude duplicates argument
    parser.add_argument(
        '-ed',
        '--excludeduplicates',
        action='store_true',
        help='Excludes duplicate characters from the password'
    )

    parser.add_argument(
        '-es',
        '--excludesymbols',
        action='store_true',
        help='Excludes symbols characters from the password'
    )

    parser.add_argument(
        '-en',
        '--excludenumbers',
        action='store_true',
        help='excludes numbers characters from the password'
    )

    parser.add_argument(
        '-ea',
        '--excludealphabet',
        action='store_true',
        help='excludes alphabet characters from the password'
    )

    # parsing the argument
    args = parser.parse_args()

    # calling the main method with the args
    main(args)
