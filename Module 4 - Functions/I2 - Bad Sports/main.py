def is_on_team(name : str) -> bool:
    if name == "Carol" or name == "Nick" or name == "Maureen":

        return True
    else:
        return False
def rick_shakes(name : str, did_win : bool):
    if did_win and name == "Nick" or not did_win and name != "Nick":
        return True
    else:
        return False
def john_shakes(name : str, did_win : bool):
        if did_win and name != "Nick" or not did_win and name == "Nick":
            return True
        else:
            return False
def jared_shakes(name : str, did_win : bool):
        if name != "Nick":
            return True
        else:
            return False

def main()-> None:
    name = input("Name: ")

    if name == "Carol" or name == "Nick" or name == "Maureen":
        did_win = input("Did you win? ") == "Yes"




    
        if did_win and name != "Nick" or not did_win and name == "Nick":
            print("Rick: *shakes hand*")
        else:
            print("Rick: ...")




        
        if did_win and name != "Nick" or not did_win and name == "Nick":
            print("John: *shakes hand*")
        else:
            print("John: ...")
        




        
        if name != "Nick":
            print("Jared: *shakes hand*")
        else:
            print("Jared: ...")
    else:
        print("You weren't even on the team!")

if __name__ == '__main__':
    main()



