file1 = open('data', 'r')
lines = file1.readlines()
ssmap = []
st = []
seeds = []
do_sts = 0
do_stf = 0
do_ftw = 0
do_wtl = 0
do_ltt = 0
do_tth = 0
do_htl = 0
sts = []
stf = []
ftw = []
wtl = []
ltt = []
tth = []
htl = []
def line_to_num(line):
    nums = []
    nm = line.split(" ")
    for n in nm:
        if len(n) > 0 and n != " ":
            nums.append(int(n))
    return nums
for line in lines:
    line = line.strip()
    if len(line) < 3:
        do_sts = 0
        do_stf = 0
        do_ftw = 0
        do_wtl = 0
        do_ltt = 0
        do_tth = 0
        do_htl = 0       
    elif "seeds:" not in line:
        try:
            ssmap.append(line_to_num(line))
        except:
            pass
        
    if do_sts:
        sts.append(line_to_num(line))
    elif do_stf:
        stf.append(line_to_num(line))
    elif do_ftw:
        ftw.append(line_to_num(line))   
    elif do_wtl:
        wtl.append(line_to_num(line))      
    elif do_ltt:
        ltt.append(line_to_num(line))
    elif do_tth:
        tth.append(line_to_num(line))   
    elif do_htl:
        htl.append(line_to_num(line))       
    if "seeds" in line:
        st = line.split("seeds:")[1].split(" ")
    if "seed-" in line:
        do_sts = 1
    if "soil-" in line:
        do_stf = 1       
    if "fertilizer-" in line:
        do_ftw = 1       
    if "water-" in line:
        do_wtl = 1
    if "light-" in line:
        do_ltt = 1        
    if "temperature-" in line:
        do_tth = 1        
    if "humidity-" in line:
        do_htl = 1      
for s in st:
    if len(s) > 0:
        seeds.append(int(s))
new_seeds = []
for x in range(0,len(seeds)-1,2):
    new_seeds.append((seeds[x],seeds[x]+seeds[x+1]))
print(new_seeds)
stuff = [sts,stf,ftw,wtl,ltt,tth,htl]
lowest = 100000000000000
l = 148000000
stuff.reverse()
actually_lowest = 100000000000000
locations = [l]
done = 0
while not done:
    for inp in locations:
        for k in stuff:
            k.reverse()
            for m in k:
                dst = m[1]
                src = m[0]
                rng = m[2]
                if inp >= src and inp < src+rng:
                    inp = dst + inp - src
                    break
        lowest = inp
    for seed in new_seeds:
        if lowest >= seed[0] and lowest <= seed[1]:
            actually_lowest = lowest
            done = 1
            break
    locations[0]+=1
    print(locations[0])
print("lowest",locations[0]-1,actually_lowest)
