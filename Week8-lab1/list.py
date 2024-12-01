from sense_hat import SenseHat
sense = SenseHat()

# temperatures = [12.0,12.5,13.0,13,12]
# print(f"Average Temp: {sum(temperatures) / len(temperatures)}C")
# print(f"Average Temp: {sum(temperatures) / len(temperatures)}C")


temperatures = [sense.get_temperature() for _ in range(5)]
print(f"Average Temp: {sum(temperatures) / len(temperatures)}C")
print(f"Average Temp: {sum(temperatures) / len(temperatures)}C")
