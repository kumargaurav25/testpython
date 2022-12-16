print("Welcome to tip Calculator")
bill = int(input("what is the total bill?"))
numpeople = int(input("how many people to split the bill"))
tippercent = int(input("what percent tip you want to give"))
tip=bill*tippercent/100
print(tip)

totalbill = int(bill + tip)
print ("total bill with tip is " + str(totalbill))

yourcontri = totalbill / numpeople

print("Your contribution including tip should be " + str(yourcontri))
