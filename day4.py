file1 = open('data', 'r')
lines = file1.readlines()
count = 0
ssum = 0
for k,line in enumerate(lines):
    line = line.strip()
    d = line.split(":")[1].split("|")
    winning = d[0].split(" ")
    my = d[1].split(" ")
    print(winning, my)
    i = 0
    mmax = 1
    local = 0
    for m in my:
        if len(m)>0 and m in winning:
            print(m)
            print(mmax)
            local =mmax
            print("seq",m)
            mmax*=2
        elif len(m)>0:
            pass
            #mmax = 1

    ssum += local
    print("max",mmax)
print(ssum)
