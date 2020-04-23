import random

details = list();
def setPassword():
      print("Enter the password of your choice: ")
      x = input()
      if len(x)>=7:
          details.append(x)
          displayDetails()
      else:
          print("You password has less than seven characters, enter atleast seven characters: ")
          setPassword()
def displayDetails():
  for y in range(0,len(details)):
        if y==0:
          print("First Name: "+ details[y])
        elif y==1:  
          print("Last Name: "+ details[y])
        elif y==2:
          print("Email address: " + details[y])
        elif y==3:
          print("Password: "+ details[y])
        else:
          break

print("You are welcome to HNG TECH\n")
print("please enter your first name: ")
x = input()
details.append(x)
print("lovely! Now enter your last name: ")
x = input()
details.append(x)
print("lovely! finally, enter your valid email address: ")
x = input()
details.append(x)

pass1=((details[0])[0:2])+((details[1])[((len(details[1]))-2):((len(details[1])))])


for i in range(1,6):
  pass1+= str(random.randrange(1,9))
print("Password: "+ pass1)
print("Enter 1 if you want to save this Password or 0 if you wish to create another one: ")
x = input()

if x=="1":
    details.append(pass1)
    displayDetails()
else:
  setPassword()


