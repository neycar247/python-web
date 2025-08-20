total = 0
while True:
    entry = input("Enter an expense (or type 'done' to finish): ")
    if entry.lower() == "done":
       break
    amount = float(entry)
    total = total + amount
print("Total spent: " + str(total))