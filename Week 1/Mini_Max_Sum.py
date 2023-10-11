def miniMaxSum(arr):
    # Sort the array in ascending order
    arr.sort()

    # Calculate minval and maxval
    minval = sum(arr[:-1])  # Sum all elements except the last one for minimum sum
    maxval = sum(arr[1:])   # Sum all elements except the first one for maximum sum

    print(minval, maxval)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)