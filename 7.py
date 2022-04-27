def main():
    y = int(input("Num = "))
    x = int(input("^ = "))
    i = 1
    aa = 1
    function(x, y, i, aa)

def function(x, y, i, aa):
    if(x >= i):
        i += 1
        aa *= y
    else:
        print(aa)
        return()
    function(x, y, i, aa)
main()