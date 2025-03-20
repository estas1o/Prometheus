def fetcher(obj, index):
    return obj[index]


class MyException(Exception):
    pass
# standard demo
if __name__ == "__main__":
        

    try:
        x = input("input string: ")
        assert len(x) < 20, "too long object"
        index = int(input("input index, please: "))
        print(fetcher(x, index))
       
    except IndexError:
        print("bad index")
        


