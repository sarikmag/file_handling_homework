def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open("txt_file/"+data).read()
    i=0
    min=0
    while i < len(f):
        if f[i].isdigit() and int(f[i])<0:
            min=int(f[i])
        i+=1
    return min
print(main("data09.txt"))
# Read data from file