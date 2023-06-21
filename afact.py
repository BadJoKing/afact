import sys
num = int(sys.argv[1]) #uses sys.argv to be able to use afact as a console command


#Checks whether the input is actually an integer
while True:
    if type(num) == int:
        break        
    else:
        print("Yeah sorry, but this program only works on integers. So, what's your number again?")
        num = input()


#x: factorialized number
#deb_tog: toggle for debug messages
#rec_toc: toggles the recursion part in the "if g/i > tmp:" block
def afact(x, deb_tog, rec_tog):
    i = 1       #this is the 'iterator' for the following while loop, because it was easier to implement it that way for some reason... 
    tmp = x     #stores x in a temporary variable

    #this loop basically divides x by 2, 3, 4, 5, ... in that order, essentially reversing wht you usually do when calculating a factorial
    while True:
        g = tmp
        if tmp<0:
            return "null"   #returns "null", if the number you entered is negative

        if i != 0:
            tmp = tmp//i    #does a floor division
            if g/i > tmp:   #compares the regular division of x with i with the floor division. 
                            #If x is a factorial it should always be an integer, thus skipping 
                            #the most complicated and probably needlessly complex part of the program.
                if deb_tog is True: 
                    print("Not a Factorial. Sorry.")
                else: 
                    return 0
                if rec_tog == True:
                    v = [None,None]
                    j = 1
                    #this loop calculates the afact for x+j and x-j over and over again until it finds at least one factorial. 
                    #This may take some while depending on the size of x
                    while True:
                        c = afact(x-j,False,False)
                        b = afact(x+j,False,False)
                        j = j+1
                        if c == "null":     #these if statements check, when one of the xs went negative
                            v[0] = 0
                            c = 0
                        if b == "null":
                            v[1] = 0
                            b = 0
                        try:
                            if c!=0 or b!=0:    #I could probably replace these with just v[0] = c and v[1] = b, 
                                if c == 1:      #but I guess I'll do that in a later version and disguise it as a performance update
                                    v[0] = 1
                                elif c > 1:
                                    v[0] = c
                                if b == 1:
                                    v[1] = 1
                                elif b > 1:
                                    v[1] = b
                        except TypeError:
                            pass
                        if (v[0] != None) or (v[1] != None):    #checks, whether the afact functions above returned something useful and breaks the loop if yes.
                            break
                    if 0 in v:
                        break
                    #Does what it says it does
                    if v[0] != None and v[1] == None:
                        print("Yeah, seems like "+str(v[0])+" may be the closest to what you're looking for")
                    elif v[0] == None and v[1] != None:
                        print("Yeah, seems like "+str(v[1])+" may be the closest to what you're looking for")
                    elif v[0] != None and v[1] != None:
                        print("Yeah, seems like "+str(v[0])+" or "+str(v[1])+" may be the closest to what you're looking for")
                break


            #checks, whether tmp is 1 and if yes and i is also 1, either displays the message down below, or returns 0 
            #should i not be 1 it just displays the result
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
