#! python3

def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"invalid literal for int() with base 10: '{temp_str}'")

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    test_values = [25, "abc", 100, -50]

    for value in test_values:
        print(f"Input data is '{value}'")

        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")
            print()
        except ValueError as temp_error:
            print(f"Caught input_temperature error: {temp_error}")
            print()

    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
