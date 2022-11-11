def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    r=f.split("\n")
    a=[]
    for i in r:
        a+=[len(i)]
    return a
f = open("txt_file/data06.txt").read()
print(main(f))
# Read data from file