from sys import argv, exit
###print("I know that these are the words the user typed on the command line: ", argv)

def user_input_is_valid(cl_args):
    b = "1234567890"
    c = "."
    if len(cl_args) < 2:
        return False
    else:
        x = str(cl_args[1])
    if (x in b) and not (c in x):
        	return True
    return False


def encrypt(text, rot):
    '''text = input("Type a Message:")
    if text.isalpha() == False:
        print("Please provide a message")
        exit()
    #rot = int(input("How much encrpytion"))
    rot = int(argv[1])'''
    encrypted = ""

    for x in text:
        if x.isalpha():
            encrypted += rotate_character(x, rot)
        elif x.isalpha() == False:
            encrypted += x
    return encrypted

def alphabet_position(letter):
    lowerLetter = letter.lower()
    ascii_value = ord(lowerLetter)
    alphabetposition = ascii_value - 97
    return alphabetposition

def rotate_character(char, rot):
    char_ascii_value = ord(char)
    char_position = alphabet_position(char)
    new_char = (char_position + rot) % 26
    rotation_char = chr(new_char + 97)
    final_char = ""
    if char.isalpha() == False:
        final_char = char
    elif char_ascii_value < 97:
        final_char = rotation_char.upper()
    else:
        final_char = rotation_char.lower()

    return final_char
