arr =   [[11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]]

print(len(arr))
sum = 0


for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            sum = sum + arr[i][j]

print(sum)

rev_sum = 0


for i in range(len(arr)-1, -1, -1):
    for j in range(len(arr)-1, -1, -1):
        if i == j:
            rev_sum = rev_sum + arr[i][(len(arr)-1-j)]


print(rev_sum)

print(abs(rev_sum-sum))
