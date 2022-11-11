def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    r=f.split("\n")
    max=len(r[0])
    for i in r:
        if len(i)>max:
            max=len(i)
    return max
f = open("txt_file/data10.txt").read()
print(main(f))
# Read data from file