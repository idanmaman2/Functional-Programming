
def check(arr:list):

    for i in arr:
        if not i.replace(".","").isdigit():
            return False
            
    return (len(arr) == 4)

def main():
    arr = input("Enter a list of 4 numbers, please:")
    arr = arr.strip("[ ]").split(",")
    if(check(arr)):
        arr = [(int(float(i)),float(i))['.' in i ] for i in arr]  
        arr.sort()
        #arr.pop(arr.index(arr.min()))
        #arr.pop(arr.index(arr.max()))
        print(arr[1:3])

    else : 
        print("the input must be a list of 4 numbers")


if __name__ == '__main__':
    main()