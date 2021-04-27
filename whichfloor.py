maximum_stories = 10
userNum = input("Enter the number of the floor your office is on: ")
changedNum = int(userNum)

while (changedNum > maximum_stories):
    print("You entered " + userNum + ". There are 10 stories in the building. Please enter a valid number.")
    userNum = input("Enter the number of the floor your office is on: ")
    changedNum = int(userNum)

print("Great job, your office is on floor: " + userNum)