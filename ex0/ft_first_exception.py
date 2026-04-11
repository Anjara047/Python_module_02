#! python3
import sys


# ================= INPUT CUSTOM =================
#! python3

def ft_input(prompt=""):
    sys.stdout.write(prompt)
    sys.stdout.flush()

    buffer = []

    while True:
        char = sys.stdin.read(1)

        if char == '\n':
            break

        elif char in ('\b', '\x7f'):
            if buffer:
                buffer.pop()
                sys.stdout.write('\b \b')
                sys.stdout.flush()

        else:
            buffer.append(char)
            sys.stdout.write(char)
            sys.stdout.flush()

    sys.stdout.write('\n')
    return ''.join(buffer)


class Temperature:
    def __init__(self, temp):
        self.temp = temp
        self.error = False

    def set_error(self):
        self.error = True

    def show(self):
        print("=== Garden Temperature ===")
        print()

        if self.error:
            print(f"Input data is '{self.temp}'")
            print(f"Caught input_temperature error: invalid literal for int() with base 10: '{self.temp}'")
            print()
        else:
            print(f"Input data is '{self.temp}'")
            print(f"Temperature is now {self.temp}°C")
            print()

        print ("All tests completed - program didn't crash!")

def ft_first_exception():
    value = ft_input("Enter a number: ")

    try:
        temp_value = int(value)
        t = Temperature(temp_value)
    except ValueError:
        t = Temperature(value)
        t.set_error()

    t.show()

#    value = ft_input("Enter a number: ")

 #   try:
 #       temp_value = int(value)
 #       t = Temperature(temp_value)
 #   except ValueError:
 #       t = Temperature(value)
 #       t.set_error()

 #   t.show()


if __name__ == "__main__":
    ft_first_exception()
