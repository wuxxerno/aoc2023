"""
Time:        56     97     78     75
Distance:   546   1927   1131   1139


"""

a = 546192711311139
b = 56977875
ssum = 0
for d in range(b):
    if d*(b-d) >= a:
        ssum += 1
print(ssum)
