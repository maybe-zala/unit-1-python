file_contents : list = []
def serialize_file(fname: str) -> list:
    tlist:list = []
    data:str = ""
    with open(fname, 'r') as file:
        data = file.read()
        tlist = data.split(":")
    tlist.remove(tlist[len(tlist)-1])
    return tlist

def main() -> None:
    file_contents = serialize_file("name.txt")
    firstuser = False
    if len(file_contents)<=0:
        firstuser = True
    else: lastuser = file_contents[len(file_contents)-1]
    if firstuser:
        print("You are the first user of this program!")
    else:
        print(f'{len(file_contents)} users have ran this program')
        print(f"{lastuser} was the last user of this program.")
    cmd :str = input("Name? ")
    with open("name.txt", "a") as file:
        file.write(cmd+":")

if __name__ == '__main__':
    main()