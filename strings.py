# 147
# s = str(input())
# print(s.count('A'), s.count('Y'), sep='\n')

# 148
# s = map(str, input().split())
# for i in s:
#     if i.startswith("A"):
#         print(i)

# 149
# s = input().split()
# c = 0
# for i in s:
#     if i.endswith("NA"):
#         c += 1
# print(c)
# for i in s:
#     if i.endswith("NA"):
#         print(i)

# 150
# s = input().split()
# word = ''
# for i in s:
#     if 'info' in i.lower():
#         word += i + ' '
# print(word.strip())
# 151
# a = ['a', 'o', 'i', 'e', 'u']
# count = 0
# s = input()
# for i in s:
#     if i.lower() in a:
#         count += 1
#
# print(count)

# 152
# s = input().split()
# r = ''
# for i in s[::-1]:
#     r += i[::-1] + ' '
# print(r.strip())

# 153
# s = input().split()
# for i in s:
#     print(i, len(i))

# 154
# s = int(input())
# sum = 0
# for i in str(s):
#     sum += int(i)
# print(sum)

# 155
# s = input().split()
# count = 0
# for i in s:
#     if i[0].isupper():
#         count += 1
#
# print(count)

# 156
# def multiple_input():
#     """
#     Read multiple inputs
#     """
#     s = input()
#     i, j = map(int, input().split())
#     return s, i, j
# s, i, j = multiple_input()
# w = s.split()
# def swap(list, i, j):
#     i, j = i - 1, j - 1
#     list[i], list[j] = list[j], list[i]
#     return list
# swap(w, i, j)
# print(" ".join(w).strip())

# 157

# def replace_i(list, i):
#     i = i - 1
#     list[i] = 'TATU'
#     return list
#
#
# def multiple_input():
#     """
#     Read multiple inputs
#     """
#     s = input()
#     i = int(input())
#     return s, i
#
#
# s, i = multiple_input()
# w = s.split()
# w = replace_i(w, i)
# print(" ".join(w).strip())

# 158
# s = input().split()
# j, t = 0, 0
# for i in s:
#     if len(i) % 2 == 0:
#         j += 1
#     else:
#         t += 1
# print(j * t)

# 159
# s = input().split()
# count = 0
# for i in s:
#     if i.lower().startswith("a") and i.lower().endswith("b"):
#         count += 1
#
# print(count)

# 160
# print(input().swapcase())

# 161

# def multiple_input():
#     i = int(input())
#     s = input()
#     return i, s
#
# i, s = multiple_input()
# d = s.split()
# data = 'ASSALOM'
# for item in d:
#     index = data.find(item)
#     if index != -1:
#         data = data[:index] + data[index + 1:]
#
# if data:
#     print("NO")
# else:
#     print("YES")

# 162
# def multiple_input():
#     i = int(input())
#     s = input()
#     return i, s
#
# print(multiple_input()[1].replace('$', ''))

# 163
# print(max(map(lambda x: (len(x), x), input().replace("’", "").split()))[1])

# 164
# def multiple_input():
#     s = input()
#     l, r = map(int, input().split())
#     return s, l, r
#
# s, l, r = multiple_input()
# if r > l:
#     print(s[l - 1:r])
# else:
#     w = s[::-1]
#     L = len(w) - l
#     R = len(w) - r
#     print(w[L:R+1])

