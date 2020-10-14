# 01000010111110100100000000000000 = 125.125
# 01000101101110110001100000000000 = 5987
# 01000111101010111100100110101001 = 87955.3203125
# 11111111100000000000000000000000 = -inf
# 01111111100000000000000000000000 = inf
# 10000000000000000000000000000000 = -0
s = input()

# 正負號判斷 0是正數 1是負數
sign = 1
if s[0] == '1':
    sign = 1
else:
    sign = -1

# 指數判斷 10000101 這段轉成二進制後-127
exp = int(s[1:9], 2)-127

# 這段只是取得尾數是不是0而已 給下面的特殊情況判斷用的
is_mantissa_all_zero = True
for i in s[10:32]:
    if i == '1':
        is_mantissa_all_zero = False
        break


if exp == 128 and is_mantissa_all_zero: # 正負無限大特殊判斷
    if sign == 1:
        ans = '-inf'
    else:
        ans = 'inf'
elif exp == -127 and is_mantissa_all_zero: # 正0負0判斷
    if sign == 1:
        ans = '-0'
    else:
        ans = '0'
elif exp == 128 and not is_mantissa_all_zero:
    ans = 'nan'
else:
    start = exp # 從exp次方開始計算
    ans = 0
    for i in '1'+s[9:32]: # + '1'是因為IEEE754的尾數其實是 1.尾數 組合的
        if i == '1':
            ans += 2**start
        start -= 1

print(ans)
