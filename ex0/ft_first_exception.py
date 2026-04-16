#! python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    test_values = ["52", "abc", "-25", "25a"]

    for data in test_values:
        try:
            print(f"Input data is '{data}'")
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
            print()

        except Exception as temp_error:
            print(f"Caught input_temperature error: {temp_error}")
            print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
