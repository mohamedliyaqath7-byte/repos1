import random

# If soil moisture is below this percentage, the plant needs water
DRY_LIMIT = 30

# Between DRY_LIMIT and this value, keep an eye on the plant
WATCH_LIMIT = 50


def read_soil_moisture():
    """Pretend soil moisture sensor. Returns a value from 0 to 100 (%)."""
    return random.randint(0, 100)


def check_plant(moisture):
    """Decision rule: remind the user if the soil is too dry."""
    if moisture < DRY_LIMIT:
        return "REMINDER: Water the plant!"
    if moisture < WATCH_LIMIT:
        return "Soil is getting dry. Keep an eye on it."
    return "Soil is fine."


if __name__ == "__main__":
    reminders = 0
    for reading in range(8):
        moisture = read_soil_moisture()
        message = check_plant(moisture)
        if message.startswith("REMINDER"):
            reminders += 1
        print(f"Reading {reading + 1}: moisture = {moisture}% -> {message}")
    print(f"Total reminders sent: {reminders}")