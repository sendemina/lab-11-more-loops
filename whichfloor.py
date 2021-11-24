maximum_stories = 38
userinput = input("On what floor of the building is your office? ")
usernum = int(userinput)
while (usernum > maximum_stories):
    print("You entered: " + str(usernum) + " but there are only " + str(maximum_stories) + " in this building. Try again...")
    userinput = input("On what floor of the building is your office? ")
    usernum = int(userinput)
print("Congrats! Your work is on floor " + str(usernum))
