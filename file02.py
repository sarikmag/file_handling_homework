def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open("txt_file/"+data).read()
    return len(f)
print(main("data02.txt"))

# Read data from file