print("Functions with input and outputs in this lesson")


def my_func(hello):
    return hello + " " + "Bob"


def to_title_case(str):
    return str.title()


print(f'{my_func("White")}')

print(f'{to_title_case("my new output")}')  # return -> My New Output
print(f'{to_title_case("mGOOO neW ouTPUt")}')  # return -> Mgooo New Output


# Multiple return value
def multi(str):
    if str == 'yes':
        return True
    else:
        return False


print(f'{multi("no")}')

