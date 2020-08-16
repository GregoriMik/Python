import random as r
tmp = []
nums = []
for i in range(6):
    rdn = r.randint(1, 49)
    while True:
        if rdn not in tmp:
            print(rdn)
            nums.append(rdn)
            break
        else:
            rdn = r.randint(1, 50)
            tmp.append(rdn)
sorted_nums = sorted(nums)
print(sorted_nums)

# import random as r
# tmp = []
# nums = []
# for i in range(6):
#     rdn = r.randint(1, 50)
#     while True:
#         if rdn not in tmp:
#             print(rdn)
#             nums.append(rdn)
#             break
#         else:
#             rdn = r.randint(1, 50)
#         tmp.append(rdn)
# sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)


# if a > b:
#     a, b = b, a
# print(a, b, c, d, e, f)
# if a > c:
#     a, c = c, a

# if a > d:
#     a, d = d, a
# print(a, b, c, d, e, f)
# if a > e:
#     a, e = e, a
# print(a, b, c, d, e, f)
# if a > f:
#     a, f = f, a
# print(a, b, c, d, e, f)                             SORTOWANIE BOMBELKOWE
# if b > c:
#     b, c = c, b
# print(a, b, c, d, e, f)
# if b > d:
#     b, d = d, b
# print(a, b, c, d, e, f)
# if b > e:
#     b, e = e, b
# print(a, b, c, d, e, f)
# if b > f:
#     b, f = f, b
# print(a, b, c, d, e, f)
# if c > d:
#     c, d = d, c
# Duzy lotek od 1 do 49, 6 liczb
