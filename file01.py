def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    r = f.split(',')
    s=[]
    for i in r:
        s+=[int(i)]
    return s
f = open("txt_file/data01.txt").read()
print(main(f))
# Read data from file