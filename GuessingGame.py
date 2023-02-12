import random
x= random.randrange(1,10)
g= int(input("Enter an number in this range(1-10): "))
chance=1

while x != g:
    if g < x:
        print("Too low")
        g = int(input("Enter number again: "))
    elif g > x:
        print("Too high!")
        g = int(input("Enter number again: "))
    else:
        break
    chance +=1
if chance==5:
    input("You failed to guess the number was it that hard?\n Press any key to exit!")

print("Well done you guessed correctly!The number was", x)
print("And it only took you", chance, "tries!\n")

 