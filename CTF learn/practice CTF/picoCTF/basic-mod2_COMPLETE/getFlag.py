file = open('message.txt','r')
content = file.read().split()

a=[]
for t in content:
    a+=[pow(int(t)%41,-1,41)]  

b = ''

for t in a:
    if t<=26:
        b+=chr(t+64)
    elif t == 37:
        b+='_'
    else:
        b+=str(t-27)

print('picoCTF{'+b+'}')
