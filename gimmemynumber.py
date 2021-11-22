userstring = input("Gimme a number greater than 100 please... ")
usernum = int(userstring)

while usernum <= 100:
    print(str(usernum) + " is less than or equal to 100. Try again, I've got all day! ")
    userstring = input("Gimme a number greater than 100 please... ")
    usernum = int(userstring)
print(str(usernum) + " is over 100, great job! ")
