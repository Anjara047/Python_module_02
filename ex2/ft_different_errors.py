#! python3

def garden_operations(operation_number):
    if operation_number == 0:
        value = "abc"
        int(value)
    if operation_number == 1:
        number = 10
        number / 0
    if operation_number == 2:
        open("/non/existent/file")
    if operation_number == 3:
        string = "hello"
        value = 5
        string + value
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")

        try:
            garden_operations(i)
            print("Operation completed successfully")

        except ValueError as error:
            print(f"Caught ValueError: {error}")

        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")

        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")

        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
