'''
Creates a tk window and handles presenting information to user and executing button commands.
'''

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

import summary
import team
import gacha
import data_access as data
import mapping

from functools import partial

# Create the window
root = tk.Tk()
root.title("Honkai Star Tracks")
root.geometry('1204x804+100+100')
root.resizable(False, False)

#---------- Window Classes -----------------

class Tab():
    def __init__(self, master) -> None:
        # Upon creating the tab, define its grid.
        self.frame = ttk.Frame(master, width=1200, height=800, borderwidth=2, relief="solid")
        self.frame.columnconfigure(0, minsize=100)
        self.frame.columnconfigure(1, minsize=100)
        self.frame.columnconfigure(2, minsize=100)
        self.frame.columnconfigure(3, minsize=100)
        self.frame.columnconfigure(4, minsize=100)
        self.frame.columnconfigure(5, minsize=100)
        self.frame.columnconfigure(6, minsize=100)
        self.frame.columnconfigure(7, minsize=100)
        self.frame.columnconfigure(8, minsize=100)
        self.frame.columnconfigure(9, minsize=100)
        self.frame.columnconfigure(10, minsize=100)
        self.frame.columnconfigure(11, minsize=100)
        self.frame.rowconfigure(0, minsize=50)
        self.frame.rowconfigure(1, minsize=50)
        self.frame.rowconfigure(2, minsize=50)
        self.frame.rowconfigure(3, minsize=50)
        self.frame.rowconfigure(4, minsize=50)
        self.frame.rowconfigure(5, minsize=50)
        self.frame.rowconfigure(6, minsize=50)
        self.frame.rowconfigure(7, minsize=50)
        self.frame.rowconfigure(8, minsize=50)
        self.frame.rowconfigure(9, minsize=50)
        self.frame.rowconfigure(10, minsize=50)
        self.frame.rowconfigure(11, minsize=50)
        self.frame.rowconfigure(12, minsize=50)
        self.frame.rowconfigure(13, minsize=50)
        self.frame.rowconfigure(14, minsize=50)
        self.frame.rowconfigure(15, minsize=50)

    
    def make_summary_tab(self):
        pass
    
    def make_gacha_tab(self, tasks:list):
        # Make the header frame for containing cost summary
        self.frame_header = ttk.Frame(self.frame, width=1196, height=50, borderwidth=2, relief="solid")
        self.frame_header.grid(column=0, row=0, columnspan=12, rowspan=1, sticky="w")
        # Header background
        self.header_image = tk.PhotoImage(file="./images/gachaheader.png")
        self.header_bg = ttk.Label(self.frame_header, image=self.header_image)
        self.header_bg.place(x=-4, y=-4)
        
        
        # High priority list
        self.frame_highpri = ttk.Frame(self.frame, width=400, height=750, borderwidth=2, relief="solid")
        self.frame_highpri.grid(column=0, row=1, columnspan=4, rowspan=15)
        # High priority background
        self.highpri_image = tk.PhotoImage(file="./images/gachahighpri.png")
        self.highpri_bg = ttk.Label(self.frame_highpri, image=self.highpri_image)
        self.highpri_bg.place(x=-4, y=-2)
        # Make a canvas to contain the tasks so they can be scrolled?
        self.highpri_listcanvas = tk.Canvas(self.frame_highpri, width=398, height=1500, bg="#2F6E6E", highlightthickness=0)
        self.highpri_listcanvas.place(x=-2,y=54)
        self.frame_highprilist = ttk.Frame(self.highpri_listcanvas, width=398, height=1500, borderwidth=2, relief="solid")
        self.frame_highprilist.place(x=-2,y=-2)
        
        self.highpri_listimage = tk.PhotoImage(file="./images/gachahighprilist.png")
        self.highpri_listbg = ttk.Label(self.frame_highprilist, image=self.highpri_listimage)
        self.highpri_listbg.place(x=-2,y=-2)
        # There is no way of knowing why this doesn't work.
        self.highpri_scrollbar = ttk.Scrollbar(self.highpri_listcanvas, orient="vertical", command=self.highpri_listcanvas.yview)
        self.highpri_listcanvas['yscrollcommand'] = self.highpri_scrollbar.set
        self.highpri_scrollbar.place(x=0,y=0,anchor="e")
        
        
        # Med priority list
        self.frame_medpri = ttk.Frame(self.frame, width=400, height=750, borderwidth=2, relief="solid")
        self.frame_medpri.grid(column=4, row=1, columnspan=4, rowspan=15)
        self.medpri_image = tk.PhotoImage(file="./images/gachamedpri.png")
        self.medpri_bg = ttk.Label(self.frame_medpri, image=self.medpri_image)
        self.medpri_bg.place(x=-4, y=-2)
        
        self.medpri_listcanvas = tk.Canvas(self.frame_medpri, width=398, height=1500, bg="#2F6E6E", highlightthickness=0)
        self.medpri_listcanvas.place(x=-2,y=54)
        self.frame_medprilist = ttk.Frame(self.medpri_listcanvas, width=398, height=1500, borderwidth=2, relief="solid")
        self.frame_medprilist.place(x=-2,y=-2)
        
        self.medpri_listimage = tk.PhotoImage(file="./images/gachamedprilist.png")
        self.medpri_listbg = ttk.Label(self.frame_medprilist, image=self.medpri_listimage)
        self.medpri_listbg.place(x=-2,y=-2)
        
        self.medpri_scrollbar = ttk.Scrollbar(self.medpri_listcanvas, orient="vertical", command=self.medpri_listcanvas.yview)
        self.medpri_listcanvas['yscrollcommand'] = self.medpri_scrollbar.set
        self.medpri_scrollbar.place(x=0,y=0,anchor="e")
        
        
        # Low priority list
        self.frame_lowpri = ttk.Frame(self.frame, width=400, height=750, borderwidth=2, relief="solid")
        self.frame_lowpri.grid(column=8, row=1 , columnspan=4, rowspan=15)
        self.lowpri_image = tk.PhotoImage(file="./images/gachalowpri.png")
        self.lowpri_bg = ttk.Label(self.frame_lowpri, image=self.lowpri_image)
        self.lowpri_bg.place(x=-4, y=-2)
        
        self.lowpri_listcanvas = tk.Canvas(self.frame_lowpri, width=398, height=1500, bg="#2F6E6E", highlightthickness=0)
        self.lowpri_listcanvas.place(x=-2,y=54)
        self.frame_lowprilist = ttk.Frame(self.lowpri_listcanvas, width=398, height=1500, borderwidth=2, relief="solid")
        self.frame_lowprilist.place(x=-2,y=-2)
        
        self.lowpri_listimage = tk.PhotoImage(file="./images/gachalowprilist.png")
        self.lowpri_listbg = ttk.Label(self.frame_lowprilist, image=self.lowpri_listimage)
        self.lowpri_listbg.place(x=-2,y=-2)
        
        self.lowpri_scrollbar = ttk.Scrollbar(self.lowpri_listcanvas, orient="vertical", command=self.lowpri_listcanvas.yview)
        self.lowpri_listcanvas['yscrollcommand'] = self.lowpri_scrollbar.set
        self.lowpri_scrollbar.place(x=0,y=0,anchor="e")
        
        # Create lists of the tasks. Each task is a newly-defined GachaTaskWidget from data
        self.highpri = []
        self.medpri = []
        self.lowpri = []
        
        for task in tasks:
            match task["priority"]:
                case "High":
                    new_widget = GachaTaskWidget(task["uuid"], self.frame_highprilist, task["pos"], task["object"], task["target"], task["priority"])
                    self.highpri.append(new_widget)
                case "Med":
                    new_widget = GachaTaskWidget(task["uuid"], self.frame_medprilist, task["pos"], task["object"], task["target"], task["priority"])
                    self.medpri.append(new_widget)
                case "Low":
                    new_widget = GachaTaskWidget(task["uuid"], self.frame_lowprilist, task["pos"], task["object"], task["target"], task["priority"])
                    self.lowpri.append(new_widget)
        
        # Sort each list by pos.
        self.highpri.sort(key = lambda k: k.pos)
        self.medpri.sort(key = lambda k: k.pos)
        self.lowpri.sort(key = lambda k: k.pos)
        
        y = 0            
        for i in range(len(self.highpri)):
            self.highpri[i].taskframe.place(x=0,y=y)
            y += 100
            
        y = 0            
        for i in range(len(self.medpri)):
            self.medpri[i].taskframe.place(x=0,y=y)
            y += 100
        
        y = 0            
        for i in range(len(self.lowpri)):
            self.lowpri[i].taskframe.place(x=0,y=y)
            y += 100    
            
        # Add task button for each list
        self.button_add_highpri = tk.Button(self.frame_highpri, text="New", command=partial(gacha_add_task, "High"))
        self.button_add_highpri.config(activebackground="#2F6E6E", activeforeground="#FFFFFF", highlightthickness=0)
        self.button_add_highpri.place(x=355,y=7,width=36,height=36)
        
        self.button_add_medpri = tk.Button(self.frame_medpri, text="New", command=partial(gacha_add_task, "Med"))
        self.button_add_medpri.config(activebackground="#2F6E6E", activeforeground="#FFFFFF", highlightthickness=0)
        self.button_add_medpri.place(x=355,y=7,width=36,height=36)
        
        self.button_add_lowpri = tk.Button(self.frame_lowpri, text="New", command=partial(gacha_add_task, "Low"))
        self.button_add_lowpri.config(activebackground="#2F6E6E", activeforeground="#FFFFFF", highlightthickness=0)
        self.button_add_lowpri.place(x=356,y=7,width=36,height=36)
        
        # Calculate Header Total
        self.totalcost75 = 0
        self.totalcost100 = 0
        for widget in self.highpri:
            self.totalcost75 += widget.cost75
            self.totalcost100 += widget.cost100
            
        for widget in self.medpri:
            self.totalcost75 += widget.cost75
            self.totalcost100 += widget.cost100
            
        for widget in self.lowpri:
            self.totalcost75 += widget.cost75
            self.totalcost100 += widget.cost100
        
        self.totalcosttext = f"{self.totalcost75} | {self.totalcost100}"
        self.totalcostwidget = tk.Label(self.frame_header, text=self.totalcosttext, bg="#FFDBB2", font=tkFont.Font(size=16))
        self.totalcostwidget.place(x=938,y=4,width=200, height=40)
        
        
    def make_team_tab(self, team:team.Team):
        # Make the header frame for containing cost summary
        self.team_index = team.team_index
        self.frame_header = ttk.Frame(self.frame, width=1196, height=50, borderwidth=2, relief="solid")
        self.frame_header.grid(column=0, row=0, columnspan=12, rowspan=1, sticky="w")
        # Header background
        self.header_image = tk.PhotoImage(file="./images/teamheader.png")
        self.header_bg = ttk.Label(self.frame_header, image=self.header_image)
        self.header_bg.place(x=-4, y=-4)
        
        # Character lists
        self.char1 = TeamColumn(self, team.character1, 0, 0)
        self.char2 = TeamColumn(self, team.character2, 3, 1)
        self.char3 = TeamColumn(self, team.character3, 6, 2)
        self.char4 = TeamColumn(self, team.character4, 9, 3)
        
        self.char1tasks = []
        self.char2tasks = []
        self.char3tasks = []
        self.char4tasks = []
        
        for task in team.tasks:
            match task.character:
                case self.char1.character:
                    match task.tasktype:
                        case "Level":
                            self.char1tasks.append(TeamTaskWidgetLevel(task.uuid, self.char1, task.pos, task.level))
                        case "WeaponLevel":
                            self.char1tasks.append(TeamTaskWidgetWeaponLevel(task.uuid, self.char1, task.pos, task.level))
                        case "AscensionTrace":
                            self.char1tasks.append(TeamTaskWidgetAscension(task.uuid, self.char1, task.pos, task.trace))
                        case "LevelledTrace":
                            self.char1tasks.append(TeamTaskWidgetTrace(task.uuid, self.char1, task.pos, task.trace, task.target))
                        case "Relic":
                            self.char1tasks.append(TeamTaskWidgetRelic(task.uuid, self.char1, task.pos, task.set, task.slot, task.mainstat, task.substats))      
                case self.char2.character:
                    match task.tasktype:
                        case "Level":
                            self.char2tasks.append(TeamTaskWidgetLevel(task.uuid, self.char2, task.pos, task.level))
                        case "WeaponLevel":
                            self.char2tasks.append(TeamTaskWidgetWeaponLevel(task.uuid, self.char2, task.pos, task.level))
                        case "AscensionTrace":
                            self.char2tasks.append(TeamTaskWidgetAscension(task.uuid, self.char2, task.pos, task.trace))
                        case "LevelledTrace":
                            self.char2tasks.append(TeamTaskWidgetTrace(task.uuid, self.char2, task.pos, task.trace, task.target))
                        case "Relic":
                            self.char2tasks.append(TeamTaskWidgetRelic(task.uuid, self.char2, task.pos, task.set, task.slot, task.mainstat, task.substats))
                case self.char3.character:
                    match task.tasktype:
                        case "Level":
                            self.char3tasks.append(TeamTaskWidgetLevel(task.uuid, self.char3, task.pos, task.level))
                        case "WeaponLevel":
                            self.char3tasks.append(TeamTaskWidgetWeaponLevel(task.uuid, self.char3, task.pos, task.level))
                        case "AscensionTrace":
                            self.char3tasks.append(TeamTaskWidgetAscension(task.uuid, self.char3, task.pos, task.trace))
                        case "LevelledTrace":
                            self.char3tasks.append(TeamTaskWidgetTrace(task.uuid, self.char3, task.pos, task.trace, task.target))
                        case "Relic":
                            self.char3tasks.append(TeamTaskWidgetRelic(task.uuid, self.char3, task.pos, task.set, task.slot, task.mainstat, task.substats))
                case self.char4.character:
                    match task.tasktype:
                        case "Level":
                            self.char4tasks.append(TeamTaskWidgetLevel(task.uuid, self.char4, task.pos, task.level))
                        case "WeaponLevel":
                            self.char4tasks.append(TeamTaskWidgetWeaponLevel(task.uuid, self.char4, task.pos, task.level))
                        case "AscensionTrace":
                            self.char4tasks.append(TeamTaskWidgetAscension(task.uuid, self.char4, task.pos, task.trace))
                        case "LevelledTrace":
                            self.char4tasks.append(TeamTaskWidgetTrace(task.uuid, self.char4, task.pos, task.trace, task.target))
                        case "Relic":
                            self.char4tasks.append(TeamTaskWidgetRelic(task.uuid, self.char4, task.pos, task.set, task.slot, task.mainstat, task.substats))
        
        # Sort each list by pos.
        self.char1tasks.sort(key = lambda k: k.pos)
        self.char2tasks.sort(key = lambda k: k.pos)
        self.char3tasks.sort(key = lambda k: k.pos)
        self.char4tasks.sort(key = lambda k: k.pos)
        
        y = 0            
        for i in range(len(self.char1tasks)):
            self.char1tasks[i].taskframe.place(x=0,y=y)
            y += self.char1tasks[i].frameheight
            y += 4
            
        y = 0            
        for i in range(len(self.char2tasks)):
            self.char2tasks[i].taskframe.place(x=0,y=y)
            y += self.char2tasks[i].frameheight
            y += 4
            
        y = 0            
        for i in range(len(self.char3tasks)):
            self.char3tasks[i].taskframe.place(x=0,y=y)
            y += self.char3tasks[i].frameheight
            y += 4
            
        y = 0            
        for i in range(len(self.char4tasks)):
            self.char4tasks[i].taskframe.place(x=0,y=y)
            y += self.char4tasks[i].frameheight
            y += 4
              
        

        
class TeamColumn():
    def __init__(self, master, character, col, char_index) -> None:
        self.characterdict = character
        self.character = self.characterdict['Name']
        self.team_index = master.team_index
        self.frame = ttk.Frame(master.frame, width=300, height=750, borderwidth=2, relief="solid")
        self.frame.grid(column=col, row=1, columnspan=3, rowspan=15)
        # Header background
        self.image = tk.PhotoImage(file="./images/gachachar.png")
        self.bg = ttk.Label(self.frame, image=self.image)
        self.bg.place(x=-4, y=-2)
        # Header Pic
        self.pic = tk.PhotoImage(file=f"./images/gacha/{mapping.imagemap[character['Name']]}.png")
        self.piccanv = tk.Canvas(self.frame, width=81, height=92, bg="#003135", highlightthickness=0)
        self.piccanv.create_image((40, 46), image=self.pic)
        self.piccanv.place(x=0,y=2)
        
        # Char Name
        self.charname = tk.StringVar(self.frame, character['Name'])
        self.headername = tk.OptionMenu(self.frame, self.charname, self.charname, *team.characternames, command=partial(team_set_character, master.team_index, char_index))
        self.headername['menu'].delete(0)
        self.headername.config(bg="#00797F", fg="#FFFFFF", activebackground="#00797F", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.headername['menu'].config(bg="#00797F", fg="#FFFFFF", activebackground="#00797F", activeforeground="#FFFFFF")
        self.headername.place(x=88,y=5,width=100,height=20)
        
        # Char Level
        self.charlevelint = tk.IntVar(self.frame, character['Level'])
        self.charlevel = tk.OptionMenu(self.frame, self.charlevelint, self.charlevelint, *[80,70,60,50,40,30,20], command=partial(team_set_character_level, master.team_index, char_index))
        self.charlevel['menu'].delete(0)
        self.charlevel.config(bg="#00797F", fg="#FFFFFF", activebackground="#00797F", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.charlevel['menu'].config(bg="#00797F", fg="#FFFFFF", activebackground="#00797F", activeforeground="#FFFFFF")
        self.charlevel.place(x=190,y=5,width=48,height=20)
        
        # Weapon Name
        self.wepname = tk.StringVar(self.frame, character['Weapon'])
        self.weaponname = tk.OptionMenu(self.frame, self.wepname, self.wepname, *team.weaponnames, command=partial(team_set_weapon, master.team_index, char_index))
        self.weaponname['menu'].delete(0)
        self.weaponname.config(bg="#005989", fg="#FFFFFF", activebackground="#005989", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.weaponname['menu'].config(bg="#005989", fg="#FFFFFF", activebackground="#005989", activeforeground="#FFFFFF")
        self.weaponname.place(x=88,y=28,width=200,height=20)
        
        # Weapon Level
        self.weplevelint = tk.IntVar(self.frame, character['WeaponLV'])
        self.weplevel = tk.OptionMenu(self.frame, self.weplevelint, self.weplevelint, *[80,70,60,50,40,30,20], command=partial(team_set_weapon_level, master.team_index, char_index))
        self.weplevel['menu'].delete(0)
        self.weplevel.config(bg="#005989", fg="#FFFFFF", activebackground="#005989", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.weplevel['menu'].config(bg="#005989", fg="#FFFFFF", activebackground="#005989", activeforeground="#FFFFFF")
        self.weplevel.place(x=240,y=5,width=48,height=20)
        
        # Basic Level
        self.tracebasictext = tk.StringVar(self.frame, f"B{character['BasicLV']}")
        self.tracebasic = tk.OptionMenu(self.frame, self.tracebasictext, self.tracebasictext, *["B6","B5","B4","B3","B2","B1"], command=partial(team_set_trace_basic, master.team_index, char_index))
        self.tracebasic['menu'].delete(0)
        self.tracebasic.config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.tracebasic['menu'].config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF")
        self.tracebasic.place(x=88,y=51,width=49,height=20)
        
        # Skill Level
        self.traceskilltext = tk.StringVar(self.frame, f"S{character['SkillLV']}")
        self.traceskill = tk.OptionMenu(self.frame, self.traceskilltext, self.traceskilltext, *["S10","S9","S8","S7","S6","S5","S4","S3","S2","S1"], command=partial(team_set_trace_skill, master.team_index, char_index))
        self.traceskill['menu'].delete(0)
        self.traceskill.config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.traceskill['menu'].config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF")
        self.traceskill.place(x=139,y=51,width=49,height=20)
        
        # Ult Level
        self.traceulttext = tk.StringVar(self.frame, f"U{character['UltLV']}")
        self.traceult = tk.OptionMenu(self.frame, self.traceulttext, self.traceulttext, *["U10","U9","U8","U7","U6","U5","U4","U3","U2","U1"], command=partial(team_set_trace_ult, master.team_index, char_index))
        self.traceult['menu'].delete(0)
        self.traceult.config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.traceult['menu'].config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF")
        self.traceult.place(x=190,y=51,width=48,height=20)
        
        # Talent Level
        self.tracetalenttext = tk.StringVar(self.frame, f"T{character['TalentLV']}")
        self.tracetalent = tk.OptionMenu(self.frame, self.tracetalenttext, self.tracetalenttext, *["T10","T9","T8","T7","T6","T5","T4","T3","T2","T1"], command=partial(team_set_trace_talent, master.team_index, char_index))
        self.tracetalent['menu'].delete(0)
        self.tracetalent.config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.tracetalent['menu'].config(bg="#212B87", fg="#FFFFFF", activebackground="#212B87", activeforeground="#FFFFFF")
        self.tracetalent.place(x=240,y=51,width=48,height=20)
        
        # A2 Yes?
        if character['A2Trace']:
            has_trace = "Y"
        else:
            has_trace = "N"
        self.traceA2text = tk.StringVar(self.frame, f"A2:{has_trace}")
        self.traceA2 = tk.OptionMenu(self.frame, self.traceA2text, self.traceA2text, *["A2:Y", "A2:N"], command=partial(team_set_ascension, master.team_index, char_index, "A2"))
        self.traceA2['menu'].delete(0)
        self.traceA2.config(bg="#3D2184", fg="#FFFFFF", activebackground="#3D2184", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.traceA2['menu'].config(bg="#3D2184", fg="#FFFFFF", activebackground="#3D2184", activeforeground="#FFFFFF")
        self.traceA2.place(x=88,y=74,width=58,height=20)
        
        # A4 Yes?
        if character['A4Trace']:
            has_trace = "Y"
        else:
            has_trace = "N"
        self.traceA4text = tk.StringVar(self.frame, f"A4:{has_trace}")
        self.traceA4 = tk.OptionMenu(self.frame, self.traceA4text, self.traceA4text, *["A4:Y", "A4:N"], command=partial(team_set_ascension, master.team_index, char_index, "A4"))
        self.traceA4['menu'].delete(0)
        self.traceA4.config(bg="#3D2184", fg="#FFFFFF", activebackground="#3D2184", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.traceA4['menu'].config(bg="#3D2184", fg="#FFFFFF", activebackground="#3D2184", activeforeground="#FFFFFF")
        self.traceA4.place(x=148,y=74,width=58,height=20)
        
        # A6 Yes?
        if character['A6Trace']:
            has_trace = "Y"
        else:
            has_trace = "N"
        self.traceA6text = tk.StringVar(self.frame, f"A6:{has_trace}")
        self.traceA6 = tk.OptionMenu(self.frame, self.traceA6text, self.traceA6text, *["A6:Y", "A6:N"], command=partial(team_set_ascension, master.team_index, char_index, "A6"))
        self.traceA6['menu'].delete(0)
        self.traceA6.config(bg="#3D2184", fg="#FFFFFF", activebackground="#3D2184", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.traceA6['menu'].config(bg="#3D2184", fg="#FFFFFF", activebackground="#3D2184", activeforeground="#FFFFFF")
        self.traceA6.place(x=208,y=74,width=58,height=20)
        
        # New Task Dropdown & Button
        self.newtaskvar = tk.StringVar(self.frame, "Char Level")
        self.newtaskbox = tk.OptionMenu(self.frame, self.newtaskvar, self.newtaskvar, *["Char Level", "Weapon Level", "Trace", "Ascension", "Relic"], command=self.update_new_task_command)
        self.newtaskbox['menu'].delete(0)
        self.newtaskbox.config(bg="#C117A5", fg="#FFFFFF", activebackground="#C117A5", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.newtaskbox['menu'].config(bg="#C117A5", fg="#FFFFFF", activebackground="#C117A5", activeforeground="#FFFFFF")
        self.newtaskbox.place(x=4,y=97,width=114,height=20)
        
        self.newtaskcommand = partial(team_add_task, master.team_index, self.character, self.newtaskvar.get())
        self.newtaskbutton = tk.Button(self.frame, text="New", command=self.newtaskcommand)
        self.newtaskbutton.config(bg="#C117A5", activebackground="#C117A5", fg="#FFFFFF", activeforeground="#FFFFFF", highlightthickness=0)
        self.newtaskbutton.place(x=120,y=97,width=36,height=20)
        
        # Clear column tasks button
        self.clearbutton = tk.Button(self.frame, text="Del All", command=partial(team_clear_column, self.team_index, self.character))
        self.clearbutton.config(bg="#000000", fg="#FFFFFF", activebackground="#C117A5", activeforeground="#FFFFFF", highlightthickness=0)
        self.clearbutton.place(x=158,y=97,width=44,height=20)
        
        #Leftright buttons
        if col > 0:
            self.leftbutton = tk.Button(self.frame, text="<-", command=partial(team_swap_character, self.team_index, char_index, "Left"))
            self.leftbutton.config(activebackground="#C117A5", activeforeground="#FFFFFF", highlightthickness=0)
            self.leftbutton.place(x=224,y=97,width=20,height=20)
            
        if col < 9:
            self.rightbutton = tk.Button(self.frame, text="->", command=partial(team_swap_character, self.team_index, char_index, "Right"))
            self.rightbutton.config(activebackground="#C117A5", activeforeground="#FFFFFF", highlightthickness=0)
            self.rightbutton.place(x=246,y=97,width=20,height=20)
        
        # Make a canvas to contain the tasks so they can be scrolled?
        self.listcanvas = tk.Canvas(self.frame, width=298, height=1500, bg="#00B0BC", highlightthickness=0)
        self.listcanvas.place(x=-2,y=122)
        self.frame_list = ttk.Frame(self.listcanvas, width=298, height=1500, borderwidth=2, relief="solid")
        self.frame_list.place(x=-2,y=-2)
        
        self.listimage = tk.PhotoImage(file="./images/gachacharlist.png")
        self.listbg = ttk.Label(self.frame_list, image=self.listimage)
        self.listbg.place(x=-2,y=-2)
        
        # There is no way of knowing why this doesn't work.
        self.scrollbar = ttk.Scrollbar(self.listcanvas, orient="vertical", command=self.listcanvas.yview)
        self.listcanvas['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.place(x=0,y=0,anchor="e")
        
        
    def update_new_task_command(self, hackvar):
        self.newtaskcommand = partial(team_add_task, self.team_index, self.character, self.newtaskvar.get())
        self.newtaskbutton.config(command=self.newtaskcommand)

class TeamTaskWidget():
    def __init__(self, uuid, pos, master) -> None:
        self.uuid = uuid
        self.pos = pos
        self.master = master
        self.character = master.character
        if team.characternames.index(self.character) < 29:
            self.is5star = True
        else:
            self.is5star = False
        
    
    def add_common_buttons(self) -> None:
        # Task button: move up
        self.buttonUp = tk.Button(self.taskframe, text="Up", command=partial(team_move_up, self.master.team_index, self.uuid, self.character))
        self.buttonUp.config(activebackground="#2F6E6E", activeforeground="#FFFFFF", highlightthickness=0)
        self.buttonUp.place(x=241,y=3,width=30,height=20)
        
        # Task button: delete
        self.buttonDelete = tk.Button(self.taskframe, text="Del", command=partial(team_delete_task, self.master.team_index, self.uuid))
        self.buttonDelete.config(activebackground="#2F6E6E", activeforeground="#FFFFFF", highlightthickness=0)
        self.buttonDelete.place(x=241,y=25,width=30,height=20)
               

class TeamTaskWidgetLevel(TeamTaskWidget):
    def __init__(self, uuid, master, pos, level) -> None:
        TeamTaskWidget.__init__(self, uuid, pos, master)
        self.frameheight = 48
        self.taskframe = ttk.Frame(master.frame_list, width=274, height=self.frameheight, borderwidth=0, relief="solid")
        self.bgimage = tk.PhotoImage(file="./images/leveltask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)
        
        self.leveltext = tk.IntVar(self.taskframe, level)
        self.levelwidget = tk.OptionMenu(self.taskframe, self.leveltext, self.leveltext, *[80,70,60,50,40,30,20], command=partial(team_level_setlevel, self.master.team_index, self.uuid))
        self.levelwidget['menu'].delete(0)
        self.levelfont = tkFont.Font(size=12)
        self.levelwidget.config(bg="#009A97", fg="#FFFFFF", activebackground="#009A97", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.levelfont)
        self.levelwidget['menu'].config(bg="#009A97", fg="#FFFFFF", activebackground="#009A97", activeforeground="#FFFFFF")
        self.levelwidget.place(x=4,y=16,width=70,height=28)
        
        # Required Materials
        self.mat_list = [team.charactermaterials[self.character]["LevelMat"], mapping.commonmats[team.charactermaterials[self.character]["CommonMat"]]]
        self.total = [0,[0,0,0]]
        levelindex = master.charlevelint.get()
        while levelindex < level:
            levelindex += 10
            if self.is5star:
                self.total[0] += team.levelmaterials5[levelindex][0]
                self.total[1][0] += team.levelmaterials5[levelindex][1][0]
                self.total[1][1] += team.levelmaterials5[levelindex][1][1]
                self.total[1][2] += team.levelmaterials5[levelindex][1][2]
            else:
                self.total[0] += team.levelmaterials4[levelindex][0]
                self.total[1][0] += team.levelmaterials4[levelindex][1][0]
                self.total[1][1] += team.levelmaterials4[levelindex][1][1]
                self.total[1][2] += team.levelmaterials4[levelindex][1][2]
        
        self.matcanv = tk.Canvas(self.taskframe, width=160, height=42, bg="#00FFFB", highlightthickness=0)
        self.matcanv.create_text(1,-1, text=f"{self.mat_list[0]}", font=tkFont.Font(size=8), anchor="nw")
        self.matcanv.create_text(1,9, text=f"{team.charactermaterials[self.character]['CommonMat']}", font=tkFont.Font(size=8), anchor="nw")
        
        self.matbossbg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
        self.matcanv.create_image((101,10), image=self.matbossbg)
        self.matbossimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[0]]}2.png")
        self.matcanv.create_image((101,10), image=self.matbossimg)
        self.matcanv.create_text(122,10, text=f"x{self.total[0]}")
        
        self.matgreenbg = tk.PhotoImage(file=f"./images/inventory/invgreen2.png")
        self.matcanv.create_image((10,32), image=self.matgreenbg)
        self.matgreenimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][0]]}2.png")
        self.matcanv.create_image((10,32), image=self.matgreenimg)
        self.matcanv.create_text(31,32, text=f"x{self.total[1][0]}")
        
        self.matbluebg = tk.PhotoImage(file=f"./images/inventory/invblue2.png")
        self.matcanv.create_image((55,32), image=self.matbluebg)
        self.matblueimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][1]]}2.png")
        self.matcanv.create_image((55,32), image=self.matblueimg)
        self.matcanv.create_text(76,32, text=f"x{self.total[1][1]}")
        
        self.matpurplebg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
        self.matcanv.create_image((101,32), image=self.matpurplebg)
        self.matpurpleimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][2]]}2.png")
        self.matcanv.create_image((101,32), image=self.matpurpleimg)
        self.matcanv.create_text(122,32, text=f"x{self.total[1][2]}")
        
        self.matcanv.place(x=102,y=3)
        
        self.add_common_buttons()
        
        
class TeamTaskWidgetWeaponLevel(TeamTaskWidget):
    def __init__(self, uuid, master, pos, level) -> None:
        TeamTaskWidget.__init__(self, uuid, pos, master)
        self.weapon = master.characterdict['Weapon']
        self.frameheight = 48
        self.taskframe = ttk.Frame(master.frame_list, width=274, height=self.frameheight, borderwidth=0, relief="solid")
        self.bgimage = tk.PhotoImage(file="./images/weaponleveltask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)
        
        self.leveltext = tk.IntVar(self.taskframe, level)
        self.levelwidget = tk.OptionMenu(self.taskframe, self.leveltext, self.leveltext, *[80,70,60,50,40,30,20], command=partial(team_weapon_setlevel, self.master.team_index, self.uuid))
        self.levelwidget['menu'].delete(0)
        self.levelfont = tkFont.Font(size=12)
        self.levelwidget.config(bg="#08679D", fg="#FFFFFF", activebackground="#08679D", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.levelfont)
        self.levelwidget['menu'].config(bg="#08679D", fg="#FFFFFF", activebackground="#08679D", activeforeground="#FFFFFF")
        self.levelwidget.place(x=4,y=16,width=70,height=28)
        
        # Required Materials
        self.mat_list = [mapping.commonmats[team.weaponmaterials[self.weapon]["CommonMat"]], mapping.tracemats[team.weaponmaterials[self.weapon]["TraceMat"]]]
        self.total = [[0,0,0],[0,0,0]]
        levelindex = master.weplevelint.get()
        while levelindex < level:
            levelindex += 10
            if self.is5star:
                self.total[0][0] += team.weaponmaterials5[levelindex][0][0]
                self.total[0][1] += team.weaponmaterials5[levelindex][0][1]
                self.total[0][2] += team.weaponmaterials5[levelindex][0][2]
                self.total[1][0] += team.weaponmaterials5[levelindex][1][0]
                self.total[1][1] += team.weaponmaterials5[levelindex][1][1]
                self.total[1][2] += team.weaponmaterials5[levelindex][1][2]
            else:
                self.total[0][0] += team.weaponmaterials4[levelindex][0][0]
                self.total[0][1] += team.weaponmaterials4[levelindex][0][1]
                self.total[0][2] += team.weaponmaterials4[levelindex][0][2]
                self.total[1][0] += team.weaponmaterials4[levelindex][1][0]
                self.total[1][1] += team.weaponmaterials4[levelindex][1][1]
                self.total[1][2] += team.weaponmaterials4[levelindex][1][2]
        
        self.matcanv = tk.Canvas(self.taskframe, width=160, height=42, bg="#08A4FF", highlightthickness=0)
        
        self.matcomgreenbg = tk.PhotoImage(file=f"./images/inventory/invgreen2.png")
        self.matcanv.create_image((10,10), image=self.matcomgreenbg)
        self.matcomgreenimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[0][0]]}2.png")
        self.matcanv.create_image((10,10), image=self.matcomgreenimg)
        self.matcanv.create_text(31,10, text=f"x{self.total[0][0]}")
        
        self.matcombluebg = tk.PhotoImage(file=f"./images/inventory/invblue2.png")
        self.matcanv.create_image((55,10), image=self.matcombluebg)
        self.matcomblueimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[0][1]]}2.png")
        self.matcanv.create_image((55,10), image=self.matcomblueimg)
        self.matcanv.create_text(76,10, text=f"x{self.total[0][1]}")
        
        self.matcompurplebg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
        self.matcanv.create_image((101,10), image=self.matcompurplebg)
        self.matcompurpleimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[0][2]]}2.png")
        self.matcanv.create_image((101,10), image=self.matcompurpleimg)
        self.matcanv.create_text(122,10, text=f"x{self.total[0][2]}")
        
        self.mattragreenbg = tk.PhotoImage(file=f"./images/inventory/invgreen2.png")
        self.matcanv.create_image((10,32), image=self.mattragreenbg)
        self.mattragreenimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][0]]}2.png")
        self.matcanv.create_image((10,32), image=self.mattragreenimg)
        self.matcanv.create_text(31,32, text=f"x{self.total[1][0]}")
        
        self.mattrabluebg = tk.PhotoImage(file=f"./images/inventory/invblue2.png")
        self.matcanv.create_image((55,32), image=self.mattrabluebg)
        self.mattrablueimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][1]]}2.png")
        self.matcanv.create_image((55,32), image=self.mattrablueimg)
        self.matcanv.create_text(76,32, text=f"x{self.total[1][1]}")
        
        self.mattrapurplebg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
        self.matcanv.create_image((101,32), image=self.mattrapurplebg)
        self.mattrapurpleimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][2]]}2.png")
        self.matcanv.create_image((101,32), image=self.mattrapurpleimg)
        self.matcanv.create_text(122,32, text=f"x{self.total[1][2]}")
        
        self.matcanv.place(x=102,y=3)
        
        self.add_common_buttons()


class TeamTaskWidgetAscension(TeamTaskWidget):
    def __init__(self, uuid, master, pos, trace) -> None:        
        TeamTaskWidget.__init__(self, uuid, pos, master)
        self.frameheight = 48
        self.taskframe = ttk.Frame(master.frame_list, width=274, height=self.frameheight, borderwidth=0, relief="solid")
        self.bgimage = tk.PhotoImage(file="./images/ascensiontask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)  
        
        self.ascensiontext = tk.IntVar(self.taskframe, trace)
        self.ascensionwidget = tk.OptionMenu(self.taskframe, self.ascensiontext, self.ascensiontext, *["A2","A4","A6"], command=partial(team_ascension_set, self.master.team_index, self.uuid))
        self.ascensionwidget['menu'].delete(0)
        self.ascensionfont = tkFont.Font(size=12)
        self.ascensionwidget.config(bg="#673E84", fg="#FFFFFF", activebackground="#673E84", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.ascensionfont)
        self.ascensionwidget['menu'].config(bg="#673E84", fg="#FFFFFF", activebackground="#673E84", activeforeground="#FFFFFF")
        self.ascensionwidget.place(x=4,y=16,width=70,height=28)
        
        self.mat_list = [team.charactermaterials[master.character]['WBMat'], mapping.tracemats[team.charactermaterials[master.character]["TraceMat"]]]
        if self.is5star:
            tracecost = [3,5,8]
        else:
            tracecost = [2,4,6] 
        self.matcanv = tk.Canvas(self.taskframe, width=160, height=42, bg="#C779FF", highlightthickness=0)
        self.matcanv.create_text(1,-1, text=f"{self.mat_list[0]}", font=tkFont.Font(size=8), anchor="nw")
        self.matcanv.create_text(1,9, text=f"{team.charactermaterials[master.character]['TraceMat']}", font=tkFont.Font(size=8), anchor="nw")
        
        match trace:
            case "A2": # tracecost[0] green mats, 1 wbmat
                self.mattrabg = tk.PhotoImage(file=f"./images/inventory/invgreen2.png")
                self.matcanv.create_image((10,32), image=self.mattrabg)
                self.mattraimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][0]]}2.png")
                self.matcanv.create_image((10,32), image=self.mattraimg)
                self.matcanv.create_text(31,32, text=f"x{tracecost[0]}")
        
                self.matwbbg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
                self.matcanv.create_image((55,32), image=self.matwbbg)
                self.matwbimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[0]]}2.png")
                self.matcanv.create_image((55,32), image=self.matwbimg)
                self.matcanv.create_text(76,32, text=f"x1")
                
            case "A4": # tracecost[1] blue mats, 1 wbmat, 1 goldmat
                self.mattrabg = tk.PhotoImage(file=f"./images/inventory/invblue2.png")
                self.matcanv.create_image((10,32), image=self.mattrabg)
                self.mattraimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][1]]}2.png")
                self.matcanv.create_image((10,32), image=self.mattraimg)
                self.matcanv.create_text(31,32, text=f"x{tracecost[1]}")
        
                self.matwbbg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
                self.matcanv.create_image((55,32), image=self.matwbbg)
                self.matwbimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[0]]}2.png")
                self.matcanv.create_image((55,32), image=self.matwbimg)
                self.matcanv.create_text(76,32, text=f"x1")
        
                self.matgoldbg = tk.PhotoImage(file=f"./images/inventory/invgold2.png")
                self.matcanv.create_image((101,32), image=self.matgoldbg)
                self.matgoldimg = tk.PhotoImage(file=f"./images/inventory/goldtrace2.png")
                self.matcanv.create_image((101,32), image=self.matgoldimg)
                self.matcanv.create_text(122,32, text=f"x1")
                
            case "A6": # tracecost[2] purple mats, 1 wbmat, 1 goldmat
                self.mattrabg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
                self.matcanv.create_image((10,32), image=self.mattrabg)
                self.mattraimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1][2]]}2.png")
                self.matcanv.create_image((10,32), image=self.mattraimg)
                self.matcanv.create_text(31,32, text=f"x{tracecost[2]}")
        
                self.matwbbg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
                self.matcanv.create_image((55,32), image=self.matwbbg)
                self.matwbimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[0]]}2.png")
                self.matcanv.create_image((55,32), image=self.matwbimg)
                self.matcanv.create_text(76,32, text=f"x1")
        
                self.matgoldbg = tk.PhotoImage(file=f"./images/inventory/invgold2.png")
                self.matcanv.create_image((101,32), image=self.matgoldbg)
                self.matgoldimg = tk.PhotoImage(file=f"./images/inventory/goldtrace2.png")
                self.matcanv.create_image((101,32), image=self.matgoldimg)
                self.matcanv.create_text(122,32, text=f"x1")
        
        self.matcanv.place(x=102,y=3)
        
        self.add_common_buttons()


class TeamTaskWidgetTrace(TeamTaskWidget):
    def __init__(self, uuid, master, pos, trace, target) -> None:        
        TeamTaskWidget.__init__(self, uuid, pos, master)
        self.frameheight = 72
        self.taskframe = ttk.Frame(master.frame_list, width=274, height=self.frameheight, borderwidth=0, relief="solid")
        self.bgimage = tk.PhotoImage(file="./images/tracetask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)  
        
        self.tracetext = tk.IntVar(self.taskframe, trace)
        self.tracewidget = tk.OptionMenu(self.taskframe, self.tracetext, self.tracetext, *["Basic","Skill","Ult","Talent"], command=partial(team_trace_settrace, self.master.team_index, self.uuid))
        self.tracewidget['menu'].delete(0)
        self.tracefont = tkFont.Font(size=12)
        self.tracewidget.config(bg="#404484", fg="#FFFFFF", activebackground="#404484", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.tracefont)
        self.tracewidget['menu'].config(bg="#404484", fg="#FFFFFF", activebackground="#404484", activeforeground="#FFFFFF")
        self.tracewidget.place(x=4,y=16,width=70,height=26)
        
        self.targettext = tk.IntVar(self.taskframe, target)
        if trace == "Basic":
            self.targetoptions = [6,5,4,3,2]
        else:
            self.targetoptions = [10,9,8,7,6,5,4,3,2]
        self.targetwidget = tk.OptionMenu(self.taskframe, self.targettext, self.targettext, *self.targetoptions, command=partial(team_trace_settarget, self.master.team_index, self.uuid))
        self.targetwidget['menu'].delete(0)
        self.targetfont = tkFont.Font(size=12)
        self.targetwidget.config(bg="#404484", fg="#FFFFFF", activebackground="#404484", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.targetfont)
        self.targetwidget['menu'].config(bg="#404484", fg="#FFFFFF", activebackground="#404484", activeforeground="#FFFFFF")
        self.targetwidget.place(x=4,y=43,width=70,height=26)
        
        if trace == "Basic":
            # Required Materials
            self.mat_list = [mapping.tracemats[team.charactermaterials[self.character]["TraceMat"]],mapping.commonmats[team.charactermaterials[self.character]["CommonMat"]]]
            self.total = [[0,0,0],[0,0,0]]
            targetindex = master.characterdict["BasicLV"]
            while targetindex < target:
                targetindex += 1
                if self.is5star:
                    self.total[0][0] += team.basicmaterials5[targetindex][0][0]
                    self.total[0][1] += team.basicmaterials5[targetindex][0][1]
                    self.total[0][2] += team.basicmaterials5[targetindex][0][2]
                    self.total[1][0] += team.basicmaterials5[targetindex][1][0]
                    self.total[1][1] += team.basicmaterials5[targetindex][1][1]
                    self.total[1][2] += team.basicmaterials5[targetindex][1][2]
                else:
                    self.total[0][0] += team.basicmaterials4[targetindex][0][0]
                    self.total[0][1] += team.basicmaterials4[targetindex][0][1]
                    self.total[0][2] += team.basicmaterials4[targetindex][0][2]
                    self.total[1][0] += team.basicmaterials4[targetindex][1][0]
                    self.total[1][1] += team.basicmaterials4[targetindex][1][1]
                    self.total[1][2] += team.basicmaterials4[targetindex][1][2]
        else:
            # Required Materials
            self.mat_list = ["",team.charactermaterials[master.character]['WBMat'], mapping.tracemats[team.charactermaterials[self.character]["TraceMat"]],\
                mapping.commonmats[team.charactermaterials[self.character]["CommonMat"]]]
            self.total = [0,0,[0,0,0],[0,0,0]]
            match trace:
                case "Skill":
                    targetindex = master.characterdict["SkillLV"]
                case "Ult":
                    targetindex = master.characterdict["UltLV"]
                case "Talent":
                    targetindex = master.characterdict["TalentLV"]
            while targetindex < target:
                targetindex += 1
                if self.is5star:
                    self.total[0] += team.tracematerials5[targetindex][0]
                    self.total[1] += team.tracematerials5[targetindex][1]
                    self.total[2][0] += team.tracematerials5[targetindex][2][0]
                    self.total[2][1] += team.tracematerials5[targetindex][2][1]
                    self.total[2][2] += team.tracematerials5[targetindex][2][2]
                    self.total[3][0] += team.tracematerials5[targetindex][3][0]
                    self.total[3][1] += team.tracematerials5[targetindex][3][1]
                    self.total[3][2] += team.tracematerials5[targetindex][3][2]
                else:
                    self.total[0] += team.tracematerials4[targetindex][0]
                    self.total[1] += team.tracematerials4[targetindex][1]
                    self.total[2][0] += team.tracematerials4[targetindex][2][0]
                    self.total[2][1] += team.tracematerials4[targetindex][2][1]
                    self.total[2][2] += team.tracematerials4[targetindex][2][2]
                    self.total[3][0] += team.tracematerials4[targetindex][3][0]
                    self.total[3][1] += team.tracematerials4[targetindex][3][1]
                    self.total[3][2] += team.tracematerials4[targetindex][3][2]
        
        self.matcanv = tk.Canvas(self.taskframe, width=170, height=66, bg="#7C84FF", highlightthickness=0)
        if trace != "Basic":
            self.matcanv.create_text(1,-1, text=f"{self.mat_list[1]}", font=tkFont.Font(size=8), anchor="nw")
        self.matcanv.create_text(1,9, text=f"{team.charactermaterials[master.character]['TraceMat']}, {team.charactermaterials[master.character]['CommonMat']}",\
            font=tkFont.Font(size=8), anchor="nw")
        
        if trace == "Basic":
            self.tracemats = self.mat_list[0]
            self.commonmats = self.mat_list[1]
            self.rankedmattotal = self.total
        else:
            self.tracemats = self.mat_list[2]
            self.commonmats = self.mat_list[3]
            self.rankedmattotal = self.total[2:]
            
        self.matcomgreenbg = tk.PhotoImage(file=f"./images/inventory/invgreen2.png")
        self.matcanv.create_image((10,32), image=self.matcomgreenbg)
        self.matcomgreenimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.commonmats[0]]}2.png")
        self.matcanv.create_image((10,32), image=self.matcomgreenimg)
        self.matcanv.create_text(31,32, text=f"x{self.rankedmattotal[0][0]}")
        
        self.matcombluebg = tk.PhotoImage(file=f"./images/inventory/invblue2.png")
        self.matcanv.create_image((55,32), image=self.matcombluebg)
        self.matcomblueimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.commonmats[1]]}2.png")
        self.matcanv.create_image((55,32), image=self.matcomblueimg)
        self.matcanv.create_text(76,32, text=f"x{self.rankedmattotal[0][1]}")
        
        self.matcompurplebg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
        self.matcanv.create_image((101,32), image=self.matcompurplebg)
        self.matcompurpleimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.commonmats[2]]}2.png")
        self.matcanv.create_image((101,32), image=self.matcompurpleimg)
        self.matcanv.create_text(122,32, text=f"x{self.rankedmattotal[0][2]}")
        
        self.mattragreenbg = tk.PhotoImage(file=f"./images/inventory/invgreen2.png")
        self.matcanv.create_image((10,54), image=self.mattragreenbg)
        self.mattragreenimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.tracemats[0]]}2.png")
        self.matcanv.create_image((10,54), image=self.mattragreenimg)
        self.matcanv.create_text(31,54, text=f"x{self.rankedmattotal[1][0]}")
        
        self.mattrabluebg = tk.PhotoImage(file=f"./images/inventory/invblue2.png")
        self.matcanv.create_image((55,54), image=self.mattrabluebg)
        self.mattrablueimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.tracemats[1]]}2.png")
        self.matcanv.create_image((55,54), image=self.mattrablueimg)
        self.matcanv.create_text(76,54, text=f"x{self.rankedmattotal[1][1]}")
        
        self.mattrapurplebg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
        self.matcanv.create_image((101,54), image=self.mattrapurplebg)
        self.mattrapurpleimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.tracemats[2]]}2.png")
        self.matcanv.create_image((101,54), image=self.mattrapurpleimg)
        self.matcanv.create_text(122,54, text=f"x{self.rankedmattotal[1][2]}")
        
        if trace != "Basic":
            self.matbossbg = tk.PhotoImage(file=f"./images/inventory/invpurple2.png")
            self.matcanv.create_image((101,10), image=self.matbossbg)
            self.matbossimg = tk.PhotoImage(file=f"./images/inventory/{mapping.imagemap[self.mat_list[1]]}2.png")
            self.matcanv.create_image((101,10), image=self.matbossimg)
            self.matcanv.create_text(122,10, text=f"x{self.total[1]}")
            
            self.matgoldbg = tk.PhotoImage(file=f"./images/inventory/invgold2.png")
            self.matcanv.create_image((144,54), image=self.matgoldbg)
            self.matgoldimg = tk.PhotoImage(file=f"./images/inventory/goldtrace2.png")
            self.matcanv.create_image((144,54), image=self.matgoldimg)
            self.matcanv.create_text(162,54, text=f"x{self.total[0]}")
        
        self.matcanv.place(x=102,y=3)
        
        self.add_common_buttons()
    
    
class TeamTaskWidgetRelic(TeamTaskWidget):
    def __init__(self, uuid, master, pos, set, slot, mainstat, substats:list) -> None:        
        TeamTaskWidget.__init__(self, uuid, pos, master)
        self.frameheight = 96
        self.taskframe = ttk.Frame(master.frame_list, width=274, height=self.frameheight, borderwidth=0, relief="solid")
        self.bgimage = tk.PhotoImage(file="./images/relictask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)
        
        self.settext = tk.StringVar(self.taskframe, set)
        self.setwidget = tk.OptionMenu(self.taskframe, self.settext, self.settext, *team.relicsets, command=partial(team_relic_setset, self.master.team_index, self.uuid))
        self.setwidget['menu'].delete(0)
        self.setfont = tkFont.Font(size=10)
        self.setwidget.config(bg="#9E517E", fg="#FFFFFF", activebackground="#9E517E", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.setfont)
        self.setwidget['menu'].config(bg="#9E517E", fg="#FFFFFF", activebackground="#9E517E", activeforeground="#FFFFFF")
        self.setwidget.place(x=4,y=4,width=155,height=28)
        
        self.slottext = tk.StringVar(self.taskframe, slot)
        self.slotwidget = tk.OptionMenu(self.taskframe, self.slottext, self.slottext, *team.relicpieces[set], command=partial(team_relic_setslot, self.master.team_index, self.uuid))
        self.slotwidget['menu'].delete(0)
        self.slotwidget.config(bg="#9E517E", fg="#FFFFFF", activebackground="#9E517E", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.setfont)
        self.slotwidget['menu'].config(bg="#9E517E", fg="#FFFFFF", activebackground="#9E517E", activeforeground="#FFFFFF")
        self.slotwidget.place(x=160,y=4,width=60,height=28)
        
        self.stattext = tk.StringVar(self.taskframe, mainstat)
        self.statwidget = tk.OptionMenu(self.taskframe, self.stattext, self.stattext, *team.relicmainstats[slot], command=partial(team_relic_setstat, self.master.team_index, self.uuid))
        self.statwidget['menu'].delete(0)
        self.statfont = tkFont.Font(size=9)
        self.statwidget.config(bg="#9E517E", fg="#FFFFFF", activebackground="#9E517E", activeforeground="#FFFFFF", justify="left", highlightthickness=0,font=self.statfont)
        self.statwidget['menu'].config(bg="#9E517E", fg="#FFFFFF", activebackground="#9E517E", activeforeground="#FFFFFF")
        self.statwidget.place(x=4,y=52,width=70,height=28)
        
        self.substat1text = tk.StringVar(self.taskframe, substats[0])
        self.substat1widget = tk.OptionMenu(self.taskframe, self.substat1text, self.substat1text, *team.relicsubstats, command=partial(team_relic_setsubstat, self.master.team_index, self.uuid, 0))
        self.substat1widget['menu'].delete(0)
        self.substatfont = tkFont.Font(size=9)
        self.substat1widget.config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000", justify="left", highlightthickness=0,font=self.statfont)
        self.substat1widget['menu'].config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000")
        self.substat1widget.place(x=91,y=41,width=70,height=24)
        
        self.substat2text = tk.StringVar(self.taskframe, substats[1])
        self.substat2widget = tk.OptionMenu(self.taskframe, self.substat2text, self.substat2text, *team.relicsubstats, command=partial(team_relic_setsubstat, self.master.team_index, self.uuid, 1))
        self.substat2widget['menu'].delete(0)
        self.substat2widget.config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000", justify="left", highlightthickness=0,font=self.statfont)
        self.substat2widget['menu'].config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000")
        self.substat2widget.place(x=162,y=41,width=70,height=24)
        
        self.substat3text = tk.StringVar(self.taskframe, substats[2])
        self.substat3widget = tk.OptionMenu(self.taskframe, self.substat3text, self.substat3text, *team.relicsubstats, command=partial(team_relic_setsubstat, self.master.team_index, self.uuid, 2))
        self.substat3widget['menu'].delete(0)
        self.substat3widget.config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000", justify="left", highlightthickness=0,font=self.statfont)
        self.substat3widget['menu'].config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000")
        self.substat3widget.place(x=91,y=66,width=70,height=24)
        
        self.substat4text = tk.StringVar(self.taskframe, substats[3])
        self.substat4widget = tk.OptionMenu(self.taskframe, self.substat4text, self.substat4text, *team.relicsubstats, command=partial(team_relic_setsubstat, self.master.team_index, self.uuid, 3))
        self.substat4widget['menu'].delete(0)
        self.substat4widget.config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000", justify="left", highlightthickness=0,font=self.statfont)
        self.substat4widget['menu'].config(bg="#FF6DD6", fg="#000000", activebackground="#FF6DD6", activeforeground="#000000")
        self.substat4widget.place(x=162,y=66,width=70,height=24)
        
        self.add_common_buttons()


class GachaTaskWidget():
    def __init__(self, uuid, master, pos, objectname, target, priority) -> None:
        self.uuid = uuid
        self.pos = pos
        self.taskframe = ttk.Frame(master, width=374, height=96, borderwidth=0, relief="solid")
        
        # Task frame image
        self.bgimage = tk.PhotoImage(file="./images/gachatask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)
        
        # Task name dropdown
        self.objectname = tk.StringVar(self.taskframe, objectname)
        self.taskname = tk.OptionMenu(self.taskframe, self.objectname, self.objectname, *gacha.objectnames, command=partial(gacha_set_object, self.uuid))
        self.taskname['menu'].delete(0)
        self.taskname.config(bg="#2F6E6E", fg="#FFFFFF", activebackground="#2F6E6E", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.taskname['menu'].config(bg="#2F6E6E", fg="#FFFFFF", activebackground="#2F6E6E", activeforeground="#FFFFFF")
        self.taskname.place(x=91,y=10,width=200,height=30)
        
        # Task target dropdown
        self.target = tk.StringVar(self.taskframe, target)
        self.tasktarget = tk.OptionMenu(self.taskframe, self.target, self.target, *gacha.targets, command=partial(gacha_set_target, self.uuid))
        self.tasktarget['menu'].delete(0)
        self.tasktarget.config(bg="#2F6E6E", fg="#FFFFFF", activebackground="#2F6E6E", activeforeground="#FFFFFF", justify="left", highlightthickness=0)
        self.tasktarget['menu'].config(bg="#2F6E6E", fg="#FFFFFF", activebackground="#2F6E6E", activeforeground="#FFFFFF")
        self.tasktarget.place(x=294,y=10,width=50,height=30)
        
        # Task image
        self.image = tk.PhotoImage(file=f"./images/gacha/{mapping.imagemap[objectname]}.png")
        self.taskimage = tk.Canvas(self.taskframe, width=81, height=92, bg="#1C4343", highlightthickness=0)
        self.taskimage.create_image((40, 46), image=self.image)
        self.taskimage.place(x=2,y=2)
        
        # Task 'predicted cost'
        self.cost75 = int((160 * (1+int(target[1])) * 78 * 3)/2)
        self.cost100 = int(160 * (1+int(target[1])) * 85 * 2)
        self.costtext = f"{self.cost75} | {self.cost100}"
        self.costwidget = tk.Label(self.taskframe, text=self.costtext, bg="#6DFFFF", font=tkFont.Font(size=10))
        self.costwidget.place(x=124,y=61)
        
        # Task button: move up
        self.buttonUp = tk.Button(self.taskframe, text="Up", command=partial(gacha_move_up, self.uuid, priority))
        self.buttonUp.config(activebackground="#2F6E6E", activeforeground="#FFFFFF", highlightthickness=0)
        self.buttonUp.place(x=303,y=57,width=30,height=30)
        
        # Task dropdown: priority
        self.priority = tk.StringVar(self.taskframe, priority)
        self.taskpriority = tk.OptionMenu(self.taskframe, self.priority, self.priority, *["High", "Med", "Low"], command=partial(gacha_change_priority, self.uuid))
        self.taskpriority['menu'].delete(0)
        self.taskpriority.config(justify="left", highlightthickness=0)
        self.taskpriority.place(x=241,y=57,width=60,height=30)
        
        # Task button: delete
        self.buttonDelete = tk.Button(self.taskframe, text="Del", command=partial(gacha_delete_task, self.uuid))
        self.buttonDelete.config(activebackground="#2F6E6E", activeforeground="#FFFFFF", highlightthickness=0)
        self.buttonDelete.place(x=335,y=57,width=30,height=30)
        


class Tabset():
    def __init__(self) -> None:
        self.notebook = ttk.Notebook(root)
        self.frame_summary = Tab(self.notebook)
        self.gacha = []
        self.frame_gacha = Tab(self.notebook)
        self.teams = []
        self.frames_teams = []
        
        self.gachasource = data.get_gacha()
        self.teamsource = data.get_teams()


    def reload(self) -> None:
        try:
            currenttab = self.notebook.index(self.notebook.select())
        except:
            pass
        self.gachasource = data.get_gacha()
        self.teamsource = data.get_teams()
        self.clear()
        self.prepare()
        self.show()
        try:
            self.notebook.select(currenttab)
        except:
            pass
    
    
    def clear(self):
        self.notebook.destroy()
        self.notebook = ttk.Notebook(root)
        self.frame_summary = Tab(self.notebook)
        self.gacha = []
        self.frame_gacha = Tab(self.notebook)
        self.teams = []
        self.frames_teams = []
        
 
    def prepare(self):
        # Separate presentation team data from storage team data
        for team in self.teamsource:
            self.teams.append(team)
        # Create team frames in frames_teams
        for team in self.teams:
            self.frames_teams.append(Tab(self.notebook))
        
        # Get presentable data from gacha tasks.
        for task in self.gachasource.tasks:
            newtask = {
                "uuid": task.uuid,
                "priority": task.priority,
                "pos": task.pos,
                "object": task.objectname,
                "target": task.target
            }
            self.gacha.append(newtask)
        

    def show(self):
        self.notebook.pack()
        
        # Show Summary tab
        self.frame_summary.frame.place(x=0,y=0)
        self.notebook.add(self.frame_summary.frame, text="Summary")
        
        
        # Show each teams tab
        for i in range(len(self.frames_teams)):
            self.frames_teams[i].frame.place(x=0,y=0)
            self.notebook.add(self.frames_teams[i].frame, text=f"Team {i+1}")
            self.frames_teams[i].make_team_tab(self.teams[i])
        
        
        # Show Gacha tab
        self.frame_gacha.frame.place(x=0,y=0)
        self.notebook.add(self.frame_gacha.frame, text="Gacha")
        self.frame_gacha.make_gacha_tab(self.gacha)
        
        
tabset = Tabset()


# ------------ Button Functions ----------------

def gacha_add_task(priority:str) -> None:
    match priority:
        case "High":
            tasklist = tabset.frame_gacha.highpri
        case "Med":
            tasklist = tabset.frame_gacha.medpri
        case "Low":
            tasklist = tabset.frame_gacha.lowpri
            
    if len(tasklist) > 0:
        pos = tasklist[len(tasklist)-1].pos + 1
    else:
        pos = 1
                
    tabset.gachasource.tasks.append(gacha.GachaTask(f"gacha{data.next_uuid()}", priority, pos, "Acheron", "E0"))
    data.set_gacha(tabset.gachasource)
    tabset.reload()
    

def gacha_move_up(uuid, priority):
    match priority:
        case "High":
            tasklist = tabset.frame_gacha.highpri
        case "Med":
            tasklist = tabset.frame_gacha.medpri
        case "Low":
            tasklist = tabset.frame_gacha.lowpri
            
    for i in range(len(tasklist)):
        if tasklist[i].uuid == uuid:
            if i == 0:
                print("Can't move top item up")
                return
            else:
                pos1 = tasklist[i].pos
                uuid2 = tasklist[i-1].uuid
                pos2 = tasklist[i-1].pos
                break
    posswapped1 = False
    posswapped2 = False
    for gachatask in tabset.gachasource.tasks:
        if gachatask.uuid == uuid:
            gachatask.pos = pos2
            posswapped1 = True
        elif gachatask.uuid == uuid2:
            gachatask.pos = pos1
            posswapped2 = True
        if posswapped1 and posswapped2:
            print(f"Moved {uuid} up")
            break
    data.set_gacha(tabset.gachasource)
    tabset.reload()


def gacha_change_priority(uuid, priority):
    print(f"setting {uuid} to {priority}")
    match priority:
        case "High":
            tasklist = tabset.frame_gacha.highpri
        case "Med":
            tasklist = tabset.frame_gacha.highpri
        case "Low":
            tasklist = tabset.frame_gacha.highpri
            
    if len(tasklist) > 0:
        pos = tasklist[len(tasklist)-1].pos + 1
    else:
        pos = 1
        
    for gachatask in tabset.gachasource.tasks:
        if gachatask.uuid == uuid:
            gachatask.priority = priority
            gachatask.pos = pos
            break
    data.set_gacha(tabset.gachasource)
    tabset.reload()


def gacha_delete_task(uuid):
    print(f"deleting {uuid}")
    for i in range(len(tabset.gachasource.tasks)):
        if tabset.gachasource.tasks[i].uuid == uuid:
            tabset.gachasource.tasks.pop(i)
            break
    data.set_gacha(tabset.gachasource)
    tabset.reload()


def gacha_set_object(uuid, objectname):
    print(f"setting {uuid} to {objectname}")
    for gachatask in tabset.gachasource.tasks:
        if gachatask.uuid == uuid:
            gachatask.objectname = objectname
            break
    data.set_gacha(tabset.gachasource)
    tabset.reload()
    

def gacha_set_target(uuid, target):
    print(f"setting {uuid} to {target}")
    for gachatask in tabset.gachasource.tasks:
        if gachatask.uuid == uuid:
            gachatask.target = target
            break
    data.set_gacha(tabset.gachasource)
    tabset.reload()


def team_set_character(team_ref, char_ref, char_name):
    print(f"setting {team_ref} {char_ref} to {char_name}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["Name"] = char_name
        case 1:
            tabset.teamsource[team_ref-1].character2["Name"] = char_name
        case 2:
            tabset.teamsource[team_ref-1].character3["Name"] = char_name
        case 3:
            tabset.teamsource[team_ref-1].character4["Name"] = char_name
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_set_weapon(team_ref, char_ref, wep_name):
    print(f"setting {team_ref} {char_ref} weapon to {wep_name}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["Weapon"] = wep_name
        case 1:
            tabset.teamsource[team_ref-1].character2["Weapon"] = wep_name
        case 2:
            tabset.teamsource[team_ref-1].character3["Weapon"] = wep_name
        case 3:
            tabset.teamsource[team_ref-1].character4["Weapon"] = wep_name
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_set_character_level(team_ref, char_ref, char_level):
    print(f"setting {team_ref} {char_ref} level to {char_level}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["Level"] = char_level
        case 1:
            tabset.teamsource[team_ref-1].character2["Level"] = char_level
        case 2:
            tabset.teamsource[team_ref-1].character3["Level"] = char_level
        case 3:
            tabset.teamsource[team_ref-1].character4["Level"] = char_level
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_set_weapon_level(team_ref, char_ref, wep_level):
    print(f"setting {team_ref} {char_ref} weapon level to {wep_level}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["WeaponLV"] = wep_level
        case 1:
            tabset.teamsource[team_ref-1].character2["WeaponLV"] = wep_level
        case 2:
            tabset.teamsource[team_ref-1].character3["WeaponLV"] = wep_level
        case 3:
            tabset.teamsource[team_ref-1].character4["WeaponLV"] = wep_level
    data.set_teams(tabset.teamsource)
    tabset.reload()

def team_set_trace_basic(team_ref, char_ref, basic_level):
    print(f"setting {team_ref} {char_ref} basic to {basic_level}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["BasicLV"] = basic_level[1:]
        case 1:
            tabset.teamsource[team_ref-1].character2["BasicLV"] = basic_level[1:]
        case 2:
            tabset.teamsource[team_ref-1].character3["BasicLV"] = basic_level[1:]
        case 3:
            tabset.teamsource[team_ref-1].character4["BasicLV"] = basic_level[1:]
    data.set_teams(tabset.teamsource)
    tabset.reload()

def team_set_trace_skill(team_ref, char_ref, skill_level):
    print(f"setting {team_ref} {char_ref} skill to {skill_level}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["SkillLV"] = skill_level[1:]
        case 1:
            tabset.teamsource[team_ref-1].character2["SkillLV"] = skill_level[1:]
        case 2:
            tabset.teamsource[team_ref-1].character3["SkillLV"] = skill_level[1:]
        case 3:
            tabset.teamsource[team_ref-1].character4["SkillLV"] = skill_level[1:]
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_set_trace_ult(team_ref, char_ref, ult_level):
    print(f"setting {team_ref} {char_ref} ult to {ult_level}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["UltLV"] = ult_level[1:]
        case 1:
            tabset.teamsource[team_ref-1].character2["UltLV"] = ult_level[1:]
        case 2:
            tabset.teamsource[team_ref-1].character3["UltLV"] = ult_level[1:]
        case 3:
            tabset.teamsource[team_ref-1].character4["UltLV"] = ult_level[1:]
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_set_trace_talent(team_ref, char_ref, talent_level):
    print(f"setting {team_ref} {char_ref} talent to {talent_level}")
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1["TalentLV"] = talent_level[1:]
        case 1:
            tabset.teamsource[team_ref-1].character2["TalentLV"] = talent_level[1:]
        case 2:
            tabset.teamsource[team_ref-1].character3["TalentLV"] = talent_level[1:]
        case 3:
            tabset.teamsource[team_ref-1].character4["TalentLV"] = talent_level[1:]
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_set_ascension(team_ref, char_ref, asc_trace, status):
    print(f"setting {team_ref} {char_ref} {asc_trace} to {status[-1]}")
    if status[-1] == "Y":
        on = 1
    else: 
        on = 0
    match char_ref:
        case 0:
            tabset.teamsource[team_ref-1].character1[f"{asc_trace}Trace"] = on
        case 1:
            tabset.teamsource[team_ref-1].character2[f"{asc_trace}Trace"] = on
        case 2:
            tabset.teamsource[team_ref-1].character3[f"{asc_trace}Trace"] = on
        case 3:
            tabset.teamsource[team_ref-1].character4[f"{asc_trace}Trace"] = on
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_add_task(team_ref, char_name, task_type):
    print(f"Adding new {task_type} task to {team_ref} {char_name}")
    if char_name == tabset.frames_teams[team_ref-1].char1.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char1tasks
    elif char_name == tabset.frames_teams[team_ref-1].char2.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char2tasks
    elif char_name == tabset.frames_teams[team_ref-1].char3.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char3tasks
    elif char_name == tabset.frames_teams[team_ref-1].char4.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char4tasks

    
    if len(tasklist) > 0:
        pos = tasklist[len(tasklist)-1].pos + 1
    else:
        pos = 1
    match task_type:
        case "Char Level":
            tabset.teamsource[team_ref-1].tasks.append(team.TeamTaskLevel(char_name, f"team{data.next_uuid()}", pos, 80))
        case "Weapon Level":
            tabset.teamsource[team_ref-1].tasks.append(team.TeamTaskWeaponLevel(char_name, f"team{data.next_uuid()}", pos, 80))
        case "Trace":
            tabset.teamsource[team_ref-1].tasks.append(team.TeamTaskLevelledTrace(char_name, f"team{data.next_uuid()}", pos, "Basic", 6))
        case "Ascension":
            tabset.teamsource[team_ref-1].tasks.append(team.TeamTaskAscensionTrace(char_name, f"team{data.next_uuid()}", pos, "A2"))
        case "Relic":
            tabset.teamsource[team_ref-1].tasks.append(team.TeamTaskRelic(char_name, f"team{data.next_uuid()}", pos, "Wild Wheat", "Head", "HP"))
    
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_clear_column(team_ref, char_name):
    print(f"Deleting all items for {team_ref} {char_name}")
    tasks_to_pop = []
    for i in range(len(tabset.teamsource[team_ref-1].tasks)):
        if tabset.teamsource[team_ref-1].tasks[i].character == char_name:
            tasks_to_pop.append(i)
    tasks_to_pop = tasks_to_pop[::-1]
    for i in tasks_to_pop:
        tabset.teamsource[team_ref-1].tasks.pop(i)
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_swap_character(team_ref, char_ref, direction):
    print(f"In {team_ref}, swapping {char_ref} {direction}")
    match char_ref:
        case 0:
            temp = tabset.teamsource[team_ref-1].character1
            if direction == "Right":
                tabset.teamsource[team_ref-1].character1 = tabset.teamsource[team_ref-1].character2
                tabset.teamsource[team_ref-1].character2 = temp
        case 1:
            temp = tabset.teamsource[team_ref-1].character2
            if direction == "Right":
                tabset.teamsource[team_ref-1].character2 = tabset.teamsource[team_ref-1].character3
                tabset.teamsource[team_ref-1].character3 = temp
            elif direction == "Left":
                tabset.teamsource[team_ref-1].character2 = tabset.teamsource[team_ref-1].character1
                tabset.teamsource[team_ref-1].character1 = temp
        case 2:
            temp = tabset.teamsource[team_ref-1].character3
            if direction == "Right":
                tabset.teamsource[team_ref-1].character3 = tabset.teamsource[team_ref-1].character4
                tabset.teamsource[team_ref-1].character4 = temp
            elif direction == "Left":
                tabset.teamsource[team_ref-1].character3 = tabset.teamsource[team_ref-1].character2
                tabset.teamsource[team_ref-1].character2 = temp
        case 3:
            temp = tabset.teamsource[team_ref-1].character4
            if direction == "Left":
                tabset.teamsource[team_ref-1].character4 = tabset.teamsource[team_ref-1].character3
                tabset.teamsource[team_ref-1].character3 = temp
    data.set_teams(tabset.teamsource)
    tabset.reload()
    
    
def team_level_setlevel(team_ref, uuid, level):
    print(f"Setting {team_ref} {uuid} level to {level}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.level = level
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_weapon_setlevel(team_ref, uuid, level):
    print(f"Setting {team_ref} {uuid} weapon level to {level}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.level = level
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_ascension_set(team_ref, uuid, trace):
    print(f"Setting {team_ref} {uuid} ascension to {trace}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.trace = trace
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_trace_settrace(team_ref, uuid, trace):
    print(f"Setting {team_ref} {uuid} trace to {trace}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.trace = trace
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()
    

def team_trace_settarget(team_ref, uuid, target):
    print(f"Setting {team_ref} {uuid} target to {target}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.target = target
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()
    

def team_relic_setset(team_ref, uuid, set):
    print(f"Setting {team_ref} {uuid} set to {set}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.set = set
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()
    
    
def team_relic_setslot(team_ref, uuid, slot):
    print(f"Setting {team_ref} {uuid} slot to {slot}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.slot = slot
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_relic_setstat(team_ref, uuid, stat):
    print(f"Setting {team_ref} {uuid} stat to {stat}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.mainstat = stat
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()
    

def team_relic_setsubstat(team_ref, uuid, index, substat):
    print(f"Setting {team_ref} {uuid} substat {index} to {substat}")
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.substats[index] = substat
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_move_up(team_ref, uuid, char_name):
    if char_name == tabset.frames_teams[team_ref-1].char1.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char1tasks
    elif char_name == tabset.frames_teams[team_ref-1].char2.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char2tasks
    elif char_name == tabset.frames_teams[team_ref-1].char3.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char3tasks
    elif char_name == tabset.frames_teams[team_ref-1].char4.characterdict["Name"]:
        tasklist = tabset.frames_teams[team_ref-1].char4tasks
            
    for i in range(len(tasklist)):
        if tasklist[i].uuid == uuid:
            if i == 0:
                print("Can't move top item up")
                return
            else:
                pos1 = tasklist[i].pos
                uuid2 = tasklist[i-1].uuid
                pos2 = tasklist[i-1].pos
                break
    posswapped1 = False
    posswapped2 = False
    for teamtask in tabset.teamsource[team_ref-1].tasks:
        if teamtask.uuid == uuid:
            teamtask.pos = pos2
            posswapped1 = True
        elif teamtask.uuid == uuid2:
            teamtask.pos = pos1
            posswapped2 = True
        if posswapped1 and posswapped2:
            print(f"Moved {uuid} up")
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()


def team_delete_task(team_ref, uuid):
    print(f"Deleting task {uuid} in {team_ref}")
    for i in range(len(tabset.teamsource[team_ref-1].tasks)):
        if tabset.teamsource[team_ref-1].tasks[i].uuid == uuid:
            tabset.teamsource[team_ref-1].tasks.pop(i)
            break
    data.set_teams(tabset.teamsource)
    tabset.reload()


# ------------- Runtime -------------


tabset.reload()
# tabset.reload()
# tabset.reload()
root.mainloop()

#--------------------- Testing --------------------------
