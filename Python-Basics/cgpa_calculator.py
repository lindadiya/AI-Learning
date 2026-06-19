total = 0

for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    total += mark

average = total / 5

print("Average:", average)