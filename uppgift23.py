def ram(r,l,t):
#r=rader l=längd t= tjocklek
    for i in range(t):
        print("*"*l)

    for j in range(r-(2*t)):
        print("*"*t," "*(l-(2*t)-2),"*"*t)

    for o in range(t):
        print("*"*l)

