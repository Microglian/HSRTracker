import gacha
import team

# -------- UUID -----------

def next_uuid() -> int:
    with open(file="./files/properties.txt", mode="r") as file:
        contents = file.readlines()
    uuid = int(contents[0].split(":")[1])
    contents[0] = f"uuid:{uuid+1}\n"
    with open(file="./files/properties.txt", mode="w") as file:
        file.writelines(contents)
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
            string = f"\n{task.uuid},{task.priority},{task.pos},{task.objectname},{task.target}"
            if i == 0:
                string = string[1:]
            file.write(string)
            i += 1

    
# -------- Teams -----------      
    
def get_teams() -> list:
    with open(file="./files/properties.txt", mode="r") as file:
        contents = file.readlines()
    list_of_teams = contents[1].split(":")[1].split(",")
    
    teams = []
    for teamname in list_of_teams:
        with open(file=f"./files/{teamname}.txt", mode="r") as file:
            contents = file.readlines()
        team_index = int(teamname[4:])
        
        #Get character dicts from string: Clara,70,Something Irreplacable,70,1,1,0,3,5,7,6
        characters = []
        for i in range(4):
            newchar = {}
            char_dets = contents[i].split(",")
            newchar["Name"] = char_dets[0]
            newchar["Level"] = int(char_dets[1])
            newchar["Weapon"] = char_dets[2]
            newchar["WeaponLV"] = int(char_dets[3])
            newchar["A2Trace"] = int(char_dets[4])
            newchar["A4Trace"] = int(char_dets[5])
            newchar["A6Trace"] = int(char_dets[6])
            newchar["BasicLV"] = int(char_dets[7])
            newchar["SkillLV"] = int(char_dets[8])
            newchar["UltLV"] = int(char_dets[9])
            newchar["TalentLV"] = int(char_dets[10])
            characters.append(newchar)
        
        teams.append(team.Team(team_index, characters[0], characters[1], characters[2], characters[3]))
        
        for i in range(4, len(contents)):
            task_dets = contents[i].split(",")
            match task_dets[0]:
                case "Level": #Level,Clara,team00000001,1,80
                    teams[-1].tasks.append(team.TeamTaskLevel(task_dets[1], task_dets[2], int(task_dets[3]), int(task_dets[4])))
                case "WeaponLevel": #WeaponLevel,Clara,team00000002,2,80
                    teams[-1].tasks.append(team.TeamTaskWeaponLevel(task_dets[1], task_dets[2], int(task_dets[3]), int(task_dets[4])))
                case "AscensionTrace": #AscensionTrace,Clara,team00000003,3,A2 (or A4 or A6)
                    teams[-1].tasks.append(team.TeamTaskAscensionTrace(task_dets[1], task_dets[2], int(task_dets[3]), task_dets[4][0:2]))
                case "LevelledTrace": #LevelledTrace,Clara,team00000004,4,Basic,8 (or Skill or Ult or Talent)
                    teams[-1].tasks.append(team.TeamTaskLevelledTrace(task_dets[1], task_dets[2], int(task_dets[3]), task_dets[4], int(task_dets[5])))
                case "Relic": #Relic,Clara,team00000005,5,Musketeer,Head,HP,[atk%,critrate,critdmg,spd]
                    task_substats = []
                    for i in range(7,len(task_dets)):
                        task_substats.append(task_dets[i])
                        if task_substats[-1][-2:] == "\n":
                            task_substats[-1] = task_substats[:-2]
                    teams[-1].tasks.append(team.TeamTaskRelic(task_dets[1], task_dets[2], int(task_dets[3]), task_dets[4], task_dets[5], task_dets[6], task_substats))
            
    return teams
    
    
def set_teams(teams:list) -> None:
    teamnames = "teams:"
    # Write each team file
    for team in teams:
        teamnames += f"team{team.team_index},"
        contents = []
        contents.append(f'{team.character1["Name"]},{team.character1["Level"]},{team.character1["Weapon"]},{team.character1["WeaponLV"]},{team.character1["A2Trace"]},{team.character1["A4Trace"]},{team.character1["A6Trace"]},{team.character1["BasicLV"]},{team.character1["SkillLV"]},{team.character1["UltLV"]},{team.character1["TalentLV"]}\n')
        contents.append(f'{team.character2["Name"]},{team.character2["Level"]},{team.character2["Weapon"]},{team.character2["WeaponLV"]},{team.character2["A2Trace"]},{team.character2["A4Trace"]},{team.character2["A6Trace"]},{team.character2["BasicLV"]},{team.character2["SkillLV"]},{team.character2["UltLV"]},{team.character2["TalentLV"]}\n')
        contents.append(f'{team.character3["Name"]},{team.character3["Level"]},{team.character3["Weapon"]},{team.character3["WeaponLV"]},{team.character3["A2Trace"]},{team.character3["A4Trace"]},{team.character3["A6Trace"]},{team.character3["BasicLV"]},{team.character3["SkillLV"]},{team.character3["UltLV"]},{team.character3["TalentLV"]}\n')
        contents.append(f'{team.character4["Name"]},{team.character4["Level"]},{team.character4["Weapon"]},{team.character4["WeaponLV"]},{team.character4["A2Trace"]},{team.character4["A4Trace"]},{team.character4["A6Trace"]},{team.character4["BasicLV"]},{team.character4["SkillLV"]},{team.character4["UltLV"]},{team.character4["TalentLV"]}\n')
        
        # Add tasks
        for task in team.tasks:
            match task.tasktype:
                case "Level":
                    contents.append(f"Level,{task.character},{task.uuid},{task.pos},{task.level}\n")
                case "WeaponLevel":
                    contents.append(f"WeaponLevel,{task.character},{task.uuid},{task.pos},{task.level}\n")
                case "AscensionTrace":
                    contents.append(f"AscensionTrace,{task.character},{task.uuid},{task.pos},{task.trace}\n")
                case "LevelledTrace":
                    contents.append(f"LevelledTrace,{task.character},{task.uuid},{task.pos},{task.trace},{task.target}\n")
                case "Relic":
                    contents.append(f"Relic,{task.character},{task.uuid},{task.pos},{task.set},{task.slot},{task.mainstat}")
                    for i in range(4):
                        if task.substats[i] != "":
                            contents[-1] += f",{task.substats[i]}"
                    contents[-1] += "\n"
        
        # Remove the \n that causes the blank line
        contents[-1] = contents[-1][0:-1]
        
        # Write to file
        with open(file=f"./files/team{team.team_index}.txt", mode="w") as file:
            file.writelines(contents)
    
    # Write teamnames to properties, leaving the uuid as is
    teamnames = teamnames[0:-1]
    with open(file="./files/properties.txt", mode="r") as file:
        properties_contents = file.readlines()
    properties_contents[1] = teamnames
    with open(file="./files/properties.txt", mode="w") as file:
        file.writelines(properties_contents)

    
# ------ Testing --------
if __name__ == '__main__':
    
    #print(next_uuid())
    testteams = get_teams()
    print(testteams[0].character1["Name"])
    print(testteams[0].tasks[0].uuid)
    testteams[0].tasks[0].character = "Acheron"
    testteams[0].tasks[1].character = "Clara"
    set_teams(testteams)
    
    # testgacha = get_gacha()
    # print(testgacha.tasks[2].target)
    
    # testgacha = gacha.Gacha()
    # testgacha.tasks.append(gacha.GachaTask("gacha00000001", "high", 1, "Clara", "E1"))
    # testgacha.tasks.append(gacha.GachaTask("gacha00000002", "high", 3, "Clara", "E2"))
    # testgacha.tasks.append(gacha.GachaTask("gacha00000003", "high", 2, "Clara", "E3"))
    # set_gacha(testgacha)