def main():
    x = int(input("x = "))
    y = int(input("y = "))
    i = 1
    aa = 0
    function(x, y, i, aa)

def function(x, y, i, aa):
    if(x >= i):
        i += 1
        aa += y
    else:
        print(aa)
        return()
    function(x, y, i, aa)
main()