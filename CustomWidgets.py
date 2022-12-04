from tkinter import *
from datetime import date
from tkcalendar import *

## Class Custom Widget
class CustomButton():
	def __init__(self, master, default_image, hover_image, press_image, df_color, hv_color, press_color, x, y, border, func):
		self.default_image = default_image
		self.hover_image = hover_image
		self.press_image = press_image
		self.df_color = df_color
		self.hv_color = hv_color
		self.defaultBackground = self.df_color
		self.press_color = press_color
		self.border = border

		self.x = x
		self.y = y

		self.MyButton = Button(master, image = self.default_image, bg = self.df_color, bd = border, command = func)
		self.MyButton.place(x = x, y = y)
		self.MyButton.bind("<Enter>", self.on_enter)
		self.MyButton.bind("<Leave>", self.on_leave)
		self.MyButton.bind("<Button-1>", self.on_press)

	def on_enter(self, event):
		self.MyButton.config(image = self.hover_image, bg = self.hv_color)

	def on_leave(self, event):
		self.MyButton.config(image = self.default_image, bg = self.df_color)

	def on_press(self, event):
		self.MyButton.config(image = self.press_image, bg = self.press_color)

class CustomFrame():
	def __init__(self, master, name, number_button, df_color, hv_color, press_color, normal_3, hover_3, press_3, func_3, 
				normal_2, hover_2, press_2, func_2,
				normal_1 = None, hover_1 = None, press_1 = None, func_1 = None):
		## Frame name
		self.name = name

		## For custom button
		self.number_button = number_button
		self.df_color = df_color
		self.hv_color = hv_color
		self.press_color = press_color

		## Add button for To Do Lit/ Edit button for Doing and Complete List
		self.normal_3 = normal_3
		self.hover_3 = hover_3
		self.press_3 = press_3
		self.func_3 = func_3

		## Filter button
		self.normal_2 = normal_2
		self.hover_2 = hover_2
		self.press_2 = press_2
		self.func_2 = func_2

		## Edit Button - Only appear in To Do List
		self.normal_1 = normal_1
		self.hover_1 = hover_1
		self.press_1 = press_1
		self.func_1 = func_1

		self.myFrame = Frame(master, bg = "#7687a2", width = 300, height = 50).pack()
		self.myLabel = Label(master, text = self.name, font = ("Tahoma", 15), fg = "#000000", bg = "#7687a2")
		self.myLabel.place(x = 10, y = 2)

		if number_button == 3:
			# Edit Button
			self.Edit = CustomButton(master,
								self.normal_1,
								self.hover_1,
								self.press_1,
								self.df_color, self.hv_color, self.press_color,
								130, 1, 0, self.func_1)

		# Ascending Button
		self.Filter_bttn = CustomButton(master,
									self.normal_2,
									self.hover_2,
									self.press_2,
									self.df_color, self.hv_color, self.press_color,
									180, 1, 0, self.func_2)

		# Add Button
		self.Add = CustomButton(master,
							self.normal_3,
							self.hover_3,
							self.press_3,
							self.df_color, self.hv_color, self.press_color,
							230, 1, 0, self.func_3)

### Title of the post "Python Tkinter ttk calendar" ###
#### Shout out to the guys (j_4321) who fix the drop down calendar issue (user9093127 who created the post) #####
class CustomDateEntry(DateEntry):
	def __init__(self, master, **kw):
		DateEntry.__init__(self, master, **kw)
		# Add black border around drop down calendar
		self._top_cal.config(bg = "black", bd = 1)
		# Display current date below
		Label(self._top_cal, bg = "gray90", anchor = "e", text = "Today %s" %date.today().strftime("%d/%m/%Y")).pack(fill = "x")

#### Shout out to the guy with 38 upvote in stackoverflow (squareRoo17) and the guy who comment in that 38 upvote post (Aprillomat) ####
## Title of the post "Display message when hovering over something with mouse cursor in Python" ##
class ToolTip(object):

    def __init__(self, widget, x_offset, y_offset):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

        self.x_offset = x_offset
        self.y_offset = y_offset

    def showtip(self, text):
        # "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + self.x_offset
        y = y + cy + self.widget.winfo_rooty() + self.y_offset
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("Tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

## Class Function
class Job_Info():
	def __init__(self, title, description, DueBool, DueDay, DueHour, DueMinute, Limit_Time = 0, importance = 0):
		self.title = title
		self.description = description
		self.DueBool = DueBool
		self.DueDay = DueDay
		self.DueHour = DueHour
		self.DueMinute = DueMinute
		self.Limit_Time = Limit_Time
		self.importance = importance

class Account_Info():
	def __init__(self, username, password, display_name, email, tag_number):
		self.username = username
		self.password = password
		self.display_name = display_name
		self.email = email
		self.tag_number = tag_number

class Project_info():
	def __init__(self, Project_name, complete_state):
		self.Project_name = Project_name
		self.complete_state = complete_state

class Project_open_info():
	def __init__(self, name_project, state, progress_state, total_job):
		self.name_project = name_project
		self.state = state
		self.progress_state = progress_state
		self.total_job = total_job

class note_info():
	def __init__(self, title, descript):
		self.title = title
		self.descript = descript