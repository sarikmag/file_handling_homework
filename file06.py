def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open("txt_file/"+data).read()
    r=f.split("\n")
    a=[]
    for i in r:
        a+=[len(i)]
    return a
print(main("data06.txt"))
# Read data from file