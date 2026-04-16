#! python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def test_plant():
    raise PlantError("The tomato plant is wilting!")


def test_water():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print()

    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
        print()

    print("Testing catching all garden errors...")

    try:
        test_plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        test_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
