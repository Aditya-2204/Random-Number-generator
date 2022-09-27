import random
import time

minval = int(str(input("Lowest number: ")))
maxval = int(str(input("Highest number: ")))

print("Rolling first dice")
time.sleep(1)
print(f"The number is {random.randint(minval, maxval)}")

time.sleep(2)

print("Rolling second dice")
time.sleep(1)
print(f"The number is {random.randint(minval, maxval)}")