def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    buffer = sum(True for i in arr)
    i = 0
    total = 0
    function(arr, buffer, i, total)

def function(arr, buffer, i, total):
    if(buffer > i):
        total += arr[i]
        i += 1
    else:
        return(print(total))
    function(arr, buffer, i, total)

main()