import sys
x = int(sys.argv[1])
i = 1
tmp = x
while True:
    g = tmp
    tmp = tmp//i
    if g/i > tmp:
        print("Not a Factorial. Sorry.")
        break
    if tmp == 1:
        if i == 1:
            print("Either 0 or 1. Choose what you like more.")
            break
        else:
            print(i)
            break
    i += 1
