userNum = input("gimme a number greater than 100: ")
changedNum = int(userNum)

while (changedNum < 100):
    print(userNum + " is less than 100, try again")
    userNum = input("gimme a number: ")
    changedNum = int(userNum)

print(userNum + " is greater than 100. Nice")