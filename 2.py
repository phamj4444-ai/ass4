
def check_hex(color):
    if len(color) != 7:
        return False

    if color[0] != "#":
        return False

    for char in color[1:]:
        if char not in "0123456789ABCDEFabcdef":
            return False

    return True


color = input("Enter hex color: ")

if check_hex(color):
    print("Valid hex color")
else:
    print("Invalid hex color")
