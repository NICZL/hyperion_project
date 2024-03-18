name = input("what is your name?")
age = input("what is your age?")
try:
    ageAsANumber = int(age)
    if(ageAsANumber > 0):
        print(ageAsANumber)
        print(name)
        print("Hello World!")
    else:
        raise Exception("Your age cannot be a negative number")
except Exception as e:
    print("Your age has to be a positive integer")