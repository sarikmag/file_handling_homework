def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    i=0
    min=0
    while i < len(f):
        if f[i].isdigit() and int(f[i])<0:
            min=int(f[i])
        i+=1
    return min
f = open("txt_file/data09.txt").read()
print(main(f))
# Read data from file