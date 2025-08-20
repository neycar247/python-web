num_expenses = int(input("How many expenses do you want to enter? "))
total = 0
for i in range(num_expenses):
    amount = float(input("Enter expense " + str(i + 1) + ": "))
    total = total + amount
print("Total spent: " + str(total))