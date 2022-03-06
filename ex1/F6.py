def listinlist(type , arr  ):
    arr2 = [] 
    for i in arr : 
        for j in i :
             arr2.append(j)
    return type(arr2)
def tolist(arr:list):
    return listinlist(list,[i for i in arr if (type(i) == tuple) ])
def totuple(arr:list): 
    return listinlist(tuple,[i for i in arr if (type(i) == list ) ])
def tostring(arr:list): 
    arr1 = tolist(arr)
    arr2 = totuple(arr)
    return [i for i in arr if type(i) == str and not i in arr1 and not i in arr2]
def tonumber(arr): 
    arr1 = tolist(arr)
    arr2 = totuple(arr)
    return tuple([i for i in arr if (type(i) == float or type(i) == int )  and not i in arr1 and not i in arr2])
def main():
    arr = eval (input(" Please, enter the nested list you want to process:\n"))
    if (type(arr) == list and len(arr) > 0  ):
        print(tolist(arr))
        print(totuple(arr))
        print(tostring(arr))
        print(tonumber(arr))
    else: 
        if(type(arr)==list and len(arr) == 0 ):
            print("ERROR - the input must be a nested non-empty list!")
        else: 
            print("ERROR - the input must be a list!")
        



        
if __name__ == '__main__':
    main()