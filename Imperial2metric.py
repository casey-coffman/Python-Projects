from Functions import conversion

x = True
av = [0, 1, 2]
mav = [0, 1]
iv = ["miles", "yards", "feet"]
mv = ["kilometers", "meters"]

while x == True:
    print("0: Miles\n1: Yards\n2: Feet")
    imperial_input = int(input("What imperial unit would you like to convert?"))
    if imperial_input in av:
        print("0: Kilometers\n1: Meters")
        metric_input = int(input("What metric unit would you like to convert to?"))
        if metric_input in mav:
            imp_user_input = iv[av.index(imperial_input)]
            met_user_input = mv[av.index(metric_input)]
            user_input = int(input("How many " + str(imp_user_input) + " would you like to convert to " + str(met_user_input) + "?"))
            print("Converted value: " + str(conversion(imperial_input, metric_input, user_input)))
            x = False
        else:
            print("You must input 0 or 1.")
            continue
    else:
        print("You must input 0, 1 or 2.")
        continue
