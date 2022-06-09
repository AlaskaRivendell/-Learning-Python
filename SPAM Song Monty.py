from random import shuffle

liste = "amazing excited gorgeous vibrant blazing fast stunning bold \
    stunning biggest fastest tremendous greatest best phenomenal \
    delightful outstanding fantastic magical revolutionary incredible \
        amazing profound screaming jaw-dropping".upper().split()
shuffle(liste)

for strophe in range(5):
    for n in range (2):
        for i in range (4):
            print("SPAM ",end='')
        print()
        el1 = liste.pop()
        el2 = liste.pop()   
        
    print("{} SPAM, {} SPAM".format(el1, el2)) #most readable solution!
    print()