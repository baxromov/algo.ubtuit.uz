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
# r = ''
# for i in input().split():
#     if i.lower().startswith("info"):
#         r += i + ' '
# print(r.strip())

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