x = 0
dict_trans = {36: None, 46: None} #ascii dictionary values for $ and . convert to blanks
import math

while x == 0:
    dv = input("Enter an amount to convert to change:")
    dv1 = dv.find("$" and ".") #$ and . return and add together
    if dv1 == 2:
        intv = int(dv.translate(dict_trans)) #removes $ and . from dv to allow for int conversion
        quarters = math.trunc(intv/25)
        remain1 = intv - (quarters * 25)
        dimes = math.trunc(remain1/10)
        remain2 = remain1 - (dimes * 10)
        nickels = math.trunc(remain2/5) #math for remainders and amount of coins
        remain3 = remain2 - (nickels * 5)
        pennies = math.trunc(remain3/1)
        remain4 = remain3 - (pennies * 1)
        print("This is equivalent to", quarters, "quarters,", dimes, "dimes", nickels, "nickels and", pennies, "pennies in change.")
        x = x + 1
    else:
        print("It must be in [$X.XX] format.")
        x = 0

#started June, 1
#finished June, 1
