#This dictionary cointains the keys for ordering cards.
SORT_ORDER = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12}

def isRoyalFlush(hand): #tiene que llegarle la hand sorteada
    suit=hand[0][-1:]
    expected=["10","J","Q","K","A"]
    for i in range(5):
        if (not hand[i][:-1] == expected[i]) or (not hand[i][-1:]==suit):    
            return False
    return True

def isStraightFlush(hand):
    suit=hand[0][-1:]
    for i in range(1,5):
        if not hand[i][-1:]==suit:
            return 0
    if SORT_ORDER[hand[1][:-1]]==SORT_ORDER[hand[0][:-1]]+1 and SORT_ORDER[hand[2][:-1]]==SORT_ORDER[hand[1][:-1]]+1 and SORT_ORDER[hand[3][:-1]]==SORT_ORDER[hand[2][:-1]]+1 and SORT_ORDER[hand[4][:-1]]==SORT_ORDER[hand[3][:-1]]+1:
        return SORT_ORDER[hand[0][:-1]]
    return 0

def isFourOfAKind(hand):
    if SORT_ORDER[hand[2][:-1]]==SORT_ORDER[hand[1][:-1]] and SORT_ORDER[hand[3][:-1]]==SORT_ORDER[hand[2][:-1]] and (SORT_ORDER[hand[4][:-1]]==SORT_ORDER[hand[3][:-1]] or SORT_ORDER[hand[1][:-1]]==SORT_ORDER[hand[0][:-1]]):
        return SORT_ORDER[hand[2][:-1]]
    return 0

def isFullHouse(hand):
    twoThree = SORT_ORDER[hand[1][:-1]]==SORT_ORDER[hand[0][:-1]] and SORT_ORDER[hand[3][:-1]]==SORT_ORDER[hand[2][:-1]] and SORT_ORDER[hand[4][:-1]]==SORT_ORDER[hand[3][:-1]]
    threeTwo = SORT_ORDER[hand[1][:-1]]==SORT_ORDER[hand[0][:-1]] and SORT_ORDER[hand[2][:-1]]==SORT_ORDER[hand[1][:-1]] and SORT_ORDER[hand[4][:-1]]==SORT_ORDER[hand[3][:-1]]
    if twoThree or threeTwo:
        vals=[]
        out=[0,0]
        for i in hand:
            vals.append(i[:-1])
        extra=set(vals)        
        for i in extra:
            vals.remove(i)
            vals.remove(i)
            if i in vals:
                out[0]=i
            else:
                out[1]=i
        return out
    return 0

def isFlush(hand):
    suit=hand[0][-1:]
    for i in range(1,5):
        if not hand[i][-1:]==suit:
            return False
    return True

def isStraight(hand):
    if SORT_ORDER[hand[1][:-1]]==SORT_ORDER[hand[0][:-1]]+1 and SORT_ORDER[hand[2][:-1]]==SORT_ORDER[hand[1][:-1]]+1 and SORT_ORDER[hand[3][:-1]]==SORT_ORDER[hand[2][:-1]]+1 and SORT_ORDER[hand[4][:-1]]==SORT_ORDER[hand[3][:-1]]+1:
        return SORT_ORDER[hand[0][:-1]]
    return 0

def isThreeOfAKind(hand):
    if (SORT_ORDER[hand[2][:-1]]==SORT_ORDER[hand[1][:-1]] and SORT_ORDER[hand[3][:-1]]==SORT_ORDER[hand[2][:-1]]) or (SORT_ORDER[hand[4][:-1]]==SORT_ORDER[hand[3][:-1]] and SORT_ORDER[hand[3][:-1]]==SORT_ORDER[hand[2][:-1]]) or (SORT_ORDER[hand[2][:-1]]==SORT_ORDER[hand[1][:-1]] and SORT_ORDER[hand[1][:-1]]==SORT_ORDER[hand[0][:-1]]):
        return SORT_ORDER[hand[2][:-1]]
    return 0

def isTwoPairs(hand):
    vals=[]
    ab=[]
    for i in hand:
        vals.append(i[:-1])
    extra=set(vals)
    for i in extra:
        vals.remove(i)
        if i in vals:
            ab.append(i)
        vals.append(i)
    if len(set(vals))==3:
        return ab
    return 0

def isOnePair(hand):
    vals=[]
    a=""
    for i in hand:
        vals.append(i[:-1])
    extra=set(vals)
    for i in extra:
        vals.remove(i)
        if i in vals:
            a=i
        vals.append(i)
    if len(set(vals))==4:
        return SORT_ORDER[a]
    return 0

def HighCard(hand1, hand2):
    for i in range(4,-1,-1):
        if SORT_ORDER[hand1[i][:-1]]>SORT_ORDER[hand2[i][:-1]]:
            return 1
        elif SORT_ORDER[hand1[i][:-1]]<SORT_ORDER[hand2[i][:-1]]:
            return 0
    return 1


def sortHand(hand): #sort cards from lower to greater value
    return sorted(hand, key=lambda val: SORT_ORDER[val[:-1]])

deck=open("poker.txt","r")
p1wins=0
for line in deck:
    cards=line.replace('\n',"").split(" ")
    hand1=[]
    hand2=[]
    for i in range(10):
        if i<=4:
            hand1.append(cards[i])
        else:
            hand2.append(cards[i])
    hand1=sortHand(hand1)
    hand2=sortHand(hand2)
    print("-------------------·")
    print("hand1: "+str(hand1))
    print("hand2: "+str(hand2))

    tmp1=isRoyalFlush(hand1)
    tmp2=isRoyalFlush(hand2)

#-----------------Royal Flush----------------
    if tmp1 or tmp2:
        print("royalflush")
        if tmp1:
            p1wins+=1

#--------------Straight Flush----------------
    else:
        tmp1=isStraightFlush(hand1)
        tmp2=isStraightFlush(hand2)
        if tmp1 or tmp2:
            print("straightflush")
            if tmp1>tmp2:
                p1wins+=1

#--------------Four Of A Kind----------------
        else:
            tmp1=isFourOfAKind(hand1)
            tmp2=isFourOfAKind(hand2)
            if tmp1 or tmp2:
                print("poker")
                if tmp1>tmp2:
                    p1wins+=1
                elif tmp1==tmp2:
                    p1wins+=HighCard(hand1, hand2)
            
#--------------Full House----------------
            else:
                tmp1=isFullHouse(hand1)
                tmp2=isFullHouse(hand2)
                if (not tmp1==0) or (not tmp2==0):
                    print("Full")
                    if (not tmp1==0) and (not tmp2==0):
                        if tmp1[0]>tmp2[0]:
                            p1wins+=1
                        elif tmp1[0]==tmp2[0]:
                            if tmp1[1]>tmp2[1]:
                                p1wins+=1
                            elif tmp1[1]==tmp2[1]:
                                p1wins+=HighCard(hand1, hand2)
                    elif not tmp1==0:
                        p1wins+=1

#--------------------Flush----------------     
                else:
                    tmp1=isFlush(hand1)
                    tmp2=isFlush(hand2)
                    if tmp1 or tmp2:
                        print("flush")
                        if tmp1 and tmp2:
                            p1wins+=HighCard(hand1,hand2)
                        elif tmp1:
                            p1wins-=1
                    
#--------------------Straight----------------  
                    else:
                        tmp1=isStraight(hand1)
                        tmp2=isStraight(hand2)
                        if tmp1 or tmp2:
                            print("straight")
                            if tmp1>=tmp2:
                                p1wins+=1
                        
#--------------------Three Of A Kind----------------
                        else:
                            tmp1=isThreeOfAKind(hand1)
                            tmp2=isThreeOfAKind(hand2)
                            if tmp1 or tmp2:
                                print("trio")
                                if tmp1>tmp2:
                                    p1wins+=1
                                elif tmp1==tmp2:
                                    p1wins+=HighCard(hand1, hand2)
                            
#--------------------Two Pairs----------------  
                            else:
                                tmp1=isTwoPairs(hand1)
                                tmp2=isTwoPairs(hand2)
                                if (not tmp1==0) or (not tmp2==0):
                                    print("doblepareja")
                                    if (not tmp1==0) and (not tmp2==0):
                                        if max(tmp1) > max(tmp2):
                                            p1wins+=1
                                        elif max(tmp1) == max(tmp2):
                                            if min(tmp1)>min(tmp2):
                                                p1wins+=1
                                            elif min(tmp1)==min(tmp2):
                                                p1wins+=HighCard(hand1, hand2)
                                    elif (not tmp1==0):
                                        p1wins+=1
                                
#--------------------One Pairs----------------
                                else:
                                    tmp1=isOnePair(hand1)
                                    tmp2=isOnePair(hand2)
                                    if tmp1 or tmp2:
                                        print("pareja")
                                        if tmp1>tmp2:
                                            p1wins+=1
                                        elif tmp1==tmp2:
                                            p1wins+=HighCard(hand1, hand2)
                                    
    #--------------------Highest Card----------------
                                    else:
                                        print("cartalata")
                                        p1wins+=HighCard(hand1, hand2)
print(p1wins)





        

