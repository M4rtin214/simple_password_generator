import sys
import os
import random
import string
import clipboard

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = "!#$%&*-_.:;?@#"

all_symbols = lower + upper + num + symbols


def main():
    if len(sys.argv) < 2:
        print("Please enter length the password as argument (example: password_generator.py 16)")
        print("The generated password will be inserted into the clipboard")
    else:
        length = sys.argv[1]
        if length.isdigit():
            if int(length) > 76:
                length = 76
            new_password = random.sample(all_symbols, int(length))
            new_password = "".join(new_password)
            clipboard.copy(new_password)
            print("Your password has been inserted into the clipboard")
            sys.exit(0)
        else:
            print("Please enter int argument for length the password: ")
            sys.exit(1)

            
if __name__ == "__main__":
    main()
