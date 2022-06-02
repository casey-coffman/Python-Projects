x = 0
y = 0
a = 0
b = 0

final_list = []
bin_values = [128, 64, 32, 16, 8, 4, 2, 1] #assigns values to each position in bin_list

while x < 1:
    bin = input("What binary number would you like to convert?")
    bin_list = list(bin) #converts bin to a list called bin_list
    bin_list = [int(y) for y in bin_list] #converts binlist to integers
    if 0 or 1 not in bin_list:
        print("A binary number can only contain 1's and 0's.")
        x = 0
        continue
    elif 0 or 1 in bin_list:
        x = x + 1
        y = y + 1
    if len(str(bin)) != 8: #determines if string is too long
        print("A binary number must have 8 characters.")
        x = 0
    elif len(str(bin)) == 8:
        x = x + 1
        y = y + 1
    if 1 in bin_list and y != 0:
        while b <= 7:
            final_list.append(bin_list[a] * bin_values[a]) #multiplies and adds values to final_list
            a = a + 1
            b = b + 1
        else:
            print(sum(final_list)) #takes sum of all values in final_list
            x = 0

#started May 28, 2022
#completed May 29, 2022
