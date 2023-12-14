#1----------------------------------------------------------------------------------------------------------------------

# a = input().split()
# counter = 0
# k = 0

# for i in a:
#     k, b = i, k
#     if i != b:
#         counter += 1

# print(counter)


#2----------------------------------------------------------------------------------------------------------------------

# a = input().split()
# b = int(input())
# counter = 1
#
# for i in range(len(a)):
#     a[i] = int(a[i])
#
# for j in a:
#     if b <= j:
#         counter +=1
#     else:
#         break
#
# print(counter)


#3----------------------------------------------------------------------------------------------------------------------

# n = int(input())
# m = int(input())
# a = []
# for i in range(n):
#     a.append([])
#     for j in range(m):
#         if i == 0 or j ==0:
#             a[i].append(int('1'))
#         else:
#             g = a[i-1][j] + a[i][j-1]
#             a[i].append(g)
#
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end='\t')
#     print('\n')


#4----------------------------------------------------------------------------------------------------------------------
# import random
# # Масиив енгизудн кереги жок
#
# n = int(input())
# m = int(input())
# a = []
#
# for i in range(n):
#     a.append([])
#     for j in range(m):
#         a[i].append(random.randint(1, 99))
#
# print("Массив:")
#
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end='\t')
#     print('\n')
#
# print("Результат:")
#
# for j in range(m):
#     for i in range(n):
#         print(a[i][j], end='\t')
#     print('\n')