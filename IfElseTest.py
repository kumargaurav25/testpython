# If Else Test

name = input("whats your name :")
length = len(name)

if length <= 5:
    print (" you have a very short name " + name)
elif length > 5 and length <= 8:
    print ("You have a medium sized name " + name)
else:
    print ("You have a really long name " + name)
