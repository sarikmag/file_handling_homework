def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open("txt_file/"+data).read()
    i=0
    r=[]
    while i<len(f):
        if f[i].isdigit():
            r+=f[i]
        i+=1
    return r
print(main("data03.txt"))
# Read data from file