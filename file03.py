def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    i=0
    r=[]
    while i<len(f):
        if f[i].isdigit():
            r+=f[i]
        i+=1
    return r
f = open("txt_file/data03.txt").read()
print(main(f))
# Read data from file