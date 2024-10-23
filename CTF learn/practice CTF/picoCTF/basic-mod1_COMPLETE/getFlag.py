
file = open('message.txt','r')
content = file.read().split()
for i in range(len(content)):
    content[i] = int(content[i]) %37
flag = ''

for i in content:
    if i<26:
        flag+=chr(i+65)
    elif i < 36:
        num = i - 26
        flag+=str(num)
    elif i == 36:
        flag+='_'

print(f'picoCTF{{{flag}}}')