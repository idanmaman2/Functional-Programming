
def main():
    arr = eval (input(" Please, enter the nested list you want to process:\n"))
    if (type(arr) == list and len(arr) > 0  ):
      dict1 = {str : 0  , int : 0,list : 0 ,  tuple : 0  , float : 0 , }
      dict_names = { list : "lists" , str :"strings" , int : "ints" , tuple:"tuples" , float : "floats"}
      for i in arr : 
          dict1[type(i)] +=1 
      for key,val in dict1.items():
          if(val > 0 ): 
            print("%d %s were found in the input."%(val,dict_names[key]))
    else: 
        if(type(arr)==list and len(arr) == 0 ):
            print("ERROR - the input must be a nested non-empty list!")
        else: 
            print("ERROR - the input must be a list!")
        



        
if __name__ == '__main__':
    main()