duplicates_2 = [1, 1, 1]
duplicates_3 = [1, 0, 0, 0]
duplicates_4 = [1, 2, 3, 1, 3, 6, 6]
duplicates_5 = [1, 2, 3, 1, 3, 0, 0]
duplicates_6 = [0, 0, 1]
duplicates_7 = [3, 2, 0, 1]

ex = [duplicates_2, duplicates_3,
      duplicates_4, duplicates_5, duplicates_6, duplicates_7]


def find_duplicates_n_square(l):
    ans = []
    n = len(l)
    j = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[i] == l[j]:
                if l[i] not in ans:
                    ans.append(l[i])
                else:
                    break
    print(ans)


def find_duplicates_n_complexity_n_space(l):
    ans = []
    y = []
    x = []
    n = len(l)
    for i in range(n):
        x.append(-1)
        y.append(-1)
    for i in l:
        if x[i] == -1:
            x[i] = i
        else:
            y[i] = i

    for i in y:
        if i != -1:
            ans.append(i)
    print(ans)


# for l in ex:
#     find_duplicates_n_square(l)

# for l in ex:
#     find_duplicates_n_complexity_n_space(l)


duplicates_4 = [1, 3, 3, 1, 2, 6, 6]


def findDuplicates(nums):
    n = len(nums)
    ans = []

    for i in range(n):
        nums[abs(i)-1] *= -1
    print(nums)


print(findDuplicates(duplicates_4))
