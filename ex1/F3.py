
def check_seq(arr:list):
    if(len(arr) == 1 and arr[0] == ''):
        return True
    for i in arr : 
        if not i.replace(".","").isdigit():
            return False
    return True

def main():
   arr = input("Enter a tuple of numbers, please:\n")
   arr = arr.strip(" [](){}").split(",")
   if(check_seq(arr)):
       if(len(arr) == 1 and arr[0] == ''): 
           print("()")
           return
       arr = [(int(float(i)),float(i))['.' in i ] for i in arr ]
       arr.sort()
       if(len(arr) >= 2 ):
           print( tuple(arr[len(arr)//2 - 1 : len(arr)//2 + 1 ]))
       else:
            print(tuple(arr))
   else: 
        print("the input must be a tuple of numbers")
      

        
if __name__ == '__main__':
    main()