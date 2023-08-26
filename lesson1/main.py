# string = "gsnmkks  ssssllll  ssss"
# nums = '1235456452'
# split = string.split('s')
# strp = string.strip()
# print(strp)
# up = string.upper()
# low = string.lower()
# print(up, low)
# isup = string.isupper()
# islow = string.islower()
# tit = string.title()
# print(tit)
# cap = string.capitalize()
# print(cap)
# rep = string.replace('s', 'l')
# print(rep)
# isnum = nums.isnumeric()
# isdiq = nums.isdigit()
# find = string.find('k')
# print(isnum, isdiq, find)
# words = ['let', 'me', 'cook']
# j = string.join(words)
# print(j)



# 2
# n = int(input(': '))
# n = str(n)
# print(len(n))



# 909
# text = input().split()
# print(len(text))




# 8989
# text = input()
# res = ''
# for i in range(len(text)):
#   if text[i] == 'a':
#     res += 'aa'
#   else:
#     res += text[i]
    
# print(res)




# 8977
# s = input()
# p1 = s[2] + s[6] + s[10]
# print(p1)
# p2 = s[0] + s[-2] + s[-1] 
# print(p2)
# p3 = s[:7]
# print(p3)
# p4 = s[4:]
# print(p4)
# p5 = s[1::2]
# print(p5)
# p6 = len(p5)
# print(p6)
# p7 = s[::-1]
# print(p7)



# 119
s = '248163264128'
c = 0
st = 1
for i in range(len(s)):
  f = s.find(str(2**st))
  if f != -1:
    c += 1
    st += 1
  else:
    break
print(c)