import re
from sense_hat import SenseHat
sense = SenseHat()
temperature = sense.get_temperature()
temp_str = f"{temperature}C" # Format temperature with one decimal place
# Pattern to match temperature format: digits, optional decimal, "C"
pattern = r"^\d+(\.\d)?C$"
if re.match(pattern, temp_str):
    print(f"Valid format: {temp_str}")
else:
    print("Invalid format")
