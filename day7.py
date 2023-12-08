powers = {"A":1.03, "K":1.02, "Q":1.01,  "T":0.99, "9":0.98, "8":0.97, "7":0.96, "6":0.95, "5":0.94, "4":0.93, "3":0.92, "2":0.91,"J":0.9}

file1 = open('data', 'r')
lines = file1.readlines()
data = []
for line in lines:
    d = line.split(" ")
    data.append((d[0], int(d[1])))

class  obj():
    def __init__(self,hand, bet):
        singles = 0
        doubles = 0
        trips = 0
        score = 0
        quads = 0
        five = 0
        j = 0
        no = 0
        self.values = []
        offsets = [10000, 1000, 100, 10, 1]
        hand2 = hand
        highest = 0
        lowest = 100
        idx = 0
        idx2 = 0
        for i,c in enumerate(hand):
            count = hand.count(c)
            if count > highest:
                highest = count
                idx = i
            if count < lowest:
                lowest = count
                idx2 = i   
        for hand.count("J"):
            
        
        
            hand2.replace()
        for i,c in enumerate(hand):
            count = hand.count(c)
            self.values.append(powers[c])
            if c != "J":
                if count == 2:
                    singles +=1
                if count == 3:
                    trips +=1
                if count == 4:
                    quads +=1
                if count == 5:
                    five +=1
            #score += powers[c] * offsets[i]
        

        
        
        
        
        
        
        

        if five:
            score += 100000000000000000000    
        if quads:
            score += 1000000000000000000     
        if trips and singles:
            score += 10000000000000000
        elif trips:
            score += 100000000000000
        if singles > 2:
            score += 10000000000
        if singles == 2:
            score += 100000000
        self.score = score
        self.bet = bet
        self.hand = hand
        
        
    
        



"""
data = [
("32T3K", 765),
("T55J5", 684),
("KK677", 28),
("KTJJT", 220),
("QQQJA", 483)
]
"""
objects = []
for item in data:
    objects.append(obj(item[0],item[1]))


# result = sorted(data, key = lambda x: (x[1], x[2]))

#objects.sort(key=lambda x: x.score, reverse=False)


objects.sort(key=lambda x: (x.score, x.values[0], x.values[1], x.values[2], x.values[3], x.values[4]), reverse=True)
#for i in range(5):
#objects.sort(key=lambda x: x.values[i], reverse=False)

ssum = 0
objects.reverse()
for i,object in enumerate(objects):
    print(object.score ,object.hand, object.bet*(i+1))
    ssum += object.bet*(i+1)
print(ssum)
    
    
    
    
"""
(765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5)


    32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
    KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
    T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
251682462
252946551

"""