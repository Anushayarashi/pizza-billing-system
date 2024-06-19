inp=input("enter size of pizza  for small(s)/medium(m)/large(l):\n")
bill=0
if inp=='s':
    bill +=100
    print(f"prize of the pizza is{bill}rs")
elif inp=='m':
        bill +=250
        print(f"prize of the pizza is{bill}rs")
elif  inp=='l' :
        bill +=300
        print(f"prize of the pizza is{bill}rs")
else:print("you order is out of availability")


ot=input ("do you want papper y/n")
if ot=='y' or ot=='y':
    inp2=input("enetr the size(s/m/l)\n")
    if inp2=='s' or inp2=='s':
        bill +=15
        print(" total bill",bill)
    elif inp2=='m' or inp2=='m':
         bill +=30
         print(" total bill",bill)
        
    elif  inp2=='l' or inp2=='l':
        bill +=50
        print(" total bill",bill)
        
    else:print("you order is out of availability")
ot2=input ("do you want chees y/n")
if ot2=='y' or ot2=='y':
    inp3=input("enetr the size(s/m/l)\n")
    if inp3=='s' or inp3=='s':
        bill +=30
        print(" total bill",bill)
    elif inp3=='m' or inp3=='m':
         bill +=50
         print(" total bill",bill)
        
    elif  inp3=='l' or inp3=='l':
        bill +=70
        print(" total bill",bill)
        
    else:print("you order is out of availability")
else:input(f"your total bill is {bill} RS")
 