from numpy import random as npr

car_fuel = 60
avg_fuel_consumption = 0.7
distance = 0

while True:
    distance += 10
    fuel_consumption_derivation = 0.5 - npr.rand()
    car_fuel -= (avg_fuel_consumption + fuel_consumption_derivation)

    check_fuel = car_fuel
    if (check_fuel - (avg_fuel_consumption + fuel_consumption_derivation)) < 0:
        print("I need more gas")
        break

print(f"Drove {distance} km.")
print(f"Fuel remaining: {car_fuel} litres.")
