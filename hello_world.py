name = input("what is your name?")
age = input("what is your age?")
try:
    ageAsANumber = age.toInt()
    print(ageAsANumber)
    print(name)
    print("Hello World!")
except Exception as e:
    print("Your age has to be an integer")