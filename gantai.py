def find_end_parantiz(a):
    for i in range(len(a)):
        if a[i]==")":
            ans2,andis = find_open_parantiz(a,i)
            ans2 = calculate_zarb(ans2)
            ans2 = calculate_tagsim(ans2)
            ans2 = calculate_menha(ans2)
            ans2 = calculate_jam(ans2)
            return ans2,i,andis
def find_open_parantiz(a,end):
    for i in range(end,-1,-1):
        if a[i]=="(":
            betweeen = split_between(a,i,end)
            return betweeen,i
def split_between(a,i,end):
    ans1 = ""
    for i in range(i+1,end):
        ans1 = ans1 + a[i]
    return ans1

#***********************************************************
def calculate_zarb(b): #mohasebe tamam zarb ha va jaigozari
    yoyo = ""
    for i in range(len(b)):
            if b[i]=="*":
                break
            elif i==len(b)-1:
                return(b)
    for i in range(len(b)):
            if b[i]=="*":
                x,y,end,start = numbers_for_zarb(b,i)
                x = float(x)
                y= float(y)
                extra = x*y
                break
    i=0
    while i!=len(b):
            
            if i==start+1:
                yoyo = yoyo+str(extra)
                i = end
            else:
                yoyo = yoyo + b[i]
                i+=1
    return calculate_zarb(yoyo)
def numbers_for_zarb(b,zarb):
    for i in range(zarb+1,len(b)):
        if b[i]=="+" or b[i]=="*" or b[i]=="m" or b[i]=="/" or i==len(b)-1:
            if i==len(b)-1:
                y = b[zarb+1:i+1]
                i = i+1
            else:
                y = b[zarb+1:i]
            break
    for j in range(zarb-1,-1,-1):
        if b[j]=="+" or b[j]=="*" or b[j]=="m" or b[j]=="/" or j==0:
            if j==0:
                x= b[j:zarb]
                j = j-1
            else:
                x = b[j+1:zarb]
            break
    return x,y,i,j

#####################################################
def calculate_tagsim(b):
    yoyo = ""
    for i in range(len(b)):
            if b[i]=="/":
                break
            elif i==len(b)-1:
                return(b)
    for i in range(len(b)):
            if b[i]=="/":
                x,y,end,start = numbers_for_tagsim(b,i)
                x = float(x)
                y= float(y)
                extra = x/y
                break
    i=0
    while i!=len(b):
            
            if i==start+1:
                yoyo = yoyo+str(extra)
                i = end
            else:
                yoyo = yoyo + b[i]
                i+=1
    return calculate_tagsim(yoyo)

def numbers_for_tagsim(b,tagsim):
    for i in range(tagsim+1,len(b)):
        if b[i]=="+" or b[i]=="*" or b[i]=="m" or b[i]=="/" or i==len(b)-1:
            if i==len(b)-1:
                y = b[tagsim+1:i+1]
                i = i+1
            else:
                y = b[tagsim+1:i]
            break
    for j in range(tagsim-1,-1,-1):
        if b[j]=="+" or b[j]=="*" or b[j]=="m" or b[j]=="/" or j==0:
            if j==0:
                x= b[j:tagsim]
                j = j-1
            else:
                x = b[j+1:tagsim]
            break
    return x,y,i,j
#####################################################
def calculate_jam(b):
    yoyo = ""
    for i in range(len(b)):
            if b[i]=="+":
                break
            elif i==len(b)-1:
                return(b)
    for i in range(len(b)):
            if b[i]=="+":
                x,y,end,start = numbers_for_jam(b,i)
                x = float(x)
                y= float(y)
                extra = x+y
                break
    i=0
    while i!=len(b):
            
            if i==start+1:
                yoyo = yoyo+str(extra)
                i = end
            else:
                yoyo = yoyo + b[i]
                i+=1
    return calculate_jam(yoyo)

def numbers_for_jam(b,jam):
    for i in range(jam+1,len(b)):
        if b[i]=="+" or b[i]=="*"  or b[i]=="/" or i==len(b)-1:
            if i==len(b)-1:
                y = b[jam+1:i+1]
                i = i+1
            else:
                y = b[jam+1:i]
            break
    for j in range(jam-1,-1,-1):
        if b[j]=="+" or b[j]=="*" or b[j]=="/" or j==0:
            if j==0:
                x= b[j:jam]
                j = j-1
            else:
                x = b[j+1:jam]
            break
    return x,y,i,j
###################################################
def calculate_menha(b):
    yoyo = ""
    for i in range(len(b)):
            if b[i]=="m":
                break
            elif i==len(b)-1:
                return(b)
    for i in range(len(b)):
            if b[i]=="m" and b[i-1]!="+":
                x,y,end,start = numbers_for_menha(b,i)
                x = float(x)
                y= float(y)
                extra = x-y
                break
    i=0
    while i!=len(b):
            
            if i==start+1:
                yoyo = yoyo+str(extra)
                i = end
            else:
                yoyo = yoyo + b[i]
                i+=1
    return calculate_menha(yoyo)

def numbers_for_menha(b,menha):
    for i in range(menha+1,len(b)):
        if b[i]=="+" or b[i]=="*" or b[i]=="m" or b[i]=="/" or i==len(b)-1:
            if i==len(b)-1:
                y = b[menha+1:i+1]
                i = i+1
            else:
                y = b[menha+1:i]
            break
    for j in range(menha-1,-1,-1):
        if b[j]=="+" or b[j]=="*" or b[j]=="m" or b[j]=="/" or j==0:
            if j==0:
                x= b[j:menha]
                j = j-1
            else:
                x = b[j+1:menha]
            break
    return x,y,i,j
#######################################################
def parantiz_for_manfi(a):
    andis1 = 0
    andis2 = 0
    for i in range(len(a)):
        if a[i]=="-" and a[i-1]=="(":
            for j in range(i,len(a)):
                if a[j]==")":
                    andis1 = i-1
                    andis2 = j
                    break
            break
    yoyo = ""
    z=0
    while z!=len(a):
        if z==andis1:
            yoyo = yoyo+a[andis1+1:andis2]
            z=andis2+1
        else:
            yoyo = yoyo+a[z]
            z+=1
    a = yoyo
    return a