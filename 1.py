def main():
    n = int(input("n = "))
    i = 1
    first(n, i)

def first(n, i):
    if(n >= i):
        print(i)
        i += 1
    else:
        return()
    first(n, i)

main()