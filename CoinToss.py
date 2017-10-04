import random

def CoinToss(y):
    hcount = 0      # outside of the for loop so that the value is not lost when the for loop runs.
    tcount = 0
    for i in range(0,y):
        toss = random.randint(0, 100)
        if toss in range(0,50):
            out ="Heads"
            hcount += 1
        elif toss in range(50,100):
            out ="Tails"
            tcount += 1
        print "attempt #", i, "throwing coin..", "it's", out, "got", hcount, "(s) so far and ", tcount, "tail(s) so far"
    else:
        print "ending program, thank you!"
CoinToss(5001)



