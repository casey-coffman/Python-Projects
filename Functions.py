def conversion(imp, met, value):
    print(imp, met, value)
    conval = 0
    if imp == 0:
        if met == 0:
            conval = 1.61
        if met == 1:
            conval = 1609.34
    if imp == 1:
        if met == 0:
            conval = .000914
        if met == 1:
            conval = .914
    if imp == 2:
        if met == 0:
            conval = .0003048
        if met == 1:
            conval = .3048
    return(value * conval)

#--------------------------------------------------

def list_duplicates_of(seq, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

#--------------------------------------------------
