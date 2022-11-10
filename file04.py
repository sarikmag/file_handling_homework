def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open("txt_file/"+data).read()
    r=[]
    i=0
    while i<len(f):
        if f[i].isalpha() or f[i]=="\n":
            r+=f[i]
        i+=1
    return r
print(main("data04.txt"))
# Read data from file