def main():
    a = int(input("enter the values of the edges one at a time:")) 
    b = int(input())
    c = int(input())
    print(("they are in error","they are correct triangle sides lengths")[(a+b )> c and (a+c) > b and (c+b) > a ]) 


if __name__ == '__main__':
    main()