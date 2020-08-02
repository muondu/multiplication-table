a = int(input("Enter where you want to start:  "))
b = int(input("Enter where you want to end:  "))
for x in range(a,b):
    for y in range(a,b):
        print("%4d " % (x*y), end = "")
    print()