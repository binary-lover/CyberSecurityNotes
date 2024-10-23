# xor of two strings and resutlant string is given


def xor(s1, s2):
    return hex(int(s1, 16) ^ int(s2, 16))[2:]



s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"
s3 = xor(s1, s2)
print(s3) # 746865206b696420646f6e277420706c6179
