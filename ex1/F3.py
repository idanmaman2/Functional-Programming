
def check_seq(arr:list):
    for i in arr : 
        if not i.replace(".","").isdigit():
            return False
    return True


def main():
   arr = input()
   arr = arr.strip("[ ]").split(",")
    if(check_seq(arr)):
        
if __name__ == '__main__':
    main()