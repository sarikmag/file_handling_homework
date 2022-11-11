def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    max=0
    i=0
    while i < len(f):
        if f[i].isdigit() and int(f[i])>max:
            max=int(f[i])
        i+=1
    return max
f = open("txt_file/data08.txt").read()
print(main(f))
# Read data from file