#start

max_num: int = None
min_num: int = None
user: int = int(input("type number: "))

while user != -999:
    user = int(input("type number: "))
    if user < 0 or user > 100:
        continue
    if user > max_num:
        max_num = user
    if user < min_num:
        min_num = user

print(f"max number is {max_num}")
print(f"min number is {min_num}")

