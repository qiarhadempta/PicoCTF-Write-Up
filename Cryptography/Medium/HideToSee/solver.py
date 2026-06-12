ciphertext = "krxlXGU{zgyzhs_xizxp_1u84w779}"
dict_small = "abcdefghijklmnopqrstuvwxyz"
dict_large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

flag = ""
for char in ciphertext:
    if char in dict_small:
        flag += dict_small[25 - dict_small.index(char)]
    elif char in dict_large:
        flag += dict_large[25 - dict_large.index(char)]
    else:
        flag += char

print(flag)
