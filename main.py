'''
Creates a tk window and handles presenting information to user and executing button commands.
'''

import tkinter as tk
from tkinter import ttk

import summary
import team
import gacha
import data_access as data
import imagemapping

from functools import partial

# Create the window
root = tk.Tk()
root.title("Honkai Star Tracks")
root.geometry('1200x800+100+100')
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
        self.frame.rowconfigure(0, minsize=100)
        self.frame.rowconfigure(1, minsize=100)
        self.frame.rowconfigure(2, minsize=100)
        self.frame.rowconfigure(3, minsize=100)
        self.frame.rowconfigure(4, minsize=100)
        self.frame.rowconfigure(5, minsize=100)
        self.frame.rowconfigure(6, minsize=100)
        self.frame.rowconfigure(7, minsize=100)

    
    def make_summary_tab(self):
        pass
    
    def make_gacha_tab(self, tasks:list):
        # Make the header frame for containing cost summary
        self.frame_header = ttk.Frame(self.frame, width=1192, height=100, borderwidth=2, relief="solid")
        self.frame_header.grid(column=0, row=0, columnspan=12, rowspan=1, sticky="w")
        
        # High priority list
        self.frame_highpri = ttk.Frame(self.frame, width=400, height=700, borderwidth=2, relief="solid")
        self.frame_highpri.grid(column=0, row=1, columnspan=4, rowspan=7)
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
        self.frame_medpri = ttk.Frame(self.frame, width=400, height=700, borderwidth=2, relief="solid")
        self.frame_medpri.grid(column=4, row=1, columnspan=4, rowspan=7)
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
        self.frame_lowpri = ttk.Frame(self.frame, width=400, height=700, borderwidth=2, relief="solid")
        self.frame_lowpri.grid(column=8, row=1 , columnspan=4, rowspan=7)
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
                case "high":
                    new_widget = GachaTaskWidget(task["uuid"], len(self.highpri), self.frame_highprilist, task["pos"], task["object"], task["target"])
                    self.highpri.append(new_widget)
                case "med":
                    new_widget = GachaTaskWidget(task["uuid"], len(self.medpri), self.frame_medprilist, task["pos"], task["object"], task["target"])
                    self.medpri.append(new_widget)
                case "low":
                    new_widget = GachaTaskWidget(task["uuid"], len(self.lowpri), self.frame_lowprilist, task["pos"], task["object"], task["target"])
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
            
                    
               
class GachaTaskWidget():
    def __init__(self, uuid, index, master, pos, object, target) -> None:
        self.uuid = uuid
        self.pos = pos
        self.index_in_column = index
        self.taskframe = ttk.Frame(master, width=374, height=96, borderwidth=0, relief="solid")
        
        # Task frame image
        self.bgimage = tk.PhotoImage(file="./images/gachatask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)
        
        # Task name
        self.text = f"{object} {target}"
        self.taskname = tk.Canvas(self.taskframe, width=250, height=31, bg="#2F6E6E", highlightthickness=0)
        self.taskname.create_text((4, 14), anchor="w", fill="#FFFFFF", font=("Calibri", 24), text=f"{object} {target}")
        self.taskname.place(x=91,y=10)
        
        # Task image
        self.image = tk.PhotoImage(file=f"./images/{imagemapping.gachamap[object]}")
        self.taskimage = tk.Canvas(self.taskframe, width=81, height=92, bg="#1C4343", highlightthickness=0)
        self.taskimage.create_image((40, 46), image=self.image)
        self.taskimage.place(x=2,y=2)
        
        # Task 'predicted cost'
        
        # Task button: move up
        
        # Task dropdown: priority
        
        # Task button: delete
        


class Tabset():
    def __init__(self) -> None:
        self.notebook = ttk.Notebook(root)
        self.frame_summary = Tab(self.notebook)
        self.gacha = []
        self.frame_gacha = Tab(self.notebook)
        self.frames_teams = []
        
        self.gachasource = data.get_gacha()
        self.teamsource = data.get_teams()

        
    def add_teamtab(self):
        teamtab = Tab(self.notebook)
        self.frames_teams.append(teamtab)


    def reload(self) -> None:
        self.gachasource = data.get_gacha()
        self.teamsource = data.get_teams()
        self.clear()
        self.prepare()
        self.show()
    
    
    def clear(self):
        self.notebook.destroy()
        self.notebook = ttk.Notebook(root)
        self.frame_summary = Tab(self.notebook)
        self.gacha = []
        self.frame_gacha = Tab(self.notebook)
        self.frames_teams = []
        
 
    def prepare(self):
        
        # Get presentable data from gacha tasks.
        for task in self.gachasource.tasks:
            newtask = {
                "uuid": task.uuid,
                "priority": task.priority,
                "pos": task.pos,
                "object": task.object,
                "target": task.target
            }
            self.gacha.append(newtask)
        

    
    def show(self):
        self.notebook.pack()
        self.frame_summary.frame.place(x=0,y=0)
        self.notebook.add(self.frame_summary.frame, text="Summary")
        
        for i in range(len(self.frames_teams)):
            self.frames_teams[i].frame.place(x=0,y=0)
            self.notebook.add(self.frames_teams[i].frame, text=f"Team {i+1}")
        
        self.frame_gacha.frame.place(x=0,y=0)
        self.notebook.add(self.frame_gacha.frame, text="Gacha")
        
        self.frame_gacha.make_gacha_tab(self.gacha)
        
        
tabset = Tabset()


# ------------ Button Functions ----------------

def gacha_add_blank_task(priority:str) -> None:
    match priority:
        case "high":
            tasklist = tabset.frame_gacha.highpri
        case "med":
            tasklist = tabset.frame_gacha.highpri
        case "low":
            tasklist = tabset.frame_gacha.highpri
            
    if len(tasklist) > 0:
        pos = tasklist[len(tasklist)-1].pos + 1
    else:
        pos = 1
                
    tabset.gachasource.tasks.append(gacha.GachaTask(f"gacha{data.next_uuid()}", priority, pos, "--", "--"))
    data.set_gacha(tabset.gachasource)
    
    tabset.reload()

def gacha_move_up(uuid):
    pass

def gacha_change_priority(uuid, priority):
    pass

def gacha_delete_task(uuid):
    pass

def gacha_set_object(uuid, object):
    pass

def gacha_set_target(uuid, target):
    pass

# ------------- Runtime -------------


tabset.reload()
# tabset.reload()
# tabset.reload()
root.mainloop()

#--------------------- Testing --------------------------
# if __name__ == '__main__':
    
#     tabset.gacha = [
#         {"uuid": "gacha00000006", "priority": "high", "pos": 5, "object": "Clara", "target": "E6"},
#         {"uuid": "gacha00000004", "priority": "high", "pos": 4, "object": "Clara", "target": "E4"},
#         {"uuid": "gacha00000001", "priority": "high", "pos": 1, "object": "Clara", "target": "E1"},
#         {"uuid": "gacha00000002", "priority": "high", "pos": 2, "object": "Clara", "target": "E2"},
#         {"uuid": "gacha00000003", "priority": "high", "pos": 3, "object": "Clara", "target": "E3"},
#         {"uuid": "gacha00000005", "priority": "high", "pos": 4, "object": "Clara", "target": "E5"},
#         {"uuid": "gacha00000007", "priority": "high", "pos": 6, "object": "Clara", "target": "E7"},
#         {"uuid": "gacha00000008", "priority": "high", "pos": 7, "object": "Clara", "target": "E8"},
#         {"uuid": "gacha00000009", "priority": "high", "pos": 8, "object": "Clara", "target": "E9"},
#         {"uuid": "gacha00000010", "priority": "med", "pos": 9, "object": "Clara", "target": "E10"},
#         {"uuid": "gacha00000011", "priority": "med", "pos": 10, "object": "Clara", "target": "E11"},
#         {"uuid": "gacha00000012", "priority": "med", "pos": 11, "object": "Clara", "target": "E12"},
#         {"uuid": "gacha00000013", "priority": "med", "pos": 12, "object": "Clara", "target": "E13"},
#         {"uuid": "gacha00000014", "priority": "med", "pos": 13, "object": "Clara", "target": "E14"},
#         {"uuid": "gacha00000015", "priority": "low", "pos": 14, "object": "Clara", "target": "E15"},
#         {"uuid": "gacha00000016", "priority": "low", "pos": 15, "object": "Clara", "target": "E16"},
#         {"uuid": "gacha00000017", "priority": "low", "pos": 16, "object": "Clara", "target": "E17"},
#         {"uuid": "gacha00000018", "priority": "low", "pos": 17, "object": "Clara", "target": "E18"},
#         {"uuid": "gacha00000020", "priority": "low", "pos": 18, "object": "Clara", "target": "E19"},
#         {"uuid": "gacha00000021", "priority": "low", "pos": 19, "object": "Clara", "target": "E20"}
#         ]
#     tabset.show()
    
    
    