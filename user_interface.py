'''
Creates a tkinter window as root when imported.
Is sent data by main to turn into frames and such, and displays
those frames appropriately.
'''
import tkinter as tk
from tkinter import ttk
import summary
import team
import gacha
from imagemapping import imagemap
from functools import partial

# Create the window
root = tk.Tk()
root.title("Honkai Star Tracks")
root.geometry('1200x800+100+100')
root.resizable(False, False)

# # Create the notebook
# tabset = ttk.Notebook(root)
# tabset.pack()


#---------- Stuff for rendering tabs -----------------


class Tab():
    def __init__(self, master) -> None:
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
        self.frame_header = ttk.Frame(self.frame, width=1192, height=100, borderwidth=2, relief="solid")
        self.frame_header.grid(column=0, row=0, columnspan=12, rowspan=1, sticky="w")
        
        #High priority list
        self.frame_highpri = ttk.Frame(self.frame, width=400, height=700, borderwidth=2, relief="solid")
        self.frame_highpri.grid(column=0, row=1, columnspan=4, rowspan=7)
        self.highpri_image = tk.PhotoImage(file="./images/gachahighpri.png")
        self.highpri_bg = ttk.Label(self.frame_highpri, image=self.highpri_image)
        self.highpri_bg.place(x=-4, y=-2)
        
        self.highpri_listcanvas = tk.Canvas(self.frame_highpri, width=398, height=1500, bg="#2F6E6E", highlightthickness=0)
        self.highpri_listcanvas.place(x=-2,y=54)
        self.frame_highprilist = ttk.Frame(self.highpri_listcanvas, width=398, height=1500, borderwidth=2, relief="solid")
        self.frame_highprilist.place(x=-2,y=-2)
        
        self.highpri_listimage = tk.PhotoImage(file="./images/gachahighprilist.png")
        self.highpri_listbg = ttk.Label(self.frame_highprilist, image=self.highpri_listimage)
        self.highpri_listbg.place(x=-2,y=-2)
        
        self.highpri_scrollbar = ttk.Scrollbar(self.highpri_listcanvas, orient="vertical", command=self.highpri_listcanvas.yview)
        self.highpri_listcanvas['yscrollcommand'] = self.highpri_scrollbar.set
        self.highpri_scrollbar.place(x=0,y=0,anchor="e")
        
        
        #Med priority list
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
        
        
        #Low priority list
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
        
        
        self.highpri = []
        self.medpri = []
        self.lowpri = []
        
        for task in tasks:
            match task["priority"]:
                case "high":
                    new_widget = GachaTaskWidget(len(self.highpri), self.frame_highprilist, task["object"], task["target"])
                    self.highpri.append(new_widget)
                case "med":
                    new_widget = GachaTaskWidget(len(self.medpri), self.frame_medprilist, task["object"], task["target"])
                    self.medpri.append(new_widget)
                case "low":
                    new_widget = GachaTaskWidget(len(self.lowpri), self.frame_lowprilist, task["object"], task["target"])
                    self.lowpri.append(new_widget)
        
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
            
                    
               
class GachaTaskWidget():
    def __init__(self, index, master, object, target) -> None:
        self.index_in_column = index
        self.taskframe = ttk.Frame(master, width=374, height=96, borderwidth=0, relief="solid")
        
        self.bgimage = tk.PhotoImage(file="./images/gachatask.png")
        self.bg = ttk.Label(self.taskframe, image=self.bgimage)
        self.bg.place(x=-2 ,y=-2)
        
        self.text = f"{object} {target}"
        self.taskname = tk.Canvas(self.taskframe, width=250, height=31, bg="#2F6E6E", highlightthickness=0)
        self.taskname.create_text((4, 14), anchor="w", fill="#FFFFFF", font=("Calibri", 24), text=f"{object} {target}")
        self.taskname.place(x=91,y=10)
        
        self.image = tk.PhotoImage(file=f"./images/{imagemap[object]}")
        self.taskimage = tk.Canvas(self.taskframe, width=81, height=92, bg="#1C4343", highlightthickness=0)
        self.taskimage.create_image((40, 46), image=self.image)
        self.taskimage.place(x=2,y=2)
        
        





class Tabset():
    def __init__(self) -> None:
        self.notebook = ttk.Notebook(root)
        self.frame_summary = Tab(self.notebook)
        self.gacha = []
        self.frame_gacha = Tab(self.notebook)
        self.frames_teams = []

        
    def add_teamtab(self):
        teamtab = Tab(self.notebook)
        self.frames_teams.append(teamtab)

    
    def clear(self):
        self.notebook = ttk.Notebook(root)
        self.frame_summary = Tab(self.notebook)
        self.gacha = []
        self.frame_gacha = Tab(self.notebook)
        self.frames_teams = []
        

    
    def prepare(self, summary:summary.Summary, gacha:gacha.Gacha, teams:list=[]):
        
        # Get presentable data from gacha tasks.
        for task in gacha.tasks:
            newtask = {
                "priority": task.priority,
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



# # Don't update tabs directly, run this after making changes to the data
# def render_tabs(summary:summary.Summary, gacha:gacha.Gacha, teams:list=[]):
#     # Clear the tabs
#     forget_all_tabs()
    
#     # Add the Summary tab
#     make_summary_frame(summary)
    
#     # Add the Teams in team_frames
#     for i in range(len(teams)):
#         make_teamtab_frame(teams[i])
#     for i in range(len(teamtab_frames)):
#         teamtab_frames[i].pack(fill='both', expand=True)
#         tabset.add(teamtab_frames[i], text=f"Team {i+1}")
    
#     # Add the Gacha tab
#     make_gacha_frame(gacha)
    

# def forget_all_tabs():
#     teamtab_frames.clear() 
#     for i in range(len(tabset.tabs())):
#         tabset.forget(0)
     

# def make_summary_frame(summary:summary.Summary):
#     frame_summary = ttk.Frame(tabset, width=400, height=280)
#     frame_summary.pack(fill='both', expand=True)
#     tabset.add(frame_summary, text='Summary')

        
# def make_teamtab_frame(team:team.Team):
#     frame_teamtab = ttk.Frame(tabset, width=400, height=280)
#     teamtab_frames.append(frame_teamtab)
 
   
# def make_gacha_frame(gacha:gacha.Gacha):
#     print("making gacha frame")
#     frame_gacha = ttk.Frame(tabset, width=400, height=280)
#     # frame_gacha.columnconfigure(0)
#     # frame_gacha.columnconfigure(1)
#     # frame_gacha.columnconfigure(2)
#     # frame_gacha.rowconfigure(0)
#     # frame_gacha.rowconfigure(1)
#     frame_gacha.pack(fill='both', expand=True)
    
#     photo = tk.PhotoImage(file="./profile.png")
#     profileImg = ttk.Label(frame_gacha, image=photo, padding=-4)
#     profileImg.place(x=0, y=0)
    
    

    
    
#     tabset.add(frame_gacha, text='Gacha')
    

# ------------- Make the rest of the window -------------
        
        
        
#--------------------- Testing --------------------------
if __name__ == '__main__':
    
    # rendertabstestfunc = partial(render_tabs, summary.Summary(), gacha.Gacha())
    # button_clear = ttk.Button(root, text="Clear", command=forget_all_tabs, 
    #                     width=80)
    # button_clear.place(width=80, height=40, x=0, y=0)
    
    # button_show = ttk.Button(root, text="Render", command=rendertabstestfunc, 
    #                     width=80)
    # button_show.place(width=80, height=40, x=0, y=41)
    
    # noteamsfunc = partial(render_tabs, summary.Summary(), gacha.Gacha(), [])
    # button_teams_none = ttk.Button(root, text="noteams", command=noteamsfunc, 
    #                     width=80)
    # button_teams_none.place(width=80, height=40, x=0, y=82)
    
    # sampleteamsfunc = partial(render_tabs, summary.Summary(), gacha.Gacha(), [team.Team(), team.Team()])
    # button_teams_sample = ttk.Button(root, text="sampleteam", command=sampleteamsfunc, 
    #                     width=80)
    # button_teams_sample.place(width=80, height=40, x=0, y=123)
    
    # render_tabs(summary.Summary(), gacha.Gacha(), [])
    
    tabset.gacha = [
        {"priority": "high", "object": "Clara", "target": "E1"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "high", "object": "Clara", "target": "E2"},
        {"priority": "med", "object": "Clara", "target": "E2"},
        {"priority": "med", "object": "Clara", "target": "E2"},
        {"priority": "med", "object": "Clara", "target": "E2"},
        {"priority": "med", "object": "Clara", "target": "E2"},
        {"priority": "med", "object": "Clara", "target": "E2"},
        {"priority": "low", "object": "Clara", "target": "E2"},
        {"priority": "low", "object": "Clara", "target": "E2"},
        {"priority": "low", "object": "Clara", "target": "E2"},
        {"priority": "low", "object": "Clara", "target": "E2"},
        {"priority": "low", "object": "Clara", "target": "E2"},
        {"priority": "low", "object": "Clara", "target": "E2"}
        ]
    tabset.show()
    
    root.mainloop()
    