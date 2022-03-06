import re 
def main():
    arr = open("/home/idang/Documents/Functional-Programming/ex1/shakespeare.txt",'r')
    text = arr.read()
    dict1 = dict()
    for i in re.split(''',|\.|\!|\?|\:|'|\;| ''',text.replace("\n","")):
         if i in dict1 : 
             dict1[i] += 1 
         else : 
             dict1.update({i: 1 })
    for key,val in dict1.items():
        print(key,val)
    arr.close()
            
        
if __name__ == '__main__':
    main()