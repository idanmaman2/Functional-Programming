
def mainF32(arr:list):
    arr.sort()
    if(len(arr) >= 2 ):
        print( tuple(arr[len(arr)//2 - 1 : len(arr)//2 + 1 ]))
    else:
        print(tuple(arr))
def main():
  arr = input("Enter a tuple of any values, please:\n") 
  arr = arr.strip(" [](){}").split(",")
  arr2= [] 
  for i in arr: 
      if "[" in i: 
          for j in i : 
              z = j  
              if z.replace(".","").isdigit(): 
                  arr2.append((int(float(j)),float(j))['.' in j ])
      elif i.replace(".","").isdigit():
          arr2.append((int(float(i)),float(i))['.' in i ])
  print(arr2)
  mainF32(arr2)

        
if __name__ == '__main__':
    main()