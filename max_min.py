# start
import random


max_num: int = -1


for i in range(10):
    numbers: int = random.randint(1, 100)
    if numbers > max_num:
        max_num = numbers
    print(numbers)
print(f"the max number is {max_num}")









