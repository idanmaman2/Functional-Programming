def shiftR(bin:str , n :int ): 
    return  bin.rjust(n+len(bin),"0")[:len(bin)]
def shiftL(bin:str , n :int ): 
    return  bin.ljust(n+len(bin),"0")[n : len(bin)+n]
def shiftCL(bin:str , n :int ): 
    return ( bin.ljust(n+len(bin),"0")[0:n] + bin.ljust(n+len(bin),"0")[2*n:len(bin)+n])[::-1]
def shiftCR(bin:str , n :int ): 
    return  (bin[:len(bin)- n ** 2 ] + bin[len(bin)-n**2 : len(bin)-n] +  bin [len(bin) - n : ] ) [::-1] 
def main():
    print(shiftL("110001110",2))
    print(shiftR("110001110",2))
    print(shiftCL("110001110",2))
    print(shiftCR("110001110",2))


        
if __name__ == '__main__':
    main()