import gantai

number = input()
number = number.replace(" ","")
user = number
number = number.replace("-","m")
number = number.replace("mm","m-")
number = number.replace("(m","(-")
number = number.replace("+m","+-")
number = number.replace("*m","*-")
number = number.replace("/m","/-")
if number[0]=="m":
    number = number.replace("m","-",1)
for i in range(len(number)):
    if number[i]=="-"and number[i-1]=="(":
        number = gantai.parantiz_for_manfi(number)
yoyo = 0
while True:
    extra_string = ""
    for i in range(len(number)):
        if number[i]=="(":
            break
        elif i==len(number)-1:
            yoyo = 1
            break
    if yoyo==1:
        break
    extra,a,b = gantai.find_end_parantiz(number)
    i = 0
    while i !=len(number):
        
        if i==b:
            extra_string = extra_string + extra
            i=a+1
        else:
            extra_string = extra_string + number[i]
            i+=1
    number = extra_string
yoyo = 0

try:
        number = float(number)
except:
        hmm = ""
        for j in range(len(number)):
            if j==0:
                hmm = hmm+"("
                hmm = hmm + number[j]
            elif j==len(number)-1:
                hmm = hmm+number[j]
                hmm = hmm+")"
                number = hmm
                yoyo = 1
            else: 
                hmm = hmm+number[j]
if yoyo==1:
    number,o,p = gantai.find_end_parantiz(number)
print(number)
f = open("answers.txt","a")
f.write(f"{user} = {number}\n")
f.close()