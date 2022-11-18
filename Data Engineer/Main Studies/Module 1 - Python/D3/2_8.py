#! Python3

# 1a
salaries = [30596, 31234, 54521, 34456, 52135, 30456, 40566]
summ = 0

for salary in salaries:
    summ += salary

print(f"Total salary payout: {summ} kr")

# 1b
salaries = [30596, 31234, 54521, 34456, 52135, 30456, 40566]
summ = 0
highest_salary = 0

for salary in salaries:
    summ += salary
    highest_salary = salary

print(f"Total salary payout: {summ} kr")

# 1c
salaries = [30596, 31234, 54521, 34456, 52135, 30456, 40566]
summ = 0
highest_salary = 0

for salary in salaries:
    summ += salary

    if salary > highest_salary:
        highest_salary = salary

print(f"Total salary payout: {summ} kr")

print(f"Highest salary: {max(salaries)}")
print(f"Total salary payout: {sum(salaries)}")

# 1d
salaries = [30596, 31234, 54521, 34456, 52135, 30456, 40566]
summ = 0
highest_salary = 0

for salary in salaries:
    summ += salary

    if salary > highest_salary:
        highest_salary = salary

print(f"Total salary payout: {summ} kr")
print(f"The highest salary is: {highest_salary} kr")
print(f"Highest salary: {max(salaries)}")
print(f"Total salary payout: {sum(salaries)}")

# 2a
to_do = ["eat", "study", "cook", "clean", "play"]
for item in to_do:
    print(item)

# 2b
to_do = ["eat", "study", "cook", "clean", "play"]
for item in to_do:
    print(item)

new_todo = input("What do you need to do?: ")
to_do.append(new_todo)

# 2c
to_do = ["eat", "study", "cook", "clean", "play"]
for item in to_do:
    print(item)

new_todo = input("What do you need to do?: ")
to_do.append(new_todo)

ask = input("Do you want another chore?:").strip().lower()
while True:
    if ask == "yes":
        if len(to_do) == 0:
            print("You have completed all tasks!")
            break
        else:
            print(f"Please do the following: {to_do[0]}")
            to_do.pop(0)
    elif ask == "no":
        if len(to_do) == 0:
            print("You have completed all tasks!")
            break
        else:
            print("You still have chores to do:")
            for item in to_do:
                print(item)

# 3a
car = {
    "brand": "Volvo",
    "year": 2002,
    "color": "red",
    "miles": 10000,
    "cost": 37500
}

for k, v in car.items():
    print(f"{k}: {v}")

# 3b
car = {
    "brand": "Volvo",
    "year": 2002,
    "color": "red",
    "miles": 10000,
    "cost": 37500
}
car2 = {
    "brand": "Ford",
    "year": 2016,
    "color": "blue",
    "miles": 2000,
    "cost": 137500
}
car3 = {
    "brand": "SAAB",
    "year": 1953,
    "color": "black",
    "miles": 13000,
    "cost": 237500
}

all_cars = [car, car2, car3]
loop = True
while loop:
    for x in all_cars:
        if loop:
            print(
                f"{x['brand']} from {x['year']} with {x['miles']}, costs only {x['cost']}!")

            ask = input("Do you wish to buy or next?: ").strip().lower()

            if ask == "buy":
                print(f"The {x['color']} {x['brand']} bought for {x['cost']}!")
                loop = False
            elif ask == "next":
                continue
