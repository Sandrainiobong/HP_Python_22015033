#program to display name, age and phone number

name=input("what is your name\t")
age=int(input("enter your age\t"))
#your age should be only number(s)e.g 12
phone=int(input("what is your phone number\t"))
print("Hello {}, you are {} years old with the phone number {}.".format(name,age,phone))