def main():
    n = int(input("n = "))
    i = 1
    function(n, i)

def function(n, i):
    if (n >= i):
        print("*" * i)
        i += 1
    else:
        return()
    function(n, i)

main()