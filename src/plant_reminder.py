import random

# If soil moisture is below this percentage, the plant needs water
DRY_LIMIT = 30


def read_soil_moisture():
    """Pretend soil moisture sensor. Returns a value from 0 to 100 (%)."""
    return random.randint(0, 100)


def check_plant(moisture):
    """Decision rule: remind the user if the soil is too dry."""
    if moisture < DRY_LIMIT:
        return "REMINDER: Water the plant!"
    return "Soil is fine."


if __name__ == "__main__":
    for reading in range(8):
        moisture = read_soil_moisture()
        print(f"Reading {reading + 1}: moisture = {moisture}% -> {check_plant(moisture)}")