def main():
    n = int(input("n = "))
    i = 1
    function(i, n)

def function(i, n):
    if(n >= i):
        print(i)
        i += 1
    else:
        return()
    function(i, n)

main()