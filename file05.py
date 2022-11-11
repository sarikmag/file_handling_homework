def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    a=0
    b=0
    c=[]
    i=0
    while i<len(f):
        if f[i].isdigit():
            a+=1
        if f[i].isalpha() or f[i]=="\n":
            b+=1
        i+=1
    c+=[a]
    c+=[b]
    return c
f = open("txt_file/data05.txt").read()
print(main(f))
# Read data from file