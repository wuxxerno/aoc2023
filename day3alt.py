file1 = open('data', 'r')
lines = file1.readlines()
count = 0
ssum = 0
for k,line in enumerate(lines):
    cords = []
    for i,c in enumerate(line):
        
        if c == "*":
            try:
                if lines[k-1][i].isdigit():
                    cords.append((k,i,k-1,i))
                    print(k,i,k-1,i)
            except:
                pass                
            try:                
                if lines[k-1][i-1].isdigit():
                    cords.append((k,i,k-1,i-1))
                    print(k,i,k-1,i-1)                    
            except:
                pass     
            try:               
                if lines[k-1][i+1].isdigit():
                    cords.append((k,i,k-1,i+1))
                    print(k,i,k-1,i+1)
            except:
                pass     
            try:                    
                if lines[k][i-1].isdigit():
                    cords.append((k,i,k,i-1))
                    print(k,i,k,i-1)                    
            except:
                pass                 
            try:         
                if lines[k][i+1].isdigit():
                    cords.append((k,i,k,i+1))
                    print(k,i,k,i+1)                          
            except:
                pass                 
            try:
                if lines[k+1][i].isdigit():
                    cords.append((k,i,k+1,i))
                    print(k,i,k+1,i)
            except:
                pass     
            try:             
                if lines[k+1][i-1].isdigit():
                    cords.append((k,i,k+1,i-1))
                    print(k,i,k+1,i-1)                    
            except:
                pass     
            try:            
                if lines[k+1][i+1].isdigit():
                    cords.append((k,i,k+1,i+1))
                    print(k,i,k+1,i+1)
            except:
                pass                        
    numbers = []
    nmap = []
    for cord in cords:
        start = 0
        stop = 0
        for x in range(10):
            try:
                if lines[cord[2]][cord[3]+x].isdigit():
                    stop = cord[3]+x
                else:
                    break
            except:
                pass
                break
        for x in range(10):
            try:
                if lines[cord[2]][cord[3]-x].isdigit():
                    start = cord[3]-x
                else:
                    break
            except:
                pass
                break
        if (start,stop,cord[2]) not in nmap:
            print(start,stop)
            number = int(lines[cord[2]][start:stop+1])
            numbers.append((cord[0],cord[1],number))
            print("number",number)
            nmap.append((start,stop,cord[2]))
    for k,number in enumerate(numbers):
        hits = 0
        tsum = 0
        values = []
        for i,number2 in enumerate(numbers):
            if i != k:
                if number[0] == number2[0] and number[1] == number2[1]:
                    done_k = k
                    values.append(number[2])
                    values.append(number2[2])
        if len(values) == 2:
            print("multiplying:",values[0] , values[1])
            ssum += (values[0] * values[1]/2)
print(ssum)
        
