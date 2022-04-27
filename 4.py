#while b > a:
#    if(arr[a] >= buffer):
#        buffer = arr[a]
#    a += 1

#print(buffer)

def main():
    arr = [1, 2, 3, 4, 5, 66, 7, 8]
    print(arr)
    a = 0
    b = sum(True for i in arr)
    buffer = arr[0]
    function(a, b, buffer, arr)

def function(a, b, buffer, arr):
    if(b > a):
        if (arr[a] >= buffer):
            buffer = arr[a]
        a += 1

    else:
        return(print(buffer))
    function(a, b, buffer, arr)

main()