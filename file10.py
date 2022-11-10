def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open("txt_file/"+data).read()
    r=f.split("\n")
    max=len(r[0])
    for i in r:
        if len(i)>max:
            max=len(i)
    return max
print(main("data10.txt"))
# Read data from file