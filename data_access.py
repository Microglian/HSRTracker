import gacha

# -------- UUID -----------

def next_uuid() -> int:
    with open(file="./files/uuid.txt", mode="r") as file:
        uuid = int(file.read())
    with open(file="./files/uuid.txt", mode="w") as file:
        file.write(f"{uuid+1}")
    string = str(uuid)
    while len(string) < 8:
        string = "0" + string
    return string 

# -------- Gacha -----------      
        
def get_gacha() -> gacha.Gacha:
    newgacha = gacha.Gacha()
    with open(file="./files/gacha.txt", mode="r") as file:
        contents = file.readlines() # Each line is csv uuid,priority,pos,object,target
    
    for line in contents:
        splitcontents = line.split(",")
        if len(splitcontents) < 5:
            continue
        newtask = gacha.GachaTask(splitcontents[0], splitcontents[1], int(splitcontents[2]), splitcontents[3], splitcontents[4][0:2])
        newgacha.tasks.append(newtask)
    
    return newgacha


def set_gacha(gacha:gacha.Gacha) -> None:
    with open(file="./files/gacha.txt", mode="w") as file:
        i = 0
        for task in gacha.tasks:
            string = f"\n{task.uuid},{task.priority},{task.pos},{task.object},{task.target}"
            if i == 0:
                string = string[1:]
            file.write(string)
            i += 1

    
# -------- Teams -----------      
    
def get_teams() -> list:
    teams = []
    
    
    return teams
    
    
    
    
    
# ------ Testing --------
if __name__ == '__main__':
    
    testgacha = get_gacha()
    print(testgacha.tasks[2].target)
    
    testgacha = gacha.Gacha()
    testgacha.tasks.append(gacha.GachaTask("gacha00000001", "high", 1, "Clara", "E1"))
    testgacha.tasks.append(gacha.GachaTask("gacha00000002", "high", 3, "Clara", "E2"))
    testgacha.tasks.append(gacha.GachaTask("gacha00000003", "high", 2, "Clara", "E3"))
    set_gacha(testgacha)