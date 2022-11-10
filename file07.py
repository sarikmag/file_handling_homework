def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open("txt_file/"+data).read()
    s=0
    i=0
    while i<len(f):
        if f[i].isdigit():
            s+=int(f[i])
        i+=1
    return s
print(main("data07.txt"))
# Read data from file