types = [0,1,True,False,None,"False"]

for t in types:
    if t:
        print("{}: bool True".format(t))
    else: 
        print("{}: bool False".format(t))
