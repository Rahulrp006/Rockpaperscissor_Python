import random
print("*******************************************")
print("*        *PAPER * ROCK * SCISSOR*         *")
print("*******************************************")
print("lets start the game!!..............")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>5):
        print("#######################")
        print("total match:",ma)
        print("human score:",hs)
        print("ai score:",cs)
        if (hs>cs):
            print("congrats you won")
        elif(cs>hs):
            print("ai won...better luck next time")
        else:
            print("match draw")
           print("########################")
           break
    c=input("choose paper->p  rock->r  scissor->s stop->stop:")
    if(c=="p"):
        print("paper")
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs=hs+1
                print("human: paper","ai:rock")
                print("match",ma,"human score:",hs,"ai score:",cs )
                print("humna: win ","ai:lost ")
                print("-----------------------")
            case 12:
                ma=ma+1
                cs=cs+1
                print("human: paper","ai:scissor")
                print("humna: lost ","ai: won ")
                print("-----------------------")
            case 13:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("human: paper","ai:paper")
                print("match draw ")
                print("-----------------------")
   if(c=="p")
    elif(c=="r"):
        print("rock")
    elif(c=="s"):
        print("scissor")
    elif(c=="stop"):
        break
print("program end")    
    