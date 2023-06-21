import sys
num = int(sys.argv[1]) #uses sys.argv to be able to use afact as a console command

while True:
    if type(num) == int:
        break        
    else:
        print("Yeah sorry, but this program only works on integers. So, what's your number again?")
        num = input()


#x: factorialized number
#deb_tog: toggle for debug messages
#rec_toc: toggles the recursion loop in the "if g/i >tmp:" block
def afact(x, deb_tog, rec_tog):
    i = 1
    tmp = x
    while True:
        
        g = tmp
        if tmp<0:
            return "null"
        if i != 0:
            tmp = tmp//i
            if g/i > tmp:
                if deb_tog is True: 
                    print("Not a Factorial. Sorry.")
                else: 
                    return 0
                if rec_tog == True:
                    v = [None,None]
                    j = 1
                    while True:
                        c = afact(x-j,False,False)
                        b = afact(x+j,False,False)
                        j = j+1
                        if c == "null":
                            v[0] = 0
                            c = 0
                        if b == "null":
                            v[1] = 0
                            b = 0
                        try:
                            if c!=0 or b!=0:
                                if c == 1:
                                    v[0] = 1
                                elif c > 1:
                                    v[0] = c
                                if b == 1:
                                    v[1] = 1
                                elif b > 1:
                                    v[1] = b
                        except TypeError:
                            pass
                        if (v[0] != None) or (v[1] != None):
                            break
                    if 0 in v:
                        break
                    if v[0] != None and v[1] == None:
                        print("Yeah, seems like "+str(v[0])+" may be the closest to what you're looking for")
                    elif v[0] == None and v[1] != None:
                        print("Yeah, seems like "+str(v[1])+" may be the closest to what you're looking for")
                    elif v[0] != None and v[1] != None:
                        print("Yeah, seems like "+str(v[0])+" or "+str(v[1])+" may be the closest to what you're looking for")
                break
            if tmp == 1:
                if i == 1:
                    if deb_tog is True: 
                        print("Either 0 or 1. Choose what you like more.")
                    else: 
                        return 0
                    break
                else:
                    if deb_tog is True: 
                        print(i)
                    else: 
                        return i
                    break
        i+=1

afact(num,True,True)
