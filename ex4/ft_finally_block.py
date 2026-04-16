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


def water_plant(plant_name):
   if plant_name != plant_name.capitalize():
       raise PlantError(f"Invalid plant name to water: '{plant_name}'")
   print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    print("=== Garden Watering System ===")
    print()

    print("\nTesting valid plants...")
    print("Opening watering system")
    plants = ("Tomato", "Lettuce", "Carrots")

    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    plants = ("Tomato", "lettuce", "Carrots")

    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
