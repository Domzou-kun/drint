from dict_viewer.drint import drint

def test_dict():

    test_d4 = {
        "g": "7",
        "h": "8",
        "i": "9"
    }

    test_d3 = {
        "e": "5",
        "f": test_d4

    }

    test_d2 = {
        "c": test_d3,
        "d": "4" 
    }

    test_d1 = {
        "a": "1",
        "b": test_d2
    }
    
    return test_d1


""" main """
def main():
    dicter = test_dict()
    drint(dicter)

if __name__ == "__main__":

    """ main program """
    main()

