# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*recur_factorial(n-1)


# l = []


# def printI(n, reverse):
#     if reverse:
#         while n:
#             if n // 10 != 0:
#                 print(n % 10, end=' ')
#             else:
#                 print(n % 10)
#             n = n // 10
#     else:
#         l = []
#         while n:
#             l.append(n % 10)
#             n = n // 10
#         for i in range(len(l)):
#             print(l[len(l)-i-1], end=' ')
#         print()


# l = []


# def printR(n, reverse):
#     if reverse:
#         if n <= 9:
#             print(n)
#         else:
#             print(n % 10, end=' ')
#             printR(n // 10, True)
#     else:
#         if n <= 9:
#             l.append(n)
#         else:
#             l.append(n % 10)
#             printR(n // 10, False)


# printR(123, True)
# printR(123, False)
# print(l)

# def hop(a, f):
#     if (a[f] == f):
#         return 0
#     # WRITE CODE
#     else:
#         y, z = a[f], a[a[f]]
#         a[f] = z
#         h = hop(a, f)
#         h = h + 1
#         a[f] = y
#     return h


# l = [5, 1, 0, 4, 2, 3]

# print(hop(l, 1))


a = [1, 2, 3, 4, 5, 4, 3, 2, 1]


def find_peak(l):
    peak_exists = False
    for i in range(len(l)):
        if i == 0:
            if l[0] > l[1]:
                peak_exists = True
                return peak_exists
        elif i == len(l) - 1:
            if l[i] > l[i-1]:
                peak_exists = True
                return peak_exists
        else:
            if l[i] > l[i-1] and l[i] > l[i+1]:
                peak_exists = True
                return peak_exists
    return peak_exists


def find_peakR(l):
    if len(l) == 1:
        return True
