import pyfiglet


def print_in_format(string):
    print(pyfiglet.figlet_format(string))


x = input("what you waaaant:")
print_in_format(x)
