from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import *
from datetime import date
from tkinter import ttk

from CustomWidgets import *
from Algorithm import *


import csv
import os
import datetime
import time
import operator
import shutil
import re
import random

#-----------------------------------------------------------------#
def check_file():
	global List_account, Login_account
	Login_account.clear()
	List_account.clear()

	if os.path.isfile("user"):
		with open("user", "r") as user:
			reader = csv.reader(user, delimiter = "|")
			for row in reader:
				List_account.append(Account_Info(row[0], row[1], row[2], row[3], row[4]))
		user.close()
	else:
		f_2 = open("user", "w+")
		f_2.close()

	if os.path.isfile("keep_login"):
		with open("keep_login", "r") as login:
			reader = csv.reader(login, delimiter = "|")
			for row in reader:
				Login_account.append(row[0])
		login.close()
	else:
		f_3 = open("keep_login", "w+")
		f_3.close()

# Check Keep login state -True/False
def login_state_check():
	global List_account, Login_account, username_saved, tag_number_int, display_name_onScreen, full_displayname

	List_account.clear()
	Login_account.clear()
	check_file()

	if not Login_account:
		login_window()
	else:
		# Check login state
		user_id_get = 0

		for i in range(0, len(List_account), 1):
			if List_account[i].username == Login_account[0]:
				user_id_get = i

		tag_number_int = List_account[user_id_get].tag_number

		display_name_onScreen = List_account[user_id_get].display_name

		full_displayname = List_account[user_id_get].display_name

		if len(List_account[user_id_get].display_name) > 12:
			print(True)
			display_name_onScreen = display_name_onScreen[:12] + ".."

		username_saved = List_account[user_id_get].username
		mainwindow()


def mainwindow():
	def error_window(text, x, y, size):
		error_WD = Toplevel()
		error_WD.geometry("")

		error_WD.title("Oops! Somethings went wrong.")
		error_WD.resizable(0, 0)
		error_WD.wm_attributes("-topmost", 1)

		error_WD_w = 350
		error_WD_h = 110

		postiion_error_WD_x = (error_WD.winfo_screenwidth()//2) - (error_WD_w//2)
		position_error_WD_y = (error_WD.winfo_screenheight()//2) - (error_WD_h//2)

		error_WD.geometry(f"{error_WD_w}x{error_WD_h}+{postiion_error_WD_x}+{position_error_WD_y}")
		error_WD.config(bg = "#1e222a")

		alert_window = Label(error_WD, text = text, font = ("Consolas", size), bg = "#1e222a", fg = "#FFFFFF")
		alert_window.place(x = x, y = y)

		close_button = Button(error_WD, text = "   OK   ", font = ("Consolas", 12), bg = "#2a5bba", fg = "#FFFFFF", command = lambda: error_WD.destroy())
		close_button.place(x = 130, y = 68)

	root = Tk()

	root.title("Project Management")

	root.geometry(f"1440x880+{root.winfo_screenwidth()//2 - 1440//2}+{root.winfo_screenheight()//2 - 880//2}")
	# root.resizable(0, 0)

	root.minsize(1240, 680)

	## Monitor Height + Width
	monitor_height = root.winfo_screenheight()
	monitor_width = root.winfo_screenwidth()

	## Variables
	Job_name = StringVar()
	Date_Time = StringVar()
	DueTime_Bool = StringVar()


	#-----------------------------------------------------------------#
	### Button Image
	## Toggle Image
	pressPic_Toggle = PhotoImage(file = "images/Toggle_icon_press.png")
	hoverPic_Toggle = PhotoImage(file = "images/Toggle_icon_hover.png")
	Toggle_image = PhotoImage(file = "images/Toggle_icon.png")

	## Home Image
	Home_image = PhotoImage(file = "images/HomePage_icon.png")
	pressPic_Home = PhotoImage(file = "images/HomePage_press_icon.png")
	hoverPic_Home = PhotoImage(file = "images/HomePage_hover_icon.png")

	## Personal Image
	Personal_image = PhotoImage(file = "images/Project_page_icon.png")
	pressPic_Personal = PhotoImage(file = "images/Project_page_press_icon.png")
	hoverPic_Personal = PhotoImage(file = "images/Project_page_hover_icon.png")

	## Team Image
	Team_image = PhotoImage(file = "images/Profile_icon.png")
	pressPic_Team = PhotoImage(file = "images/Profile_press_icon.png")
	hoverPic_Team = PhotoImage(file = "images/Profile_hover_icon.png")

	#-----------------------------------------------------------------#
	# Create New Image Button
	Create_image = PhotoImage(file = "images/Personal Project Page/Create_New_icon.png")
	Create_Hover_Image = PhotoImage(file = "images/Personal Project Page/Create_New_Button_Hover_icon.png")
	Create_Press_Image = PhotoImage(file = "images/Personal Project Page/Create_New_Button_Press_icon.png")

	# Open Image Button
	Open_image = PhotoImage(file = "images/Personal Project Page/Open_icon.png")
	Open_Hover_Image = PhotoImage(file = "images/Personal Project Page/Open_Hover_icon.png")
	Open_Press_Image = PhotoImage(file = "images/Personal Project Page/Open_Press_icon.png")

	#-----------------------------------------------------------------#
	### Custom Widget - Using For Class
	## Item Components
	# Edit icon
	Edit_icon = PhotoImage(file = "images/CustomFrame/Edit_icon.png")
	Edit_hover_icon = PhotoImage(file = "images/CustomFrame/Edit_Hover_icon.png")
	Edit_press_icon = PhotoImage(file = "images/CustomFrame/Edit_Press_icon.png")

	# Add icon
	Add_icon = PhotoImage(file = "images/CustomFrame/Add_icon.png")
	Add_hover_icon = PhotoImage(file = "images/CustomFrame/Add_hover_icon.png")
	Add_press_icon = PhotoImage(file = "images/CustomFrame/Add_press_icon.png")

	# Ascending icon
	Filter_image = PhotoImage(file ="images/CustomFrame/Filter_icon.png")
	Filter_hover_image = PhotoImage(file ="images/CustomFrame/Filter_hover_icon.png")
	Filter_press_image = PhotoImage(file ="images/CustomFrame/Filter_press_icon.png")

	#-----------------------------------------------------------------#
	## Class Custom Frame
	#-----------------------------------------------------------------#
	### Personal Project Management Page
	## Personal Project Frame

	## Entry to add projet name
	## Function
	def check_dir():
		if not os.path.exists("Project/%s" %tag_number_int):
			os.makedirs("Project/%s" %tag_number_int)
		else:
			pass

		if os.path.isfile("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int)):
			with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), 'r') as file:
				reader = csv.reader(file, delimiter = '|')
				for row in reader:
					Temp_list.append(row[0])
				# for line in file:
				# 	Temp_list.append(line)
			file.close()
		else:
			f = open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "w+")
			f.close()

		if not os.path.isfile("Project/%s/Project_list_Diary_%s" %(tag_number_int, tag_number_int)):
			f = open("Project/%s/Project_list_Diary_%s" %(tag_number_int, tag_number_int), "w+")
			f.close()
		else:
			if not os.path.exists("Project/%s/%s" %(tag_number_int, empty_String)):
				os.makedirs("Project/%s/%s" %(tag_number_int, empty_String))
			else:
				pass

	def create_initial_file(complete_state, progress_state, job_total):
		with open("Project/%s/%s/%s.txt" %(tag_number_int, empty_String, empty_String), "w") as intial:
			intial.write("".join(str(empty_String)))
			intial.write("|")
			intial.write("".join(str(complete_state)))
			intial.write("|")
			intial.write("".join(str(progress_state)))
			intial.write("|")
			intial.write("".join(str(job_total)))
			intial.write("\n")
		intial.close()

	def save_project_list_diary(action, state):
		now = datetime.datetime.now()

		with open("Project/%s/Project_list_Diary_%s" %(tag_number_int, tag_number_int), "a") as diary:
			diary.write(''.join(str(now)))
			diary.write('|')
			diary.write(''.join(str(action)))
			diary.write('|')
			diary.write(''.join(str(empty_String)))
			diary.write('|')
			diary.write(''.join(str(state)))
			diary.write('\n')
		diary.close()

	def save_project_list(state):
		with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), 'a') as f:
			f.write(''.join(str(empty_String)))
			f.write('|')
			f.write(''.join(str(state)))
			f.write('\n')
		f.close()

	def remove_job_ToDo():
		### store temp value get from Complete listbox ###
		empty_temp_1 = ""

		global job_total, progress_value

		if len(submitted_late) == 0:
			pass
		else:
			for index_i in Comp_List.curselection():
				empty_temp_1 = Comp_List.get(index_i)

			if search(submitted_late, empty_temp_1.strip()) == True:
				submitted_late.remove(empty_temp_1.strip())

			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as rwrite_sub:
				for i in range(0, len(submitted_late), 1):
					rwrite_sub.write("".join(str(submitted_late[i])))
					rwrite_sub.write("\n")
			rwrite_sub.close()

		remove_job(Todo_List, Job_list, Title[0], Alert_label)

		## Total job
		job_total = job_total - 1

		## Double check progress value
		if job_total != 0:
			progress_value = int((len(Complete_List))/(int(job_total))*100)
		else:
			progress_value = 0

		if progress_value >= 100:
			create_initial_file("Finished", 100, job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("Completed", "Finished")
		else:
			create_initial_file("WIP", int(progress_value), job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("WIP", "Unfinished")

		Progress_display_value.config(text = "%s%s" %(progress_value, percent))

	def remove_job_doing():
		### store temp value get from Complete listbox ###
		empty_temp_2 = ""

		global job_total, progress_value

		if len(submitted_late) == 0:
			pass
		else:
			for index_i in Comp_List.curselection():
				empty_temp_2 = Comp_List.get(index_i)

			if search(submitted_late, empty_temp_2.strip()) == True:
				submitted_late.remove(empty_temp_2.strip())

			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as rwrite_sub:
				for i in range(0, len(submitted_late), 1):
					rwrite_sub.write("".join(str(submitted_late[i])))
					rwrite_sub.write("\n")
			rwrite_sub.close()
		
		remove_job(Doing_Listbox, Doing_list, Title[1], Alert_label_doing)

		## Total job
		job_total = job_total - 1

		## Double check progress value
		if job_total != 0:
			progress_value = int((len(Complete_List))/(int(job_total))*100)
		else:
			progress_value = 0

		if progress_value >= 100:
			create_initial_file("Finished", 100, job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("Completed", "Finished")
		else:
			create_initial_file("WIP", int(progress_value), job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("WIP", "Unfinished")

		Progress_display_value.config(text = "%s%s" %(progress_value, percent))

	def remove_job_complete():
		### store temp value get from Complete listbox ###
		empty_temp = ""

		global job_total, progress_value

		if len(submitted_late) == 0:
			pass
		else:
			for index_i in Comp_List.curselection():
				empty_temp = Comp_List.get(index_i)

			if search(submitted_late, empty_temp.strip()) == True:
				submitted_late.remove(empty_temp.strip())

			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as rwrite_sub:
				for i in range(0, len(submitted_late), 1):
					rwrite_sub.write("".join(str(submitted_late[i])))
					rwrite_sub.write("\n")
			rwrite_sub.close()

		remove_job(Comp_List, Complete_List, Title[2], Alert_label_complete)

		## Total job
		job_total = job_total - 1

		## Double check progress value
		if job_total != 0:
			progress_value = int((len(Complete_List))/(int(job_total))*100)
		else:
			progress_value = 0

		if progress_value >= 100:
			create_initial_file("Finished", 100, job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("Completed", "Finished")
		else:
			create_initial_file("WIP", int(progress_value), job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("WIP", "Unfinished")

		Progress_display_value.config(text = "%s%s" %(progress_value, percent))

	def remove_job(Todo_List, Job_list, Doing_stat, Alert_label):
		# Temp empty string
		temp_string = ""

		# Delete item from listbox
		for i in Todo_List.curselection():
			temp_string = Todo_List.get(i)
			Todo_List.delete(i)

		# Delete item from Job list
		for i in range(0, len(Job_list), 1):
			if Job_list[i].title == temp_string.strip():
				Job_list.remove(Job_list[i])
				break

		# Adjust height of listbox
		if len(Job_list) == 0:
			# Adjust display To Do List Value
			global TodoList_Bool
			TodoList_Bool = False

			# Hide To Do List
			Todo_List.config(height = len(Job_list))
			# ToDo_Frame_List.place_forget()
			Alert_label.place_forget()
		elif len(Job_list) > 14:
			# Adjust Height of To Do List
			Alert_label.place(x = 36, y = 510)
			Todo_List.config(height = 14)

		elif len(Job_list) == 14:
			Alert_label.place_forget()
			Todo_List.config(height = len(Job_list))

		else:
			Alert_label.place_forget()
			Todo_List.config(height = len(Job_list))

		# Rewrite (wipe) list back to file
		with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Doing_stat), "w") as new_file:
			for i in range(0, len(Job_list), 1):
				new_file.write(''.join(str(Job_list[i].title)))
				new_file.write('|')
				new_file.write(''.join(str(Job_list[i].description)))
				new_file.write('|')
				new_file.write(''.join(str(Job_list[i].DueBool)))
				new_file.write('|')
				new_file.write(''.join(str(Job_list[i].DueDay)))
				new_file.write('|')
				new_file.write(''.join(str(Job_list[i].DueHour)))
				new_file.write('|')
				new_file.write(''.join(str(Job_list[i].DueMinute)))
				new_file.write('|')
				new_file.write(''.join(str(Job_list[i].Limit_Time)))
				new_file.write('|')
				new_file.write(''.join(str(Job_list[i].importance)))
				new_file.write('\n')
		new_file.close()

	# Pop up menu in To Do List
	def popup_menu(event):
		if len(Job_list) == 0:
			pass
		else:
			Todo_List.selection_clear(0, END)
			Todo_List.selection_set(Todo_List.nearest(event.y))
			Todo_List.activate(Todo_List.nearest(event.y))
			widget = event.widget
			index = widget.nearest(event.y)
			_, y_offset, _, height = widget.bbox(index)
			if event.y > y_offset + height:
				# Outside of widget
				return
			menu_function.post(event.x_root, event.y_root)

	## Pop up menu in Doing List
	def popup_menu_doing(event):
		if len(Doing_list) == 0:
			pass
		else:
			Doing_Listbox.selection_clear(0, END)
			Doing_Listbox.selection_set(Doing_Listbox.nearest(event.y))
			Doing_Listbox.activate(Doing_Listbox.nearest(event.y))
			widget = event.widget
			index = widget.nearest(event.y)
			_, y_offset, _, height = widget.bbox(index)
			if event.y > y_offset + height:
				# Outside of widget
				return
			menu_function_doing.post(event.x_root, event.y_root)

	### Pop up menu in Complete List
	def popup_menu_Compelete(event):
		if len(Complete_List) == 0:
			pass
		else:
			Comp_List.selection_clear(0, END)
			Comp_List.selection_set(Comp_List.nearest(event.y))
			Comp_List.activate(Comp_List.nearest(event.y))
			widget = event.widget
			index = widget.nearest(event.y)
			_, y_offset, _, height = widget.bbox(index)
			if event.y > y_offset + height:
				# Outside of widget
				return
			menu_function_complete.post(event.x_root, event.y_root)

	### Pop up menu in Complete List
	def popup_menu_notelist(event):
		if len(note_list) == 0:
			pass
		else:
			note_listbox.selection_clear(0, END)
			note_listbox.selection_set(note_listbox.nearest(event.y))
			note_listbox.activate(note_listbox.nearest(event.y))
			widget = event.widget
			index = widget.nearest(event.y)
			_, y_offset, _, height = widget.bbox(index)
			if event.y > y_offset + height:
				# Outside of widget
				return
			menu_function_notelist.post(event.x_root, event.y_root)

	def edit_window_ToDo():
		edit_Window(Job_list, Todo_List, Title[0], Alert_label)

	def edit_window_Doing():
		edit_Window(Doing_list, Doing_Listbox, Title[1], Alert_label_doing)

	def edit_window_Complete():
		edit_Window(Complete_List, Comp_List, Title[2], Alert_label_complete)

	def edit_Window(Job_list, Todo_List, doing_stt_, Alert_label):
		# Temp list to store item selected in treeview
		Display_joblist = []
		for i in range(0, len(Job_list), 1):
			Display_joblist.append(Job_list[i])

		# Sort bool - check if list is sorted
		sort_bool = False

		## id value store - use for edit purpose
		selected_og = []

		edit_WD = Toplevel()
		edit_WD.wm_attributes("-topmost", 1)

		# Variable #
		display_timelimit = StringVar()
		display_importance = StringVar()
		display_date = StringVar()
		display_hour = StringVar()
		display_minute = StringVar()

		def confirm_save_changes():
			def confirm_change():
				if doing_stt_ == Title[2]:
					make_change_complete()
				else:
					make_change()
				confirm_window_2.destroy()

			confirm_window_2 = Toplevel()
			confirm_window_2.geometry(f"370x100+{(confirm_window_2.winfo_screenwidth()//2) - (370//2)}+{(confirm_window_2.winfo_screenheight()//2) - (100//2)}")
			confirm_window_2.resizable(0, 0)
			confirm_window_2.wm_attributes('-topmost', 1)

			confirm_window_2.title("Confirm save changes")
			confirm_window_2.config(bg = "#262a34")

			confirm_label = Label(confirm_window_2,
								text = "Do you want to save any changes?",
								font = ("Consolas", 13), bg = "#262a34", fg = "#FFFFFF")
			confirm_label.place(x = 10, y = 15)

			confirm_yes = Button(confirm_window_2, text = "  Yes  ", font = ("Consolas", 11), bg = "#1544a0", fg = "#FFFFFF",
								command = confirm_change)
			confirm_yes.place(x = 120, y = 55)

			confirm_no = Button(confirm_window_2, text = "  No  ", font = ("Consolas", 11), bg = "#1544a0", fg = "#FFFFFF",
								command = lambda: confirm_window_2.destroy())
			confirm_no.place(x = 200, y = 55)

			confirm_cancel = Button(confirm_window_2, text = "  Cancel  ", font = ("Consolas", 11), bg = "#ed2249", fg = "#FFFFFF",
									command = lambda: confirm_window_2.destroy())
			confirm_cancel.place(x = 270, y = 55)

		## Go to Search Frame
		def Search_tab():
			Search_button_active.place(x = 0, y = 0)
			Search_Frame.place(x = 143, y = 50)
			Edit_Button_Ex_Active.place_forget()
			Edit_Frame.place_forget()
			# Filter_Frame.place_forget()
			# Filter_Button_active.place_forget()

		# ## Check area mouse clicking - will delete soon
		# def on_click_tree(event):
		# 	region = Tree_result.identify("region", event.x, event.y)
		# 	print(region)

		def search_list(): ## Need to check again
			# If Filter Search = To Do
			# if Search_In.get() == "To Do":
			# Signal_Label.config(text = "Result:")
			Tree_result.delete(*Tree_result.get_children())

			if Search_Entry.get() == "":
				Display_joblist.clear()
				for i in range(0, len(Job_list), 1):
					Display_joblist.append(Job_list[i])

				for i in range(0, len(Display_joblist), 1):
					Tree_result.insert(parent = '',
										index = 'end',
										iid = i, text = "",
										values =(
											Display_joblist[i].title,
											Display_joblist[i].description,
											Display_joblist[i].DueBool,
											Display_joblist[i].DueDay,
											str(Display_joblist[i].DueHour)+":"+str(Display_joblist[i].DueMinute),
											Display_joblist[i].Limit_Time,
											Display_joblist[i].importance))
			else:
				Display_joblist.clear()
				# # Sort before insert back to list
				# MergeSort_title(Job_list)

				# Clear Treeview first
				# Insert any value that has search value in
				for i in range(0, len(Job_list), 1):
					if (Search_Entry.get()).lower() in (str(Job_list[i].title)).lower():
						Display_joblist.append(Job_list[i])

				for i in range(0, len(Display_joblist), 1):
					Tree_result.insert(parent = '',
									index = 'end',
									iid = i, text = "",
									values =(
										Display_joblist[i].title,
										Display_joblist[i].description,
										Display_joblist[i].DueBool,
										Display_joblist[i].DueDay,
										str(Display_joblist[i].DueHour)+":"+str(Display_joblist[i].DueMinute),
										Display_joblist[i].Limit_Time,
										Display_joblist[i].importance))


		def del_selected():
			global job_total, progress_value

			# Create two temp list for display
			selected_display_list = []
			selected_og_list = []
			selected_submitLate = []

			# Select entire treeview list
			id_selection = Tree_result.selection()
			for record in id_selection:
				selected_display_list.append(int(record))

			# Delete all records from treeview
			Tree_result.delete(*Tree_result.get_children())

			# Append to list any value in select to selected original list
			length_list = len(Job_list)
			for i in selected_display_list:
				for j in range(0, length_list, 1):
					if Display_joblist[i].title == Job_list[j].title:
						selected_og_list.append(j)

			# Reverse List
			selected_display_list = selected_display_list[::-1]
			selected_og_list = selected_og_list[::-1]

			for i in selected_og_list:
				for j in range(0, len(submitted_late), 1):
					if Job_list[i].title == submitted_late[j]:
						selected_submitLate.append(j)

			### Reverse selected submit late list
			MergeSort_desc(selected_submitLate)

			# print(selected_display_list)
			# print(selected_og_list)

			for i in selected_display_list:
				# Remove item on treeview
				Display_joblist.remove(Display_joblist[i])

			for i in selected_og_list:
				# Remove item from listbox
				Todo_List.delete(i)

				# Remove item from original list
				Job_list.remove(Job_list[i])

			for j in selected_submitLate:
				submitted_late.remove(submitted_late[j])

			# Rewrite back to file
			with open("Project/%s/%s/%s" %(tag_number_int, empty_String, doing_stt_), "w") as new_file:
				for i in range(0, len(Job_list), 1):
					new_file.write(''.join(str(Job_list[i].title)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].description)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueBool)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueDay)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueHour)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueMinute)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].Limit_Time)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].importance)))
					new_file.write('\n')
			new_file.close()

			## Rewrite submitted_late.txt file
			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as new_late:
				for i in range(0, len(submitted_late), 1):
					new_late.write("".join(str(submitted_late[i])))
					new_late.write("\n")
			new_late.close()


			# Append all value from display list to Treeview
			for i in range(0, len(Display_joblist), 1):
				Tree_result.insert(parent = '',
						index = 'end',
						iid = i, text = "",
						values =(
								Display_joblist[i].title,
								Display_joblist[i].description,
								Display_joblist[i].DueBool,
								Display_joblist[i].DueDay,
								str(Display_joblist[i].DueHour)+":"+str(Display_joblist[i].DueMinute),
								Display_joblist[i].Limit_Time,
								Display_joblist[i].importance))

			# Adjust height of listbox
			if len(Job_list) == 0:
				# Adjust display To Do List Value
				global TodoList_Bool
				TodoList_Bool = False

				# Hide To Do List
				Todo_List.config(height = len(Job_list))
				Todo_List.place_forget()
				Alert_label.place_forget()
			elif len(Job_list) > 14:
				# Adjust Height of To Do List
				Todo_List.config(height = 14)
				Alert_label.place(x = 36, y = 510)

			elif len(Job_list) == 14:
				Todo_List.config(height = len(Job_list))
				Alert_label.place_forget()

			else:
				Todo_List.config(height = len(Job_list))
				Alert_label.place_forget()


			job_total = job_total - len(selected_og_list)

			# Signal_Label.config(text = "Select a job to remove")
			selected_og_list.clear()
			selected_display_list.clear()

			## Double check progress value
			if job_total != 0:
				progress_value = int((len(Complete_List))/(int(job_total))*100)
			else:
				progress_value = 0

			if progress_value >= 100:
				create_initial_file("Finished", 100, job_total)
				rewrite_project_list(empty_String, progress_value)
				save_project_list_diary("Completed", "Finished")
			else:
				create_initial_file("WIP", int(progress_value), job_total)
				rewrite_project_list(empty_String, progress_value)
				save_project_list_diary("WIP", "Unfinished")

			Progress_display_value.config(text = "%s%s" %(progress_value, percent))
			Team_Project_name.config(text = "%s%s" %(progress_value, percent))

		def del_all():
			global job_total, progress_value

			if not Job_list:
				pass
			else:
				submitLate_exist_list = []

				for i in range(0, len(Job_list), 1):
					for j in range(0, len(submitted_late), 1):
						if Job_list[i].title == submitted_late[j]:
							submitLate_exist_list.append(j)

				## reverse list
				MergeSort_desc(submitLate_exist_list)

				# Clear To do listbox
				Todo_List.delete(0, END)

				# Resize To do listbox height back to 0
				Todo_List.config(height = 0)

				# Hide To do listbox
				# ToDo_Frame_List.place_forget()

				# Adjust To do List bool display value to False
				global TodoList_Bool
				TodoList_Bool = False

				# Reduce job total
				job_total = job_total - len(Job_list)

				# Clear Job list
				Job_list.clear()
				# Clear Display Job list
				Display_joblist.clear()

				# Clear treeview
				Tree_result.delete(*Tree_result.get_children())

				# Clear all values in file text
				open("Project/%s/%s/%s" %(tag_number_int, empty_String, doing_stt_), "w").close()

				# Clear any value in listbox has in submitted late job file
				if len(submitLate_exist_list) != 0:
					for i in submitLate_exist_list:
						submitted_late.remove(submitted_late[i])

					with open("Project/%s/%s/submitted_late" %(tag_number_int,empty_String), "w") as rewrite_late:
						for i in range(0, len(submitted_late), 1):
							rewrite_late.write("".join(str(submitted_late[i])))
							rewrite_late.write("\n")
					rewrite_late.close()

				submitLate_exist_list.clear()


				# Hide "scroll down to see more" label
				Alert_label.place_forget()

				## Double check progress value
				if job_total != 0:
					progress_value = int((len(Complete_List))/(int(job_total))*100)
				else:
					progress_value = 0

				if progress_value >= 100:
					create_initial_file("Finished", 100, job_total)
					rewrite_project_list(empty_String, progress_value)
					save_project_list_diary("Completed", "Finished")

				else:
					create_initial_file("WIP", int(progress_value), job_total)
					rewrite_project_list(empty_String, progress_value)
					save_project_list_diary("WIP", "Unfinished")

				Progress_display_value.config(text = "%s%s" %(progress_value, percent))
				Team_Project_name.config(text = "%s%s" %(progress_value, percent))

		def make_change_complete():
			### Check quit confirm ###
			Quit_Confirm_2 = False

			temp_id_2 = selected_og[0]

			new_descript_get_2 = (Description_entry.get('1.0', 'end-1c')).strip()
			new_title_get_2 = (Entry_title.get()).strip()

			# Check due time set "On" or "Off":
			if Due_time_Entry.get() == "On":
				if new_title_get_2 != "":
					if new_descript_get_2 != "":

						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						Force_ToNextStep = False

						if Job_list[int(temp_id_2)].title == new_title_get_2:
							Force_ToNextStep = True

						for i in range(0, len(Job_list), 1):
							if new_title_get_2 == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if new_title_get_2 == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if new_title_get_2 == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and Force_ToNextStep == False:
							Status_change.config(text = "Job already been created.")
						else:						
							## Adjust quit confirm value ##
							Quit_Confirm_2 = True

							for index in range(0, len(submitted_late), 1):
								if submitted_late[index] == Job_list[int(temp_id_2)].title:
									submitted_late[index] = new_title_get_2

							Job_list[int(temp_id_2)].title = new_title_get_2
							Job_list[int(temp_id_2)].description = new_descript_get_2
					else:
						status_due.config(text = "Please add job description")
				else:
					status_due.config(text = "Please add job title")
			else:
				if new_title_get_2 != "":
					if new_descript_get_2 != "":

						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						Force_ToNextStep = False

						if Job_list[int(temp_id_2)].title == new_title_get_2:
							Force_ToNextStep = True

						for i in range(0, len(Job_list), 1):
							if new_title_get_2 == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if new_title_get_2 == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if new_title_get_2 == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and Force_ToNextStep == False:
							Status_change.config(text = "Job already been created.")
						else:						
							## Adjust quit confirm value ##
							Quit_Confirm_2 = True

							for index in range(0, len(submitted_late), 1):
								if submitted_late[index] == Job_list[int(temp_id_2)].title:
									submitted_late[index] = new_title_get_2

							Job_list[int(temp_id_2)].title = new_title_get_2
							Job_list[int(temp_id_2)].description = new_descript_get_2
					else:
						status_nodue.config(text = "Please add job description")
				else:
					status_nodue.config(text = "Please add job title")

			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as rwite_2:
				for i in range(0, len(submitted_late), 1):
					rwite_2.write("".join(str(submitted_late[i])))
					rwite_2.write("\n")
			rwite_2.close()

			if not Quit_Confirm_2:
				pass
			else:
				# Delete value and add back to the top listbox
				Todo_List.delete(temp_id_2)
				Todo_List.insert(0, "  %s" %Job_list[temp_id_2].title)

				# Store temporarily new value in temp list and delete new value from the OG list
				store_list_3 = []
				store_list_3.append(Job_list[temp_id_2])

				Job_list.remove(Job_list[temp_id_2])

				# Add back to the top of To do List - Job list
				Job_list.insert(0, store_list_3[0])

				with open("Project/%s/%s/%s" %(tag_number_int, empty_String, doing_stt_), "w") as new_rewrite_1:
					for i in range(0, len(Job_list), 1):
						new_rewrite_1.write(''.join(str(Job_list[i].title)))
						new_rewrite_1.write('|')
						new_rewrite_1.write(''.join(str(Job_list[i].description)))
						new_rewrite_1.write('|')
						new_rewrite_1.write(''.join(str(Job_list[i].DueBool)))
						new_rewrite_1.write('|')
						new_rewrite_1.write(''.join(str(Job_list[i].DueDay)))
						new_rewrite_1.write('|')
						new_rewrite_1.write(''.join(str(Job_list[i].DueHour)))
						new_rewrite_1.write('|')
						new_rewrite_1.write(''.join(str(Job_list[i].DueMinute)))
						new_rewrite_1.write('|')
						new_rewrite_1.write(''.join(str(Job_list[i].Limit_Time)))
						new_rewrite_1.write('|')
						new_rewrite_1.write(''.join(str(Job_list[i].importance)))
						new_rewrite_1.write('\n')
				new_rewrite_1.close()

				for i in range(0, len(Job_list), 1):
					for j in range(0, len(submitted_late), 1):
						if Job_list[i].title == submitted_late[j]:
							Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")

				edit_WD.destroy()
				store_list_3.clear()

		def make_change():
			# Get id edit job #
			temp_id = selected_og[0]
			# Get current time
			cr_day_e = time.strftime("%d")
			cr_month_e = time.strftime("%m")
			cr_year_e = time.strftime("%Y")
			cr_hour_24f2 = time.strftime("%H")
			cr_minute_e = time.strftime("%M")

			# Quit confirm value:
			Quit_Confirm_b = False

			# Get new description
			new_descript_get = (Description_entry.get('1.0', 'end-1c')).strip()
			
			# Get new title
			new_title_get = (Entry_title.get()).strip()

			# Get new date
			new_date_get = display_date.get()

			# Get new Time
			new_hour_get =  Hour_spin.get()
			new_minute_get = Minute_spin.get()

			# Get new priority + time limit
			new_importance_get = Importance_edit_2.get()

			new_timelimit_get = Time_limit_edit.get()

			temp_ = new_date_get.split('/')

			### Get old title ###
			old_title = Job_list[temp_id].title

			# If Due time set == "On"
			if Due_Time_Box.get() == "On":
				if new_title_get != "":
					if new_descript_get != "":

						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						force_nextStep = False

						if Job_list[temp_id].title == new_title_get:
							force_nextStep = True

						for i in range(0, len(Job_list), 1):
							if new_title_get == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if new_title_get == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if new_title_get == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and force_nextStep == False:
							Status_change.config(text = "Job already been created.")
						else:						
							if int(temp_[2]) > int(cr_year_e):
								# Adjust quit confirm value
								Quit_Confirm_b = True

								# Adjust Due time set
								Job_list[int(temp_id)].DueBool = "True"

								# Adjust Limit Time and Priority back to 0
								Job_list[int(temp_id)].Limit_Time = 0
								Job_list[int(temp_id)].importance = 0

								# Adjust Due Day and Due Time
								Job_list[int(temp_id)].DueDay = new_date_get
								Job_list[int(temp_id)].DueHour = new_hour_get
								Job_list[int(temp_id)].DueMinute = new_minute_get

								# Adujst new Title and description
								Job_list[int(temp_id)].title = new_title_get
								Job_list[int(temp_id)].description = new_descript_get

							elif int(temp_[2]) == int(cr_year_e):
								if int(temp_[1]) > int(cr_month_e):
									# Adjust quit confirm value
									Quit_Confirm_b = True

									# Adjust Due time set
									Job_list[int(temp_id)].DueBool = "True"

									# Adjust Limit Time and Priority back to 0
									Job_list[int(temp_id)].Limit_Time = 0
									Job_list[int(temp_id)].importance = 0

									# Adjust Due Day and Due Time
									Job_list[int(temp_id)].DueDay = new_date_get
									Job_list[int(temp_id)].DueHour = new_hour_get
									Job_list[int(temp_id)].DueMinute = new_minute_get

									# Adujst new Title and description
									Job_list[int(temp_id)].title = new_title_get
									Job_list[int(temp_id)].description = new_descript_get

								elif int(temp_[1]) == int(cr_month_e):
									if int(temp_[0]) > int(cr_day_e):
										# Adjust quit confirm value
										Quit_Confirm_b = True

										# Adjust Due time set
										Job_list[int(temp_id)].DueBool = "True"

										# Adjust Limit Time and Priority back to 0
										Job_list[int(temp_id)].Limit_Time = 0
										Job_list[int(temp_id)].importance = 0

										# Adjust Due Day and Due Time
										Job_list[int(temp_id)].DueDay = new_date_get
										Job_list[int(temp_id)].DueHour = new_hour_get
										Job_list[int(temp_id)].DueMinute = new_minute_get

										# Adujst new Title and description
										Job_list[int(temp_id)].title = new_title_get
										Job_list[int(temp_id)].description = new_descript_get

									elif int(temp_[0]) == int(cr_day_e):
										if int(new_hour_get) > int(cr_hour_24f2):
											# Adjust quit confirm value
											Quit_Confirm_b = True

											# Adjust Due time set
											Job_list[int(temp_id)].DueBool = "True"

											# Adjust Limit Time and Priority back to 0
											Job_list[int(temp_id)].Limit_Time = 1
											Job_list[int(temp_id)].importance = 0

											# Adjust Due Day and Due Time
											Job_list[int(temp_id)].DueDay = new_date_get
											Job_list[int(temp_id)].DueHour = new_hour_get
											Job_list[int(temp_id)].DueMinute = new_minute_get

											# Adujst new Title and description
											Job_list[int(temp_id)].title = new_title_get
											Job_list[int(temp_id)].description = new_descript_get

										elif int(new_hour_get) == int(cr_hour_24f2):
											if int(new_minute_get) > int(cr_minute_e):
												# Adjust quit confirm value
												Quit_Confirm_b = True

												# Adjust Due time set
												Job_list[int(temp_id)].DueBool = "True"

												# Adjust Limit Time and Priority back to 0
												Job_list[int(temp_id)].Limit_Time = 0
												Job_list[int(temp_id)].importance = 0

												# Adjust Due Day and Due Time
												Job_list[int(temp_id)].DueDay = new_date_get
												Job_list[int(temp_id)].DueHour = new_hour_get
												Job_list[int(temp_id)].DueMinute = new_minute_get

												# Adujst new Title and description
												Job_list[int(temp_id)].title = new_title_get
												Job_list[int(temp_id)].description = new_descript_get

											else:
												Status_change.config(text = "Invalid minute (too late)")
										else:
											Status_change.config(text = "Invalid hour (too late)")
									else:
										Status_change.config(text = "Invalid day (too late)")
								else:
									Status_change.config(text = "Invalid month (too late)")
							else:
								Status_change.config(text = "Invalid year (too late)")
					else:
						Status_change.config(text = "Please add job description")
				else:
					Status_change.config(text = "Please add job title")

			# If Due time set == "None"
			else:
				if new_title_get != "":
					if new_descript_get != "":

						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						force_nextStep = False

						if Job_list[temp_id].title == new_title_get:
							force_nextStep = True

						for i in range(0, len(Job_list), 1):
							if new_title_get == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if new_title_get == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if new_title_get == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and force_nextStep == False:
							Status_change.config(text = "Job already been created.")
						else:								
							# Adjust quit confirm value
							Quit_Confirm_b = True

							# Add new title
							Job_list[int(temp_id)].title = new_title_get
							Job_list[int(temp_id)].description = new_descript_get

							# Adjust due time set
							Job_list[int(temp_id)].DueBool = "False"

							## Delete due date and due time
							# Remove Due date
							Job_list[int(temp_id)].DueDay = "None"

							# Remove Due time
							Job_list[int(temp_id)].DueHour = 0
							Job_list[int(temp_id)].DueMinute = 0

							# Adjust new time limit and importance value
							Job_list[int(temp_id)].Limit_Time = new_timelimit_get
							Job_list[int(temp_id)].importance = new_importance_get

					else:
						Status_change.config(text = "Please add job description")
				else:
					Status_change.config(text = "Please add job title")

			for i in range(0, len(submitted_late), 1):
				if submitted_late[i] == old_title:
					submitted_late[i] = new_title_get
					break

			## rewrite submitted_late.txt ##
			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as rewrite_submit:
				for i in range(0, len(submitted_late), 1):
					rewrite_submit.write("".join(str(submitted_late[i])))
					rewrite_submit.write("\n")
			rewrite_submit.close()

			if not Quit_Confirm_b:
				pass
			else:
				# Delete value and add back to the top listbox
				Todo_List.delete(temp_id)
				Todo_List.insert(0, "  %s" %Job_list[temp_id].title)

				# Store temporarily new value in temp list and delete new value from the OG list
				store_list_2 = []
				store_list_2.append(Job_list[temp_id])

				Job_list.remove(Job_list[temp_id])

				# Add back to the top of To do List - Job list
				Job_list.insert(0, store_list_2[0])

				with open("Project/%s/%s/%s" %(tag_number_int, empty_String, doing_stt_), "w") as new_rewrite:
					for i in range(0, len(Job_list), 1):
						new_rewrite.write(''.join(str(Job_list[i].title)))
						new_rewrite.write('|')
						new_rewrite.write(''.join(str(Job_list[i].description)))
						new_rewrite.write('|')
						new_rewrite.write(''.join(str(Job_list[i].DueBool)))
						new_rewrite.write('|')
						new_rewrite.write(''.join(str(Job_list[i].DueDay)))
						new_rewrite.write('|')
						new_rewrite.write(''.join(str(Job_list[i].DueHour)))
						new_rewrite.write('|')
						new_rewrite.write(''.join(str(Job_list[i].DueMinute)))
						new_rewrite.write('|')
						new_rewrite.write(''.join(str(Job_list[i].Limit_Time)))
						new_rewrite.write('|')
						new_rewrite.write(''.join(str(Job_list[i].importance)))
						new_rewrite.write('\n')
				new_rewrite.close()
				edit_WD.destroy()
				store_list_2.clear()

		def error():
			alert = Toplevel()
			alert.title("Oops! Somethings went wrong.")
			alert.resizable(0, 0)

			alert_w = 350
			alert_h = 120

			postiion_alert_x = (alert.winfo_screenwidth()//2) - (alert_w//2)
			position_alert_y = (alert.winfo_screenheight()//2) - (alert_h//2)

			alert.geometry(f"{alert_w}x{alert_h}+{postiion_alert_x}+{position_alert_y}")
			alert.config(bg = "#1e222a")

			bg_image = PhotoImage(file = "images/Edit Window/alert.png")
			bg_ = Label(alert, image = bg_image, bg = "#1e222a")
			bg_.photo = bg_image

			bg_.place(x = 0, y = 0, relwidth = 1)

			close_button = Button(alert, text = "   OK   ", font = ("Consolas", 12), bg = "#2a5bba", fg = "#FFFFFF", command = lambda: alert.destroy())
			close_button.place(x = 130, y = 76)

		def edit_tab():
			Search_button_active.place_forget()
			Search_Frame.place_forget()
			Edit_Button_Ex_Active.place(x = 0, y = 60)
			Edit_Frame.place(x = 143, y = 50)
			# Filter_Frame.place_forget()
			# Filter_Button_active.place_forget()

		def go_to_edit():
			selected_og.clear()
			# Create two temp list for display
			selected_display_ = []

			# Select entire treeview list
			id_selection = Tree_result.selection()
			for record in id_selection:
				selected_display_.append(int(record))

			# print(selected_display_)

			if len(selected_display_) > 1:
				error()
			elif len(selected_display_) == 1:
				# Append to list any value in select to selected original list
				length_list = len(Job_list)
				for i in selected_display_:
					for j in range(0, length_list, 1):
						if Display_joblist[i].title == Job_list[j].title:
							selected_og.append(j)

				# Hide disable button
				Edit_Button_Ex_disable.place_forget()
				Search_button_active.place_forget()
				Search_Frame.place_forget()
				Edit_Button_Ex_Active.place(x = 0, y = 60)
				Edit_Frame.place(x = 143, y = 50)

				if not selected_og:
					pass
				else:
					## Store temp value id ##
					# print(selected_og[0])
					temp = selected_og[0]

					if Job_list[temp].DueBool == "True":
						Due_Frame.place(x = 350, y = 210)
						NoDue_Frame.place_forget()

						if doing_stt_ == Title[2]:
							Due_Time_Box.place_forget()
							Date_Edit.place_forget()
							Hour_spin.place_forget()
							Minute_spin.place_forget()

							Due_time_Entry.place(x = 350, y = 120)
							Due_time_Entry.config(state = NORMAL)
							Due_time_Entry.delete(0, 'end')
							Due_time_Entry.insert(END, "On")
							Due_time_Entry.config(state = "readonly")

							Date_display.place(x = 90, y = 10)
							Date_display.config(state = NORMAL)
							Date_display.delete(0, 'end')
							Date_display.insert(END, Job_list[temp].DueDay)
							Date_display.config(state = "readonly")

							Time_label.place(x = 5, y = 70)
							Hour_display.place(x = 90, y = 70)
							Hour_display.config(state = NORMAL)
							Hour_display.delete(0, 'end')
							Hour_display.insert(END, Job_list[temp].DueHour)
							Hour_display.config(state = "readonly")

							colon_lbl.place(x = 145, y = 70)

							Minute_display.place(x = 170, y = 70)
							Minute_display.config(state = NORMAL)
							Minute_display.delete(0, 'end')
							Minute_display.insert(END, Job_list[temp].DueMinute)
							Minute_display.config(state = "readonly")

							Status_change.place(x = 350, y = 465)

							note_lbl.place(x = 5, y = 140)

							# hide
							old_time_lim.place_forget()
							old_importance_.place_forget()
							old_due_t.place_forget()
							old_due_date.place_forget()
						else:
							Due_Time_Box.current(1)
							old_time_lim.config(text = "Your old time limit: %s" %Job_list[temp].Limit_Time)
							old_importance_.config(text = "Your old importance value: %s" %Job_list[temp].importance)
							old_due_t.config(text = "Your old due time: %s:%s" %(Job_list[temp].DueHour, Job_list[temp].DueMinute))
							old_due_date.config(text = "Your old due date: %s" %(Job_list[temp].DueDay))
							Status_change.place(x = 350, y = 450)
					else:
						Due_Frame.place_forget()
						NoDue_Frame.place(x = 350, y = 210)

						if doing_stt_ == Title[2]:
							Due_Time_Box.place_forget()
							Time_limit_edit.place_forget()
							Importance_edit_2.place_forget()

							Due_time_Entry.place(x = 350, y = 120)
							Due_time_Entry.config(state = NORMAL)
							Due_time_Entry.delete(0, 'end')
							Due_time_Entry.insert(END, "None")
							Due_time_Entry.config(state = "readonly")

							Time_limit_display.place(x = 180, y = 5)
							Time_limit_display.config(state = NORMAL)
							Time_limit_display.delete(0, 'end')
							Time_limit_display.insert(END, Job_list[temp].Limit_Time)
							Time_limit_display.config(state = "readonly")

							Importance_display.place(x = 180, y = 70)
							Importance_display.config(state = NORMAL)
							Importance_display.delete(0, 'end')
							Importance_display.insert(END, Job_list[temp].importance)
							Importance_display.config(state = "readonly")

							Importance_label.place(x = 5, y = 70)

							note_lbl_no.place(x = 5, y = 140)

							Status_change.place(x = 350, y = 465)

							## hide
							old_time_lim.place_forget()
							old_importance_.place_forget()
							old_due_t.place_forget()
							old_due_date.place_forget()

						else:
							Due_Time_Box.current(0)
							old_due_t.config(text = "Your old due time: 00:00")
							old_due_date.config(text = "Your old due date:")
							old_time_lim.config(text = "Your old time limit: %s" %Job_list[temp].Limit_Time)
							old_importance_.config(text = "Your old importance value: %s" %Job_list[temp].importance)

							Status_change.place(x = 350, y = 450)
							
					## Clear entr before add
					Entry_title.delete(0, 'end')
					Description_entry.delete('1.0', END)

					## Add value to entry
					Entry_title.insert(0, Job_list[temp].title)
					Description_entry.insert(END, Job_list[temp].description)
					selected_display_.clear()

		## Change due set ##
		def change_due_value(event):
			if Due_Time_Box.get() == "On":
				Due_Frame.place(x = 350, y = 210)
				NoDue_Frame.place_forget()
			else:
				Due_Frame.place_forget()
				NoDue_Frame.place(x = 350, y = 210)

		## Window UI
		edit_WD.title("%s list: Edit content" %doing_stt_)

		edwm_height = 600
		edwm_width = 870

		mn_height = edit_WD.winfo_screenheight()
		mn_width = edit_WD.winfo_screenwidth()

		p_x = (mn_width//2) - (edwm_width//2)
		p_y = (mn_height//2) - (edwm_height//2)

		edit_WD.geometry(f"{edwm_width}x{edwm_height}+{p_x}+{p_y}")
		edit_WD.resizable(0,0)

		edit_WD.config(bg = "#262a34")

		## Top Bar Frame
		Top_Bar_Frame = Frame(edit_WD, width = 870, height = 40, bg = "#1e222a")
		Top_Bar_Frame.pack(anchor = "n")

		## Label on top bar frame
		Todo_Edit_window = Label(Top_Bar_Frame, text = "%s list: Edit content" %doing_stt_, font = ("Consolas", 15, "bold"), bg = "#1e222a", fg = "#FFFFFF")
		Todo_Edit_window.place(x = 300, y = 5)

		## Lefside Frame Button
		Lf_Button = Frame(edit_WD, width = 142, height = 600, bg = "#1e222a")
		Lf_Button.pack(anchor = "sw")

		### Image Button ###
		## Search Icon Image
		Search_icon_normal = PhotoImage(file = "images/Edit Window/Search_Button_Normal.png")
		Search_icon_hover = PhotoImage(file = "images/Edit Window/Search_Button_Hover.png")
		Search_icon_press = PhotoImage(file = "images/Edit Window/Search_Button_Press.png")

		## Edit Icon Image
		Edit_Icon_Normal = PhotoImage(file = "images/Edit Window/Edit_Button_Normal.png")
		Edit_Icon_Hover = PhotoImage(file = "images/Edit Window/Edit_Button_Hover.png")
		Edit_Icon_Press = PhotoImage(file = "images/Edit Window/Edit_Button_Press.png")
		Edit_icon_Normal_disable = PhotoImage(file = "images/Edit Window/Edit_Button_Normal_disable.png")

		## Filter Icon Image
		Filter_Icon_Normal = PhotoImage(file = "images/Edit Window/Filter_Button_Normal.png")
		Filter_Icon_Hover = PhotoImage(file = "images/Edit Window/Filter_Button_Hover.png")
		Filter_Icon_Press = PhotoImage(file = "images/Edit Window/Filter_Button_Press.png")

		## Button UI
		# Search Button
		Search_button = CustomButton(Lf_Button,
									Search_icon_normal,
									Search_icon_hover,
									Search_icon_press,
									"#1e222a", "#2b313c", "#2a5bba",
									0, 0, 0, Search_tab)
		Search_button_active = Label(Lf_Button, image = Search_icon_press, bg = "#2a5bba", bd = 1)
		Search_button_active.place(x = 0, y = 0)

		# Edit Button
		Edit_Button_Ex = CustomButton(Lf_Button,
									Edit_Icon_Normal,
									Edit_Icon_Hover,
									Edit_Icon_Press,
									"#1e222a", "#2b313c", "#2a5bba",
									0, 60, 0, edit_tab)
		Edit_Button_Ex_Active = Label(Lf_Button, image = Edit_Icon_Press, bg = "#2a5bba", bd = 0)
		Edit_Button_Ex_disable = Label(Lf_Button, image = Edit_icon_Normal_disable, bg = "#1e222a", bd = 1)
		Edit_Button_Ex_disable.photo = Edit_icon_Normal_disable
		Edit_Button_Ex_disable.place(x = 0, y = 60)


		## Search Frame
		Search_Frame = Frame(edit_WD, bg = "#262a34", width = 800, height = 650)
		Search_Frame.place(x = 143, y = 50)

		Search_Label = Label(Search_Frame, text = "Search:", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Search_Label.place(x = 20, y = 10)

		Search_Entry = Entry(Search_Frame, width = 15, font = ("Consolas", 15))
		Search_Entry.place(x = 100, y = 12)

		# Search_In = ttk.Combobox(Search_Frame, value = Filter_In, font = ("Consolas", 15), width = 12, state = "readonly")
		# Search_In.place(x = 280, y = 12)
		# Search_In.current(0)

		# Search_Job = ttk.Combobox(Search_Frame, value = Filter_List, font = ("Consolas", 15), width = 10, state = "readonly")
		# Search_Job.place(x = 430, y = 12)
		# Search_Job.current(0)

		Initiate_Search = Button(Search_Frame, text = "Search job", font = ("Consolas", 13, "bold"), bg = "#2a5bba", fg = "#FFFFFF", command = search_list)
		# Initiate_Search.place(x = 450, y = 11)
		Initiate_Search.place(x = 280, y = 10)

		## Edit Button
		Edit_bttn = Button(Search_Frame, text = "Edit", font = ("Consolas", 13, "bold"), bg = "#2b313c", fg = "#FFFFFF", command = go_to_edit)
		Edit_bttn.place(x = 400, y = 10)

		Signal_Label = Label(Search_Frame, text = "Result:", font = ("Consolas", 15, 'bold'), bg = "#262a34", fg = "#FFFFFF")
		Signal_Label.place(x = 20, y = 58)

		Delete_Selected = Button(Search_Frame, text = "Delete selected", font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34", command = del_selected)
		Delete_Selected.place(x = 20, y = 495)

		Delete_All = Button(Search_Frame, text = "Delete all", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF", command = del_all)
		Delete_All.place(x = 220, y = 495)

		## Result Frame
		# Contain Result Frame
		Result_Frame = Frame(Search_Frame, width = 700, height = 378, bg = "#1e222a")
		Result_Frame.place(x = 10, y = 100)

		### Tree View ###
		Tree_result = ttk.Treeview(Result_Frame)

		# Set Column
		Tree_result['column'] = ("Title", "Description", "Due Set", "Due Date", "Due Time", "Time Limit", "Importance")

		# Format Columns
		Tree_result.column("#0", width = 0, stretch = NO)
		Tree_result.column("Title", anchor = "w", width = 100)
		Tree_result.column("Description", anchor = "w", width = 140)
		Tree_result.column("Due Set", anchor = "center", width = 100)
		Tree_result.column("Due Date", anchor = "center", width = 100)
		Tree_result.column("Due Time", anchor = "center", width = 100)
		Tree_result.column("Time Limit", anchor = "center", width = 80)
		Tree_result.column("Importance", anchor = "center", width = 80)

		# Set Headings
		Tree_result.heading("#0", text = "", anchor = "center")
		Tree_result.heading("Title", text = "Title", anchor = "w")
		Tree_result.heading("Description", text = "Description", anchor = "w")
		Tree_result.heading("Due Set", text = "Due Set", anchor = "center")
		Tree_result.heading("Due Date", text = "Due Date", anchor = "center")
		Tree_result.heading("Due Time", text = "Due Time", anchor = "center")
		Tree_result.heading("Time Limit", text = "Time Limit", anchor = "center")
		Tree_result.heading("Importance", text = "Importance", anchor = "center")

		for i in range(0, len(Job_list), 1):
			Tree_result.insert(parent = '',
								index = 'end',
								iid = i, text = "",
								values =(
									Display_joblist[i].title,
									Display_joblist[i].description,
									Display_joblist[i].DueBool,
									Display_joblist[i].DueDay,
									str(Display_joblist[i].DueHour)+":"+str(Display_joblist[i].DueMinute),
									Display_joblist[i].Limit_Time,
									Display_joblist[i].importance))

		# Create Style
		style = ttk.Style()
		style.configure('Treeview', rowheight = 35, font = ("Consolas", 12))
		Tree_result.place(x = 0, y = 0)
		# Tree_result.bind("<Button-1>", on_click_tree)
		# Tree_result.bind("<Button-1>", selectedItem)

		## Edit Frame
		Edit_Frame = Frame(edit_WD, bg = "#262a34", width = 800, height = 650)

		## Status changes ##
		Status_change = Label(Edit_Frame, font = ("Consolas", 15, "bold"), bg = "#262a34", fg = "#55aaff")

		## Save change button
		save_button = Button(Edit_Frame, text = "Save change", font = ("Consolas", 20, "bold"), bg = "#2a5bba", fg = "#FFFFFF", command = confirm_save_changes)
		save_button.place(x = 110, y = 450)

		# Editing mode - readonly/ edit mode
		Editing_state = Label(Edit_Frame, text = "View mode:", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		# Editing_state.place(x = 400, y = 5)

		# Comobox to change editing state/ mode
		Editing_mode = ttk.Combobox(Edit_Frame, value = Edit_mode, font = ("Consolas", 15), width = 10, state = "readonly")
		# Editing_mode.place(x = 530, y = 5)
		# Editing_mode.current(0)

		# Title label + entry
		Title_Label = Label(Edit_Frame, text = "Title:", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Title_Label.place(x = 20, y = 45)

		Entry_title = Entry(Edit_Frame, font = ("Consolas", 15), width = 25)
		Entry_title.place(x = 20, y = 80)

		# Description label + entry
		Description_Label = Label(Edit_Frame, text = "Description", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Description_Label.place(x = 20, y = 120)

		Description_entry = Text(Edit_Frame, font = ("Consolas", 15), width = 25, height = 10)
		Description_entry.place(x = 20, y = 160)

		# Due Time Set + Combobox
		Due_Time_Label = Label(Edit_Frame, text = "Due Time Set:", font = ("Consolas", 20), bg = "#262a34", fg = "#FFFFFF")
		Due_Time_Label.place(x = 350, y = 75)

		Due_Time_Box = ttk.Combobox(Edit_Frame, value = Sign_list, font = ("Consolas", 20), width = 8, state = "readonly")
		Due_Time_Box.bind("<<ComboboxSelected>>", change_due_value)
		Due_Time_Box.place(x = 350, y = 120)

		Due_time_Entry = Entry(Edit_Frame, font = ("Consolas", 20), width = 8)

		## Seperate line
		Line_ = Label(Edit_Frame, text = "______________________", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Line_.place(x = 350, y = 160)

		## No Due time Frame
		NoDue_Frame = Frame(Edit_Frame, width = 330, height = 230, bg = "#262a34")

		note_lbl_no = Label(NoDue_Frame, text = note_complete, font = ("Consolas", 10), fg = "#7687a2", bg = "#262a34", justify = "left")

		status_nodue = Label(NoDue_Frame, font = ("Consolas", 15), bg = "#262a34", fg = "#55aaff")
		status_nodue.place(x = 5, y = 250)

		old_time_lim = Label(NoDue_Frame, text = "Your old time limit: ", font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		old_time_lim.place(x = 5, y = 55)

		old_importance_ = Label(NoDue_Frame, text = "Your old importance value: ", font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		old_importance_.place(x = 5, y = 167)

		Time_limit_lbl = Label(NoDue_Frame, text = "Time Limit:", font = ("Consolas", 20), bg = "#262a34", fg = "#FFFFFF")
		Time_limit_lbl.place(x = 5, y = 5)

		Time_limit_edit = Spinbox(NoDue_Frame, font = ("Consolas", 20), from_ = 1, to = 23, width = 2)
		Time_limit_edit.place(x = 180, y = 5)

		Time_limit_display = Entry(NoDue_Frame, font = ("Consolas", 20), width = 2, state = "readonly", textvariable = display_timelimit)

		Importance_label = Label(NoDue_Frame, text = "Importance:", font = ("Consolas", 20), bg = "#262a34", fg = "#FFFFFF")
		Importance_label.place(x = 5, y = 120)

		Importance_display = Entry(NoDue_Frame, font = ("Consolas", 20), width = 2, state = "readonly", textvariable = display_importance)

		Importance_edit_2 = Spinbox(NoDue_Frame, font = ("Consolas", 20), from_ = 1, to = 9, width = 2)
		Importance_edit_2.place(x = 180, y = 120)

		## Due Time Frame
		Due_Frame = Frame(Edit_Frame, width = 350, height = 220, bg = "#262a34")

		status_due = Label(Due_Frame, font = ("Consolas", 15), bg = "#262a34", fg = "#55aaff")
		status_due.place(x = 5, y = 250)

		note_lbl = Label(Due_Frame, text = note_complete, font = ("Consolas", 10), fg = "#7687a2", bg = "#262a34", justify = "left")

		Date_label = Label(Due_Frame, text = "Date:", font = ("Consolas", 20), bg = "#262a34", fg = "#FFFFFF")
		Date_label.place(x = 5, y = 5)

		Date_display = Entry(Due_Frame, font = ("Consolas", 20), width = 11)

		Date_Edit = CustomDateEntry(Due_Frame,
			selectbackground='gray80',
	        selectforeground='black',
			normalbackground='white',
			normalforeground='black',
	        background='gray90',
	        foreground='black',
	        bordercolor='gray90',
	        othermonthforeground='gray50',
	        othermonthbackground='white',
	        othermonthweforeground='gray50',
	        othermonthwebackground='white',
	        headersbackground='white',
	        headersforeground='gray70',
	        date_pattern = "dd/mm/yyyy",
	        font = ("Consolas", 15),
	        textvariable = display_date,
	        selectmode = "day",
	        state = "readonly")
		Date_Edit.place(x = 90, y = 10)

		old_due_t = Label(Due_Frame, text = "Your old due time: ", font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		old_due_t.place(x = 5, y = 180)

		old_due_date = Label(Due_Frame, text = "Your old due date: ", font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		old_due_date.place(x = 5, y = 60)

		Time_label = Label(Due_Frame, text = "Time:", font = ("Consolas", 20), bg = "#262a34", fg = "#FFFFFF")
		Time_label.place(x = 5, y = 120)

		Hour_spin = Spinbox(Due_Frame, font = ("Consolas", 20), from_ = 00, to = 23, width = 2, state = "readonly", format = "%02.0f")
		Hour_spin.place(x = 90, y = 125)

		Hour_display = Entry(Due_Frame, font = ("Consolas", 20), textvariable = display_hour, width = 3)

		colon_lbl = Label(Due_Frame, text = ":", font = ("Consolas", 20), bg = "#262a34", fg = "#FFFFFF")
		colon_lbl.place(x = 145, y = 120)

		Minute_spin = Spinbox(Due_Frame, font = ("Consolas", 20), from_ = 00, to = 59, width = 2, state = "readonly", format = "%02.0f")
		Minute_spin.place(x = 170, y = 125)

		Minute_display = Entry(Due_Frame, font = ("Consolas", 20), textvariable = display_minute, width = 3)


	## Double click to edit menu
	def edit_item_Do(event):
		edit_item_window(Job_list, Todo_List, Title[0])

	def edit_item_doing_(event):
		edit_item_window(Doing_list, Doing_Listbox, Title[1])

	def edit_item_complete_(event):
		edit_item_window(Complete_List, Comp_List, Title[2])

	def edit_item_window(Job_list, Todo_List, Doing_stt):
		# Confirm save change
		def confirm_save():
			def confirm_change():
				if Doing_stt == Title[2]:
					save_change_complete()
				else:
					save_change_job()
				confirm_window.destroy()

			def deny_change():
				edit_item.destroy()
				confirm_window.destroy()

			confirm_window = Toplevel()
			confirm_window.geometry(f"370x100+{(confirm_window.winfo_screenwidth()//2) - (370//2)}+{(confirm_window.winfo_screenheight()//2) - (100//2)}")
			confirm_window.resizable(0, 0)
			confirm_window.wm_attributes('-topmost', 1)

			confirm_window.title("Confirm save changes")
			confirm_window.config(bg = "#262a34")

			confirm_label = Label(confirm_window,
								text = "Do you want to save any changes?",
								font = ("Consolas", 13), bg = "#262a34", fg = "#FFFFFF")
			confirm_label.place(x = 10, y = 15)

			confirm_yes = Button(confirm_window, text = "  Yes  ", font = ("Consolas", 11), bg = "#1544a0", fg = "#FFFFFF",
								command = confirm_change)
			confirm_yes.place(x = 120, y = 55)

			confirm_no = Button(confirm_window, text = "  No  ", font = ("Consolas", 11), bg = "#1544a0", fg = "#FFFFFF",
								command = deny_change)
			confirm_no.place(x = 200, y = 55)

			confirm_cancel = Button(confirm_window, text = "  Cancel  ", font = ("Consolas", 11), bg = "#ed2249", fg = "#FFFFFF",
									command = lambda: confirm_window.destroy())
			confirm_cancel.place(x = 270, y = 55)

		# Save change function
		def save_change_job():
			global late_submitted

			# Quit confirm value:
			Quit_Confirm = False

			# Get current time
			day_ = time.strftime("%d")
			month_ = time.strftime("%m")
			year_ = time.strftime("%Y")
			hour_24f = time.strftime("%H")
			minute_ = time.strftime("%M")

			# Get new description
			new_descript = (Description_entr.get('1.0', 'end-1c')).strip()
			
			# Get new title
			new_title = (Title_entry.get()).strip()

			# Get new date
			date_get = display_cal.get()

			# Get new Time
			new_hour =  Hour_onScr.get()
			new_minute = Minute_onScr.get()

			# Get new priority + time limit
			new_importance = Importance_edit.get()
			new_timelimit = Time_lim_edit.get()

			temp = date_get.split('/')

			### Old title job ###
			old_titl_get = Job_list[empty_temp_string].title

			# If Due time set == "On"
			if Due_set_box.get() == "On":
				if new_title != "":
					if new_descript != "":

						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						forceNext_step = False

						if Job_list[empty_temp_string].title == new_title:
							forceNext_step = True

						for i in range(0, len(Job_list), 1):
							if new_title == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if new_title == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if new_title == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and forceNext_step == False:
							Status_label.config(text = "Job already been created.")

						else:
							if int(temp[2]) > int(year_):
								# Adjust quit confirm value
								Quit_Confirm = True

								# Adjust Due time set
								Job_list[int(empty_temp_string)].DueBool = "True"

								# Adjust Limit Time and Priority back to 0
								Job_list[int(empty_temp_string)].Limit_Time = 0
								Job_list[int(empty_temp_string)].importance = 0

								# Adjust Due Day and Due Time
								Job_list[int(empty_temp_string)].DueDay = date_get
								Job_list[int(empty_temp_string)].DueHour = new_hour
								Job_list[int(empty_temp_string)].DueMinute = new_minute

								# Adujst new Title and description
								Job_list[int(empty_temp_string)].title = new_title
								Job_list[int(empty_temp_string)].description = new_descript

							elif int(temp[2]) == int(year_):
								if int(temp[1]) > int(month_):
									# Adjust quit confirm value
									Quit_Confirm = True

									# Adjust Due time set
									Job_list[int(empty_temp_string)].DueBool = "True"

									# Adjust Limit Time and Priority back to 0
									Job_list[int(empty_temp_string)].Limit_Time = 0
									Job_list[int(empty_temp_string)].importance = 0

									# Adjust Due Day and Due Time
									Job_list[int(empty_temp_string)].DueDay = date_get
									Job_list[int(empty_temp_string)].DueHour = new_hour
									Job_list[int(empty_temp_string)].DueMinute = new_minute

									# Adujst new Title and description
									Job_list[int(empty_temp_string)].title = new_title
									Job_list[int(empty_temp_string)].description = new_descript

								elif int(temp[1]) == int(month_):
									if int(temp[0]) > int(day_):
										# Adjust quit confirm value
										Quit_Confirm = True

										# Adjust Due time set
										Job_list[int(empty_temp_string)].DueBool = "True"

										# Adjust Limit Time and Priority back to 0
										Job_list[int(empty_temp_string)].Limit_Time = 0
										Job_list[int(empty_temp_string)].importance = 0

										# Adjust Due Day and Due Time
										Job_list[int(empty_temp_string)].DueDay = date_get
										Job_list[int(empty_temp_string)].DueHour = new_hour
										Job_list[int(empty_temp_string)].DueMinute = new_minute

										# Adujst new Title and description
										Job_list[int(empty_temp_string)].title = new_title
										Job_list[int(empty_temp_string)].description = new_descript

									elif int(temp[0]) == int(day_):
										if int(new_hour) > int(hour_24f):
											# Adjust quit confirm value
											Quit_Confirm = True

											# Adjust Due time set
											Job_list[int(empty_temp_string)].DueBool = "True"

											# Adjust Limit Time and Priority back to 0
											Job_list[int(empty_temp_string)].Limit_Time = 1
											Job_list[int(empty_temp_string)].importance = 0

											# Adjust Due Day and Due Time
											Job_list[int(empty_temp_string)].DueDay = date_get
											Job_list[int(empty_temp_string)].DueHour = new_hour
											Job_list[int(empty_temp_string)].DueMinute = new_minute

											# Adujst new Title and description
											Job_list[int(empty_temp_string)].title = new_title
											Job_list[int(empty_temp_string)].description = new_descript

										elif int(new_hour) == int(hour_24f):
											if int(new_minute) > int(minute_):
												# Adjust quit confirm value
												Quit_Confirm = True

												# Adjust Due time set
												Job_list[int(empty_temp_string)].DueBool = "True"

												# Adjust Limit Time and Priority back to 0
												Job_list[int(empty_temp_string)].Limit_Time = 0
												Job_list[int(empty_temp_string)].importance = 0

												# Adjust Due Day and Due Time
												Job_list[int(empty_temp_string)].DueDay = date_get
												Job_list[int(empty_temp_string)].DueHour = new_hour
												Job_list[int(empty_temp_string)].DueMinute = new_minute

												# Adujst new Title and description
												Job_list[int(empty_temp_string)].title = new_title
												Job_list[int(empty_temp_string)].description = new_descript

											else:
												Status_label.config(text = "Invalid minute (too late)")
										else:
											Status_label.config(text = "Invalid hour (too late)")
									else:
										Status_label.config(text = "Invalid day (too late)")
								else:
									Status_label.config(text = "Invalid month (too late)")
							else:
								Status_label.config(text = "Invalid year (too late)")

					else:
						Status_label.config(text = "Please add job description")

				else:
					Status_label.config(text = "Please add job title")

			# If Due time set == "None"
			else:
				if new_title != "":
					if new_descript != "":
						
						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						forceNext_step = False

						if Job_list[empty_temp_string].title == new_title:
							forceNext_step = True

						for i in range(0, len(Job_list), 1):
							if new_title == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if new_title == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if new_title == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and forceNext_step == False:
							Status_label.config(text = "Job already been created.")
						else:
							# Adjust quit confirm value
							Quit_Confirm = True

							# Add new title
							Job_list[int(empty_temp_string)].title = new_title
							Job_list[int(empty_temp_string)].description = new_descript

							# Adjust due time set
							Job_list[int(empty_temp_string)].DueBool = "False"

							## Delete due date and due time
							# Remove Due date
							Job_list[int(empty_temp_string)].DueDay = "None"

							# Remove Due time
							Job_list[int(empty_temp_string)].DueHour = 0
							Job_list[int(empty_temp_string)].DueMinute = 0

							# Adjust new time limit and importance value
							Job_list[int(empty_temp_string)].Limit_Time = new_timelimit
							Job_list[int(empty_temp_string)].importance = new_importance

					elif new_descript.strip() == "":
						Status_label.config(text = "Please add job description")

				elif new_title.strip() == "":
					Status_label.config(text = "Please add job title")

			for i in range(0, len(submitted_late), 1):
				if submitted_late[i] == old_titl_get:
					submitted_late[i] = new_title
					break

			## rewrite submitted_late.txt ##
			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as rewrite_submit:
				for i in range(0, len(submitted_late), 1):
					rewrite_submit.write("".join(str(submitted_late[i])))
					rewrite_submit.write("\n")
			rewrite_submit.close()

			if not Quit_Confirm:
				pass
			else:
				# Delete value and add back to the top listbox
				Todo_List.delete(empty_temp_string)
				Todo_List.insert(0, "  %s" %Job_list[empty_temp_string].title)

				# Store temporarily new value in temp list and delete new value from the OG list
				store_list = []
				store_list.append(Job_list[empty_temp_string])

				Job_list.remove(Job_list[empty_temp_string])

				# Add back to the top of To do List - Job list
				Job_list.insert(0, store_list[0])

				with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Doing_stt), "w") as new_f:
					for i in range(0, len(Job_list), 1):
						new_f.write(''.join(str(Job_list[i].title)))
						new_f.write('|')
						new_f.write(''.join(str(Job_list[i].description)))
						new_f.write('|')
						new_f.write(''.join(str(Job_list[i].DueBool)))
						new_f.write('|')
						new_f.write(''.join(str(Job_list[i].DueDay)))
						new_f.write('|')
						new_f.write(''.join(str(Job_list[i].DueHour)))
						new_f.write('|')
						new_f.write(''.join(str(Job_list[i].DueMinute)))
						new_f.write('|')
						new_f.write(''.join(str(Job_list[i].Limit_Time)))
						new_f.write('|')
						new_f.write(''.join(str(Job_list[i].importance)))
						new_f.write('\n')

				new_f.close()
				edit_item.destroy()

		def save_change_complete():
			### Check quit confirm ###
			Quit_Confirm_3 = False

			n_description = (Description_entr.get('1.0', 'end-1c')).strip()

			n_title = (Title_entry.get()).strip()

			# Check due time set "On" or "Off":
			if Due_set_entry.get() == "On":
				if n_title != "":
					if n_description != "":

						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						forceTo_nextStep = False

						if Job_list[int(empty_temp_string)].title == n_title:
							forceTo_nextStep = True

						for i in range(0, len(Job_list), 1):
							if n_title == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if n_title == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if n_title == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and forceTo_nextStep == False:
							Status_label.config(text = "Job already been created.")
						else:
							## Adjust quit confirm value ##
							Quit_Confirm_3 = True

							for index in range(0, len(submitted_late), 1):
								if submitted_late[index] == Job_list[int(empty_temp_string)].title:
									submitted_late[index] = n_title

							Job_list[int(empty_temp_string)].title = n_title
							Job_list[int(empty_temp_string)].description = n_description
					else:
						Status_label.config(text = "Please add job description")
				else:
					Status_label.config(text = "Please add job title")
			else:
				if n_title != "":
					if n_description != "":

						Job_list_true = False
						Doing_list_true = False
						Complete_List_true = False

						next_step_true = False

						forceTo_nextStep = False

						if Job_list[int(empty_temp_string)].title == n_title:
							forceTo_nextStep = True

						for i in range(0, len(Job_list), 1):
							if n_title == Job_list[i].title:
								Job_list_true = True
								break

						if Job_list_true == True:
							pass
						else:
							for i in range(0, len(Doing_list), 1):
								if n_title == Doing_list[i].title:
									Doing_list_true = True
									break

						if Doing_list_true == True:
							pass
						else:
							for i in range(0, len(Complete_List), 1):
								if n_title == Complete_List[i].title:
									Complete_List_true = True
									break

						if Job_list_true == False and Doing_list_true == False and Complete_List_true == False:
							next_step_true = True

						if next_step_true == False and forceTo_nextStep == False:
							Status_label.config(text = "Job already been created.")
						else:
							## Adjust quit confirm value ##
							Quit_Confirm_3 = True

							for index in range(0, len(submitted_late), 1):
								if submitted_late[index] == Job_list[int(empty_temp_string)].title:
									submitted_late[index] = n_title

							Job_list[int(empty_temp_string)].title = n_title
							Job_list[int(empty_temp_string)].description = n_description
					else:
						Status_label.config(text = "Please add job description")
				else:
					Status_label.config(text = "Please add job title")

			with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as rwite_2:
				for i in range(0, len(submitted_late), 1):
					rwite_2.write("".join(str(submitted_late[i])))
					rwite_2.write("\n")
			rwite_2.close()

			if not Quit_Confirm_3:
				pass
			else:
				# Delete value and add back to the top listbox
				Todo_List.delete(empty_temp_string)
				Todo_List.insert(0, "  %s" %Job_list[empty_temp_string].title)

				# Store temporarily new value in temp list and delete new value from the OG list
				store_list_x = []
				store_list_x.append(Job_list[empty_temp_string])

				Job_list.remove(Job_list[empty_temp_string])

				# Add back to the top of To do List - Job list
				Job_list.insert(0, store_list_x[0])

				with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Doing_stt), "w") as new_rewrite_:
					for i in range(0, len(Job_list), 1):
						new_rewrite_.write(''.join(str(Job_list[i].title)))
						new_rewrite_.write('|')
						new_rewrite_.write(''.join(str(Job_list[i].description)))
						new_rewrite_.write('|')
						new_rewrite_.write(''.join(str(Job_list[i].DueBool)))
						new_rewrite_.write('|')
						new_rewrite_.write(''.join(str(Job_list[i].DueDay)))
						new_rewrite_.write('|')
						new_rewrite_.write(''.join(str(Job_list[i].DueHour)))
						new_rewrite_.write('|')
						new_rewrite_.write(''.join(str(Job_list[i].DueMinute)))
						new_rewrite_.write('|')
						new_rewrite_.write(''.join(str(Job_list[i].Limit_Time)))
						new_rewrite_.write('|')
						new_rewrite_.write(''.join(str(Job_list[i].importance)))
						new_rewrite_.write('\n')
				new_rewrite_.close()

				for i in range(0, len(Job_list), 1):
					for j in range(0, len(submitted_late), 1):
						if Job_list[i].title == submitted_late[j]:
							Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")

				edit_item.destroy()
				store_list_x.clear()
				

		def change_due_set(event):
			if Due_set_box.get() == "On":
				Due_time_Frame.place(x = 270, y = 130)
				NoDueTime_Frame.place_forget()
				if Job_list[int(empty_temp_string)].DueBool == "False":
					Old_date.config(text = "Your old date:")
					# Old_due_time.config(text = "Your old due time: _:_")
			else:
				NoDueTime_Frame.place(x = 270, y = 130)
				Due_time_Frame.place_forget()

		# Get item id
		empty_temp_string = ""
		for i in Todo_List.curselection():
			empty_temp_string = Todo_List.get(i)

		for i in range(0, len(Job_list), 1):
			if Job_list[i].title == empty_temp_string.strip():
				empty_temp_string = i
				break

		edit_item = Toplevel()

		# Variable
		display_cal = StringVar()

		app_h = 450
		app_w = 630

		mnt_height = edit_item.winfo_screenheight()
		mnt_width = edit_item.winfo_screenwidth()
	
		ps_x = (mnt_width//2) - (app_w//2)
		ps_y = (mnt_height//2) - (app_h//2)

		edit_item.geometry(f"{app_w}x{app_h}+{ps_x}+{ps_y}")
		edit_item.resizable(0, 0)
		edit_item.config(bg = "#262a34")
		edit_item.title("Edit content - %s list" %Doing_stt)

		# Window always on top others
		edit_item.wm_attributes('-topmost', 1)

		## Button save change
		save_change = Button(edit_item, text = "Save change", font = ("Consolas", 20), bg = "#2a5bba", fg = "#FFFFFF", command = confirm_save)
		save_change.place(x = 350, y = 360)

		## Save status label
		Status_label = Label(edit_item, font = ("Consolas", 15, "bold"), bg = "#262a34", fg = "#55aaff")
		Status_label.place(x = 270, y = 300)

		note_label = Label(edit_item, text = note_complete, font = ("Consolas", 10), bg = "#262a34",  fg = "#7687a2", justify = "left")

		## Title Job
		Title_lbl = Label(edit_item, text = "Title", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Title_lbl.place(x = 15, y = 20)

		Title_entry = Entry(edit_item, font = ("Consolas", 15), width = 20)
		Title_entry.place(x = 15, y = 60)
		Title_entry.insert(0, Job_list[int(empty_temp_string)].title)

		## Description Job
		Description_lbl = Label(edit_item, text = "Description", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Description_lbl.place(x = 15, y = 110)

		Description_entr = Text(edit_item, font = ("Consolas", 15), width = 20, height = 10)
		Description_entr.place(x = 15, y = 150)
		Description_entr.insert(END, Job_list[int(empty_temp_string)].description)

		## Due Time Set
		Due_set_label = Label(edit_item, text = "Due Time Set", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Due_set_label.place(x = 270, y = 50)
		Due_set_box = ttk.Combobox(edit_item, value = Sign_list, font = ("Consolas", 15), width = 5, state = "readonly")
		Due_set_box.place(x = 420, y = 50)
		Due_set_box.bind("<<ComboboxSelected>>", change_due_set)

		Due_set_entry = Entry(edit_item, font = ("Consolas", 15), width = 6)
		
		## Divide Line
		Divide_line = Label(edit_item, text = "____________________", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Divide_line.place(x = 270, y = 80)

		### No Due Time Frame ###
		NoDueTime_Frame = Frame(edit_item, width = 350, height = 170, bg = "#262a34")

		# Time limit job
		Time_lim_lbl = Label(NoDueTime_Frame, text = "Time Limit:", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Time_lim_lbl.place(x = 5, y = 5)

		time_limit_entry = Entry(NoDueTime_Frame, font = ("Consolas", 15), width = 3)

		Time_lim_edit = Spinbox(NoDueTime_Frame, font = ("Consolas", 15), from_ = 1, to = 23, width = 2, state = "readonly")
		Time_lim_edit.place(x = 135, y = 5)

		Old_time = Label(NoDueTime_Frame, text = "Your old time: %s" %Job_list[int(empty_temp_string)].Limit_Time,
						font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		Old_time.place(x = 5, y = 40)

		Importance_lbl = Label(NoDueTime_Frame, text = "Importance:", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Importance_lbl.place(x = 5, y = 85)

		Importance_entry = Entry(NoDueTime_Frame, font = ("Consolas", 15), width = 3)

		Importance_edit = Spinbox(NoDueTime_Frame, font = ("Consolas", 15), from_ = 1, to = 9, width = 2, state = "readonly")
		Importance_edit.place(x = 135, y = 85)

		Old_Importance = Label(NoDueTime_Frame, text = "Your old importance value: %s" %Job_list[int(empty_temp_string)].importance,
							font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		Old_Importance.place(x = 5, y = 120)

		### Due Time Frame ###
		## Due Time Frame
		Due_time_Frame = Frame(edit_item, width = 300, height = 170, bg = "#262a34")

		Date_lbl = Label(Due_time_Frame, text = "Date:", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Date_lbl.place(x = 5, y = 5)

		Date_Entrdisplay = Entry(Due_time_Frame, font = ("Consolas", 15), width = 11)

		Date_onScr = CustomDateEntry(Due_time_Frame,
			selectbackground='gray80',
	        selectforeground='black',
			normalbackground='white',
			normalforeground='black',
	        background='gray90',
	        foreground='black',
	        bordercolor='gray90',
	        othermonthforeground='gray50',
	        othermonthbackground='white',
	        othermonthweforeground='gray50',
	        othermonthwebackground='white',
	        headersbackground='white',
	        headersforeground='gray70',
	        date_pattern = "dd/mm/yyyy",
	        font = ("Consolas", 13),
	        textvariable = display_cal,
	        selectmode = "day",
	        state = "readonly")
		Date_onScr.place(x = 75, y = 6)

		# Display old date
		Old_date = Label(Due_time_Frame, text = "Your old date: %s" %Job_list[int(empty_temp_string)].DueDay,
						font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		Old_date.place(x = 5, y = 40)

		Time_lbl = Label(Due_time_Frame, text = "Time:", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Time_lbl.place(x = 5, y = 95)

		Hour_onScr = Spinbox(Due_time_Frame, font = ("Consolas", 15), from_ = 00, to = 23, width = 2, state = "readonly", format = "%02.0f")
		Hour_onScr.place(x = 70, y = 95)

		Hour_Entrdisplay = Entry(Due_time_Frame, font = ("Consolas", 15), width = 3)
		Hour_Entrdisplay.insert(0, Job_list[int(empty_temp_string)].DueHour)
		# Hour_Entrdisplay.config(state = "readonly")
		
		colon_line = Label(Due_time_Frame, text = ":", font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		colon_line.place(x = 110, y = 95)

		Minute_Entrdisplay = Entry(Due_time_Frame, font = ("Consolas", 15), width = 3)
		Minute_Entrdisplay.insert(0, Job_list[int(empty_temp_string)].DueMinute)
		# Minute_Entrdisplay.config(state = "readonly")

		Minute_onScr = Spinbox(Due_time_Frame, font = ("Consolas", 15), from_ = 00, to = 59, width = 2, state = "readonly", format = "%02.0f")
		Minute_onScr.place(x = 130, y = 95)

		#Display old time
		Old_due_time = Label(Due_time_Frame, text = "Your old due time: %s:%s"
							%(Job_list[int(empty_temp_string)].DueHour, Job_list[int(empty_temp_string)].DueMinute),
							font = ("Consolas", 15), fg = "#7687a2", bg = "#262a34")
		Old_due_time.place(x = 5, y = 130)

		if Job_list[empty_temp_string].DueBool == "True":
			Due_time_Frame.place(x = 270, y = 130)
			if Doing_stt == Title[2]:
				edit_item.geometry(f"{app_w}x480+{ps_x}+{mnt_height//2 - 480//2}")
				Due_time_Frame.config(height = 90)
				save_change.place(x = 350, y = 400)

				Due_set_entry.place(x = 420, y = 50)
				Due_set_entry.config(state = NORMAL)
				Due_set_entry.delete(0, 'end')
				Due_set_entry.insert(END, "On")
				Due_set_entry.config(state = "readonly")

				Date_onScr.place_forget()
				Old_date.place_forget()
				Hour_onScr.place_forget()
				Minute_onScr.place_forget()
				Old_due_time.place_forget()

				Date_Entrdisplay.place(x = 70, y = 6)
				Date_Entrdisplay.config(state = NORMAL)
				Date_Entrdisplay.delete(0, 'end')
				Date_Entrdisplay.insert(END, Job_list[int(empty_temp_string)].DueDay)
				Date_Entrdisplay.config(state = "readonly")

				Minute_Entrdisplay.place(x = 130, y = 50)
				Minute_Entrdisplay.config(state = NORMAL)
				Minute_Entrdisplay.delete(0, 'end')
				Minute_Entrdisplay.insert(END, Job_list[int(empty_temp_string)].DueMinute)
				Minute_Entrdisplay.config(state = "readonly")

				Hour_Entrdisplay.place(x = 70, y = 50)
				Hour_Entrdisplay.config(state = NORMAL)
				Hour_Entrdisplay.delete(0, 'end')
				Hour_Entrdisplay.insert(END, Job_list[int(empty_temp_string)].DueHour)
				Hour_Entrdisplay.config(state = "readonly")

				Time_lbl.place(x = 5, y = 50)
				colon_line.place(x = 110, y = 50)

				note_label.place(x = 270, y = 250)

				Status_label.place(x = 15, y = 420)

			Due_set_box.current(1)
		else:
			NoDueTime_Frame.place(x = 270, y = 130)

			if Doing_stt == Title[2]:
				Due_set_entry.place(x = 420, y = 50)
				Due_set_entry.config(state = NORMAL)
				Due_set_entry.delete(0, 'end')
				Due_set_entry.insert(END, "None")
				Due_set_entry.config(state = "readonly")

				edit_item.geometry(f"{app_w}x480+{ps_x}+{mnt_height//2 - 480//2}")

				Time_lim_edit.place_forget()
				Importance_edit.place_forget()
				Due_set_box.place_forget()

				Old_time.place_forget()
				Old_Importance.place_forget()

				NoDueTime_Frame.config(height = 90)

				Importance_entry.place(x = 135, y = 50)
				Importance_entry.config(state = NORMAL)
				Importance_entry.delete(0, 'end')
				Importance_entry.insert(END, Job_list[int(empty_temp_string)].importance)
				Importance_entry.config(state = "readonly")

				Importance_lbl.place(x = 5, y = 50)

				time_limit_entry.place(x = 135, y = 5)
				time_limit_entry.config(state = NORMAL)
				time_limit_entry.delete(0, 'end')
				time_limit_entry.insert(END, Job_list[int(empty_temp_string)].Limit_Time)
				time_limit_entry.config(state = "readonly")

				save_change.place(x = 350, y = 400)

				Status_label.place(x = 15, y = 420)

				note_label.place(x = 270, y = 250)
			else:
				Due_set_box.current(0)


	def rewrite_project_list(pj_name, complete_stt):
		Project_list.clear()

		with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "r") as old:
			reader = csv.reader(old, delimiter = '|')
			for row in reader:
				Project_list.append(Project_info(row[0], row[1]))
		old.close()

		for i in range(0, len(Project_list), 1):
			if Project_list[i].Project_name == pj_name:
				# Check progress value
				if complete_stt >= 100:
					Project_list[i].complete_state = "Finished"
				else:
					Project_list[i].complete_state = "WIP"

		with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "w") as new:
			for i in range(0, len(Project_list), 1):
				new.write("".join(str(Project_list[i].Project_name)))
				new.write("|")
				new.write("".join(str(Project_list[i].complete_state)))
				new.write("\n")
		new.close()

	### Note: Only Transfer to Complete list need to check due time (for extra step) before add to listbox/ list
	# Transfer job from Doing list to Complete list
	def transfer_doing_Complete():
		late_submitted_2 = False

		## Get current time
		cr_day = time.strftime("%d")
		cr_month = time.strftime("%m")
		cr_year = time.strftime("%Y")
		cr_hour_24 = time.strftime("%H")
		cr_minute = time.strftime("%M")

		global job_total, progress_value, submitted_late
		## Store temp value ##
		temp_val_2 = ""
		id_get = 0

		for i in Doing_Listbox.curselection():
			temp_val_2 = Doing_Listbox.get(i)

		for i in range(0, len(Doing_list), 1):
			if Doing_list[i].title == temp_val_2.strip():
				id_get = i
				break

		# If job has due time, then store date value into temp variable
		if Doing_list[id_get].DueBool == "False":
			pass
		else:
			day_split = (Doing_list[id_get].DueDay).split("/")

		## Check if complete job in/ on time
		if Doing_list[id_get].DueBool == "False":
			Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")
		else:
			if int(day_split[2]) > int(cr_year):
				Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

			elif int(day_split[2]) == int(cr_year):
				if int(day_split[1]) > int(cr_month):
					Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

				elif int(day_split[1]) == int(cr_month):
					if int(day_split[0]) > int(cr_day):						
						Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

					elif int(day_split[0]) == int(cr_day):
						if int(Doing_list[id_get].DueHour) > int(cr_hour_24):
							Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

						elif int(Doing_list[id_get].DueHour) == int(cr_hour_24):
							if int(Doing_list[id_get].DueMinute) > int(cr_minute):
								Status_job.config(text = "Status: Congrats! You completed your task just in time.", fg = "#55aaff")

							else:
								late_submitted_2 = True
								Status_job.config(text = "Status: Sorry you're late. (--> minute)", fg = "#ed1e45")

						else:
							late_submitted_2 = True
							Status_job.config(text = "Status: Sorry you're late. (--> hour)", fg = "#ed1e45")

					else:
						late_submitted_2 = True
						Status_job.config(text = "Status: Sorry you're late. (--> day)", fg = "#ed1e45")

				else:
					late_submitted_2 = True
					Status_job.config(text = "Status: Sorry you're late. (--> month)", fg = "#ed1e45")

			else:
				late_submitted_2 = True
				Status_job.config(text = "Status: Sorry you're late. (--> year)", fg = "#ed1e45")

		transfer_job_to_(Doing_Listbox, Doing_list, Comp_List, Complete_List, Alert_label_doing, Alert_label_complete, Title[1], Title[2])

		if late_submitted_2 == True:
			if len(submitted_late) == 0:
				submitted_late.append(temp_val_2.strip())
			else:
				if search(submitted_late, temp_val_2.strip()) == False:
					submitted_late.append(temp_val_2.strip())

		elif late_submitted_2 == False:
			if search(submitted_late, temp_val_2.strip()) == True:
				submitted_late.remove(temp_val_2.strip())

		if len(submitted_late) != 0:
			for i in range(0, len(Complete_List), 1):
				for j in range(0, len(submitted_late), 1):
					if Complete_List[i].title == submitted_late[j]:
						Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")

		with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as submit_late:
			for i in range(0, len(submitted_late), 1):
				submit_late.write("".join(str(submitted_late[i])))
				submit_late.write("\n")
		submit_late.close()

		# Check progress value
		if job_total != 0:
			progress_value = int((len(Complete_List))/(int(job_total))*100)
		else:
			progress_value = 0

		if progress_value >= 100:
			create_initial_file("Finished", 100, job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("Completed", "Finished")
		else:
			create_initial_file("WIP", int(progress_value), job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("WIP", "Unfinished")

		Team_Project_name.config(text = "%s%s" %(progress_value, percent))
		Progress_display_value.config(text = "%s%s" %(progress_value, percent))

	# Transfer job back from Doing list to To Do List
	def transfer_doing_toDo():
		transfer_job_to_(Doing_Listbox, Doing_list, Todo_List, Job_list, Alert_label_doing, Alert_label, Title[1], Title[0])

		Status_job.config(text = "")

	# Transfer job back from Complete to Doing list
	def transfer_complete_doing():
		transfer_job_to_(Comp_List, Complete_List, Doing_Listbox, Doing_list, Alert_label_complete, Alert_label_doing, Title[2], Title[1])

		# Check progress value
		if job_total != 0:
			progress_value = int((len(Complete_List))/(int(job_total))*100)
		else:
			progress_value = 0

		if progress_value >= 100:
			create_initial_file("Finished", 100, job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("Completed", "Finished")
		else:
			create_initial_file("WIP", int(progress_value), job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("WIP", "Unfinished")

		Team_Project_name.config(text = "%s%s" %(progress_value, percent))
		Progress_display_value.config(text = "%s%s" %(progress_value, percent))

		Status_job.config(text = "")

	# Transfer job back from Complete list to To Do List
	def transfer_complete_todo():
		transfer_job_to_(Comp_List, Complete_List, Todo_List, Job_list, Alert_label_complete, Alert_label, Title[2], Title[0])

		# Check progress value
		if job_total != 0:
			progress_value = int((len(Complete_List))/(int(job_total))*100)
		else:
			progress_value = 0

		if progress_value >= 100:
			create_initial_file("Finished", 100, job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("Completed", "Finished")
		else:
			create_initial_file("WIP", int(progress_value), job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("WIP", "Unfinished")

		Team_Project_name.config(text = "%s%s" %(progress_value, percent))
		Progress_display_value.config(text = "%s%s" %(progress_value, percent))

		Status_job.config(text = "")

	## Transfer job from To Do list to Doing list
	def transfer_Do_Doing():
		transfer_job_to_(Todo_List, Job_list, Doing_Listbox, Doing_list, Alert_label, Alert_label_doing, Title[0], Title[1])

		Status_job.config(text = "")

	## Transfer job from To Do list to Complete list
	def transfer_Do_complete():
		late_submitted = False

		# Get current time
		cr_day_2 = time.strftime("%d")
		cr_month_2 = time.strftime("%m")
		cr_year_2 = time.strftime("%Y")
		cr_hour_24f = time.strftime("%H")
		cr_minute_2 = time.strftime("%M")

		global job_total, progress_value, submitted_late
		## Store temp value ##
		temp_val = ""
		id_locate = 0

		for i in Todo_List.curselection():
			temp_val = Todo_List.get(i)

		for i in range(0, len(Job_list), 1):
			if Job_list[i].title == temp_val.strip():
				id_locate = i
				break

		# If job has due time, then store date value into temp variable
		if Job_list[id_locate].DueBool == "False":
			pass
		else:
			day_split = (Job_list[id_locate].DueDay).split("/")

		## Check if complete job in/ on time
		if Job_list[id_locate].DueBool == "False":
			Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")
		else:
			if int(day_split[2]) > int(cr_year_2):
				Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

			elif int(day_split[2]) == int(cr_year_2):
				if int(day_split[1]) > int(cr_month_2):
					Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

				elif int(day_split[1]) == int(cr_month_2):
					if int(day_split[0]) > int(cr_day_2):
						Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

					elif int(day_split[0]) == int(cr_day_2):
						if int(Job_list[id_locate].DueHour) > int(cr_hour_24f):
							Status_job.config(text = "Status: Task completed on time.", fg = "#55aaff")

						elif int(Job_list[id_locate].DueHour) == int(cr_hour_24f):
							if int(Job_list[id_locate].DueMinute) > int(cr_minute_2):
								Status_job.config(text = "Status: Congrats! You completed your task just in time.", fg = "#55aaff")

							else:
								late_submitted = True								
								Status_job.config(text = "Status: Sorry you're late. (--> minute)", fg = "#ed1e45")

						else:
							late_submitted = True							
							Status_job.config(text = "Status: Sorry you're late. (--> hour)", fg = "#ed1e45")

					else:
						late_submitted = True						
						Status_job.config(text = "Status: Sorry you're late. (--> day)", fg = "#ed1e45")

				else:
					late_submitted = True
					Status_job.config(text = "Status: Sorry you're late. (--> month)", fg = "#ed1e45")

			else:
				late_submitted = True			
				Status_job.config(text = "Status: Sorry you're late. (--> year)", fg = "#ed1e45")
		
		transfer_job_to_(Todo_List, Job_list, Comp_List, Complete_List, Alert_label, Alert_label_complete, Title[0], Title[2])

		if late_submitted == True:
			if len(submitted_late) == 0:
				submitted_late.append(temp_val.strip())
			else:
				if search(submitted_late, temp_val.strip()) == False:
					submitted_late.append(temp_val.strip())

		elif late_submitted == False:
			if search(submitted_late, temp_val.strip()) == True:
				submitted_late.remove(temp_val.strip())

		if len(submitted_late) != 0:
			for i in range(0, len(Complete_List), 1):
				for j in range(0, len(submitted_late), 1):
					if Complete_List[i].title == submitted_late[j]:
						Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")

		### Write submitted late list to file ###
		with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as submit_late:
			for i in range(0, len(submitted_late), 1):
				submit_late.write("".join(str(submitted_late[i])))
				submit_late.write("\n")
		submit_late.close()

		if job_total != 0:
			progress_value = int((len(Complete_List))/(int(job_total))*100)
		else:
			progress_value = 0

		if progress_value >= 100:
			create_initial_file("Finished", 100, job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("Completed", "Finished")
		else:
			create_initial_file("WIP", int(progress_value), job_total)
			rewrite_project_list(empty_String, progress_value)
			save_project_list_diary("WIP", "Unfinished")

		### Project progress ###
		Team_Project_name.config(text = "%s%s" %(progress_value, percent))
		Progress_display_value.config(text = "%s%s" %(progress_value, percent))

	def transfer_job_to_(Todo_List, Job_list, Doing_Listbox, Doing_list, Alert_label, Alert_label_doing, Doing_stt_A, Doing_stt_B):
		# Doing_list not Doing List
		# Get id value selected from To Do Listbox
		value_get = ""

		for i in Todo_List.curselection():
			value_get = Todo_List.get(i)
			Todo_List.delete(i)

		for i in range(0, len(Job_list), 1):
			if Job_list[i].title == value_get.strip():
				Doing_list.append(Job_list[i])
				Job_list.remove(Job_list[i])
				break

		# Adjust height of "B" listbox
		if Doing_Listbox.cget('height') >= 14:
			Doing_Listbox.delete(0, END)
			Doing_Listbox.config(height = 14)
			for index in range(0, len(Doing_list), 1):
				Doing_Listbox.insert(END, "  %s" %Doing_list[index].title)
			Alert_label_doing.place(x = 36, y = 510)
		else:
			Doing_Listbox.delete(0, END)
			Doing_Listbox.config(height = len(Doing_list))
			for index in range(0, len(Doing_list), 1):
				Doing_Listbox.insert(END, "  %s" %Doing_list[index].title)

		# Adjust height of "A" listbox
		if len(Job_list) == 0:
			# Adjust display To Do List Value
			global TodoList_Bool
			TodoList_Bool = False

			# Hide To Do List
			Todo_List.config(height = len(Job_list))
			# ToDo_Frame_List.place_forget()
			Alert_label.place_forget()
		elif len(Job_list) > 14:
			# Adjust Height of To Do List
			Alert_label.place(x = 36, y = 510)
			Todo_List.config(height = 14)

		elif len(Job_list) == 14:
			Alert_label.place_forget()
			Todo_List.config(height = len(Job_list))

		else:
			Alert_label.place_forget()
			Todo_List.config(height = len(Job_list))

		# Rewrite value back to "A" list
		with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Doing_stt_A), "w") as renew_file:
			for i in range(0, len(Job_list), 1):
				renew_file.write(''.join(str(Job_list[i].title)))
				renew_file.write('|')
				renew_file.write(''.join(str(Job_list[i].description)))
				renew_file.write('|')
				renew_file.write(''.join(str(Job_list[i].DueBool)))
				renew_file.write('|')
				renew_file.write(''.join(str(Job_list[i].DueDay)))
				renew_file.write('|')
				renew_file.write(''.join(str(Job_list[i].DueHour)))
				renew_file.write('|')
				renew_file.write(''.join(str(Job_list[i].DueMinute)))
				renew_file.write('|')
				renew_file.write(''.join(str(Job_list[i].Limit_Time)))
				renew_file.write('|')
				renew_file.write(''.join(str(Job_list[i].importance)))
				renew_file.write('\n')
		renew_file.close()

		# Rewrite value back to "B" list
		with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Doing_stt_B), "w") as create_new:
			for i in range(0, len(Doing_list), 1):
				create_new.write(''.join(str(Doing_list[i].title)))
				create_new.write('|')
				create_new.write(''.join(str(Doing_list[i].description)))
				create_new.write('|')
				create_new.write(''.join(str(Doing_list[i].DueBool)))
				create_new.write('|')
				create_new.write(''.join(str(Doing_list[i].DueDay)))
				create_new.write('|')
				create_new.write(''.join(str(Doing_list[i].DueHour)))
				create_new.write('|')
				create_new.write(''.join(str(Doing_list[i].DueMinute)))
				create_new.write('|')
				create_new.write(''.join(str(Doing_list[i].Limit_Time)))
				create_new.write('|')
				create_new.write(''.join(str(Doing_list[i].importance)))
				create_new.write('\n')
		create_new.close()

	def OpenNewProject():
		def search_project_(event):
			key_typed = event.widget.get()

			if key_typed == "":
				Project_listbox_display.delete(0, END)

				for i in range(0, len(temp_list_display), 1):
					Project_listbox_display.insert(END, "  %s" %temp_list_display[i].Project_name)

			else:
				Project_listbox_display.delete(0, END)

				for i in range(0, len(temp_list_display), 1):
					if key_typed in (temp_list_display[i].Project_name).lower():
						Project_listbox_display.insert(END, "  %s" %temp_list_display[i].Project_name)

		def show_info_display(event):
			item_selected = ""
			list_display = []

			for i in Project_listbox_display.curselection():
				item_selected = (Project_listbox_display.get(i)).strip()

			with open("Project/%s/%s/%s.txt" %(tag_number_int, item_selected, item_selected), "r") as display_info:
				reader = csv.reader(display_info, delimiter = "|")
				for row in reader:
					list_display.append(Project_open_info(row[0], row[1], row[2], row[3]))
			display_info.close()

			### Display title project selected ###
			Title_entry_display.config(state = NORMAL)
			Title_entry_display.delete(0, END)
			Title_entry_display.insert(END, list_display[0].name_project)
			Title_entry_display.config(state = "readonly")

			### Display current state project selected ###
			if list_display[0].state == "WIP":
				state_current.config(text = "Work in progress...")
			else:
				state_current.config(text = list_display[0].state)

			### Display current project progress ###
			progress_display.config(text = "%s%s" %(list_display[0].progress_state, percent))

			### Display total jobs that selected project has ###
			total_jobs_display.config(text = list_display[0].total_job)

		def openProject():
			### clear all list ###
			Job_list.clear()
			Doing_list.clear()
			Complete_List.clear()
			submitted_late.clear()
			note_list.clear()

			### Clear all listbox ###
			Todo_List.delete(0, END)
			Doing_Listbox.delete(0, END)
			Comp_List.delete(0, END)
			note_listbox.delete(0, END)

			### hide all alert label ###
			Alert_label.place_forget()
			Alert_label_doing.place_forget()
			Alert_label_complete.place_forget()

			### Reset alert text ###
			Status_job.config(text = "")

			### Reset other widget just in case ###
			## Hide and adjust widget in right side tab - create note tab ##
			Entry_issues.delete(0, END)
			Entry_issues.place_forget()
			Create_note_button.place(x = 40, y = 120)
			Home_Custombttn_active.place(x = 192)
			Search_Custombttn_active.place_forget()

			### Add new project back to list ###
			open_project(Project_listbox_display)

			### Remove value in search entry if it has any value in it ###
			Entry_search_display.delete(0, END)

			### close current window ###
			open_window.destroy()

		def sort_project():
			global flag_sort

			flag_sort == False

			if flag_sort == False:
				MergeSort_projectName(temp_list_display)
				flag_sort = True
			else:
				MergeSort__desc_projectName(temp_list_display)
				flag_sort = False

			Project_listbox_display.delete(0, END)

			for i in range(0, len(temp_list_display), 1):
				Project_listbox_display.insert(END, "  %s" %temp_list_display[i].Project_name)

		open_window = Toplevel()
		open_window.wm_attributes("-topmost", 1)
		open_window.geometry(f"870x600+{open_window.winfo_screenwidth()//2 - 870//2}+{open_window.winfo_screenheight()//2 - 600//2}")
		open_window.title("Open new project")
		open_window.resizable(0, 0)
		open_window.config(bg = "#1e222a")

		Open_label = Label(open_window, text = "Open new project", font = ("Consolas", 40, "bold"), bg = "#1e222a", fg = "#55aaff")
		Open_label.place(x = 15, y = 15)

		total_project_label = Label(open_window, font = ("Consolas", 12), bg = "#1e222a", fg = "#55aaff")
		total_project_label.place(x = 15, y = 115)

		Project_listbox_display = Listbox(open_window,
										font = ("Consolas", 20),
										width = 30, height = 10,
										bg = "#383e4d", fg = "#FFFFFF",
										bd = 0,
										activestyle = "none",
										exportselection = False)
		Project_listbox_display.place(x = 15, y = 150)
		Project_listbox_display.bind("<<ListboxSelect>>", show_info_display)

		### temp project list store to display on screen ###
		temp_list_display = []

		with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "r") as read_list:
			reader = csv.reader(read_list, delimiter = "|")
			for row in reader:
				temp_list_display.append(Project_info(row[0], row[1]))


		### add project to listbox ###
		for i in range(0, len(temp_list_display), 1):
			Project_listbox_display.insert(END, "  %s" %temp_list_display[i].Project_name)

		if Project_listbox_display.size() <=1 :
			total_project_label.config(text = "You have %s project in total" %Project_listbox_display.size())
		else:
			total_project_label.config(text = "You have %s projects in total" %Project_listbox_display.size())

		#### GUI ####
		Entry_search_display = Entry(open_window, font = ("Consolas", 20), width = 20)
		Entry_search_display.place(x = 500, y = 160)
		Entry_search_display.bind("<KeyRelease>", search_project_)

		search_display = Label(open_window, text = "Search:", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
		search_display.place(x = 500, y = 120)

		line_ = Label(open_window, text = "__________________________________", font = ("Consolas"), fg = "#FFFFFF", bg = "#1e222a")
		line_.place(x = 500, y = 210)

		Detail_title = Label(open_window, text = "Detail project", font = ("Consolas", 15), fg = "#FFFFFF", bg = "#1e222a")
		Detail_title.place(x = 575, y = 215)

		### Button ###
		Open_bttn = Button(open_window, text = "  Open  ", font = ("Consolas", 20), bg = "#2a5bba", fg = "#FFFFFF", command = openProject)
		Open_bttn.place(x = 15, y = 505)

		sort_button = Button(open_window, text = "  Sort  ", font = ("Consolas", 20), bg = "#ed1e45", fg = "#FFFFFF", command = sort_project)
		sort_button.place(x = 180, y = 505)

		### GUI ###

		Title_project = Label(open_window, text = "Title:", font = ("Consolas", 15), bg = "#1e222a", fg = "#55aaff")
		Title_project.place(x = 500, y = 280)

		Title_entry_display = Entry(open_window, font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF", readonlybackground = "#1e222a", bd = 0, state = "readonly")
		Title_entry_display.place(x = 575, y = 282)

		line_sep_1 = Label(open_window, text = "___________________________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
		line_sep_1.place(x = 500, y = 310)

		State_cr_label = Label(open_window, text = "State:", font = ("Consolas", 15), bg = "#1e222a", fg = "#55aaff")
		State_cr_label.place(x = 500, y = 350)

		state_current = Label(open_window, font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
		state_current.place(x = 575, y = 350)

		line_sep_2 = Label(open_window, text = "___________________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
		line_sep_2.place(x = 500, y = 378)

		progress_label = Label(open_window, text = "Progress:", font = ("Consolas", 15), bg = "#1e222a", fg = "#55aaff")
		progress_label.place(x = 500, y = 418)

		progress_display = Label(open_window, font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
		progress_display.place(x = 610, y = 418)

		line_sep_3 = Label(open_window, text = "_________________________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
		line_sep_3.place(x = 500, y = 446)

		Job_total_label = Label(open_window, text = "Total jobs:", font = ("Consolas", 15), bg = "#1e222a", fg = "#55aaff")
		Job_total_label.place(x = 500, y = 486)

		total_jobs_display = Label(open_window, font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
		total_jobs_display.place(x = 635, y = 486)

		line_sep_4 = Label(open_window, text = "______________________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
		line_sep_4.place(x = 500, y = 512)

	def save_file(doing_status):
		global empty_String

		with open("Project/%s/%s/%s" % (tag_number_int, empty_String, doing_status), 'w') as f:
			i = 0
			for i in range(len(Job_list)):
				f.write(''.join(str(Job_list[i].title)))
				f.write('|')
				f.write(''.join(str(Job_list[i].description)))
				f.write('|')
				f.write(''.join(str(Job_list[i].DueBool)))
				f.write('|')
				f.write(''.join(str(Job_list[i].DueDay)))
				f.write('|')
				f.write(''.join(str(Job_list[i].DueHour)))
				f.write('|')
				f.write(''.join(str(Job_list[i].DueMinute)))
				f.write('|')
				f.write(''.join(str(Job_list[i].Limit_Time)))
				f.write('|')
				f.write(''.join(str(Job_list[i].importance)))
				f.write('\n')
		f.close()

	# Add Job
	def Add_Job_name():
		DiagLog_Projet = Toplevel()

		Window_width = 340
		Window_height = 460

		position_x = (monitor_width//2) - (Window_width//2)
		position_y = (monitor_height//2) - (Window_height//2)

		DiagLog_Projet.geometry(f"{Window_width}x{Window_height}+{position_x}+{position_y}")
		DiagLog_Projet.resizable(0, 0)
		DiagLog_Projet.config(bg = "#262a34")
		# DiagLog_Projet.wm_attributes('-topmost', 1)
		DiagLog_Projet.title("Add New Project")

		### alert Label ###
		alert_lbl = Label(DiagLog_Projet, font = ("Consolas", 15), bg = "#262a34", fg = "#ed1e45")
		alert_lbl.place(x = 20, y = 388)

		## Expand window
		def check_Due_Time(event):
			if Due_Setting.get() == "On":
				Importance_Box.place_forget()
				Time_limit_box.place_forget()

				Due_Day_importance.config(text = "Day:")
				Due_Day_importance.place(x = 10, y = 300)

				Due_Time_Limit.config(text = "Time:")
				Due_Time_Limit.place(x = 10, y = 340)
				
				Date_Picker.place(x = 60, y = 300)
				
				Hour_Time.place(x = 70, y = 340)
				Colon_Label.place(x = 115, y = 340)
				Minute_Time.place(x = 130, y = 340)

			else:
				Due_Day_importance.config(text = "Importance:")
				Due_Day_importance.place(x = 10, y = 340)

				Due_Time_Limit.config(text = "Time Limit:")
				Due_Time_Limit.place(x = 10, y = 300)

				Importance_Box.place(x = 140, y = 340)
				Time_limit_box.place(x = 140, y = 300)
		
				Date_Picker.place_forget()
				Hour_Time.place_forget()
				Colon_Label.place_forget()
				Minute_Time.place_forget()

		### Create_job ###
		def create_job():
			global job_total, progress_value

			Add_Job()

			# Create job total
			job_total = job_total + 1

			## Double check progress value
			if job_total != 0:
				progress_value = int((len(Complete_List))/(int(job_total))*100)
			else:
				progress_value = 0

			if progress_value >= 100:
				create_initial_file("Finished", 100, job_total)
				rewrite_project_list(empty_String, progress_value)
				save_project_list_diary("Completed", "Finished")
			else:
				create_initial_file("WIP", int(progress_value), job_total)
				rewrite_project_list(empty_String, progress_value)
				save_project_list_diary("WIP", "Unfinished")
				
			Progress_display_value.config(text = "%s%s" %(progress_value, percent))
			Team_Project_name.config(text = "%s%s" %(progress_value, percent))
			# Rewrite/ create initial file
			# create_initial_file("Unfinished", progress_value, job_total)

			Status_job.config(text = "")

			save_file(Title[0])
			DiagLog_Projet.destroy()
			DiagLog_Projet.update()

		# Create New Project
		def Create_New_Job(event):
			# Get current time
			current_day = time.strftime("%d")
			current_month = time.strftime("%m")
			current_year = time.strftime("%Y")
			current_hour_24 = time.strftime("%H")
			current_minute = time.strftime("%M")

			entry_title_get = (Entry_Job.get()).strip()
			entry_description_get = (Entry_Description.get('1.0', 'end-1c')).strip()

			Createbutton.config(image = CreatePress_bttn, bg = "#1544a0")
			if entry_title_get != "":
				if entry_description_get != "":
					Job_list_in = False
					Doing_list_in = False
					Complete_List_in = False

					next_step = False

					for i in range(0, len(Job_list), 1):
						if Entry_Job.get() == Job_list[i].title:
							Job_list_in = True
							break

					if Job_list_in == True:
						pass
					else:
						for i in range(0, len(Doing_list), 1):
							if Entry_Job.get() == Doing_list[i].title:
								Doing_list_in = True
								break

					if Doing_list_in == True:
						pass
					else:
						for i in range(0, len(Complete_List), 1):
							if Entry_Job.get() == Complete_List[i].title:
								Complete_List_in = True
								break

					if Job_list_in == False and Doing_list_in == False and Complete_List_in == False:
						next_step = True

					if next_step == True:						
						if Due_Setting.get() == "On":
							### get date sign up ###
							date_sign = Date_Time.get()
							date_split = date_sign.split("/")

							if int(date_split[2]) > int(current_year):
								create_job()

							elif int(date_split[2]) == int(current_year):
								if int(date_split[1]) > int(current_month):
									create_job()

								elif int(date_split[1]) == int(current_month):
									if int(date_split[0]) > int(current_day):
										create_job()

									elif int(date_split[0]) == int(current_day):
										if int(Hour_Time.get()) > int(current_hour_24):
											create_job()

										elif int(Hour_Time.get()) == int(current_hour_24):
											if int(Minute_Time.get()) > int(current_minute):
												create_job()

											else:
												alert_lbl.config(text = "Too late (-> Hour).")
												DiagLog_Projet.geometry(f"{Window_width}x{510}")
												Createbutton.place(x = 160, y = 438)

										else:
											alert_lbl.config(text = "Too late (-> Hour).")
											DiagLog_Projet.geometry(f"{Window_width}x{510}")
											Createbutton.place(x = 160, y = 438)

									else:
										alert_lbl.config(text = "Too late (-> Day).")
										DiagLog_Projet.geometry(f"{Window_width}x{510}")
										Createbutton.place(x = 160, y = 438)

								else:
									alert_lbl.config(text = "Too late (-> Month).")
									DiagLog_Projet.geometry(f"{Window_width}x{510}")
									Createbutton.place(x = 160, y = 438)

							else:
								alert_lbl.config(text = "Too late (-> Year).")
								DiagLog_Projet.geometry(f"{Window_width}x{510}")
								Createbutton.place(x = 160, y = 438)

						else:
							create_job()

					else:
						alert_lbl.config(text = "Job already been created.")
						DiagLog_Projet.geometry(f"{Window_width}x{510}")
						Createbutton.place(x = 160, y = 438)

				else:
					DiagLog_Projet.geometry(f"{Window_width}x{510}")
					Createbutton.place(x = 160, y = 438)
					alert_lbl.config(text = "Please add job description.")

			else:
				DiagLog_Projet.geometry(f"{Window_width}x{510}")
				Createbutton.place(x = 160, y = 438)
				alert_lbl.config(text = "Please add job title.")


		# Create Button - Toplevel() Window
		Create_bttn = PhotoImage(file = "images/Personal Project Page/Toplevel/Create_Normal_icon.png")
		CreateHover_bttn = PhotoImage(file = "images/Personal Project Page/Toplevel/Create_Hover_icon.png")
		CreatePress_bttn = PhotoImage(file = "images/Personal Project Page/Toplevel/Create_Press_icon.png")

		# Create New Button
		def Createbttn_Hover(event):
			Createbutton.config(image = CreateHover_bttn, bg = "#2b313c")

		def Createbttn_NormalState(event):
			Createbutton.config(image = Create_bttn, bg = "#1e222a")

		#Add Job to List box
		def Add_Job():
			title_Job = (Entry_Job.get()).strip()
			description_Job = (Entry_Description.get('1.0', 'end-1c')).strip()

			if Todo_List.cget('height') >= 14:
				Todo_List.config(height = 14)
				Todo_List.insert(END, "  %s" %(title_Job))
				Alert_label.place(x = 36, y = 510)
			else:
				Todo_List.config(height = Todo_List.cget('height') + 1)
				Todo_List.insert(END, "  %s" %(title_Job))

			if (Due_Setting.get() == "On"):
				Job_list.append(Job_Info(title_Job, description_Job, "True", Date_Time.get(), Hour_Time.get(), Minute_Time.get()))
				Entry_Job.delete(0, 'end')
			else:
				Job_list.append(Job_Info(title_Job, description_Job, "False", "None", 0, 0, Time_limit_box.get(), Importance_Box.get()))
				Entry_Job.delete(0, 'end')

		# Job Title Entry
		Job_title = Label(DiagLog_Projet, text = "Job Name:",font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34")
		Job_title.place(x = 10, y = 10)

		Entry_Job = Entry(DiagLog_Projet, textvariable = Job_name, font = ("Consolas", 20))
		Entry_Job.delete(0, END)
		Entry_Job.place(x = 10, y = 45)

		# Job Description Entry
		Job_title = Label(DiagLog_Projet, text = "Job Description:",font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34")
		Job_title.place(x = 10, y = 110)

		Entry_Description = Text(DiagLog_Projet, width = 23, height = 3, font = ("Consolas", 18))
		Entry_Description.place(x = 10, y = 150)

		## Due Label
		Due_Label = Label(DiagLog_Projet, text = "Due Time:",font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34")
		Due_Label.place(x = 10, y = 255)

		## Due Day + Due Time
		# Due Day
		Due_Day_importance = Label(DiagLog_Projet, text = "Importance:",font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34")
		Due_Day_importance.place(x = 10, y = 340)	

		# Due Time
		Due_Time_Limit = Label(DiagLog_Projet, text = "Time Limit:",font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34")
		Due_Time_Limit.place(x = 10, y = 300)

		## Priority Box
		Importance_Box = Spinbox(DiagLog_Projet, from_ = 1, to = 9, font = ("Consolas", 15), width = 2, state = "readonly")
		Importance_Box.place(x = 140, y = 340)

		## Spinbox Time Limit
		Time_limit_box = Spinbox(DiagLog_Projet, from_ = 1, to = 23, font = ("Consolas", 15), width = 2, state = "readonly")
		Time_limit_box.place(x = 140, y = 300)

		## Button
		Createbutton = Button(DiagLog_Projet, image = Create_bttn, borderwidth = 1, bg = "#2b313c")
		Createbutton.place(x = 160, y = 388)
		Createbutton.bind("<Enter>", Createbttn_Hover)
		Createbutton.bind("<Leave>", Createbttn_NormalState)
		Createbutton.bind("<ButtonRelease-1>", Create_New_Job)
		DiagLog_Projet.bind("<Return>", Create_New_Job)

		# Due Setting
		Sign = StringVar()
		Sign.set(Sign_list[0])

		Due_Setting = ttk.Combobox(DiagLog_Projet, value = Sign_list, font = ("Consolas", 15), width = 5, state = "readonly")
		Due_Setting.current(0)
		Due_Setting.bind("<<ComboboxSelected>>", check_Due_Time)
		Due_Setting.place(x = 120, y = 255)

		## Due Time
		Hour_Time = Spinbox(DiagLog_Projet, from_ = 00, to = 23, font = ("Consolas", 15), width = 2, state = "readonly", format = "%02.0f")

		Colon_Label = Label(DiagLog_Projet, text = ":", font = ("Consolas", 15, "bold"), bg = "#262a34", fg = "#FFFFFF")

		Minute_Time = Spinbox(DiagLog_Projet, from_ = 00, to = 59, font = ("Consolas", 15), width = 2, state = "readonly", format = "%02.0f")

		## Calendar Picker
		# Date Display
		Date_Picker = CustomDateEntry(DiagLog_Projet,
			selectbackground='gray80',
	        selectforeground='black',
			normalbackground='white',
			normalforeground='black',
	        background='gray90',
	        foreground='black',
	        bordercolor='gray90',
	        othermonthforeground='gray50',
	        othermonthbackground='white',
	        othermonthweforeground='gray50',
	        othermonthwebackground='white',
	        headersbackground='white',
	        headersforeground='gray70',
	        date_pattern = "dd/mm/yyyy",
	        font = ("Consolas", 13),
	        textvariable = Date_Time,
	        selectmode = "day",
	        state = "readonly")

	#-----------------------------------------------------------------#
	# Toplevel in Personal Page - Before starting project
	def Add_Project_name():
		global Temp_list

		Temp_list.clear()
		check_dir()
		DiagLog_Projet = Toplevel()

		Window_height = 100
		Window_width = 480

		position_x = (monitor_width//2) - (Window_width//2)
		position_y = (monitor_height//2) - (Window_height//2)

		DiagLog_Projet.geometry(f"{Window_width}x{Window_height}+{position_x}+{position_y}")
		DiagLog_Projet.resizable(0, 0)
		DiagLog_Projet.config(bg = "#262a34")
		# DiagLog_Projet.wm_attributes('-topmost', 1)
		DiagLog_Projet.title("Add New Project")

		# Create New Project
		def Create_New_Project():
			if (Entry_Name.get()).strip() != '':
				keyword = (Entry_Name.get()).strip()

				if keyword in Temp_list:
					DiagLog_Projet.geometry("480x140")
					alert_deny.config(text = "Project already been created.")			

				elif search_keyword(invalid_keyword, keyword) == True:
					DiagLog_Projet.geometry("480x140")
					alert_deny.config(text = 'Avoid \\/:*?"<>|. when naming your project.')			
				
				else:
					global stayValue, empty_String, job_total, progress_value
					stayValue = True
					## Label Project
					
					### Adjust new value ###
					empty_String = keyword
					CR_Project_Name.config(text = keyword)

					# Home Page
					Personal_Project_name.config(text = keyword)
					Team_Project_name.config(text = "0%s" %percent)
					Progress_display_value.config(text = "0%s" %percent)

					Entry_Name.delete(0, "end")

					### Clear all list ###
					Job_list.clear()
					Doing_list.clear()
					Complete_List.clear()
					submitted_late.clear()
					note_list.clear()

					#### Clear all listbox ####
					Todo_List.delete(0, END)
					Doing_Listbox.delete(0, END)
					Comp_List.delete(0, END)
					note_listbox.delete(0, END)

					job_total = 0
					progress_value = 0

					### Adjust height of listbox ###
					Todo_List.config(height = 0)
					Doing_Listbox.config(height = 0)
					Comp_List.config(height = 0)

					Alert_label.place_forget()
					Alert_label_doing.place_forget()
					Alert_label_complete.place_forget()

					## Hide and adjust widget in right side tab - create note tab ##
					Entry_issues.delete(0, END)
					Entry_issues.place_forget()
					Create_note_button.place(x = 40, y = 120)
					Home_Custombttn_active.place(x = 192)
					Search_Custombttn_active.place_forget()

					total_note.config(text = "You have %s note in total" %len(note_list))

					if not os.path.exists("Project/%s/%s" %(tag_number_int, empty_String)):
						os.makedirs("Project/%s/%s" %(tag_number_int, empty_String))
					else:
						pass

					create_initial_file("Unfinished", 0, job_total)
					save_project_list("Unfinished")
					save_project_list_diary("Created", "Unfinished")

					DiagLog_Projet.destroy()
					DiagLog_Projet.update()
			else:
				DiagLog_Projet.geometry("480x140")
				alert_deny.config(text = "Please choose your project name.")

		def create_new(event):
			Create_New_Project()

		# Create Button - Toplevel() Window
		Create_bttn = PhotoImage(file = "images/Personal Project Page/Toplevel/Create_Normal_icon.png")
		CreateHover_bttn = PhotoImage(file = "images/Personal Project Page/Toplevel/Create_Hover_icon.png")
		CreatePress_bttn = PhotoImage(file = "images/Personal Project Page/Toplevel/Create_Press_icon.png")

		# Create New Button
		Createbutton = CustomButton(DiagLog_Projet,
									Create_bttn,
									CreateHover_bttn,
									CreatePress_bttn,
									"#1e222a", "#2b313c", "#1544a0",
									320, 38, 1, Create_New_Project)

		Project_title = Label(DiagLog_Projet, text = "Project Name:",font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34")
		Project_title.place(x = 10, y = 10)

		Entry_Name = Entry(DiagLog_Projet, font = ("Consolas", 20))
		Entry_Name.place(x = 10, y = 45)
		Entry_Name.delete(0, END)
		DiagLog_Projet.bind("<Return>", create_new)

		alert_deny = Label(DiagLog_Projet, font = ("Consolas", 14, "bold"), bg = "#262a34", fg = "#ed1e45")
		alert_deny.place(x = 10, y = 95)

	### Function in create project frame ###
	# Create new Project
	def Create_Project():
		## Clear list before add to list ##
		global Temp_list, ProjectName_short
		Temp_list.clear()
		# check file before add project to list
		check_dir()
		# print(Temp_list)



		valid_name = False
		if (Entry_project.get()).strip() == '':
			alert_.config(text = "Please choose your project name.")

		elif (Entry_project.get()).strip() in Temp_list:
			alert_.config(text = "Your project already been created.")

		elif (Entry_project.get()).strip() != '':
			if search_keyword(invalid_keyword, Entry_project.get()) == True:
				valid_name = False
				alert_.config(text = 'Avoid \\/:*?"<>|. when naming your project.')
			else:
				valid_name = True

		if valid_name == False:
			pass
		else:
			# print(Temp_list)
			global stayValue, empty_String
			stayValue = True
			First_Frame_Personal.pack_forget()
			Second_Frame_Personal.pack(fill = "both", expand = 1)

			## Label Project
			# Personal Page
			empty_String = (Entry_project.get()).strip()

			if len(empty_String) > 10:
				ProjectName_short = empty_String[:10] + ".."
			else:
				ProjectName_short = empty_String

			CR_Project_Name.config(text = ProjectName_short)

			# Home Page
			Personal_Project_name.config(text = ProjectName_short)
			Entry_project.delete(0, "end")

			if not os.path.exists("Project/%s/%s" %(tag_number_int, empty_String)):
				os.makedirs("Project/%s/%s" %(tag_number_int, empty_String))
			else:
				pass

			create_initial_file("Unfinished", 0, job_total)
			save_project_list("Unfinished")
			save_project_list_diary("Created", "Unfinished")

	## Open new frame ##
	def Open_project_():
		search_project.delete(0, END)

		Project_listbox.config(height = 10)
		Project_listbox.place(x = 60, y = 170)

		search_project.place_forget()
		search_lbl.place_forget()

		Title_open.place(x = 80, y = 80)

		Home_button_icon.config(image = home_icon_press, bg = "#2b313c")
		Home_button_icon.photo = home_icon_press

		Search_bttn.config(image = search_image, bg = "#2a5bba", bd = 1)
		Search_bttn.photo = search_image

		Edit_button_open.config(image = edit_image, bg = "#ed1e45", bd = 1)
		Edit_button_open.photo = edit_image

		open_button_project.config(text = "  Open  ", bg = "#2a5bba", fg = "#FFFFFF")
		open_button_project.place(x = 377, y = 501)

		## Clear listbox any value in label and entry has value on sceen ##
		Project_listbox.delete(0, END)

		Project_name_display.config(state = NORMAL)
		Project_name_display.delete(0, 'end')
		Project_name_display.config(state = "readonly")

		Current_percent.config(text = "")
		Current_state_.config(text = "")
		Total_jobs_int.config(text = "")

		Status_job.config(text = "")

		check_dir()
		## temporary list ##
		temp_list_ = []

		Open_Button_active.place(x = 25, y = 330)
		
		introduce_frame.place_forget()
		create_Project_Frame.place(x = 0, y = 0)
		CreateNew_button_active.place_forget()

		with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "r") as open_file:
			reader = csv.reader(open_file, delimiter = "|")
			for row in reader:
				temp_list_.append(Project_info(row[0], row[1]))
		open_file.close()

		if len(temp_list_) == 0:
			No_project_found.place(x = 0)
			Open_project_frame.place_forget()
		else:
			Open_project_frame.place(x = 0)
			No_project_found.place_forget()

		if len(temp_list_) <= 1:
			total_project.config(text = "You have %s project in total" %(len(temp_list_)))
		else:
			total_project.config(text = "You have %s projects in total" %(len(temp_list_)))

		# Append to listbox
		for i in range(0, len(temp_list_), 1):
			Project_listbox.insert(END, "  %s" %temp_list_[i].Project_name)

	## Create new Frame ##
	def create_new_Frame():
		Entry_project.delete(0, 'end')
		alert_.config(text = "")

		CreateNew_button_active.place(x = 25, y = 260)
		introduce_frame.place_forget()
		create_Project_Frame.place(x = 0, y = 0)
		No_project_found.place_forget()
		Open_Button_active.place_forget()
		Open_project_frame.place_forget()

	### Return to default page ###
	def return_page():
		CreateNew_button_active.place_forget()
		introduce_frame.place(x = 0, y = 0)
		create_Project_Frame.place_forget()
		No_project_found.place_forget()
		Open_Button_active.place_forget()
		Open_project_frame.place_forget()

	#-----------------------------------------------------------------#
	### Left Side Menu Size
	## Contract Window
	def contract_window():
		size = leftside_frame.cget('width')
		if (size <= 250 and size > 65):
			size -= 5
			leftside_frame.config(width = size)
			leftside_frame.after(4, contract_window)

	## Expand Window
	def expand_window():
		size = leftside_frame.cget('width')
		if (size < 250):
			size += 5
			leftside_frame.config(width = size)
			leftside_frame.after(3, expand_window)

	## Check before expand/ contract window
	def expand_window_check():
		if (int(leftside_frame.cget("width")) == 65):
			expand_window()
		else:
			contract_window()

	#-----------------------------------------------------------------#
	# Home Button
	def pressHome():
		Home_Button_active.place(x = 0, y = 18)
		Personal_Button_active.place_forget()
		bg_Frame_Home.pack(fill = "both", expand = 1)
		First_Frame_Personal.pack_forget()
		Second_Frame_Personal.pack_forget()

	# Personal Button
	def pressPersonal():
		Home_Button_active.place_forget()
		Personal_Button_active.place(x = 0, y = 78)
		bg_Frame_Home.pack_forget()
		if not stayValue:
			First_Frame_Personal.pack(fill = "both", expand = 1)
		else:
			Second_Frame_Personal.pack(fill = "both", expand = 1)

	#-----------------------------------------------------------------#
	#### UI TKINTER ####
	### Home page
	## Home Frame

	# Grid Home Page
	bg_Frame_Home = Frame(root, bg = "#262a34")
	bg_Frame_Home.pack(fill = "both", expand = 1)

	# for i in range(1440):
	# 	Grid.rowconfigure(bg_Frame_Home, i, weight = 1)

	# for i in range(300):
	# 	Grid.columnconfigure(bg_Frame_Home, i , weight = 1)

	# Frame Contain Widgets in Page Home

	# Frame_Home = Frame(bg_Frame_Home, width = 300, height = 300)
	# Frame_Home.grid(row = 100, column = 100, sticky = "NSEW")

	Frame_Welcome_text = Frame(bg_Frame_Home, width = 1860, height = 900, bg = "#262a34")
	Frame_Welcome_text.place(x = 100, y = 80)
	# Frame_Welcome_text.pack(anchor = "n", side = "left", pady = 95, padx = 100)

	# Welcome Text
	Welcome_text = Label(Frame_Welcome_text, text = "WELCOME", font = ("Consolas", 110, "bold"), bg = "#262a34", fg = "#ffffff")
	Welcome_text.place(x = 40, y = 70)
	Welcome_text_2 = Label(Frame_Welcome_text, text = "TO PROJECT MANAGEMENT", font = ("Consolas", 30), bg = "#262a34", fg = "#55aaff")
	Welcome_text_2.place(x = 140, y = 230)

	Credit_label = Label(Frame_Welcome_text, text = "Created by Gt Creator", font = ("Consolas", 15, "bold"), bg = "#262a34", fg = "#55aaff")
	Credit_label.place(x = 370, y = 300)

	Line_seperate = Frame(Frame_Welcome_text, width = 10, height = 350, bg = "#55aaff")
	Line_seperate.place(x = 670, y = 70)


	### Show tip/ tutorial ###
	Logo_label = PhotoImage(file = "images/bg.png")

	display_logo = Label(Frame_Welcome_text, image = Logo_label, bg = "#262a34")
	display_logo.photo = Logo_label
	display_logo.place(x = 700, y = 10)

	# User Label
	# username_label = Label(Frame_Welcome_text, text = "Current user:", font = ("Consolas", 20), bg = "#262a34", fg = "#55aaff")
	# username_label.place(x = 50, y = 150)

	# user_label = Label(Frame_Welcome_text, text = display_name_onScreen, font = ("Consolas", 65, "bold"), bg = "#262a34", fg = "#55aaff")
	# user_label.place(x = 50, y = 200)

	# Pesonal Project Progress

	### Line seperate ###

	LineSeperate_ = Frame(Frame_Welcome_text, width = 300, height = 3)
	LineSeperate_.place(x = 40, y = 520)

	Personal_Progress = Label(Frame_Welcome_text, text = "YOUR CURRENT PROJECT:", font = ("Consolas", 25, "bold"), bg = "#262a34", fg = "#9da6b1")
	Personal_Progress.place(x = 40, y = 600)

	Personal_Project_name = Label(Frame_Welcome_text, font = ("Consolas", 25), bg = "#262a34", fg = "#55aaff")
	Personal_Project_name.place(x = 440, y = 600)

	Team_Progress = Label(Frame_Welcome_text, text = "YOUR CURRENT PROJECT PROGRESS:", font = ("Consolas", 25, "bold"), bg = "#262a34", fg = "#9da6b1")
	Team_Progress.place(x = 40, y = 650)

	Team_Project_name = Label(Frame_Welcome_text, text = "0%s" %(percent), font = ("Consolas", 25), bg = "#262a34", fg = "#55aaff")
	Team_Project_name.place(x = 600, y = 650)

	#-----------------------------------------------------------------#
	# Frist Frame - Before starting project
	First_Frame_Personal = Frame(root, bg = "#262a34")

	# Grid Personal Project Frame
	for i in range(1440):
		Grid.rowconfigure(First_Frame_Personal, i, weight = 1)

	for i in range(8):
		Grid.columnconfigure(First_Frame_Personal, i , weight = 1)

	### Home Personal Project Page
	## First Page - Before starting project
	Before_starting = Frame(First_Frame_Personal, width = 1800, height = 1000, bg = "#262a34")
	# Before_starting.grid(row = 700, column = 5)
	Before_starting.place(x = 120, y = 20)

	Title_Page = Label(Before_starting, text = "Starting Your Project", font = ("Consolas", 20), bg = "#262a34", fg = "#ffffff")
	Title_Page.place(x = 15, y = 205)

	# Create New Button
	CreateNew_button = CustomButton(Before_starting,
									Create_image,
									Create_Hover_Image,
									Create_Press_Image,
									"#1e222a", "#2b313c", "#1544a0",
									25, 260, 1, create_new_Frame)
	CreateNew_button_active = Label(Before_starting, image = Create_Press_Image, bg = "#1544a0")

	# Open Button
	Open_Button = CustomButton(Before_starting,
								Open_image,
								Open_Hover_Image,
								Open_Press_Image,
								"#1e222a", "#2b313c", "#1544a0",
								25, 330, 1, Open_project_)
	Open_Button_active = Label(Before_starting, image = Open_Press_Image, bg = "#1544a0")

	## First Page - Recent Project
	Recent_project = Frame(Before_starting, width = 900, height = 600, bg = "#1e222a")
	Recent_project.place(x = 370, y = 180)
	# Recent_project.pack(anchor = "e", side = "right")

	introduce_frame = Frame(Recent_project, width = 900, height = 600, bg = "#1e222a")
	introduce_frame.place(x = 0, y = 0)

	Choose_your_path = Label(introduce_frame, text = "Choose your path", font = ("Consolas", 25, "bold"), bg = "#1e222a", fg = "#55aaff")
	Choose_your_path.place(x = 50, y = 50)

	instruction_image = PhotoImage(file = "images/Alert window/instruction.png")

	temp_frame = Frame(introduce_frame, width = 900, height = 500)
	temp_frame.place(x = 0, y = 100)

	instruction_label = Label(temp_frame, image = instruction_image)
	instruction_label.photo = instruction_image
	instruction_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

	### Create Project Frame ###
	create_Project_Frame = Frame(Recent_project, width = 900, height = 600, bg = "#1e222a")

	### Choose your project name ###
	cr_your_proj_label = Label(create_Project_Frame, text = "- CHOOSE YOUR PROJECT NAME -", font = ("Consolas", 20, "bold"), bg = "#1e222a", fg = "#55aaff")
	cr_your_proj_label.place(x = 226, y = 15)

	Home_ = Button(create_Project_Frame, text = "  Go back  ", font = ("Consolas", 10), bg = "#2a5bba", fg = "#FFFFFF", bd = 1, command = return_page)
	Home_.place(x = 0)

	## Below Frame ##
	Type_Frame = Frame(create_Project_Frame, width = 850, height = 200, bg = "#1e222a")
	Type_Frame.place(x = 10, y = 100)

	Your_project = Label(Type_Frame, text = "Your project name:", font = ("Consolas", 20), bg = "#1e222a", fg = "#FFFFFF")
	Your_project.place(x = 15, y = 10)

	Entry_project = Entry(Type_Frame, width = 22, font = ("Consolas", 20))
	Entry_project.place(x = 300, y = 13)

	Create_button = Button(Type_Frame, text = "  CREATE  ", font = ("Consolas", 15), bg = "#2a5bba", fg = "#FFFFFF", command = Create_Project)
	Create_button.place(x = 650, y = 12)

	alert_ = Label(Type_Frame, text = "", font = ("Consolas", 15), bg = "#1e222a", fg = "#ed1e45")
	alert_.place(x = 15, y = 70)

	### Alert Frame ###
	annouce_label = Label(create_Project_Frame, text = note_create, font = ("Consolas", 12), bg = "#1e222a", fg = "#566279", justify = "left")
	annouce_label.place(x = 10, y = 470)

	#### Open Frame ####
	### Function in project frame ###
	def decide_function():
		if "Open" in open_button_project.cget("text"):
			open_project(Project_listbox)
		else:
			remove_project(Project_listbox)

	def remove_project(Project_listbox):
		item_val = ""

		for i in Project_listbox.curselection():
			item_val = (Project_listbox.get(i)).strip()

		#### Allow to remove ####
		if item_val != "":
			## temp list ##
			temp_list_get = []

			with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "r") as read_project:
				reader = csv.reader(read_project, delimiter = "|")
				for row in reader:
					temp_list_get.append(Project_info(row[0], row[1]))
			read_project.close()

			for i in range(0, len(temp_list_get), 1):
				if temp_list_get[i].Project_name == item_val:
					temp_list_get.remove(temp_list_get[i])
					break

			Project_listbox.delete(0, END)
			for i in range(0, len(temp_list_get), 1):
				Project_listbox.insert(END, "  %s" %temp_list_get[i].Project_name)

			with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "w") as rewrite_project:
				for i in range(0, len(temp_list_get), 1):
					rewrite_project.write("".join(str(temp_list_get[i].Project_name)))
					rewrite_project.write("|")
					rewrite_project.write("".join(str(temp_list_get[i].complete_state)))
					rewrite_project.write("\n")
			rewrite_project.close()

			shutil.rmtree("Project/%s/%s" %(tag_number_int, item_val))

			### Create diary ###
			now = datetime.datetime.now()

			with open("Project/%s/Project_list_Diary_%s" %(tag_number_int, tag_number_int), "a") as diary:
				diary.write(''.join(str(now)))
				diary.write('|')
				diary.write(''.join(str("Deleted")))
				diary.write('|')
				diary.write(''.join(str(item_val)))
				diary.write('\n')
			diary.close()

		search_project.delete(0, END)

		if Project_listbox.size() <= 1:
			total_project.config(text = "You have %s project in total" %Project_listbox.size())
		else:
			total_project.config(text = "You have %s projects in total" %Project_listbox.size())


	def open_project(Project_listbox):
		global stayValue, empty_String, job_total, progress_value, ProjectName_short
		item_ = ""
		
		ToDo = False
		Doing = False
		Complete = False
		late_submit = False
		note_exists = False

		for i in Project_listbox.curselection():
			item_ = Project_listbox.get(i)

		empty_String = item_.strip()

		if len(empty_String) > 10:
			ProjectName_short = empty_String[:10] + ".."
		else:
			ProjectName_short = empty_String

		# print(empty_String)

		if empty_String == "":
			pass
		else:
			stayValue = True
			First_Frame_Personal.pack_forget()
			Second_Frame_Personal.pack(fill = "both", expand = 1)

			# job_total
			with open("Project/%s/%s/%s.txt" %(tag_number_int, empty_String, empty_String), "r") as jobs:
				reader = csv.reader(jobs, delimiter = "|")
				for row in reader:
					job_total = int(row[3])
					progress_value = int(row[2])
			# print(type(job_total))

			if os.path.isfile("Project/%s/%s/To Do" %(tag_number_int, empty_String)):
				ToDo = True

			if os.path.isfile("Project/%s/%s/Doing" %(tag_number_int, empty_String)):
				Doing = True

			if os.path.isfile("Project/%s/%s/Complete" %(tag_number_int, empty_String)):
				Complete = True

			if os.path.isfile("Project/%s/%s/submitted_late" %(tag_number_int, empty_String)):
				late_submit = True

			if os.path.isfile("Project/%s/%s/note_list" %(tag_number_int, empty_String)):
				note_exists = True

			## Read file To Do.txt
			if ToDo == True:
				with open("Project/%s/%s/To Do" %(tag_number_int, empty_String), "r") as read_file:
					reader = csv.reader(read_file, delimiter = "|")
					for row in reader:
						Job_list.append(Job_Info(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
				read_file.close()

			if Doing == True:
				## Read file Doing.txt
				with open("Project/%s/%s/Doing" %(tag_number_int, empty_String), "r") as read_file:
					reader = csv.reader(read_file, delimiter = "|")
					for row in reader:
						Doing_list.append(Job_Info(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
				read_file.close()

			if Complete == True:
				## Read file Complete.txt
				with open("Project/%s/%s/Complete" %(tag_number_int, empty_String), "r") as read_file:
					reader = csv.reader(read_file, delimiter = "|")
					for row in reader:
						Complete_List.append(Job_Info(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
				read_file.close()

			if note_exists == True:
				### Read file note_list.txt
				with open("Project/%s/%s/note_list" %(tag_number_int, empty_String), "r") as read_file:
					reader = csv.reader(read_file, delimiter = "|")
					for row in reader:
						note_list.append(note_info(row[0], row[1]))
				read_file.close()

			if late_submit == True:
				## Read file submitted_late.txt
				with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "r") as read_file:
					reader = csv.reader(read_file, delimiter = "|")
					for row in reader:
						submitted_late.append(row[0])
				read_file.close()

			### Insert value to To Do list, Doing list, Complete list ###
			for i in range(0, len(Job_list), 1):
				Todo_List.insert(END, "  %s" %Job_list[i].title)

			for i in range(0, len(Doing_list), 1):
				Doing_Listbox.insert(END, "  %s" %Doing_list[i].title)

			for i in range(0, len(Complete_List), 1):
				Comp_List.insert(END, "  %s" %Complete_List[i].title)

			for i in range(0, len(Complete_List), 1):
				for j in range(0, len(submitted_late), 1):
					if Complete_List[i].title == submitted_late[j]:
						Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")

			for i in range(0, len(note_list), 1):
				note_listbox.insert(END, " %s" %note_list[i].title)

			CR_Project_Name.config(text = ProjectName_short)
			Personal_Project_name.config(text = ProjectName_short)

			### Adjust length of To Do list ###
			Todo_List.config(height = len(Job_list))
			Doing_Listbox.config(height = len(Doing_list))
			Comp_List.config(height = len(Complete_List))

			### Adjust length of To Do list, Doing list, Complete list ### - 2nd time - double check
			if Todo_List.cget("height") > 14:
				Todo_List.config(height = 14)
				Alert_label.place(x = 36, y = 510)

			if Doing_Listbox.cget("height") > 14:
				Doing_Listbox.config(height = 14)
				Alert_label_doing.place(x = 36, y = 510)

			if Comp_List.cget("height") > 14:
				Comp_List.config(height = 14)
				Alert_label_complete.place(x = 36, y = 510)

			Team_Project_name.config(text = "%s%s" %(progress_value, percent))
			Progress_display_value.config(text = "%s%s" %(progress_value, percent))

			if len(note_list) <= 1:
				total_note.config(text = "You have %s note in total" %len(note_list))
			else:
				total_note.config(text = "You have %s notes in total" %len(note_list))

	## Click project to show info ##
	def show_info(event):
		## temp list to open and remove in open menu##
		_temp_list = []

		item_get = ""
		for i in Project_listbox.curselection():
			item_get = Project_listbox.get(i)

		with open("Project/%s/%s/%s.txt" %(tag_number_int, item_get.strip(), item_get.strip()), "r") as open_new:
			reader = csv.reader(open_new, delimiter = '|')
			for row in reader:
				_temp_list.append(Project_open_info(row[0], row[1], row[2], row[3]))
		open_new.close()

		Project_name_display.config(state = NORMAL)
		Project_name_display.delete(0, 'end')
		Project_name_display.insert(END, _temp_list[0].name_project)
		Project_name_display.config(state = "readonly")

		Current_percent.config(text = "%s%s" %(_temp_list[0].progress_state, percent))
		if _temp_list[0].state == "WIP":
			Current_state_.config(text = "Work in progress...")
		elif _temp_list[0].state == "Unfinished":
			Current_state_.config(text = "Unfinished")
		else:
			Current_state_.config(text = "Finished")
		Total_jobs_int.config(text = _temp_list[0].total_job)

	### Search project when typing ###
	def find_project(event):
		### temp list to store value ###
		temp_list_find  = []

		with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "r") as open_file:
			reader = csv.reader(open_file, delimiter = "|")
			for row in reader:
				temp_list_find.append(Project_info(row[0], row[1]))
		open_file.close()

		### get value when typing ###
		typed = event.widget.get()

		Project_listbox.delete(0, END)

		if typed == "":
			for i in range(0, len(temp_list_find), 1):
				Project_listbox.insert(END, "  %s" %temp_list_find[i].Project_name)

		if typed != "":
			for i in range(0, len(temp_list_find), 1):
				if typed in temp_list_find[i].Project_name:
					Project_listbox.insert(END, "  %s" %temp_list_find[i].Project_name)


	Open_project_frame = Frame(Recent_project, width = 900, height = 600, bg = "#1e222a")

	goback_Home_ = Button(Open_project_frame, text = "  Go back  ", font = ("Consolas", 10), bg = "#2a5bba", fg = "#FFFFFF", bd = 1, command = return_page)
	goback_Home_.place(x = 0)

	Title_open = Label(Open_project_frame, text = "Select your project:", font = ("Consolas", 20, "bold"), bg = "#1e222a", fg = "#55aaff")
	Title_open.place(x = 80, y = 80)

	search_lbl = Label(Open_project_frame, text = "Search project", font = ("Consolas", 12), bg = "#1e222a", fg = "#FFFFFF")

	search_project = Entry(Open_project_frame, width = 28, font = ("Consolas", 20), bg = "#383e4d", fg = "#FFFFFF", bd = 0)
	search_project.bind("<KeyRelease>", find_project)
	
	## Listbox contain project list ##
	Project_listbox = Listbox(Open_project_frame,
							font = ("Consolas", 20),
							width = 28, height = 10,
							bg = "#383e4d", fg = "#FFFFFF",
							bd = 0,
							highlightthickness = 0,
							activestyle = "none",
							exportselection = False)
	Project_listbox.place(x = 60, y = 170)
	Project_listbox.bind("<<ListboxSelect>>", show_info)

	### Side button - left side button ###
	### Function button ###
	def change_color_home(event):
		Home_button_icon.config(image = home_icon_press, bg = "#2b313c")
		Home_button_icon.photo = home_icon_press

		Search_bttn.config(image = search_image, bg = "#2a5bba", bd = 1)
		Search_bttn.photo = search_image

		## Clear listbox any value in label and entry has value on sceen ##
		Project_listbox.delete(0, END)

		Project_name_display.config(state = NORMAL)
		Project_name_display.delete(0, 'end')
		Project_name_display.config(state = "readonly")

		Current_percent.config(text = "")
		Current_state_.config(text = "")
		Total_jobs_int.config(text = "")

		Status_job.config(text = "")

		check_dir()
		## temporary list ##
		temp_list_ = []

		Open_Button_active.place(x = 25, y = 330)
		
		introduce_frame.place_forget()
		create_Project_Frame.place(x = 0, y = 0)
		CreateNew_button_active.place_forget()

		with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "r") as open_file:
			reader = csv.reader(open_file, delimiter = "|")
			for row in reader:
				temp_list_.append(Project_info(row[0], row[1]))
		open_file.close()

		if len(temp_list_) == 0:
			No_project_found.place(x = 0)
			Open_project_frame.place_forget()
		else:
			Open_project_frame.place(x = 0)
			No_project_found.place_forget()

		if len(temp_list_) <= 1:
			total_project.config(text = "You have %s project in total" %(len(temp_list_)))
		else:
			total_project.config(text = "You have %s projects in total" %(len(temp_list_)))

		# Append to listbox
		for i in range(0, len(temp_list_), 1):
			Project_listbox.insert(END, "  %s" %temp_list_[i].Project_name)

		search_project.delete(0, END)

		Project_listbox.config(height = 10)
		Project_listbox.place(x = 60, y = 170)

		search_project.place_forget()
		search_lbl.place_forget()

		Title_open.place(x = 80, y = 80)

	def change_color_edit(event):
		if Edit_button_open.cget("bg") == "#ed1e45":
			Edit_button_open.config(image = edit_image_press, bg = "#2b313c", bd = 1)
			Edit_button_open.photo = edit_image_press

			open_button_project.config(text = "  Remove  ", bg = "#ed1e45", fg = "#FFFFFF")
			open_button_project.place(x = 355, y = 501)

		else:
			Edit_button_open.config(image = edit_image, bg = "#ed1e45", bd = 1)
			Edit_button_open.photo = edit_image

			open_button_project.config(text = "  Open  ", bg = "#2a5bba", fg = "#FFFFFF")
			open_button_project.place(x = 377, y = 501)

	def change_color_search(event):
		Home_button_icon.config(image = home_icon, bg = "#1d803b")
		Home_button_icon.photo = home_icon

		Search_bttn.config(image = search_image_press, bg = "#2b313c", bd = 1)
		Search_bttn.photo = search_image_press

		search_project.place(x = 58, y = 120)
		search_lbl.place(x = 58, y = 90)
		Project_listbox.place(x = 60, y = 170)

		Title_open.place(x = 80, y = 40)

	#### Edit project window ####
	def edit_project_window():
		edit_project_wd = Toplevel()
		edit_project_wd.geometry(f"480x100+{edit_project_wd.winfo_screenwidth()//2 - 480//2}+{edit_project_wd.winfo_screenheight()//2 - 100//2}")
		edit_project_wd.resizable(0, 0)
		edit_project_wd.wm_attributes("-topmost", 1)
		edit_project_wd.title("Edit project name")
		edit_project_wd.config(bg = "#262a34")

		# Create Button - Toplevel() Window
		save_change_icon = PhotoImage(file = "images/Personal Project Page/Toplevel/save_change_icon.png")
		save_change_hover_icon = PhotoImage(file = "images/Personal Project Page/Toplevel/save_change_hover_icon.png")
		save_change_press_icon = PhotoImage(file = "images/Personal Project Page/Toplevel/save_change_press_icon.png")

		def return_save_project(event):
			save_change_project()

		def save_change_project():
			global empty_String, progress_value, job_total, ProjectName_short

			if (Entry_PJ.get()).strip() == empty_String:
				edit_project_wd.destroy()
			else:
				if (Entry_PJ.get()).strip() != "":
					if search_keyword(invalid_keyword, (Entry_PJ.get()).strip()) == True:
						edit_project_wd.geometry("480x140")
						alert_deny_.config(text = 'Avoid \\/:*?"<>| when naming your project.')
					else:
						### temp list to search value ###
						temp_project_list = []
						temp_append_list = []
						temp_initial_store = []

						with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "r") as read_value:
							reader = csv.reader(read_value, delimiter = "|")
							for row in reader:
								temp_project_list.append(Project_info(row[0], row[1]))
						read_value.close()

						### Allow edit value ###
						allow_edit = True

						for i in range(0, len(temp_project_list), 1):
							if (Entry_PJ.get()).strip() == temp_project_list[i].Project_name:
								allow_edit = False
								break

						if allow_edit == False:
							edit_project_wd.geometry("480x140")
							alert_deny_.config(text = "Project have already been created.")

						else:
							for i in range(0, len(temp_project_list), 1):
								if empty_String == temp_project_list[i].Project_name:
									## delete old folder ##
									shutil.rmtree("Project/%s/%s" %(tag_number_int, empty_String))

									### Append to new list and add back to og list later ###
									temp_project_list[i].Project_name = (Entry_PJ.get()).strip()
									temp_append_list.append(temp_project_list[i])
									temp_project_list.remove(temp_project_list[i])

									break

							temp_project_list.insert(0, temp_append_list[0])
							temp_append_list.clear()

							with open("Project/%s/Project_list_%s" %(tag_number_int, tag_number_int), "w") as rewrite:
								for i in range(0, len(temp_project_list), 1):
									rewrite.write("".join(str(temp_project_list[i].Project_name)))
									rewrite.write("|")
									rewrite.write("".join(str(temp_project_list[i].complete_state)))
									rewrite.write("\n")
							rewrite.close()

							### Change current project name ###
							empty_String = (Entry_PJ.get()).strip()

							if len(empty_String) > 10:
								ProjectName_short = empty_String[:10] + ".."
							else:
								ProjectName_short = empty_String

							CR_Project_Name.config(text = ProjectName_short)
							Personal_Project_name.config(text = ProjectName_short)

							### create new folder and delete old folder ###
							os.makedirs("Project/%s/%s" %(tag_number_int, empty_String))

							### Create new initial file ###
							if progress_value >= 100:
								create_initial_file("Finished", 100, job_total)
								save_project_list_diary("Completed", "Finished")
							else:
								create_initial_file("WIP", int(progress_value), job_total)
								save_project_list_diary("WIP", "Unfinished")

							### write To do/ Doing/ Complete/submitted_late/ note_list.txt file to new folder ###
							## write To Do.txt to new folder ##
							if len(Job_list) != 0:
								with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Title[0]), "w") as to_do:
									for i in range(0, len(Job_list), 1):
										to_do.write("".join(str(Job_list[i].title)))
										to_do.write("|")
										to_do.write("".join(str(Job_list[i].description)))
										to_do.write("|")
										to_do.write("".join(str(Job_list[i].DueBool)))
										to_do.write("|")
										to_do.write("".join(str(Job_list[i].DueDay)))
										to_do.write("|")
										to_do.write("".join(str(Job_list[i].DueHour)))
										to_do.write("|")
										to_do.write("".join(str(Job_list[i].DueMinute)))
										to_do.write("|")
										to_do.write("".join(str(Job_list[i].Limit_Time)))
										to_do.write("|")
										to_do.write("".join(str(Job_list[i].importance)))
										to_do.write("\n")
								to_do.close()

							## write Doing.txt to new folder ##
							if len(Doing_list) != 0:
								with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Title[1]), "w") as doing_write:
									for i in range(0, len(Doing_list), 1):
										doing_write.write("".join(str(Doing_list[i].title)))
										doing_write.write("|")
										doing_write.write("".join(str(Doing_list[i].description)))
										doing_write.write("|")
										doing_write.write("".join(str(Doing_list[i].DueBool)))
										doing_write.write("|")
										doing_write.write("".join(str(Doing_list[i].DueDay)))
										doing_write.write("|")
										doing_write.write("".join(str(Doing_list[i].DueHour)))
										doing_write.write("|")
										doing_write.write("".join(str(Doing_list[i].DueMinute)))
										doing_write.write("|")
										doing_write.write("".join(str(Doing_list[i].Limit_Time)))
										doing_write.write("|")
										doing_write.write("".join(str(Doing_list[i].importance)))
										doing_write.write("\n")
								doing_write.close()

							## write Complete.txt to new folder ##
							if len(Complete_List) != 0:
								with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Title[2]), "w") as complete_write:
									for i in range(0, len(Complete_List), 1):
										complete_write.write("".join(str(Complete_List[i].title)))
										complete_write.write("|")
										complete_write.write("".join(str(Complete_List[i].description)))
										complete_write.write("|")
										complete_write.write("".join(str(Complete_List[i].DueBool)))
										complete_write.write("|")
										complete_write.write("".join(str(Complete_List[i].DueDay)))
										complete_write.write("|")
										complete_write.write("".join(str(Complete_List[i].DueHour)))
										complete_write.write("|")
										complete_write.write("".join(str(Complete_List[i].DueMinute)))
										complete_write.write("|")
										complete_write.write("".join(str(Complete_List[i].Limit_Time)))
										complete_write.write("|")
										complete_write.write("".join(str(Complete_List[i].importance)))
										complete_write.write("\n")
								complete_write.close()

							## write submitted_late.txt to new folder ##
							if len(submitted_late) != 0:
								with open("Project/%s/%s/submitted_late" %(tag_number_int, empty_String), "w") as late_rewrite:
									for i in range(0, len(submitted_late), 1):
										late_rewrite.write("".join(str(submitted_late[i])))
										late_rewrite.write("\n")
								late_rewrite.close()

							## write note_list to new folder ##
							if len(note_list) != 0:
								with open("Project/%s/%s/note_list" %(tag_number_int, empty_String), "w") as note_rewrite:
									for i in range(0, len(note_list), 1):
										note_rewrite.write("".join(str(note_list[i].title)))
										note_rewrite.write("|")
										note_rewrite.write("".join(str(note_list[i].descript)))
										note_rewrite.write("\n")
								note_rewrite.close()

							### Close window after complete change ###
							edit_project_wd.destroy()


				else:
					edit_project_wd.geometry("480x140")
					alert_deny_.config(text = "Please choose your project name.")

		# Create New Button
		save_change_button = CustomButton(edit_project_wd,
										save_change_icon,
										save_change_hover_icon,
										save_change_press_icon,
										"#1e222a", "#2b313c", "#1544a0",
										320, 38, 1, save_change_project)

		PJ_title = Label(edit_project_wd, text = "Project Name:",font = ("Consolas", 15), fg = "#FFFFFF", bg = "#262a34")
		PJ_title.place(x = 10, y = 10)

		Entry_PJ = Entry(edit_project_wd, font = ("Consolas", 20))
		Entry_PJ.place(x = 10, y = 45)
		Entry_PJ.delete(0, END)
		Entry_PJ.insert(END, empty_String)
		edit_project_wd.bind("<Return>", return_save_project)

		alert_deny_ = Label(edit_project_wd, font = ("Consolas", 14, "bold"), bg = "#262a34", fg = "#ed1e45")
		alert_deny_.place(x = 10, y = 95)


	def sort_job_ToDo():
		sort_job(Job_list, Todo_List, "To Do", Alert_label)

	def sort_job_Doing():
		sort_job(Doing_list, Doing_Listbox, "Doing", Alert_label_doing)

	def sort_job_Complete():
		sort_job(Complete_List, Comp_List, "Complete", Alert_label_complete)

	def sort_job(Job_list, Todo_List, Doing_stat, Alert_label):
		def renew_comp_list(Doing_stat):
			if Doing_stat == "Complete":
				if len(submitted_late) != 0:
					for i in range(0, len(Complete_List), 1):
						for j in range(0, len(submitted_late), 1):
							if Complete_List[i].title == submitted_late[j]:
								Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")


		def rewrite_file(Doing_stat):
			with open("Project/%s/%s/%s" %(tag_number_int, empty_String, Doing_stat), "w") as new_file:
				for i in range(0, len(Job_list), 1):
					new_file.write(''.join(str(Job_list[i].title)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].description)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueBool)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueDay)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueHour)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].DueMinute)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].Limit_Time)))
					new_file.write('|')
					new_file.write(''.join(str(Job_list[i].importance)))
					new_file.write('\n')
			new_file.close()

		def sort_function():
			sort_ascending = True

			temp_no_due = []
			temp_has_due = []

			if asc_desc_box.get() == "Descending":
				sort_ascending = False
			else:
				sort_ascending = True

			for i in range(0, len(Job_list), 1):
				if Job_list[i].DueBool == "True":
					temp_has_due.append(Job_list[i])
				else:
					temp_no_due.append(Job_list[i])

			if sortBy_Box.get() == "Due Date":
				if child_filter.get() == "Year":
					if sort_ascending == True:
						MergeSort_dueYear(temp_has_due)
					else:
						MergeSort_desc_dueYear(temp_has_due)

					Job_list.clear()
					for i in range(0, len(temp_has_due), 1):
						Job_list.append(temp_has_due[i])

					for i in range(0, len(temp_no_due), 1):
						Job_list.append(temp_no_due[i])

					Todo_List.delete(0, END)
					for i in range(0, len(Job_list), 1):
						Todo_List.insert(END, "  %s" %Job_list[i].title)

					rewrite_file(Doing_stat)
					renew_comp_list(Doing_stat)

					temp_no_due.clear()
					temp_has_due.clear()

					sort_window.destroy()

				elif child_filter.get() == "Month":
					if sort_ascending == True:
						MergeSort_dueMonth(temp_has_due)
					else:
						MergeSort_desc_dueMonth(temp_has_due)

					Job_list.clear()
					for i in range(0, len(temp_has_due), 1):
						Job_list.append(temp_has_due[i])

					for i in range(0, len(temp_no_due), 1):
						Job_list.append(temp_no_due[i])

					Todo_List.delete(0, END)
					for i in range(0, len(Job_list), 1):
						Todo_List.insert(END, "  %s" %Job_list[i].title)

					rewrite_file(Doing_stat)
					renew_comp_list(Doing_stat)

					temp_no_due.clear()
					temp_has_due.clear()

					sort_window.destroy()

				elif child_filter.get() == "Day":
					if sort_ascending == True:
						MergeSort_dueDay(temp_has_due)
					else:
						MergeSort_desc_dueDay(temp_has_due)

					Job_list.clear()
					for i in range(0, len(temp_has_due), 1):
						Job_list.append(temp_has_due[i])

					for i in range(0, len(temp_no_due), 1):
						Job_list.append(temp_no_due[i])

					Todo_List.delete(0, END)
					for i in range(0, len(Job_list), 1):
						Todo_List.insert(END, "  %s" %Job_list[i].title)

					rewrite_file(Doing_stat)
					renew_comp_list(Doing_stat)

					temp_no_due.clear()
					temp_has_due.clear()

					sort_window.destroy()

			elif sortBy_Box.get() == "Due Hour":
				if sort_ascending == True:
					MergeSort_dueHour(temp_has_due)
				else:
					MergeSort_desc_dueHour(temp_has_due)

				Job_list.clear()
				for i in range(0, len(temp_has_due), 1):
					Job_list.append(temp_has_due[i])

				for i in range(0, len(temp_no_due), 1):
					Job_list.append(temp_no_due[i])

				Todo_List.delete(0, END)
				for i in range(0, len(Job_list), 1):
					Todo_List.insert(END, "  %s" %Job_list[i].title)

				rewrite_file(Doing_stat)
				renew_comp_list(Doing_stat)

				temp_no_due.clear()
				temp_has_due.clear()

				sort_window.destroy()

			elif sortBy_Box.get() == "Time Limit":
				if sort_ascending == True:
					MergeSort_TimeLimit(temp_no_due)
				else:
					MergeSort_desc_TimeLimit(temp_no_due)

				Job_list.clear()
				for i in range(0, len(temp_no_due), 1):
					Job_list.append(temp_no_due[i])

				for i in range(0, len(temp_has_due), 1):
					Job_list.append(temp_has_due[i])

				Todo_List.delete(0, END)
				for i in range(0, len(Job_list), 1):
					Todo_List.insert(END, "  %s" %Job_list[i].title)

				rewrite_file(Doing_stat)
				renew_comp_list(Doing_stat)

				temp_no_due.clear()
				temp_has_due.clear()

				sort_window.destroy()

			elif sortBy_Box.get() == "Importance":
				if sort_ascending == True:
					MergeSort_Importance(temp_no_due)
				else:
					MergeSort_desc_Importance(temp_no_due)

				Job_list.clear()
				for i in range(0, len(temp_no_due), 1):
					Job_list.append(temp_no_due[i])

				for i in range(0, len(temp_has_due), 1):
					Job_list.append(temp_has_due[i])

				Todo_List.delete(0, END)
				for i in range(0, len(Job_list), 1):
					Todo_List.insert(END, "  %s" %Job_list[i].title)

				rewrite_file(Doing_stat)
				renew_comp_list(Doing_stat)

				temp_no_due.clear()
				temp_has_due.clear()

				sort_window.destroy()

			elif sortBy_Box.get() == "Title":
				if sort_ascending == True:
					MergeSort_title(Job_list)
				else:
					MergeSort_desc_title(Job_list)

				Todo_List.delete(0, END)
				for i in range(0, len(Job_list), 1):
					Todo_List.insert(END, "  %s" %Job_list[i].title)

				rewrite_file(Doing_stat)
				renew_comp_list(Doing_stat)

				temp_no_due.clear()
				temp_has_due.clear()

				sort_window.destroy()				


		def show_sortBy(event):
			if sortBy_Box.get() == "Due Date":
				sort_window.geometry("220x330")
				by_label.place(x = 10, y = 90)
				child_filter.place(x = 10, y = 130)
				mode_label.place(x = 10, y = 170)
				asc_desc_box.place(x = 10, y = 210)
				sortList_button.place(x = 60, y = 270)
			else:
				sort_window.geometry("220x280")
				mode_label.place(x = 10, y = 100)
				asc_desc_box.place(x = 10, y = 140)
				sortList_button.place(x = 60, y = 200)
				by_label.place_forget()
				child_filter.place_forget()


		sort_window = Toplevel()
		sort_window.geometry(f"220x280+{sort_window.winfo_screenwidth()//2 - 220//2}+{sort_window.winfo_screenheight()//2 - 280//2}")
		sort_window.title("Sort options")
		sort_window.resizable(0, 0)
		sort_window.wm_attributes("-topmost", 1)
		sort_window.config(bg = "#1e222a")

		### GUI ###
		sort_label = Label(sort_window, text = "Sort:", font = ("Consolas", 20, "bold"), bg = "#1e222a", fg = "#FFFFFF")
		sort_label.place(x = 10, y = 10)

		## Comobobox sort by ##
		sortBy_Box = ttk.Combobox(sort_window, value = sortBy_list, font = ("Consolas", 15), state = "readonly", width = 15)
		sortBy_Box.place(x = 10, y = 55)
		sortBy_Box.current(0)
		sortBy_Box.bind("<<ComboboxSelected>>", show_sortBy)

		mode_label = Label(sort_window, text = "Order:", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
		mode_label.place(x = 10, y = 100)

		asc_desc_box = ttk.Combobox(sort_window, value = sortUp_down, font = ("Consolas", 15), state = "readonly", width = 15)
		asc_desc_box.place(x = 10, y = 140)
		asc_desc_box.current(0)

		sortList_button = Button(sort_window, text = " Sort ", font = ("Consolas", 18), bg = "#2a5bba", fg = "#FFFFFF", command = sort_function)
		sortList_button.place(x = 60, y = 200)

		by_label = Label(sort_window, text = "By:", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")

		child_filter = ttk.Combobox(sort_window, value = sortChild_filter, font = ("Consolas", 15), state = "readonly", width = 15)
		child_filter.current(0)

	### Icon button ###
	edit_image = PhotoImage(file = "images/Open window/edit_image.png")
	edit_image_press = PhotoImage(file = "images/Open window/edit_press_image.png")

	home_icon = PhotoImage(file = "images/Open window/home_image.png")
	home_icon_press = PhotoImage(file = "images/Open window/home_press_image.png")
	home_icon_hover = PhotoImage(file = "images/Open window/home_hover_image.png")

	search_image = PhotoImage(file = "images/Open window/search_image.png")
	search_image_press = PhotoImage(file = "images/Open window/search_press_image.png")
	search_image_hover = PhotoImage(file = "images/Open window/search_hover_image.png")

	### Buttons ###
	Home_button_icon = Button(Open_project_frame, image = home_icon_press, bg = "#2b313c", bd = 1)
	Home_button_icon.photo = home_icon
	Home_button_icon.place(x = 15, y = 205)
	Home_button_icon.bind("<ButtonRelease-1>", change_color_home)

	Search_bttn = Button(Open_project_frame, image = search_image, bg = "#2a5bba", bd = 1)
	Search_bttn.photo = search_image
	Search_bttn.place(x = 15, y = 170)
	Search_bttn.bind("<ButtonRelease-1>", change_color_search)

	Edit_button_open = Button(Open_project_frame, image = edit_image, bg = "#ed1e45", bd = 1)
	Edit_button_open.photo = edit_image
	Edit_button_open.place(x = 15, y = 240)
	Edit_button_open.bind("<ButtonRelease-1>", change_color_edit)


	### Open Project button ###
	open_button_project = Button(Open_project_frame, text = "  Open  ", font = ("Consolas", 15), bg = "#2a5bba", fg = "#FFFFFF", bd = 1, command = decide_function)
	open_button_project.place(x = 377, y = 501)

	### Total project ###
	total_project = Label(Open_project_frame, font = ("Consolas", 11), bg = "#1e222a", fg = "#55aaff")
	total_project.place(x = 60, y = 515)


	### Current Project progress selected ### - If project list >< 0
	CR_Project_selected = Frame(Open_project_frame, width = 340, height = 500, bg = "#1e222a")
	CR_Project_selected.place(x = 530, y = 80)

	Project_title_info = Label(CR_Project_selected, text = "Project name:", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
	Project_title_info.place(x = 0, y = 10)

	# Project_name_display = Label(CR_Project_selected, text = "Test project name", font = ("Consolas", 20), bg = "#1e222a", fg = "#55aaff")
	# Project_name_display.place(x = 0, y = 50)

	Project_name_display = Entry(CR_Project_selected, font = ("Consolas", 20), bg = "#1e222a", fg = "#55aaff", bd = 0)
	Project_name_display.place(x = 0, y = 50)
	Project_name_display.config(state = "readonly", readonlybackground = "#1e222a")

	_line = Label(CR_Project_selected, text = "______________________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
	_line.place(x = 0, y = 80)

	Current_Progress = Label(CR_Project_selected, text = "Current progress:", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
	Current_Progress.place(x = 0, y = 130)

	Current_percent = Label(CR_Project_selected, font = ("Consolas", 20), bg = "#1e222a", fg = "#55aaff")
	Current_percent.place(x = 0, y = 165)

	_line_2 = Label(CR_Project_selected, text = "_________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
	_line_2.place(x = 0, y = 200)

	Current_state_label = Label(CR_Project_selected, text = "Current state:", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
	Current_state_label.place(x = 0, y = 245)

	Current_state_ = Label(CR_Project_selected, font = ("Consolas", 20), bg = "#1e222a", fg = "#55aaff")
	Current_state_.place(x = 0, y = 285)

	_line_3 = Label(CR_Project_selected, text = "______________________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
	_line_3.place(x = 0, y = 320)

	Total_jobs = Label(CR_Project_selected, text = "Total jobs:", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
	Total_jobs.place(x = 0, y = 365)

	Total_jobs_int = Label(CR_Project_selected, font = ("Consolas", 20), bg = "#1e222a", fg = "#55aaff")
	Total_jobs_int.place(x = 0, y = 400)

	_line_4 = Label(CR_Project_selected, text = "________", font = ("Consolas"), bg = "#1e222a", fg = "#55aaff")
	_line_4.place(x = 0, y = 440)

	#### No project was found/ created #### - If project == 0
	No_project_found = Frame(Recent_project, width = 900, height = 600, bg = "#1e222a")

	Error_ = Label(No_project_found, text = "Oops! Something went wrong.", font = ("Consolas", 25, "bold"), bg = "#1e222a", fg = "#55aaff")
	Error_.place(x = 70, y = 70)

	Error_2 = Label(No_project_found, text = "We can't find your project list", font = ("Consolas", 20), bg = "#1e222a", fg = "#FFFFFF")
	Error_2.place(x = 73, y = 130)

	No_project_label = Label(No_project_found, text = error_text, justify = "left", font = ("Consolas", 20), bg = "#1e222a", fg = "#FFFFFF")
	No_project_label.place(x = 50, y = 225)

	return_Home_ = Button(No_project_found, text = "  Go back  ", font = ("Consolas", 10), bg = "#2a5bba", fg = "#FFFFFF", bd = 1, command = return_page)
	return_Home_.place(x = 0)

	# if 

	#-----------------------------------------------------------------#
	## Second Frame - After creating project
	Second_Frame_Personal = Frame(root, bg = "#262a34")

	# Grid Personal Project Frame - 2nd Frame
	# for i in range(1920):
	# 	Grid.rowconfigure(Second_Frame_Personal, i, weight = 1)

	# for i in range(1080):
	# 	Grid.columnconfigure(Second_Frame_Personal, i , weight = 1)

	##### Frame #####
	# 2nd Frame contain widgets
	Contain_LabelWidget = Frame(Second_Frame_Personal, bg = "#262a34")
	Contain_LabelWidget.pack(fill = "both", expand = 1)

	## Frame Contains ToDo/ Doing/ Complete Frame
	Rectangle_Frame = Frame(Contain_LabelWidget, width = 1000, height = 50, bg = "#262a34")
	Rectangle_Frame.place(x = 150, y = 260)

	ToDo_Frame = Frame(Rectangle_Frame, width = 300, height = 50, bg = "#7687a2")
	ToDo_Frame.place(x = 0, y = 0)

	Doing_Frame = Frame(Rectangle_Frame, width = 300, height = 50, bg = "#7687a2")
	Doing_Frame.place(x = 350, y = 0)

	Complete_Frame = Frame(Rectangle_Frame, width = 300, height = 50, bg = "#7687a2")
	Complete_Frame.place(x = 700, y = 0)

	Contain_Todo_Frame = Frame(ToDo_Frame)
	Contain_Todo_Frame.place(x = 10, y = 10)

	Contain_Doing_Frame = Frame(Doing_Frame)
	Contain_Doing_Frame.place(x = 10, y = 10)

	Contain_Complete_Frame = Frame(Complete_Frame)
	Contain_Complete_Frame.place(x = 10, y = 10)

	# To Do + Doing + Complete List
	ToDo_Custom_Frame = CustomFrame(Contain_Todo_Frame, Title[0],
									3, "#1e222a", "#2b313c", "#1544a0",
									Add_icon, Add_hover_icon, Add_press_icon, Add_Job_name,
									Filter_image, Filter_hover_image, Filter_press_image, sort_job_ToDo,
									Edit_icon, Edit_hover_icon, Edit_press_icon, edit_window_ToDo)

	Doing_Custom_Frame = CustomFrame(Contain_Doing_Frame, Title[1],
									2, "#1e222a", "#2b313c", "#1544a0",
									Edit_icon, Edit_hover_icon, Edit_press_icon, edit_window_Doing,
									Filter_image, Filter_hover_image, Filter_press_image, sort_job_Doing)

	Complete_Custom_Frame = CustomFrame(Contain_Complete_Frame, Title[2],
									2, "#1e222a", "#2b313c", "#1544a0",
									Edit_icon, Edit_hover_icon, Edit_press_icon, edit_window_Complete,
									Filter_image, Filter_hover_image, Filter_press_image, sort_job_Complete)

	# Current Project Name
	Current_Project = Label(Contain_LabelWidget, text = "Your Current Project:", font = ("Consolas", 20, "bold"), fg = "#96abd1", bg = "#262a34")
	Current_Project.place(x = 150, y = 125)

	CR_Project_Name = Label(Contain_LabelWidget, font = ("Consolas", 20), fg = "#55aaff", bg = "#262a34")
	CR_Project_Name.place(x = 530, y = 125)

	#### Edit project icon ####
	edit_project = PhotoImage(file = "images/Personal Project Page/edit_project_icon.png")
	edit_project_hover = PhotoImage(file = "images/Personal Project Page/edit_project_hover_icon.png")
	edit_project_press = PhotoImage(file = "images/Personal Project Page/edit_project_press_icon.png")

	#### Edit project button ####
	Edit_Project_bttn = CustomButton(Contain_LabelWidget,
									edit_project, edit_project_hover,
									edit_project_press,
									"#1e222a", "#2b313c", "#1544a0",
									477, 130, 1, edit_project_window)

	# Open Button - Starting Project Page
	Open_Button_2nd = CustomButton(Contain_LabelWidget,
									Open_image, Open_Hover_Image,
									Open_Press_Image,
									"#1e222a", "#2b313c", "#1544a0",
									150, 180, 1, OpenNewProject)

	# Create New Button - Starting Project Page
	CreateNew_button_2nd = CustomButton(Contain_LabelWidget,
										Create_image, Create_Hover_Image,
										Create_Press_Image,
										"#1e222a", "#2b313c", "#1544a0",
										320, 180, 1, Add_Project_name)

	## Status job ##
	Status_job = Label(Contain_LabelWidget, font = ("Consolas", 20, "bold"), fg = "#55aaff", bg = "#262a34")
	Status_job.place(x = 540, y = 195)

	# Test_Frame = Frame(Contain_LabelWidget, width = 30, height = 30, bg = "#262a34")
	# Test_Frame.place(x = 20 , y = 100)

	### Background Content
	bg_Content = Frame(Contain_LabelWidget, bg = "#262a34", width = 1200, height = 800)
	bg_Content.place(x = 125, y = 325)

	### TO Do List Function
	menu_function = Menu(tearoff = False, font = ("Tahoma", 10))
	menu_function.add_command(label = "Edit", command = lambda: edit_item_window(Job_list, Todo_List, Title[0]))
	menu_function.add_command(label = "Mark as doing", command = transfer_Do_Doing)
	menu_function.add_command(label = "Mark as complete", command = transfer_Do_complete)
	menu_function.add_separator()
	menu_function.add_command(label = "Remove", command = remove_job_ToDo)

	## To Do List
	ToDo_Frame_List = Frame(bg_Content, bg = "#262a34", width = 350, height = 600)
	ToDo_Frame_List.place(x = 0)

	Todo_List = Listbox(ToDo_Frame_List,
						font = ("Consolas", 21),
						width = 20, height = 0,
						bg = "#383e4d", fg = "#FFFFFF",
						bd = 0,
						highlightthickness = 0,
						activestyle = "none")
	Todo_List.place(x = 29, y = 24)
	Todo_List.bind("<Double-1>", edit_item_Do)
	Todo_List.bind("<Button-3>", popup_menu)

	# Alert label - scroll down to see more
	Alert_label = Label(ToDo_Frame_List,
						text = "Scroll down to see more",
						font = ("Consolas", 16, "bold"), bg = "#262a34",
						fg = "#FFFFFF")

	def create_KnapSack():
		KnapSack_window = Toplevel()

		height_app = 135
		width_app = 330

		post_x = ((KnapSack_window.winfo_screenwidth())//2) - (width_app//2)
		post_y = ((KnapSack_window.winfo_screenheight())//2) - (height_app//2)

		KnapSack_window.geometry(f"{width_app}x{height_app}+{post_x}+{post_y}")
		KnapSack_window.resizable(0, 0)
		KnapSack_window.title("Create filter list")

		KnapSack_window.config(bg = "#262a34")

		## Function create KnapSack List - Filter List
		def create_KnapSack():
			Filter_list_og.clear()
			## Store temporarily
			Og_id = []

			time_list = []
			importance_list = []

			KnapSack_list.clear()

			## Store old time limit use
			global time_limit_value
			time_limit_value = int(Time_limit_spin.get())

			# Time limit use for knapsack algorithm
			time_limit_get = int(Time_limit_spin.get())

			for i in range(0, len(Job_list), 1):
				if Job_list[i].DueBool == 'False':
					Og_id.append(int(i))
					time_list.append(int(Job_list[i].Limit_Time))
					importance_list.append(int(Job_list[i].importance))

			length_ls = len(time_list)

			K = [[0 for x in range(int(time_limit_get) + 1)] for x in range(int(length_ls) + 1)]

			# Testing value get
			total_importance_get = knapSack(time_limit_get, time_list, importance_list, length_ls, K)
			print(total_importance_get)

			truyvet(length_ls, time_limit_get, K, time_list, KnapSack_list)
			print(Og_id)
			print(f"time list: {time_list}")
			print(f"importance list: {importance_list}")
			print(KnapSack_list)

			if KnapSack_list_button.winfo_ismapped() == 0:
				# Place knapsack button on screen			
				KnapSack_list_button.place(x = 0, y = 62)

				# Change all others button to default color
				NoDue_list_button.config(bg = "#363d4a")
				Due_list_button.config(bg = "#363d4a")
				main_list_button.config(bg = "#363d4a")

				## Add value to to do listbox
				Todo_List.delete(0, END)
				for i in KnapSack_list:
					for j in Og_id:
						if int(Job_list[j].Limit_Time) == time_list[i]:
							Filter_list_og.append(j)
							Todo_List.insert(END, "  %s" %Job_list[int(j)].title)

				time_list.clear()
				importance_list.clear()
				Og_id.clear()
				KnapSack_window.destroy()
			else:
				# Change knapsack button to press state
				KnapSack_list_button.config(image = KnapSack_press_hover_image, bg = "#2f63cc")
				KnapSack_list_button.photo = KnapSack_press_hover_image

				# Change all others button to default color
				NoDue_list_button.config(bg = "#363d4a")
				Due_list_button.config(bg = "#363d4a")
				main_list_button.config(bg = "#363d4a")

				## Add value to to do listbox
				Todo_List.delete(0, END)
				for i in KnapSack_list:
					for j in Og_id:
						if int(Job_list[j].Limit_Time) == time_list[i]:
							Filter_list_og.append(j)
							Todo_List.insert(END, "  %s" %Job_list[int(j)].title)

				time_list.clear()
				Og_id.clear()
				importance_list.clear()
				KnapSack_window.destroy()

		# Create time limit label
		Create_time_label = Label(KnapSack_window, text = "Put your time limit:",
								font = ("Consolas", 15), bg = "#262a34", fg = "#FFFFFF")
		Create_time_label.place(x = 10, y = 20)

		# Spinbox time limit
		Time_limit_spin = Spinbox(KnapSack_window, font = ("Consolas", 15),
								from_ = 1, to = 23, format = ("%02.0f"),
								state = "readonly", width = 2)
		Time_limit_spin.place(x = 240, y = 25)

		# Old total time limit
		Old_time_limit = Label(KnapSack_window, font = ("Consolas", 13),
								text = "Your old limit time: %s" %time_limit_value,
								bg = "#262a34", fg = "#7687a2")
		Old_time_limit.place(x = 10, y = 55)

		Create_knapSack_Button = Button(KnapSack_window, text = "CREATE",
										font = ("Consolas", 15),
										bg = "#2a5bba", fg = "#FFFFFF",
										bd = 1, command = create_KnapSack)
		Create_knapSack_Button.place(x = 240, y = 80)

	### Color for button ###
	# default_color = "#363d4a"
	# pressbutton_color = "#2a5bba"
	### Change color when hover/ leave/ enter button ###
	## Change color when hover/ leave button
	def change_hover_bttn(event):
		if event.widget.cget('bg') == "#363d4a":
			event.widget.config(image = KnapSack_hover_image, bg = "#545f73")
			event.widget.photo = KnapSack_hover_image

		elif event.widget.cget('bg') == "#2a5bba":
			event.widget.config(image = KnapSack_press_hover_image, bg = "#2f63cc")
			event.widget.photo = KnapSack_press_hover_image

	def back_to_normal(event):
		if event.widget.cget('bg') == "#545f73":
			event.widget.config(image = KnapSack_image, bg = "#363d4a")
			event.widget.photo = KnapSack_image

		elif event.widget.cget('bg') == "#2f63cc":
			event.widget.config(image = KnapSack_press_image, bg = "#2a5bba")
			event.widget.photo = KnapSack_press_image


	###### Use for To Do List/ Doing List/ Complete List #######
	def press_button(event):
		if event.widget.cget('bg') == "#545f73":
			event.widget.config(image = KnapSack_press_image, bg = "#2a5bba")
			event.widget.photo = KnapSack_press_image

			Due_list_button.config(bg = "#363d4a")
			NoDue_list_button.config(bg = "#363d4a")
			main_list_button.config(bg = "#363d4a")

	def on_enter(event):
		if event.widget.cget('bg') == "#363d4a":
			event.widget.config(bg = "#545f73")

		elif event.widget.cget('bg') == "#2a5bba":
			event.widget.config(bg = "#2f63cc")

	def on_leave(event):
		if event.widget.cget('bg') == "#545f73":
			event.widget.config(bg = "#363d4a")

		elif event.widget.cget('bg') == "#2f63cc":
			event.widget.config(bg = "#2a5bba")

	## Display value to listbox
	def display_all_job():
		Todo_List.delete(0, END)
		for i in range(0, len(Job_list), 1):
			Todo_List.insert(END, "  %s" %Job_list[i].title)

	def display_due_job():
		Todo_List.delete(0, END)
		for i in range(0, len(Job_list), 1):
			if Job_list[i].DueBool == "True":
				Todo_List.insert(END, "  %s" %Job_list[i].title)

	def display_nodue_job():
		Todo_List.delete(0, END)
		for i in range(0, len(Job_list), 1):
			if Job_list[i].DueBool == "False":
				Todo_List.insert(END, "  %s" %Job_list[i].title)

	def display_filter_job():
		Todo_List.delete(0, END)
		for i in Filter_list_og:
			Todo_List.insert(END, "  %s" %Job_list[int(i)].title)

	## Change color when press button
	def change_color_main(event):
		if main_list_button.cget('bg') == "#545f73":
			Due_list_button.config(bg = "#363d4a")
			NoDue_list_button.config(bg = "#363d4a")
			main_list_button.config(bg = "#2a5bba")

			KnapSack_list_button.config(image = KnapSack_image, bg = "#363d4a")
			KnapSack_list_button.photo = KnapSack_image

	def change_color_due(event):
		if Due_list_button.cget('bg') == "#545f73":
			Due_list_button.config(bg = "#2a5bba")
			NoDue_list_button.config(bg = "#363d4a")
			main_list_button.config(bg = "#363d4a")

			KnapSack_list_button.config(image = KnapSack_image, bg = "#363d4a")
			KnapSack_list_button.photo = KnapSack_image

	def change_color_nodue(event):
		if NoDue_list_button.cget('bg') == "#545f73":
			Due_list_button.config(bg = "#363d4a")
			NoDue_list_button.config(bg = "#2a5bba")
			main_list_button.config(bg = "#363d4a")

			KnapSack_list_button.config(image = KnapSack_image, bg = "#363d4a")
			KnapSack_list_button.photo = KnapSack_image

	### Filter list
	## Main List display button
	main_list_button = Button(ToDo_Frame_List,
							text = "  Main  ",
							font = ("Consolas", 10, "bold"),
							bg = "#2a5bba", fg = "#FFFFFF",
							bd = 1, command = display_all_job)
	main_list_button.place(x = 29)
	main_list_button.bind("<Enter>", on_enter)
	main_list_button.bind("<Leave>", on_leave)
	main_list_button.bind("<ButtonRelease-1>", change_color_main)

	## Due list display button
	Due_list_button = Button(ToDo_Frame_List,
							text = "  Due List  ",
							font = ("Consolas", 10, "bold"),
							bg = "#363d4a", fg = "#FFFFFF",
							bd = 1, command = display_due_job)
	Due_list_button.place(x = 95)
	Due_list_button.bind("<Enter>", on_enter)
	Due_list_button.bind("<Leave>", on_leave)
	Due_list_button.bind("<ButtonRelease-1>", change_color_due)

	## No due list display button
	NoDue_list_button = Button(ToDo_Frame_List,
								text = "  No due List  ",
								font = ("Consolas", 10, "bold"),
								bg = "#363d4a", fg = "#FFFFFF",
								bd = 1, command = display_nodue_job)
	NoDue_list_button.place(x = 189)
	NoDue_list_button.bind("<Enter>", on_enter)
	NoDue_list_button.bind("<Leave>", on_leave)
	NoDue_list_button.bind("<ButtonRelease-1>", change_color_nodue)

	## Add Knap Sack list - filter list
	KnapSack_image = PhotoImage(file = "images/CustomButton/Filter_list.png")
	KnapSack_hover_image = PhotoImage(file = "images/CustomButton/Filter_list_hover.png")
	KnapSack_press_image = PhotoImage(file = "images/CustomButton/Filter_list_press.png")
	KnapSack_press_hover_image = PhotoImage(file = "images/CustomButton/Filter_list_press_hover.png")

	KnapSack_list_button = Button(ToDo_Frame_List,
								image = KnapSack_press_image,
								bg = "#2a5bba", fg = "#FFFFFF",
								bd = 1, command = display_filter_job)
	KnapSack_list_button.photo = KnapSack_image
	KnapSack_list_button.bind("<Enter>", change_hover_bttn)
	KnapSack_list_button.bind("<Leave>", back_to_normal)
	KnapSack_list_button.bind("<ButtonRelease-1>", press_button)

	Create_KnapSack_list = Button(ToDo_Frame_List,
								text = "+", font = ("Consolas", 15, "bold"),
								bg = "#363d4a", fg = "#FFFFFF",
								bd = 1, command = create_KnapSack)
	Create_KnapSack_list.place(x = 3, y = 23)

	### Function in doing list
	## Display value to listbox
	def display_all_job_doing():
		Doing_Listbox.delete(0, END)
		for i in range(0, len(Doing_list), 1):
			Doing_Listbox.insert(END, "  %s" %Doing_list[i].title)

	def display_due_job_doing():
		Doing_Listbox.delete(0, END)
		for i in range(0, len(Doing_list), 1):
			if Doing_list[i].DueBool == "True":
				Doing_Listbox.insert(END, "  %s" %Doing_list[i].title)

	def display_nodue_job_doing():
		Doing_Listbox.delete(0, END)
		for i in range(0, len(Doing_list), 1):
			if Doing_list[i].DueBool == "False":
				Doing_Listbox.insert(END, "  %s" %Doing_list[i].title)

	### Change color when press button - use for Doing List
	def change_color_main_doing(event):
		if main_list_doing.cget('bg') == "#545f73":
			Due_list_doing.config(bg = "#363d4a")
			NoDue_list_doing.config(bg = "#363d4a")
			main_list_doing.config(bg = "#2a5bba")

	def change_color_due_doing(event):
		if Due_list_doing.cget('bg') == "#545f73":
			Due_list_doing.config(bg = "#2a5bba")
			NoDue_list_doing.config(bg = "#363d4a")
			main_list_doing.config(bg = "#363d4a")

	def change_color_nodue_doing(event):
		if NoDue_list_doing.cget('bg') == "#545f73":
			Due_list_doing.config(bg = "#363d4a")
			NoDue_list_doing.config(bg = "#2a5bba")
			main_list_doing.config(bg = "#363d4a")

	### Doing List ###
	menu_function_doing = Menu(tearoff = False, font = ("Tahoma", 10))
	menu_function_doing.add_command(label = "Edit", command = lambda: edit_item_window(Doing_list, Doing_Listbox, Title[1]))
	menu_function_doing.add_command(label = "Mark as Complete", command = transfer_doing_Complete)
	menu_function_doing.add_command(label = 'Transfer back to To Do List', command = transfer_doing_toDo)
	menu_function_doing.add_separator()
	menu_function_doing.add_command(label = "Remove", command = remove_job_doing)

	Doing_Frame_List = Frame(bg_Content, bg = "#262a34", width = 350, height = 600)
	Doing_Frame_List.place(x = 345)

	Doing_Listbox = Listbox(Doing_Frame_List,
						font = ("Consolas", 21),
						width = 20, height = 0,
						bg = "#383e4d", fg = "#FFFFFF",
						bd = 0,
						highlightthickness = 0,
						activestyle = "none")
	Doing_Listbox.place(x = 29, y = 24)
	Doing_Listbox.bind("<Double-1>", edit_item_doing_)
	Doing_Listbox.bind("<Button-3>", popup_menu_doing)
	
	## Main List display button
	main_list_doing = Button(Doing_Frame_List,
							text = "  Main  ",
							font = ("Consolas", 10, "bold"),
							bg = "#2a5bba", fg = "#FFFFFF",
							bd = 1, command = display_all_job_doing)
	main_list_doing.place(x = 29)
	main_list_doing.bind("<Enter>", on_enter)
	main_list_doing.bind("<Leave>", on_leave)
	main_list_doing.bind("<ButtonRelease-1>", change_color_main_doing)

	## Due list display button
	Due_list_doing = Button(Doing_Frame_List,
							text = "  Due List  ",
							font = ("Consolas", 10, "bold"),
							bg = "#363d4a", fg = "#FFFFFF",
							bd = 1, command = display_due_job_doing)
	Due_list_doing.place(x = 95)
	Due_list_doing.bind("<Enter>", on_enter)
	Due_list_doing.bind("<Leave>", on_leave)
	Due_list_doing.bind("<ButtonRelease-1>", change_color_due_doing)

	## No due list display button
	NoDue_list_doing = Button(Doing_Frame_List,
								text = "  No due List  ",
								font = ("Consolas", 10, "bold"),
								bg = "#363d4a", fg = "#FFFFFF",
								bd = 1, command = display_nodue_job_doing)
	NoDue_list_doing.place(x = 189)
	NoDue_list_doing.bind("<Enter>", on_enter)
	NoDue_list_doing.bind("<Leave>", on_leave)
	NoDue_list_doing.bind("<ButtonRelease-1>", change_color_nodue_doing)

	# Alert label - scroll down to see more
	Alert_label_doing = Label(Doing_Frame_List,
						text = "Scroll down to see more",
						font = ("Consolas", 16, "bold"), bg = "#262a34",
						fg = "#FFFFFF")

	### Function in Complete list
	## Display value to listbox
	def display_all_job_complete():
		Comp_List.delete(0, END)
		for i in range(0, len(Complete_List), 1):
			Comp_List.insert(END, "  %s" %Complete_List[i].title)

		if len(submitted_late) != 0:
			for i in range(0, len(Complete_List), 1):
				for j in range(0, len(submitted_late), 1):
					if Complete_List[i].title == submitted_late[j]:
						Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")

	def display_due_job_complete():
		### temp list ###
		_temp_list_ = []

		Comp_List.delete(0, END)
		for i in range(0, len(Complete_List), 1):
			if Complete_List[i].DueBool == "True":
				Comp_List.insert(END, "  %s" %Complete_List[i].title)
				_temp_list_.append(Complete_List[i].title)

		if len(submitted_late) != 0:
			for i in range(0, len(_temp_list_), 1):
				for j in range(0, len(submitted_late), 1):
					if _temp_list_[i] == submitted_late[j]:
						Comp_List.itemconfig(i, bg = "#ed1e45", fg = "#FFFFFF")

	def display_nodue_job_complete():
		Comp_List.delete(0, END)
		for i in range(0, len(Complete_List), 1):
			if Complete_List[i].DueBool == "False":
				Comp_List.insert(END, "  %s" %Complete_List[i].title)

	### Change color when press button - use for Doing List
	def change_color_main_complete(event):
		if main_list_complete.cget('bg') == "#545f73":
			Due_list_complete.config(bg = "#363d4a")
			NoDue_list_complete.config(bg = "#363d4a")
			main_list_complete.config(bg = "#2a5bba")

	def change_color_due_complete(event):
		if Due_list_complete.cget('bg') == "#545f73":
			Due_list_complete.config(bg = "#2a5bba")
			NoDue_list_complete.config(bg = "#363d4a")
			main_list_complete.config(bg = "#363d4a")

	def change_color_nodue_complete(event):
		if NoDue_list_complete.cget('bg') == "#545f73":
			Due_list_complete.config(bg = "#363d4a")
			NoDue_list_complete.config(bg = "#2a5bba")
			main_list_complete.config(bg = "#363d4a")

	### Compelete Listbox ###
	menu_function_complete = Menu(tearoff = False, font = ("Tahoma", 10))
	menu_function_complete.add_command(label = "Edit", command = lambda: edit_item_window(Complete_List, Comp_List, Title[2]))
	menu_function_complete.add_command(label = 'Transfer back to Doing List', command = transfer_complete_doing)
	menu_function_complete.add_command(label = 'Transfer back to To Do List', command = transfer_complete_todo)
	menu_function_complete.add_separator()
	menu_function_complete.add_command(label = "Remove", command = remove_job_complete)

	Complete_Frame_List = Frame(bg_Content, bg = "#262a34", width = 350, height = 600)
	Complete_Frame_List.place(x = 696)

	Comp_List = Listbox(Complete_Frame_List,
						font = ("Consolas", 21),
						width = 20, height = 0,
						bg = "#383e4d", fg = "#FFFFFF",
						bd = 0,
						highlightthickness = 0,
						activestyle = "none")
	Comp_List.place(x = 29, y = 24)
	Comp_List.bind("<Double-1>", edit_item_complete_)
	Comp_List.bind("<Button-3>", popup_menu_Compelete)
	
	## Main List display button
	main_list_complete = Button(Complete_Frame_List,
							text = "  Main  ",
							font = ("Consolas", 10, "bold"),
							bg = "#2a5bba", fg = "#FFFFFF",
							bd = 1, command = display_all_job_complete)
	main_list_complete.place(x = 29)
	main_list_complete.bind("<Enter>", on_enter)
	main_list_complete.bind("<Leave>", on_leave)
	main_list_complete.bind("<ButtonRelease-1>", change_color_main_complete)

	## Due list display button
	Due_list_complete = Button(Complete_Frame_List,
							text = "  Due List  ",
							font = ("Consolas", 10, "bold"),
							bg = "#363d4a", fg = "#FFFFFF",
							bd = 1, command = display_due_job_complete)
	Due_list_complete.place(x = 95)
	Due_list_complete.bind("<Enter>", on_enter)
	Due_list_complete.bind("<Leave>", on_leave)
	Due_list_complete.bind("<ButtonRelease-1>", change_color_due_complete)

	## No due list display button
	NoDue_list_complete = Button(Complete_Frame_List,
								text = "  No due List  ",
								font = ("Consolas", 10, "bold"),
								bg = "#363d4a", fg = "#FFFFFF",
								bd = 1, command = display_nodue_job_complete)
	NoDue_list_complete.place(x = 189)
	NoDue_list_complete.bind("<Enter>", on_enter)
	NoDue_list_complete.bind("<Leave>", on_leave)
	NoDue_list_complete.bind("<ButtonRelease-1>", change_color_nodue_complete)

	# Alert label - scroll down to see more
	Alert_label_complete = Label(Complete_Frame_List,
						text = "Scroll down to see more",
						font = ("Consolas", 16, "bold"), bg = "#262a34",
						fg = "#FFFFFF")

	# Ribbon Tabs
	Ribbon_Tabs = Frame(Contain_LabelWidget, width = 1920, height = 82, bg = "#363d4a")
	Ribbon_Tabs.pack(anchor = "s")

	# Exit_Project = Button(Ribbon_Tabs, text = "exit", font = (20))
	# Exit_Project.place(x = 66, y = 47)

	def confirm_exit_changes():
		def confirm_change():
			exit_project()
			confirm_window_2.destroy()

		confirm_window_2 = Toplevel()
		confirm_window_2.geometry(f"370x100+{(confirm_window_2.winfo_screenwidth()//2) - (370//2)}+{(confirm_window_2.winfo_screenheight()//2) - (100//2)}")
		confirm_window_2.resizable(0, 0)
		confirm_window_2.wm_attributes('-topmost', 1)

		confirm_window_2.title("Confirm save changes")
		confirm_window_2.config(bg = "#262a34")

		confirm_label = Label(confirm_window_2,
							text = "Do you want to exit current project?",
							font = ("Consolas", 13), bg = "#262a34", fg = "#FFFFFF")
		confirm_label.place(x = 10, y = 15)

		confirm_yes = Button(confirm_window_2, text = "  Yes  ", font = ("Consolas", 11), bg = "#1544a0", fg = "#FFFFFF",
							command = confirm_change)
		confirm_yes.place(x = 120, y = 55)

		confirm_no = Button(confirm_window_2, text = "  No  ", font = ("Consolas", 11), bg = "#1544a0", fg = "#FFFFFF",
							command = lambda: confirm_window_2.destroy())
		confirm_no.place(x = 200, y = 55)

		confirm_cancel = Button(confirm_window_2, text = "  Cancel  ", font = ("Consolas", 11), bg = "#ed2249", fg = "#FFFFFF",
								command = lambda: confirm_window_2.destroy())
		confirm_cancel.place(x = 270, y = 55)


	def exit_project():
		global stayValue, empty_String, job_total, progress_value
		job_total = 0
		progress_value = 0

		### Clear list ###
		Job_list.clear()
		Doing_list.clear()
		Complete_List.clear()
		submitted_late.clear()

		note_list.clear()

		empty_String = ""

		Alert_label.place_forget()
		Alert_label_doing.place_forget()
		Alert_label_complete.place_forget()

		stayValue = False
		First_Frame_Personal.pack(fill = "both", expand = 1)
		Second_Frame_Personal.pack_forget()

		Open_Button_active.place_forget()
		Open_project_frame.place_forget()
		CreateNew_button_active.place_forget()
		create_Project_Frame.place_forget()

		### Adjust back to default - note list ###
		right_side_tab.config(width = 25)

		Home_Custombttn_active.place(x = 192)
		Title_func.config(text = "Create note")

		Create_note_button.place(x = 40, y = 120)
		
		## Clear all listbox ##
		note_listbox.delete(0, END)
		Todo_List.delete(0, END)
		Todo_List.config(height = len(Job_list))

		Doing_Listbox.delete(0, END)
		Doing_Listbox.config(height = len(Doing_list))

		Comp_List.delete(0, END)
		Comp_List.config(height = len(Complete_List))


		Search_Custombttn_active.place_forget()
		Entry_issues.delete(0, END)
		Entry_issues.place_forget()

		introduce_frame.place(x = 0, y = 0)

		Personal_Project_name.config(text = "")
		Team_Project_name.config(text = "0%s" %percent)
		Progress_display_value.config(text = "0%s" %percent)

		if len(note_list) <= 1:
			total_note.config(text = "You have %s note in total" %len(note_list))
		else:
			total_note.config(text = "You have %s notes in total" %len(note_list))


	#### Right size Frame function ####

	def change_color(event):
		event.widget.config(bg = "#5b6066")

	def change_color_leave(event):
		event.widget.config(bg = "#2b313c")

	def check_size_frame():
		if right_side_tab.cget('width') < 280:
			extract_window_()
			extract_button.config(text = " > ")
		else:
			contract_window_()
			extract_button.config(text = " < ")

	def extract_window_():
		size = int(right_side_tab.cget('width'))
		if (size < 280):
			size = size + 5
			right_side_tab.config(width = size)
			right_side_tab.after(3, extract_window_)		

	def contract_window_():
		size = int(right_side_tab.cget('width'))
		if size <= 280 and size > 25:
			size = size - 5
			right_side_tab.config(width = size)
			right_side_tab.after(4, contract_window_)

	#### On Horizontal bar ###
	def back_to_note():
		Home_Custombttn_active.place(x = 192)
		Search_Custombttn_active.place_forget()
		Entry_issues.place_forget()
		Create_note_button.place(x = 40, y = 120)
		Title_func.config(text = "Create note")

		Entry_issues.delete(0, END)

		note_listbox.delete(0, END)
		for i in range(0, len(note_list), 1):
			note_listbox.insert(END, " %s" %note_list[i].title)

	def go_to_search():
		Home_Custombttn_active.place_forget()
		Search_Custombttn_active.place(x = 236)
		Entry_issues.place(x = 40, y = 130)
		Create_note_button.place_forget()
		Title_func.config(text = "Search note")

		note_listbox.delete(0, END)
		for i in range(0, len(note_list), 1):
			note_listbox.insert(END, " %s" %note_list[i].title)

	### Create note ###
	def create_note():
		def create_():
			add_confirm = True
			
			if (Title_entry_.get()).strip() != "":
				if (Descript_entry.get('1.0', 'end-1c')).strip() != "":

					## check in list first ##
					for i in range(0, len(note_list), 1):
						if Title_entry_.get() == note_list[i].title:
							add_confirm = False

					if add_confirm == False:
						note_window.geometry(f"300x400+{note_window.winfo_screenwidth()//2 - 300//2}+{note_window.winfo_screenheight()//2 - 400//2}")
						Create_note_bttn.place(x = 100, y = 330)
						status_.config(text = "Note have already\nbeen created.", justify = "center")
						status_.place(x = 50, y = 260)
					else:
						note_listbox.delete(0, END)
						note_list.append(note_info((Title_entry_.get()).strip(), (Descript_entry.get('1.0', 'end-1c')).strip()))

						for i in range(0, len(note_list), 1):
							note_listbox.insert(END, " %s" %note_list[i].title)

						with open("Project/%s/%s/note_list" %(tag_number_int, empty_String), "w") as note_file:
							for i in range(0, len(note_list), 1):
								note_file.write("".join(str(note_list[i].title)))
								note_file.write("|")
								note_file.write("".join(str(note_list[i].descript)))
								note_file.write("\n")
						note_file.close()

						if len(note_list) <= 1:
							total_note.config(text = "You have %s note in total" %len(note_list))
						else:
							total_note.config(text = "You have %s notes in total" %len(note_list))

						note_window.destroy()
				else:
					note_window.geometry(f"300x400+{note_window.winfo_screenwidth()//2 - 300//2}+{note_window.winfo_screenheight()//2 - 400//2}")
					Create_note_bttn.place(x = 100, y = 330)
					status_.config(text = "Please add description.")
					status_.place(x = 20, y = 270)
			else:
				note_window.geometry(f"300x400+{note_window.winfo_screenwidth()//2 - 300//2}+{note_window.winfo_screenheight()//2 - 400//2}")
				Create_note_bttn.place(x = 100, y = 330)
				status_.config(text = "Please add title before\ncreating note.")
				status_.place(x = 20, y = 260)

		note_window = Toplevel()
		note_window.geometry(f"300x350+{note_window.winfo_screenwidth()//2 - 300//2}+{note_window.winfo_screenheight()//2 - 350//2}")
		note_window.resizable(0, 0)
		note_window.title("Create note")
		note_window.config(bg = "#2b313c")
		note_window.wm_attributes('-topmost', 1)

		Title_note = Label(note_window, text = "Title:", font = ("Consolas", 15), bg = "#2b313c", fg = "#FFFFFF")
		Title_note.place(x = 10, y = 10)

		Title_entry_ = Entry(note_window, font = ("Consolas", 18), width = 21)
		Title_entry_.place(x = 10, y = 45)

		Descript_label = Label(note_window, text = "Description", font = ("Consolas", 15), bg = "#2b313c", fg = "#FFFFFF")
		Descript_label.place(x = 10, y = 95)

		Descript_entry = Text(note_window, font = ("Consolas", 18), width = 21, height = 4)
		Descript_entry.place(x = 10, y = 130)

		Create_note_bttn = Button(note_window, text = "Create", font = ("Consolas", 18), bg = "#2a5bba", fg = "#FFFFFF", command = create_)
		Create_note_bttn.place(x = 100, y = 280)

		# Status label
		status_ = Label(note_window, font = ("Consolas", 15), bg = "#2b313c", fg = "#ed1e45")

	#### note list function - right click #####
	def edit_note_():
		empty_item = ""
		empty_int = 0

		for item in note_listbox.curselection():
			empty_item = note_listbox.get(item)

		for i in range(0, len(note_list), 1):
			if note_list[i].title == empty_item.strip():
				empty_int = i
				break

		def edit_():
			add_confirm = True
			
			if (Title_entry_.get()).strip() != "":
				if (Descript_entry.get('1.0', 'end-1c')).strip() != "":

					## check in list first ##
					for i in range(0, len(note_list), 1):
						if (Title_entry_.get()).strip() == note_list[i].title:
							add_confirm = False

					if add_confirm == False:
						edit_note_window.destroy()
					else:
						# note_listbox.insert(0, Title_entry_.get())
						note_listbox.delete(0, END)

						note_list.remove(note_list[empty_int])

						temp_st_list = []
						temp_st_list.append(note_info((Title_entry_.get()).strip(), (Descript_entry.get('1.0', 'end-1c').strip())))

						note_list.insert(0, temp_st_list[0])

						for i in range(0, len(note_list), 1):
							note_listbox.insert(END, " %s" %note_list[i].title)

						with open("Project/%s/%s/note_list" %(tag_number_int, empty_String), "w") as note_file:
							for i in range(0, len(note_list), 1):
								note_file.write("".join(str(note_list[i].title)))
								note_file.write("|")
								note_file.write("".join(str(note_list[i].descript)))
								note_file.write("\n")
						note_file.close()

						#### Clear entry if entry was typed before ####
						Entry_issues.delete(0, END)

						temp_st_list.clear()

						if len(note_list) <= 1:
							total_note.config(text = "You have %s note in total" %len(note_list))
						else:
							total_note.config(text = "You have %s notes in total" %len(note_list))

						edit_note_window.destroy()
				else:
					edit_note_window.geometry(f"300x400+{edit_note_window.winfo_screenwidth()//2 - 300//2}+{edit_note_window.winfo_screenheight()//2 - 400//2}")
					save_note_bttn.place(x = 70, y = 330)
					status_.config(text = "Please add description.")
					status_.place(x = 20, y = 270)
			else:
				edit_note_window.geometry(f"300x400+{edit_note_window.winfo_screenwidth()//2 - 300//2}+{edit_note_window.winfo_screenheight()//2 - 400//2}")
				save_note_bttn.place(x = 70, y = 330)
				status_.config(text = "Please add title before\ncreating note.")
				status_.place(x = 20, y = 260)

		edit_note_window = Toplevel()
		edit_note_window.title("Edit note")
		edit_note_window.geometry(f"300x350+{edit_note_window.winfo_screenwidth()//2 - 300//2}+{edit_note_window.winfo_screenheight()//2 - 350//2}")
		edit_note_window.resizable(0, 0)
		edit_note_window.config(bg = "#2b313c")
		edit_note_window.wm_attributes('-topmost', 1)

		Title_note = Label(edit_note_window, text = "Title:", font = ("Consolas", 15), bg = "#2b313c", fg = "#FFFFFF")
		Title_note.place(x = 10, y = 10)

		Title_entry_ = Entry(edit_note_window, font = ("Consolas", 18), width = 21)
		Title_entry_.place(x = 10, y = 45)
		Title_entry_.insert(END, note_list[empty_int].title)

		Descript_label = Label(edit_note_window, text = "Description", font = ("Consolas", 15), bg = "#2b313c", fg = "#FFFFFF")
		Descript_label.place(x = 10, y = 95)

		Descript_entry = Text(edit_note_window, font = ("Consolas", 18), width = 21, height = 4)
		Descript_entry.place(x = 10, y = 130)
		Descript_entry.insert(END, note_list[empty_int].descript)

		save_note_bttn = Button(edit_note_window, text = "Save change", font = ("Consolas", 18), bg = "#2a5bba", fg = "#FFFFFF", command = edit_)
		save_note_bttn.place(x = 70, y = 280)

		# Status label
		status_ = Label(edit_note_window, font = ("Consolas", 15), bg = "#2b313c", fg = "#ed1e45")

	def remove_note_():
		temp_item = ""

		### get selected value from listbox ###
		for item in note_listbox.curselection():
			temp_item = note_listbox.get(item)

		### remove value from list ###
		for i in range(0, len(note_list), 1):
			if note_list[i].title == temp_item.strip():
				note_list.remove(note_list[i])
				break

		note_listbox.delete(0, END)
		for i in range(0, len(note_list), 1):
			note_listbox.insert(END, " %s" %note_list[i].title)

		## rewrite value back to file ##
		with open("Project/%s/%s/note_list" %(tag_number_int, empty_String), "w") as note_file:
			for i in range(0, len(note_list), 1):
				note_file.write("".join(str(note_list[i].title)))
				note_file.write("|")
				note_file.write("".join(str(note_list[i].descript)))
				note_file.write("\n")
		note_file.close()

		Entry_issues.delete(0, END)

		if len(note_list) <= 1:
			total_note.config(text = "You have %s note in total" %len(note_list))
		else:
			total_note.config(text = "You have %s notes in total" %len(note_list))

	def search_note():
		pass

	def search_item(event):
		### get value in real time when typed ###
		typed = event.widget.get()

		### if typed variable equal " " or non blank
		if typed == "":
			note_listbox.delete(0, END)

			for i in range(0, len(note_list), 1):
				note_listbox.insert(END, " %s" %note_list[i].title)

		else:
			note_listbox.delete(0, END)

			for i in range(0, len(note_list), 1):
				if typed in note_list[i].title:
					note_listbox.insert(END, " %s" %note_list[i].title)

	### Clear all note ###
	def clearAll_note():
		def confirmClear():
			if os.path.isfile("Project/%s/%s/note_list" %(tag_number_int, empty_String)):
				# Clear list notes #
				note_list.clear()
				note_listbox.delete(0, END)

				### Clear search entry if it has any value in it ###
				Entry_issues.delete(0, END)

				open("Project/%s/%s/note_list" %(tag_number_int, empty_String), "w").close()

			confirm_window_5.destroy()

		confirm_window_5 = Toplevel()
		confirm_window_5.geometry(f"370x100+{(confirm_window_5.winfo_screenwidth()//2) - (370//2)}+{(confirm_window_5.winfo_screenheight()//2) - (100//2)}")
		confirm_window_5.resizable(0, 0)
		confirm_window_5.wm_attributes('-topmost', 1)

		confirm_window_5.title("Confirm save changes")
		confirm_window_5.config(bg = "#262a34")

		confirm_label = Label(confirm_window_5,
							text = "Do you want to sign out your account?",
							font = ("Consolas", 13), bg = "#262a34", fg = "#FFFFFF")
		confirm_label.place(x = 10, y = 15)

		confirm_yes = Button(confirm_window_5, text = "  Yes  ", font = ("Consolas", 11, "bold"), bg = "#1544a0", fg = "#FFFFFF",
							command = confirmClear)
		confirm_yes.place(x = 110, y = 55)

		confirm_no = Button(confirm_window_5, text = "  No  ", font = ("Consolas", 11, "bold"), bg = "#ed1e45", fg = "#FFFFFF",
							command = lambda: confirm_window_5.destroy())
		confirm_no.place(x = 190, y = 55)


	## Exit button image
	Exit_icon = PhotoImage(file = "images/Project window/Exit_icon.png")
	Exit_hover_icon = PhotoImage(file = "images/Project window/Exit_hover_icon.png")
	Exit_press_icon = PhotoImage(file = "images/Project window/Exit_press_icon.png")

	Exit_Project_bttn = CustomButton(Ribbon_Tabs,
									Exit_icon, Exit_hover_icon,
									Exit_press_icon,
									"#cd0134", "#800121", "#2db26f",
									66, 51, 0, confirm_exit_changes)

	Work_space = Label(Ribbon_Tabs, text = "Project managment: Working area", font = ("Consolas", 15), fg = "#9da6b1", bg = "#363d4a")
	Work_space.place(x = 120, y = 51)

	right_side_tab = Frame(Contain_LabelWidget, width = 25, height = 1080, bg = "#1e222a")
	right_side_tab.pack(anchor = "e", side = "right")

	horizontal_frame = Frame(right_side_tab, width = 500, height = 30, bg = "#9da6b1")
	horizontal_frame.place(x= 0)

	Note_label = Label(horizontal_frame, text = "| Note tab", font = ("Consolas", 15), bg = "#9da6b1")
	Note_label.place(x = 30)

	#### Custom button on horizontal bar ####
	Search_Custombttn = CustomButton(horizontal_frame,
									search_image,
									search_image_hover,
									search_image_press,
									"#2a5bba", "#173266", "#2b313c",
									236, 0, 1, go_to_search)
	Search_Custombttn_active = Label(horizontal_frame, image = search_image_press, bg = "#2b313c")

	Home_Custombttn = CustomButton(horizontal_frame,
									home_icon,
									home_icon_hover,
									home_icon_press,
									"#239947", "#17662f", "#2b313c",
									192, 0, 1, back_to_note)
	Home_Custombttn_active = Label(horizontal_frame, image = home_icon_press, bg = "#2b313c")
	Home_Custombttn_active.place(x = 192)

	vertical_frame = Frame(right_side_tab, width = 25 , height = 1080, bg = "#262a34")
	vertical_frame.place(x = 0)

	extract_button = Button(right_side_tab, text = " < ", font = ("Consolas", 8, "bold"), bg = "#2b313c", fg = "#FFFFFF", bd = 1, command = check_size_frame)
	extract_button.place(x = 0)
	extract_button.bind("<Enter>", change_color)
	extract_button.bind("<Leave>", change_color_leave)

	### Create issues tab ###
	Title_func = Label(right_side_tab, text = "Create note", font = ("Consolas", 15), bg = "#1e222a", fg = "#FFFFFF")
	Title_func.place(x = 40, y = 50)

	note_ = Label(right_side_tab, text = "Making note is really important\nwhen you need to remember something.",
					font = ("Consolas", 8), bg = "#1e222a", fg = "#44484d", justify = "left")
	note_.place(x = 40, y = 80)

	### Search widgets ###
	Entry_issues = Entry(right_side_tab, font = ("Consolas", 15), width = 18)
	Entry_issues.bind("<KeyRelease>", search_item)

	Create_note_button = Button(right_side_tab, text = "Create note", font = ("Consolas", 15), bg = "#2a5bba", fg = "#FFFFFF", bd = 1, command = create_note)
	Create_note_button.place(x = 40, y = 120)

	#### Line separator ####
	line_sep = Label(right_side_tab, text = "____________________", font = ("Consolas"), bg = "#1e222a", fg = "#FFFFFF")
	line_sep.place(x = 40, y = 160)

	### Listbox contain note ###
	menu_function_notelist = Menu(tearoff = False, font = ("Tahoma", 10))
	menu_function_notelist.add_command(label = "Edit", command = edit_note_)
	menu_function_notelist.add_command(label = "Remove", command = remove_note_)

	note_listbox = Listbox(right_side_tab,
						font = ("Consolas", 15),
						width = 20, height = 20,
						bg = "#383e4d", fg = "#FFFFFF",
						bd = 0,
						highlightthickness = 0,
						activestyle = "none")
	note_listbox.place(x = 40, y = 230)
	note_listbox.bind("<Button-3>", popup_menu_notelist)

	total_note = Label(right_side_tab, text = "You have %s note in total" %len(note_list), font = ("Consolas", 10), bg = "#1e222a", fg = "#55aaff")
	total_note.place(x = 40, y = 195)

	ClearAll_button = Button(right_side_tab, text = "    Clear all    ", font = ("Consolas", 15), bg = "#ed1e45", fg = "#FFFFFF", command = clearAll_note)
	ClearAll_button.place(x = 48, y = 730)


	# Chart_Button = Button(Ribbon_Tabs, text = "Chart Board", font = (20))
	# Chart_Button.place(x = 104, y = 47)

	# Edit_Button = Button(Ribbon_Tabs, text = "Edit Project", font = (20))
	# Edit_Button.place(x = 204, y = 47)


	#-----------------------------------------------------------------#
	### Left Side Button
	# Left Side Frame
	leftside_frame = Frame(root, bg = "#1e222a", height = 1080, width = 65)
	leftside_frame.place(x = 0, y = 30)

	# Top Bar Function
	descriptionBar = Frame(root, bg = "#1e222a", width = 1920, height = 50)
	descriptionBar.place(x = 0, y = 0)

	# Toggle Button
	ToggleButton = CustomButton(root,
								Toggle_image,
								hoverPic_Toggle,
								pressPic_Toggle,
								"#1e222a", "#2b313c", "#1544a0",
								0, 0, 0, expand_window_check)

	# Home Button
	Home_Button = CustomButton(leftside_frame,
								Home_image,
								hoverPic_Home,
								pressPic_Home,
								"#1e222a", "#2b313c", "#1544a0",
								0, 18, 0, pressHome)

	Home_Button_active = Label(leftside_frame, image = pressPic_Home, bg = "#1544a0", bd = 0)
	Home_Button_active.place(x = 0, y = 18)

	# Personal Button
	Personal_Button = CustomButton(leftside_frame,
									Personal_image,
									hoverPic_Personal,
									pressPic_Personal,
									"#1e222a", "#2b313c", "#1544a0",
									0, 78, 0, pressPersonal)

	Personal_Button_active = Label(leftside_frame, image = pressPic_Personal, bg = "#1544a0", bd = 0)


	### Current Project Progress ###
	Progress_text = Label(descriptionBar, text = "Current project progress: ", font = ("Consolas", 15), bg = "#1e222a", fg = "#b3b3b3")
	Progress_text.place(x = 380, y = 10)

	Progress_display_value = Label(descriptionBar, text = "0%s" %percent, font = ("Consolas", 15), bg = "#1e222a", fg = "#b3b3b3")
	Progress_display_value.place(x = 665, y = 10)

	### user display top left Frame ###

	def expand_FrameUser():
		size = UserTopLeft_frame.cget('height')

		if size < 120:
			size += 5
			UserTopLeft_frame.config(height = size)
			UserTopLeft_frame.after(4, expand_FrameUser)

	def contract_Frameuser():
		size = UserTopLeft_frame.cget('height')

		if size <= 120 and size > 50:
			size -= 5
			UserTopLeft_frame.config(height = size)
			UserTopLeft_frame.after(4, contract_Frameuser)


	UserTopLeft_frame = Frame(root, width = 300, height = 50, bg = "#13171c")
	UserTopLeft_frame.place(x = 65)

	avatar_frame = Frame(UserTopLeft_frame, width = 5, height = 40, bg = "#55aaff")
	avatar_frame.place(x = 10, y = 5)

	display_nameTopBar = Label(UserTopLeft_frame, text = "Name:", font = ("Consolas", 13, "bold"), bg = "#13171c", fg = "#55aaff")
	display_nameTopBar.place(x = 30, y = 2)

	display_nameText = Label(UserTopLeft_frame, text = display_name_onScreen, font = ("Consolas", 13), bg = "#13171c", fg = "#FFFFFF")
	display_nameText.place(x = 85, y = 2)

	display_tagLabel = Label(UserTopLeft_frame, text = "ID Number:", font = ("Consolas", 10, "bold"), bg = "#13171c", fg = "#55aaff")
	display_tagLabel.place(x = 30, y = 25)

	TagNumber_Label = Label(UserTopLeft_frame, text = tag_number_int, font = ("Consolas", 10), bg = "#13171c", fg = "#FFFFFF")
	TagNumber_Label.place(x = 108, y = 25)

	#### Dropdown icon ####
	dropdown_icon = PhotoImage(file = "images/dropdown_icon.png")
	dropdown_hover = PhotoImage(file = "images/dropdown_hover_icon.png")

	dropdown_reverse_icon = PhotoImage(file = "images/dropdown_icon_reverse.png")
	dropdown_reverse_hover = PhotoImage(file = "images/dropdown_hover_icon_reverse.png")

	### Expand user frame ###
	def expand_userFrame():
		global pressButton_bool

		if pressButton_bool == False:
			dropdown_button.config(image = dropdown_reverse_icon, bg = "#1e222a")
			dropdown_button.photo = dropdown_reverse_icon

			expand_FrameUser()

			pressButton_bool = True

		else:
			dropdown_button.config(image = dropdown_icon, bg = "#1e222a")
			dropdown_button.photo = dropdown_icon

			contract_Frameuser()

			pressButton_bool = False

	### Function ###
	def defaultColor_icon(event):
		global pressButton_bool

		if pressButton_bool == False:
			dropdown_button.config(image = dropdown_icon, bg = "#1e222a")
			dropdown_button.photo = dropdown_icon

		else:
			dropdown_button.config(image = dropdown_reverse_icon, bg = "#1e222a")
			dropdown_button.photo = dropdown_reverse_icon

	def change_color_icon(event):
		global pressButton_bool

		if pressButton_bool == False:
			dropdown_button.config(image = dropdown_hover, bg = "#2b313c")
			dropdown_button.photo = dropdown_hover

		else:
			dropdown_button.config(image = dropdown_reverse_hover, bg = "#2b313c")
			dropdown_button.photo = dropdown_reverse_hover


	dropdown_button = Button(UserTopLeft_frame, image = dropdown_icon, bg = "#1e222a", bd = 1, command = expand_userFrame)
	dropdown_button.photo = dropdown_icon
	dropdown_button.place(x = 250, y = 8)
	dropdown_button.bind("<Enter>", change_color_icon)
	dropdown_button.bind("<Leave>", defaultColor_icon)


	### Function in Button ###
	def hover_button(event):
		event.widget.config(bg = "#2b313c")

	def default_color(event):
		event.widget.config(bg = "#13171c")


	### Function - Log out ###
	def LogEverythingOut():
		global login_bool, empty_String, display_name_onScreen, username_saved, username_find_temp, flag_sort, time_limit_value, full_displayname

		## Clear all list ##
		Job_list.clear()
		Doing_list.clear()
		Complete_List.clear()
		submitted_late.clear()
		note_list.clear()

		### Clear all listbox ###
		Todo_List.delete(0, END)
		Doing_Listbox.delete(0, END)
		Comp_List.delete(0, END)
		note_listbox.delete(0, END)		

		leftside_frame.config(width = 65)
		right_side_tab.config(width = 25)		

		tag_number_int = ""

		login_bool = False

		open("keep_login", "w").close()

		empty_String = ""
		display_name_onScreen = ""
		full_displayname = ""

		username_saved = ""
		username_find_temp = ""
		stayValue = False

		job_total = 0
		progress_value = 0

		flag_sort = False

		Filter_list_og.clear()
		KnapSack_list.clear()
		time_limit_value = 0

		Temp_list.clear()
		Project_list.clear()
		List_account.clear()
		Login_account.clear()


		root.destroy()
		login_window()

	def LogOut():
		global pressButton_bool
		pressButton_bool = False

		dropdown_button.config(image = dropdown_icon, bg = "#1e222a")
		dropdown_button.photo = dropdown_icon
		contract_Frameuser()

		def confirm_change():
			global stayValue, job_total, progress_value, count_stop, count_expand, stop_widget

			stayValue = False
			job_total = 0
			progress_value = 0
			
			count_stop = 0
			count_expand = 0
			stop_widget = False

			LogEverythingOut()


		confirm_window_3 = Toplevel()
		confirm_window_3.geometry(f"370x100+{(confirm_window_3.winfo_screenwidth()//2) - (370//2)}+{(confirm_window_3.winfo_screenheight()//2) - (100//2)}")
		confirm_window_3.resizable(0, 0)
		confirm_window_3.wm_attributes('-topmost', 1)

		confirm_window_3.title("Confirm save changes")
		confirm_window_3.config(bg = "#262a34")

		confirm_label = Label(confirm_window_3,
							text = "Do you want to sign out your account?",
							font = ("Consolas", 13), bg = "#262a34", fg = "#FFFFFF")
		confirm_label.place(x = 10, y = 15)

		confirm_yes = Button(confirm_window_3, text = "  Yes  ", font = ("Consolas", 11, "bold"), bg = "#1544a0", fg = "#FFFFFF",
							command = confirm_change)
		confirm_yes.place(x = 110, y = 55)

		confirm_no = Button(confirm_window_3, text = "  No  ", font = ("Consolas", 11, "bold"), bg = "#ed1e45", fg = "#FFFFFF",
							command = lambda: confirm_window_3.destroy())
		confirm_no.place(x = 190, y = 55)

		confirm_cancel = Button(confirm_window_3, text = "  Cancel  ", font = ("Consolas", 11), bg = "#ed2249", fg = "#FFFFFF",
								command = lambda: confirm_window_3.destroy())


	### Setting window ###
	def setting_window():
		global pressButton_bool, full_displayname, EditDisplayName, EditPassword, Edit_Email, display_name_onScreen
		List_account.clear()
		check_file()

		### Check which edit button turn on ###
		EditDisplayName = False
		EditPassword = False
		Edit_Email = False

		### temp id ###
		temp_id_use = 0

		### star letter to hide text ###
		star_string = ""

		for i in range(0, len(List_account), 1):
			if List_account[i].username == username_saved:
				temp_id_use = i
				break

		emailUse_display = str(List_account[temp_id_use].email).split("@")
		emailGet = emailUse_display[0]

		for i in range(1, len(emailGet), 1):
			star_string += "*"

		emailGet = emailGet[:1] + star_string
		complete_emailDisplay = emailGet + "@" + emailUse_display[1]

		pressButton_bool = False

		dropdown_button.config(image = dropdown_icon, bg = "#1e222a")
		dropdown_button.photo = dropdown_icon
		contract_Frameuser()

		setting_window = Toplevel()
		setting_window.geometry(f"730x560+{setting_window.winfo_screenwidth()//2 - 730//2}+{setting_window.winfo_screenheight()//2 - 560//2}")
		setting_window.resizable(0, 0)
		setting_window.title("User settings")
		setting_window.config(bg = "#1e222a")


		### Function ###
		## Turn on edit display name ##
		def turnOnDisplay():
			global EditDisplayName

			if EditDisplayName == False:

				EditDisplayName = True

				DisplayName_entry.config(state = NORMAL, bg = "#FFFFFF", fg = "#000000", bd = 1)
				DisplayName_entry.delete(0, END)
				DisplayName_entry.insert(END, full_displayname)

			else:
				EditDisplayName = False

				DisplayName_entry.config(state = NORMAL)
				DisplayName_entry.delete(0, END)
				DisplayName_entry.insert(END, display_name_onScreen)
				DisplayName_entry.config(state = "readonly", readonlybackground = "#1e222a", fg = "#FFFFFF", bd = 0)

		## Turn on edit Password ##
		def turnOnPassword():
			global EditPassword

			if EditPassword == False:

				EditPassword = True

				passwordReview_entry.config(state = NORMAL, bg = "#FFFFFF", fg = "#000000", bd = 1)
				passwordReview_entry.delete(0, END)

			else:
				EditPassword = False

				passwordReview_entry.config(state = NORMAL)
				passwordReview_entry.delete(0, END)
				passwordReview_entry.insert(END, "***********")
				passwordReview_entry.config(state = "readonly", readonlybackground = "#1e222a", fg = "#FFFFFF", bd = 0)

		## Turn on edit email ##
		def turnOnEmail():
			global Edit_Email, new_email, verification_code

			new_email = ""
			verification_code = ""
			verify_entry.delete(0, END)

			if Edit_Email == False:

				Edit_Email = True

				Email_entry.config(state = NORMAL, bg = "#FFFFFF", fg = "#000000", bd = 1, width = 25)
				Email_entry.delete(0, END)
				Email_entry.insert(END, List_account[temp_id_use].email)

				setting_window.geometry("730x620")

				TagNumber_Lbl.place(x = 200, y = 450)
				TagNumber_display.place(x = 340, y = 452)
				SaveChangeButton.place(x = 270, y = 535)

				IDNumber_tip.place(x = 180, y = 450)

				SendVerifyCode.place(x = 100, y = 380)

				verify_entry.place(x = 291, y = 380)


			else:
				Edit_Email = False

				Email_entry.config(state = NORMAL)
				Email_entry.delete(0, END)
				Email_entry.insert(END, complete_emailDisplay)
				Email_entry.config(width = len(complete_emailDisplay))
				Email_entry.config(state = "readonly", readonlybackground = "#1e222a", fg = "#FFFFFF", bd = 0)

				setting_window.geometry("730x560")

				TagNumber_Lbl.place(x = 200, y = 390)
				TagNumber_display.place(x = 340, y = 392)
				SaveChangeButton.place(x = 270, y = 475)

				IDNumber_tip.place(x = 180, y = 390)

				SendVerifyCode.place_forget()
				verify_entry.place_forget()


		### Function Save change ###
		def write_newUserFile():
			with open("user", "w") as newUser_file:
				for i in range(0, len(List_account), 1):
					newUser_file.write("".join(str(List_account[i].username)))
					newUser_file.write("|")
					newUser_file.write("".join(str(List_account[i].password)))
					newUser_file.write("|")
					newUser_file.write("".join(str(List_account[i].display_name)))
					newUser_file.write("|")
					newUser_file.write("".join(str(List_account[i].email)))
					newUser_file.write("|")
					newUser_file.write("".join(str(List_account[i].tag_number)))
					newUser_file.write("\n")
			newUser_file.close()

		def sendVerify_Code():
			global verification_code, username_saved, new_email

			if Email_entry.get() != "":
				if Email_entry.get() != List_account[temp_id_use].email:
					if (Email_entry.get()).strip() != "" and check_valid_email(Email_entry.get()) == True and bool(re.search(r"\s", Email_entry.get())) == False and search_keyword(upper, Email_entry.get()) == False :

						new_email = Email_entry.get()

						verification_code = ""
						random_choices = random.choices(list(all_string), k = 7)

						for i in range(0, len(random_choices), 1):
							verification_code += str(random_choices[i])

						# ## Send to desktop ##
						# with open("C:/Users/Cryptor/Desktop/Verification code.txt", "w") as verify_code:
						# 	verify_code.write("Username: " + str(username_saved))
						# 	verify_code.write("\n")
						# 	verify_code.write("Your verification code to change new email: "+ str(verification_code))
						# 	verify_code.write("\n")
						# 	verify_code.write("You email you want to change to: "+str(new_email))
						# verify_code.close()

						## Send to Mail folder ##
						with open("Mail/Verification code.txt", "w") as verify_code:
							verify_code.write("Username: " + str(username_saved))
							verify_code.write("\n")
							verify_code.write("Your verification code to change new email: "+ str(verification_code))
							verify_code.write("You email you want to change to: "+str(new_email))
						verify_code.close()


						error_window("Your verification code already\nbeen sent to your email.", 30, 10, 13)

					else:
						error_window("Your new email is invalid.\nPlease try again.", 55, 10, 13)

				else:
					error_window("Your current email are similar\nto the old one.", 30, 10, 13)

			else:
				error_window("Email entry is empty.", 40, 20, 15)

		def save_change_user():
			global EditDisplayName, EditPassword, Edit_Email, full_displayname, display_name_onScreen, verification_code, new_email
			if EditDisplayName == True:
				if EditPassword == True:
					if Edit_Email == True:
						print("Change displayname, password and email")
						
						if (DisplayName_entry.get()).strip() != "" and ("|" in (DisplayName_entry.get()).strip()) == False:

							if (passwordReview_entry.get()).strip() != "":

								## if display name are the same only change password and email ##
								if List_account[temp_id_use].display_name == (DisplayName_entry.get()).strip():

									if List_account[temp_id_use].password != sha1(passwordReview_entry.get()):

										if (passwordReview_entry.get()).strip() != "" and search_keyword(symbol, passwordReview_entry.get()) == False and search_keyword(upper, passwordReview_entry.get()) == True and search_keyword(number, passwordReview_entry.get()) == True:

											if len(passwordReview_entry.get()) >= 10:

												if (verify_entry.get()).strip() != "":
													if Email_entry.get() == new_email:
														if verification_code == verify_entry.get():

															print("Change only password and email")

															List_account[temp_id_use].password = sha1(passwordReview_entry.get())
															List_account[temp_id_use].email = new_email

															write_newUserFile()
															
															## Close window after complete processs
															setting_window.destroy()

														else:
															error_window("Your verification code is either\ninvalid or have already been expired.", 22, 10, 11)

													else:
														error_window("Your email entry doesn't match\nwith new email we send verify code to.", 18, 10, 11)

												else:
													error_window("Please complete your change email\nprocress before making any changes.", 18, 10, 12)

											else:
												error_window("Your password is too weak.\nTry again.", 55, 10, 13)

										else:
											error_window("Your password need to contain aleast\n1 uppercase character and 1 number.", 12, 10, 13)

									else:
										error_window("Your current password are similar\nto the old one.", 30, 10, 13)


								## If display name are different change everything ##
								elif List_account[temp_id_use].display_name != (DisplayName_entry.get()).strip():

									if List_account[temp_id_use].password != sha1(passwordReview_entry.get()):

										if (passwordReview_entry.get()).strip() != "" and search_keyword(symbol, passwordReview_entry.get()) == False and search_keyword(upper, passwordReview_entry.get()) == True and search_keyword(number, passwordReview_entry.get()) == True:

											if len(passwordReview_entry.get()) >= 10:

												if (verify_entry.get()).strip() != "":
													if Email_entry.get() == new_email:
														if verification_code == verify_entry.get():
															print("Change everything")

															List_account[temp_id_use].display_name = (DisplayName_entry.get()).strip()
															List_account[temp_id_use].password = sha1(passwordReview_entry.get())
															List_account[temp_id_use].email = new_email

															full_displayname = List_account[temp_id_use].display_name

															if len(full_displayname) > 12:
																display_name_onScreen = full_displayname[:12] + ".."
															else:
																display_name_onScreen = full_displayname

															display_nameText.config(text = display_name_onScreen)														

															write_newUserFile()
															
															## Close window after complete processs
															setting_window.destroy()

														else:
															error_window("Your verification code is either\ninvalid or have already been expired.", 22, 10, 11)

													else:
														error_window("Your email entry doesn't match\nwith new email we send verify code to.", 18, 10, 11)

												else:
													error_window("Please complete your change email\nprocress before making any changes.", 18, 10, 12)											

											else:
												error_window("Your password is too weak.\nTry again.", 55, 10, 13)

										else:
											error_window("Your password need to contain aleast\n1 uppercase character and 1 number.", 12, 10, 13)

									else:
										error_window("Your current password are similar\nto the old one.", 20, 10, 13)

							else:
								error_window("Password entry is empty.", 40, 20, 15)

						else:
							error_window("Display name is empty or\ncontains some invalid keywords.", 30, 10, 13)

					else:
						display_name_onScreen = ""
						print("Change displayname and password")

						if (DisplayName_entry.get()).strip() != "" and ("|" in (DisplayName_entry.get()).strip()) == False:

							if (passwordReview_entry.get()).strip() != "":

								if List_account[temp_id_use].display_name == (DisplayName_entry.get()).strip():

									if List_account[temp_id_use].password != sha1(passwordReview_entry.get()):

										if (passwordReview_entry.get()).strip() != "" and search_keyword(symbol, passwordReview_entry.get()) == False and search_keyword(upper, passwordReview_entry.get()) == True and search_keyword(number, passwordReview_entry.get()) == True:

											if len(passwordReview_entry.get()) >= 10:

												List_account[temp_id_use].password = sha1(passwordReview_entry.get())

												write_newUserFile()
												### Close window after complete process
												setting_window.destroy()

											else:
												error_window("Your password is too weak.\nTry again.", 55, 10, 13)

										else:
											error_window("Your password need to contain aleast\n1 uppercase character and 1 number.", 12, 10, 13)

									else:
										error_window("Your current password are similar\nto the old one.", 30, 10, 13)


								elif List_account[temp_id_use].display_name != (DisplayName_entry.get()).strip():

									if List_account[temp_id_use].password != sha1(passwordReview_entry.get()):

										if (passwordReview_entry.get()).strip() != "" and search_keyword(symbol, passwordReview_entry.get()) == False and search_keyword(upper, passwordReview_entry.get()) == True and search_keyword(number, passwordReview_entry.get()) == True:

											if len(passwordReview_entry.get()) >= 10:

												List_account[temp_id_use].display_name = (DisplayName_entry.get()).strip()
												List_account[temp_id_use].password = sha1(passwordReview_entry.get())

												write_newUserFile()

												full_displayname = List_account[temp_id_use].display_name

												if len(full_displayname) > 12:
													display_name_onScreen = full_displayname[:12] + ".."
												else:
													display_name_onScreen = full_displayname

												display_nameText.config(text = display_name_onScreen)
												## Close window after complete processs
												setting_window.destroy()

											else:
												error_window("Your password is too weak.\nTry again.", 55, 10, 13)

										else:
											error_window("Your password need to contain aleast\n1 uppercase character and 1 number.", 12, 10, 13)

									else:
										error_window("Your current password are similar\nto the old one.", 20, 10, 13)

							else:
								error_window("Password entry is empty.", 40, 20, 15)

						else:
							error_window("Display name is empty or\ncontains some invalid keywords.", 30, 10, 13)


				elif Edit_Email == True:
					print("Change displayname and email")

					if (DisplayName_entry.get()).strip() != "" and ("|" in (DisplayName_entry.get()).strip()) == False:

						if (verify_entry.get()).strip() != "":

							if Email_entry.get() == new_email:

								if verification_code == verify_entry.get():

									### change to new email and display name ###
									List_account[temp_id_use].email = new_email
									List_account[temp_id_use].display_name = (DisplayName_entry.get()).strip()

									full_displayname = List_account[temp_id_use].display_name

									if len(full_displayname) > 12:
										display_name_onScreen = full_displayname[:12] + ".."
									else:
										display_name_onScreen = full_displayname

									display_nameText.config(text = display_name_onScreen)

									write_newUserFile()

									## Close window after complete process ##
									setting_window.destroy()

								else:
									error_window("Your verification code is either\ninvalid or have already been expired.", 22, 10, 11)

							else:
								error_window("Your email entry doesn't match\nwith new email we send verify code to.", 18, 10, 11)

						else:
							error_window("Please complete your change email\nprocress before making any changes.", 18, 10, 12)

					else:
						error_window("Display name is empty or\ncontains some invalid keywords.", 30, 10, 13)

				else:
					print("Change only display name")

					if (DisplayName_entry.get()).strip() != "" and ("|" in (DisplayName_entry.get()).strip()) == False:

						### Display name - If old display name = new display name - do nothing ###
						if List_account[temp_id_use].display_name != (DisplayName_entry.get()).strip():

							List_account[temp_id_use].display_name = (DisplayName_entry.get()).strip()
							write_newUserFile()

							full_displayname = List_account[temp_id_use].display_name

							if len(full_displayname) > 12:
								display_name_onScreen = full_displayname[:12] + ".."
							else:
								display_name_onScreen = full_displayname

							display_nameText.config(text = display_name_onScreen)

							setting_window.destroy()

						else:
							setting_window.destroy()

					else:
						error_window("Display name is empty or\ncontains some invalid keywords.", 30, 10, 13)


			elif EditPassword == True:
				if Edit_Email == True:
					print("Change PW and Email")

					# Check password first #
					if (passwordReview_entry.get()).strip() != "":
						if List_account[temp_id_use].password != sha1(passwordReview_entry.get()):

							if (passwordReview_entry.get()).strip() != "" and search_keyword(symbol, passwordReview_entry.get()) == False and search_keyword(upper, passwordReview_entry.get()) == True and search_keyword(number, passwordReview_entry.get()) == True:

								if len(passwordReview_entry.get()) >= 10:

									## Check email second ##
									if (verify_entry.get()).strip() != "":

										if Email_entry.get() == new_email:

											if verification_code == verify_entry.get():

												## Change to new value ##
												List_account[temp_id_use].password = sha1(passwordReview_entry.get())
												List_account[temp_id_use].email = new_email

												write_newUserFile()

												## Close window after complete changing value ##
												setting_window.destroy()

											else:
												error_window("Your verification code is either\ninvalid or have already been expired.", 22, 10, 11)

										else:
											error_window("Your email entry doesn't match\nwith new email we send verify code to.", 18, 10, 11)

									else:
										error_window("Please complete your change email\nprocress before making any changes.", 18, 10, 12)

								else:
									error_window("Your password is too weak.\nTry again.", 55, 10, 13)

							else:
								error_window("Your password need to contain aleast\n1 uppercase character and 1 number.", 12, 10, 13)

						else:
							error_window("Your current password are similar\nto the old one.", 20, 10, 13)

					else:
						error_window("Password entry is empty.", 40, 20, 15)


				else:
					print("Change only password")

					if (passwordReview_entry.get()).strip() != "":
						if List_account[temp_id_use].password != sha1(passwordReview_entry.get()):

							if (passwordReview_entry.get()).strip() != "" and search_keyword(symbol, passwordReview_entry.get()) == False and search_keyword(upper, passwordReview_entry.get()) == True and search_keyword(number, passwordReview_entry.get()) == True:

								if len(passwordReview_entry.get()) >= 10:									

									## Change password user ##
									List_account[temp_id_use].password = sha1(passwordReview_entry.get())

									write_newUserFile()

									## Close window after complete process ##
									setting_window.destroy()

								else:
									error_window("Your password is too weak.\nTry again.", 55, 10, 13)

							else:
								error_window("Your password need to contain aleast\n1 uppercase character and 1 number.", 12, 10, 13)

						else:
							error_window("Your current password are similar\nto the old one.", 20, 10, 13)

					else:
						error_window("Password entry is empty.", 40, 20, 15)

			elif Edit_Email == True:
				print("Change only email")

				if (verify_entry.get()).strip() != "":
					if Email_entry.get() == new_email:
						if verification_code == verify_entry.get():
							List_account[temp_id_use].email = new_email

							write_newUserFile()

							## Close window after complete process ##
							setting_window.destroy()

						else:
							error_window("Your verification code is either\ninvalid or have already been expired.", 22, 10, 11)

					else:
						error_window("Your email entry doesn't match\nwith new email we send verify code to.", 18, 10, 11)

				else:
					error_window("Please complete your change email\nprocress before making any changes.", 18, 10, 12)

						# send verification code #			

			else:
				setting_window.destroy()

		def DeleteUser():
			def confirmDelete():
				global stayValue

				stayValue = False

				Home_Button_active.place(x = 0, y = 18)
				Home_Button_active.config(image = Home_image)

				Personal_Button_active.place(x = 0, y = 78)
				Personal_Button_active.config(image = Personal_image)

				Team_Button_active.place(x = 0, y = 138)
				Team_Button_active.config(image = Team_image)

				First_Frame_Personal.pack_forget()
				Second_Frame_Personal.pack_forget()

				bg_Frame_Home.pack_forget()

				confirm_window_6.destroy()

				setting_window.destroy()

				dropdown_button.config(state = DISABLED)

				### destory/quit everthing ###
				def quiteverything():
					### Delete folder first ###
					if os.path.exists("Project/%s" %tag_number_int):
						shutil.rmtree("Project/%s" %tag_number_int)

					### Delete from 
					List_account.remove(List_account[temp_id_use])

					write_newUserFile()

					LogEverythingOut()

				error_WD = Toplevel()
				error_WD.geometry("")

				error_WD.title("Oops! Somethings went wrong.")
				error_WD.resizable(0, 0)
				error_WD.wm_attributes("-topmost", 1)

				error_WD_w = 380
				error_WD_h = 110

				postiion_error_WD_x = (error_WD.winfo_screenwidth()//2) - (error_WD_w//2)
				position_error_WD_y = (error_WD.winfo_screenheight()//2) - (error_WD_h//2)

				error_WD.geometry(f"{error_WD_w}x{error_WD_h}+{postiion_error_WD_x}+{position_error_WD_y}")
				error_WD.config(bg = "#1e222a")

				alert_window = Label(error_WD, text = "Press OK, your account will be deleted\nand you will be sent back to log in screen.", font = ("Consolas", 11), bg = "#1e222a", fg = "#FFFFFF")
				alert_window.place(x = 15, y = 10)

				close_button = Button(error_WD, text = "   OK   ", font = ("Consolas", 12), bg = "#2a5bba", fg = "#FFFFFF", command = quiteverything)
				close_button.place(x = 140, y = 68)

			confirm_window_6 = Toplevel()
			confirm_window_6.geometry(f"370x230+{(confirm_window_6.winfo_screenwidth()//2) - (370//2)}+{(confirm_window_6.winfo_screenheight()//2) - (230//2)}")
			confirm_window_6.resizable(0, 0)
			confirm_window_6.wm_attributes('-topmost', 1)

			confirm_window_6.title("Confirm save changes")
			confirm_window_6.config(bg = "#262a34")

			confirm_label = Label(confirm_window_6,
								text = "Do you want to delete your account?\nPlease note that once you deleted,\nyour account will be gone so be\ncareful with your action.",
								font = ("Consolas", 13, "bold"), bg = "#262a34", fg = "#FFFFFF", justify = "left")
			confirm_label.place(x = 10, y = 15)

			confirm_yes = Button(confirm_window_6, text = "  Yes, delete it.  ", font = ("Consolas", 13, "bold"), bg = "#1544a0", fg = "#FFFFFF",
								command = confirmDelete)
			confirm_yes.place(x = 40, y = 127)

			confirm_no = Button(confirm_window_6, text = "  Noooo! Don't do it.  ", font = ("Consolas", 13, "bold"), bg = "#ed1e45", fg = "#FFFFFF",
								command = lambda: confirm_window_6.destroy())
			confirm_no.place(x = 40, y = 175)


		def confirm_anyChange():
			def confirm_change():
				save_change_user()
				confirm_window_4.destroy()

			def deny_saveChange():
				setting_window.destroy()
				confirm_window_4.destroy()

			confirm_window_4 = Toplevel()
			confirm_window_4.geometry(f"370x100+{(confirm_window_4.winfo_screenwidth()//2) - (370//2)}+{(confirm_window_4.winfo_screenheight()//2) - (100//2)}")
			confirm_window_4.resizable(0, 0)
			confirm_window_4.wm_attributes('-topmost', 1)

			confirm_window_4.title("Confirm save changes")
			confirm_window_4.config(bg = "#262a34")

			confirm_label = Label(confirm_window_4,
								text = "Do you want to save your changes?",
								font = ("Consolas", 13), bg = "#262a34", fg = "#FFFFFF")
			confirm_label.place(x = 10, y = 15)

			confirm_yes = Button(confirm_window_4, text = "  Yes  ", font = ("Consolas", 11, "bold"), bg = "#1544a0", fg = "#FFFFFF",
								command = confirm_change)
			confirm_yes.place(x = 110, y = 55)

			confirm_no = Button(confirm_window_4, text = "  No  ", font = ("Consolas", 11, "bold"), bg = "#ed1e45", fg = "#FFFFFF",
								command = deny_saveChange)
			confirm_no.place(x = 190, y = 55)

			confirm_cancel = Button(confirm_window_4, text = "  Cancel  ", font = ("Consolas", 11, "bold"), bg = "#2b313c", fg = "#FFFFFF",
									command = lambda: confirm_window_4.destroy())
			confirm_cancel.place(x = 260, y = 55)


		## setting label ##
		Setting_label = Label(setting_window, text = "Setings", font = ("Consolas", 50), fg = "#55aaff", bg = "#1e222a")
		Setting_label.place(x = 230, y = 10)

		SeperateLine = Frame(setting_window, width = 330, height = 5)
		SeperateLine.place(x = 200, y = 120)

		### Display name ###
		DisplayName_label = Label(setting_window, text = "Display name:", font = ("Consolas", 15, "bold"), fg = "#55aaff", bg = "#1e222a")
		DisplayName_label.place(x = 200, y = 170)

		DisplayName_entry = Entry(setting_window, font = ("Consolas", 15), width = 22, fg = "#FFFFFF")
		DisplayName_entry.insert(END, display_name_onScreen)
		DisplayName_entry.config(state = "readonly", readonlybackground = "#1e222a", bd = 0)
		DisplayName_entry.place(x = 365, y = 172)

		Edit_button = Button(setting_window, text = " Edit ", font = ("Consolas", 13, "bold"), bg = "#2a5bba", fg = "#FFFFFF", command = turnOnDisplay)
		Edit_button.place(x = 100, y = 170)

		### Username ###
		username_label = Label(setting_window, text = "Username:", font = ("Consolas", 15, "bold"), fg = "#55aaff", bg = "#1e222a")
		username_label.place(x = 200, y = 220)

		username_display = Entry(setting_window, font = ("Consolas", 15), width = len(username_saved), fg = "#FFFFFF")
		username_display.insert(END, username_saved)
		username_display.config(state = "readonly", readonlybackground = "#1e222a", bd = 0)
		username_display.place(x = 320, y = 222)

		### Password ###
		password_label = Label(setting_window, text = "Password:", font = ("Consolas", 15, "bold"), fg = "#55aaff", bg = "#1e222a")
		password_label.place(x = 200, y = 270)

		passwordReview_entry = Entry(setting_window, font = ("Consolas", 15), width = 20, fg = "#FFFFFF", show = "*")
		passwordReview_entry.insert(END, "***********")
		passwordReview_entry.config(state = "readonly", readonlybackground = "#1e222a", bd = 0)
		passwordReview_entry.place(x = 320, y = 272)

		EditPw_button = Button(setting_window, text = " Edit ", font = ("Consolas", 13, "bold"), bg = "#2a5bba", fg = "#FFFFFF", command = turnOnPassword)
		EditPw_button.place(x = 100, y = 270)

		### Email ###
		Email_label = Label(setting_window, text = "Email:", font = ("Consolas", 15, "bold"), fg = "#55aaff", bg = "#1e222a")
		Email_label.place(x = 200, y = 320)

		Email_entry = Entry(setting_window, font = ("Consolas", 15), width = len(complete_emailDisplay), fg = "#FFFFFF")
		Email_entry.insert(END, complete_emailDisplay)
		Email_entry.config(state = "readonly", readonlybackground = "#1e222a", bd = 0)
		Email_entry.place(x = 285, y = 322)

		EditEmail_button = Button(setting_window, text = " Edit ", font = ("Consolas", 13, "bold"), bg = "#2a5bba", fg = "#FFFFFF", command = turnOnEmail)
		EditEmail_button.place(x = 100, y = 320)

		### Tag number - ID Number ###
		TagNumber_Lbl = Label(setting_window, text= "ID Number:", font = ("Consolas", 15, "bold"), fg = "#55aaff", bg = "#1e222a")
		TagNumber_Lbl.place(x = 200, y = 390)

		TagNumber_display = Entry(setting_window, font = ("Consolas", 15), width = len(List_account[temp_id_use].tag_number), fg = "#FFFFFF")
		TagNumber_display.insert(END, List_account[temp_id_use].tag_number)
		TagNumber_display.config(state = "readonly", readonlybackground = "#1e222a", bd = 0)
		TagNumber_display.place(x = 340, y = 392)

		### Verify code when change email Entry:
		SendVerifyCode = Button(setting_window, text = " Send verify code ", font = ("Consolas", 13, "bold"), bg = "#2b313c", fg = "#FFFFFF", command = sendVerify_Code)
		verify_entry = Entry(setting_window, font = ("Consolas", 18), width = 10)

		### Save change button ###
		SaveChangeButton = Button(setting_window, text = "Save change", font = ("Consolas", 20, "bold"), bg = "#ed1e45", fg = "#FFFFFF", command = confirm_anyChange)
		SaveChangeButton.place(x = 270, y = 475)

		### Delete Account ###
		Delete_Account = Button(setting_window, text = "Delete account", font = ("Consolas", 11, "bold"), bg = "#2b313c", fg = "#FFFFFF", command = DeleteUser)
		Delete_Account.place(x = 10, y = 10)

		###############
		### Tip box ###
		display_tip = Label(setting_window, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#1e222a")
		display_tip.place(x = 180, y = 172)

		username_tip = Label(setting_window, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#1e222a")
		username_tip.place(x = 180, y = 220)

		email_tip = Label(setting_window, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#1e222a")
		email_tip.place(x = 180, y = 320)

		passwrodTip = Label(setting_window, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#1e222a")
		passwrodTip.place(x = 180, y = 270)

		IDNumber_tip = Label(setting_window, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#1e222a")
		IDNumber_tip.place(x = 180, y = 390)

		## Display name tip ##
		CreateToolTip(display_tip, 'Avoid using "|" as much as possible.', 20, 20)

		## Username tip ##
		CreateToolTip(username_tip, """Unfortunately, you can't edit your username.""", 20, 20)

		## Email tip ##
		CreateToolTip(email_tip, """All we can say is: Follow the email format. (example@gmail.com)""", 20, 20)

		## Password tip ##
		CreateToolTip(passwrodTip, """Your password need to meet those requirements:
- Length >= 10.
- Included atleast 1 uppercase word (A-Z) and 1 number (0-9).
- Avoid using @#$%*()!/|<>\\-_+=[]{}~., (blank space is not recommended).""", 20, 20)

		## Password tip ##
		CreateToolTip(IDNumber_tip, """- Your ID account will be different from each other
and will be randomized when you created your account.
- Unfortunately, you can't edit your ID, either.""", 20, 20)


	### Setting button ###
	setting_button = Button(UserTopLeft_frame, text = "       Settings			  	 ", font = ("Consolas", 12, "bold"), bg = "#13171c", fg = "#FFFFFF", bd = 0, command = setting_window)
	setting_button.place(x = 0, y = 62)
	setting_button.bind("<Enter>", hover_button)
	setting_button.bind("<Leave>", default_color)

	LogOut_button = Button(UserTopLeft_frame, text = "       Log out			  	 ", font = ("Consolas", 12, "bold"), bg = "#13171c", fg = "#FFFFFF", bd = 0, command = LogOut)
	LogOut_button.place(x = 0, y = 91)
	LogOut_button.bind("<Enter>", hover_button)
	LogOut_button.bind("<Leave>", default_color)

	### Left side Button - Profile button ###
	# Team Button
	Team_Button = CustomButton(leftside_frame,
								Team_image,
								hoverPic_Team,
								pressPic_Team,
								"#1e222a", "#2b313c", "#1544a0",
								0, 138, 0, setting_window)
	Team_Button_active = Label(leftside_frame, image = pressPic_Team, bg = "#1544a0", bd = 0)

	root.config(bg = "#262a34")

###------------------------------------------------------------###
### Login Window
def login_window():
	## Login screen ##
	def save_login_state(login_bool):

		if login_bool == True:
			check_string = str(user_emptystring.get())
			with open("keep_login", 'w') as file:
				file.write(''.join(str(user_emptystring.get())))
			file.close()

	def check_account():
		global List_account, display_name_onScreen, username_saved, full_displayname, tag_number_int
		List_account.clear()
		check_file()

		# List_account.sort(key = operator.attrgetter('username'))
		MergeSort_Username(List_account)
		username = []
		password = []
		for i in range(0, len(List_account), 1):
			username.append(List_account[i].username)

		# List_account.sort(key = operator.attrgetter('password'))
		MergeSort_Password(List_account)
		for i in range(0, len(List_account), 1):
			password.append(List_account[i].password)

		target_username = user_emptystring.get()
		length_username_list = len(username) - 1
		result_username = ExponentialSearch(username, length_username_list, target_username)

		password_get = password_emptystring.get()
		target_password = sha1(password_get)
		length_password_list = len(password) - 1
		result_password = ExponentialSearch(password, length_password_list, target_password)

		if result_username != -1 and result_password != -1:
			# messagebox.showinfo(title="Congrats", message="Acount exist")
			Error_Label.place_forget()
			login_window.destroy()
			save_login_state(login_bool)

			# List_account.sort(key = operator.attrgetter('username'))
			MergeSort_Username(List_account)

			display_name_onScreen = List_account[result_username].display_name

			full_displayname = List_account[result_username].display_name

			tag_number_int = List_account[result_username].tag_number

			if len(List_account[result_username].display_name) > 12:
				display_name_onScreen = display_name_onScreen[:12] + "..."

			username_saved = List_account[result_username].username

			## Save User's Project List
			# Check user saved path
			mainwindow()
			username.clear()
			password.clear()
		else:
			# messagebox.showinfo(title=":(", message="Nope")
			Error_Label.place(x = 135, y = 505)
			username.clear()
			password.clear()

	def login(event):
		check_account()

	def keep_login():
		global login_bool
		login_bool = True
		Check_button.place_forget()
		Check_button_press.place(x = 180, y = 474)

	def dont_keep_login():
		global login_bool
		login_bool = False
		Check_button_press.place_forget()
		Check_button.place(x = 180, y = 474)

	## Function
	def create_account_frame():
		username_entry_new.config(state = NORMAL)
		display_entry_new.config(state = NORMAL)
		email_entry_new.config(state = NORMAL)
		password_entry_new.config(state = NORMAL)
		confirm_password_entry.config(state = NORMAL)

		CreateAcc_Frame.place(x = 0)
		User_name_entry.delete(0, END)
		User_name_entry.config(state = "readonly")
		password_entry.delete(0, END)
		password_entry.config(state = "readonly")
		Check_button.config(state = DISABLED)

	def get_backAccount():
		choose_method.place(x = 0)
		type_entry.config(state = NORMAL)

		User_name_entry.delete(0, END)
		User_name_entry.config(state = "readonly")
		password_entry.delete(0, END)
		password_entry.config(state = "readonly")
		Check_button.config(state = DISABLED)

	#### extract window ####
	### Close manual ###
	def extract_frame():
		global stop_widget

		stop_widget = False

		size = right_Message.cget('width')
		if size < 400:
			size += 5
			right_Message.config(width = size)
			right_Message.after(3, extract_frame)

	def contract_frame():
		global stop_widget

		stop_widget = True

		size = right_Message.cget("width")
		if size <= 400 and size > 0:
			size -= 5
			right_Message.config(width = size)
			right_Message.after(3, contract_frame)


	#### Auto expand and contract window ####
	def auto_contract():
		global count_stop, count_expand, stop_widget

		stop_widget = False

		size = right_Message.cget('width')
		if size <= 400 and size > 0:
			size -= 5
			count_stop = 0
			count_expand = 0
			right_Message.config(width = size)
			right_Message.after(5, auto_contract)

	def auto_expand():
		global count_stop, count_expand, stop_widget

		size = right_Message.cget('width')

		stop_widget = True

		if stop_widget == True:
			if size < 400:
				count_expand += 5
				size += 5
				right_Message.config(width = size)
				right_Message.after(4, auto_expand)

			## If width size already = 400
			elif count_expand >= 400:
				if count_stop < 5:
					count_stop += 1
					right_Message.after(500, auto_expand)
				else:
					auto_contract()

	def create_account():
		global tag_number_int

		tag_number_int = ""

		random_tag = "#"

		## Check valid keyword ##
		if (display_entry_new.get()).strip() != "" and ("|" in display_entry_new.get()) == False:

			## check valid keyword for display user
			if username_entry_new.get().strip() != "" and search_keyword(symbol, username_entry_new.get()) == False and bool(re.search(r"\s", username_entry_new.get())) == False and existed_username(username_entry_new.get()) == False and stringAndNumber(lower, username_entry_new.get()) == True:

				## check valid email
				if (email_entry_new.get()).strip() != "" and check_valid_email(email_entry_new.get()) == True and bool(re.search(r"\s", email_entry_new.get())) == False and search_keyword(upper, email_entry_new.get()) == False:

					## check valid password
					if (password_entry_new.get()).strip() != "" and search_keyword(symbol, password_entry_new.get()) == False and search_keyword(upper, password_entry_new.get()) == True and search_keyword(number, password_entry_new.get()) == True:

						if len(password_entry_new.get()) >= 10:
							### Check confirm password and password either the same or not
							if (confirm_password_entry.get()).strip() != "" and password_entry_new.get() == confirm_password_entry.get():

								## Create random tag number ##
								random_number = random.choices(list(number), k = 5)

								for index in random_number:
									random_tag += str(index)

								tag_number_int = random_tag

								test_value = sha1(confirm_password_entry.get())
								
								## Write new account to file ##
								with open("user", "a") as write_user:
									write_user.write("".join(str((username_entry_new.get()).lower())))
									write_user.write("|")
									write_user.write("".join(str(test_value)))
									write_user.write("|")
									write_user.write("".join(str((display_entry_new.get()).strip())))
									write_user.write("|")
									write_user.write("".join(str((email_entry_new.get()).lower())))
									write_user.write("|")
									write_user.write("".join(str(tag_number_int)))
									write_user.write("\n")
								write_user.close()

								error_displayText.config(text = "Congrats!! You've just\ncreated a new account", font = ("Consolas", 15))

								if right_Message.cget('width') == 0:
									auto_expand()
								else:
									extract_frame()

								username_entry_new.delete(0, END)
								username_entry_new.config(state = "readonly")

								display_entry_new.delete(0, END)
								display_entry_new.config(state = "readonly")

								email_entry_new.delete(0, END)
								email_entry_new.config(state = "readonly")

								password_entry_new.delete(0, END)
								password_entry_new.config(state = "readonly")

								confirm_password_entry.delete(0, END)
								confirm_password_entry.config(state = "readonly")

								CreateAcc_Frame.place_forget()

								success_text.config(text = "Create account successfully")
								success_text.place(x = 100, y = 430)

								succes_frame.place(x = 0)


							else:
								if right_Message.cget('width') < 400:
									extract_frame()
								error_displayText.config(text = "Those passwords didn’t\nmatch.Try again.", font = ("Consolas", 15))

						else:
							if right_Message.cget('width') < 400:
								extract_frame()
							error_displayText.config(text = "Your password is too weak.\nTry another one.", font = ("Consolas", 15))

					else:
						if right_Message.cget('width') < 400:
							extract_frame()
						error_displayText.config(text = "Your password is either\nempty or contain some\ninvalid keywords", font = ("Consolas", 15))

				else:
					if right_Message.cget('width') < 400:
						extract_frame()
					error_displayText.config(text = "Please type valid email", font = ("Consolas", 18))

			else:
				if right_Message.cget('width') < 400:
					extract_frame()
				error_displayText.config(text = "Invalid username\nor username already\nexisted.", font = ("Consolas", 15))
		else:
			if right_Message.cget('width') < 400:
				extract_frame()
			error_displayText.config(text = "Please type valid\ndisplay name", font = ("Consolas", 18))

	def return_login():
		global count_expand, count_stop, stop_widget

		Error_Label.place_forget()
		CreateAcc_Frame.place_forget()
		User_name_entry.config(state = NORMAL)
		password_entry.config(state = NORMAL)
		Check_button.config(state = NORMAL)

		### clear all value in sign up window ###
		username_entry_new.delete(0, END)
		username_entry_new.config(state = "readonly")

		display_entry_new.delete(0, END)
		display_entry_new.config(state = "readonly")

		email_entry_new.delete(0, END)
		email_entry_new.config(state = "readonly")

		password_entry_new.delete(0, END)
		password_entry_new.config(state = "readonly")

		confirm_password_entry.delete(0, END)
		confirm_password_entry.config(state = "readonly")

		#### clear all value in get back account or choose method window ###
		choose_method.place_forget()
		type_entry.delete(0, END)
		type_entry.config(state = "readonly")

		error_display.config(text = "")

		#### hide success Screen ####
		succes_frame.place_forget()

		if stop_widget == False:
			contract_frame()


	def return_chooseMethod():
		choose_method.place(x = 0)
		get_backAcc_frame.place_forget()

		verification_entry.delete(0, END)
		verification_entry.config(state = "readonly")

		new_password_entry_2.delete(0, END)
		new_password_entry_2.config(state = "readonly")

		confirm_password_entry_2.delete(0, END)
		confirm_password_entry_2.config(state = "readonly")

	def setNewPassword():
		global verification_code, username_find_temp

		account_list = []
		password_list = []

		temp = ""
		id_int = 0

		with open("user", "r") as user_read:
			reader = csv.reader(user_read, delimiter = "|")
			for row in reader:
				account_list.append(Account_Info(row[0], row[1], row[2], row[3], row[4]))
		user_read.close()

		verification_entry.config(state = NORMAL)
		new_password_entry_2.config(state = NORMAL)
		confirm_password_entry_2.config(state = NORMAL)

		next_step = False
		add_file = True

		if (verification_entry.get()).strip() != "":
			if verification_entry.get() == verification_code:
				next_step = True		
				

		if next_step == True:
			if (new_password_entry_2.get()).strip() != "" and search_keyword(symbol, new_password_entry_2.get()) == False and search_keyword(upper, new_password_entry_2.get()) == True and search_keyword(number, new_password_entry_2.get()) == True:

				if len(new_password_entry_2.get()) >= 10:

					if (confirm_password_entry_2.get()).strip() != "" and new_password_entry_2.get() == confirm_password_entry_2.get():
							
						### rewrite file and account ###
						
						for i in range(0, len(account_list), 1):
							if account_list[i].username == username_find_temp:
								id_int = i
								break
							
						if account_list[id_int].password == sha1(new_password_entry_2.get()):
							add_file = False

						if add_file == True:

							account_list[id_int].password = sha1(new_password_entry_2.get())

							with open("user", "w") as new_password:
								for i in range(0, len(account_list), 1):
									new_password.write("".join(str(account_list[i].username)))
									new_password.write("|")
									new_password.write("".join(str(account_list[i].password)))
									new_password.write("|")
									new_password.write("".join(str(account_list[i].display_name)))
									new_password.write("|")
									new_password.write("".join(str(account_list[i].email)))
									new_password.write("|")
									new_password.write("".join(str(account_list[i].tag_number)))
									new_password.write("\n")
							new_password.close()

							### Clear all value in entry before hide current frame ###
							verification_entry.delete(0, END)
							verification_entry.config(state = "readonly")

							new_password_entry_2.delete(0, END)
							new_password_entry_2.config(state = "readonly")

							confirm_password_entry_2.delete(0, END)
							confirm_password_entry_2.config(state = "readonly")

							get_backAcc_frame.place_forget()

							success_text.config(text = "Set new password successfully")
							success_text.place(x = 100, y = 430)

							succes_frame.place(x = 0)

							username_find_temp = ""

							error_displayText.config(text = "Congrats! Set new password\nsuccessfully.", font = ("Consolas", 15))

							if right_Message.cget('width') == 0:
								auto_expand()
							else:
								extract_frame()

						else:
							if right_Message.cget('width') == 0:
								auto_expand()
								error_displayText.config(text = "Your new password are\nsimilar to the old one.", font = ("Consolas", 15))					

					else:
						if right_Message.cget('width') == 0:
							auto_expand()
							error_displayText.config(text = "Those passwords didn’t\nmatch.Try again.", font = ("Consolas", 15))

				else:
					if right_Message.cget('width') == 0:
						auto_expand()
						error_displayText.config(text = "Your new password is too\nweak.Try another one.", font = ("Consolas", 15))
					
			else:
				if right_Message.cget('width') == 0:
					auto_expand()
					error_displayText.config(text = "Your password is either\nempty or contain some\ninvalid keywords", font = ("Consolas", 15))
		else:
			if right_Message.cget('width') == 0:
				auto_expand()
				error_displayText.config(text = "Your code either is invalid\nor already expired", font = ("Consolas", 15))



	## Function for Custom Widget
	def on_enter_nonpress(event):
		event.widget.config(image = check_icon_nonpress_hover)

	def on_leave_nonpress(event):
		event.widget.config(image = check_icon_nonpress)

	def on_enter_press(event):
		event.widget.config(image = check_icon_hover_press)

	def on_leave_press(event):
		event.widget.config(image = check_icon_press)


	def confirm_username():
		verification_entry.config(state = NORMAL)
		new_password_entry_2.config(state = NORMAL)
		confirm_password_entry_2.config(state = NORMAL)		

		global List_account, verification_code, username_find_temp
		List_account.clear()
		check_file()

		next_step = False

		if (type_entry.get()).strip() != "":
			for i in range(0, len(List_account), 1):
				if type_entry.get() == List_account[i].username:
					next_step = True

		if next_step == True:
			username_find_temp = type_entry.get()

			verification_code = ""
			error_displayText.config(text = "A verification code\nalready been sent\nto your email address", font = ("Consolas", 15))

			if right_Message.cget('width') == 0:
				auto_expand()

			choose_method.place_forget()
			get_backAcc_frame.place(x = 0)

			### get random key word in all strings list ###
			random_choices = random.choices(list(all_string), k = 7)

			for i in range(0, len(random_choices), 1):
				verification_code += str(random_choices[i])

			# #### for showcase only - write to desktop ####
			# with open("C:/Users/Cryptor/Desktop/Verification code.txt", "w") as verify_code:
			# 	verify_code.write("Username: " + str(type_entry.get()))
			# 	verify_code.write("\n")
			# 	verify_code.write("Your verification code to set new password: "+ str(verification_code))
			# verify_code.close()

			#### for other user - write to Mail folder ####
			if not os.path.exists("Mail"):
				os.makedirs("Mail")

			with open("Mail/Verification code.txt", "w") as verify_code:
				verify_code.write("Username: " + str(type_entry.get()))
				verify_code.write("\n")
				verify_code.write("Your verification code to set new password: "+ str(verification_code))
			verify_code.close()

			# with open("Mail/Verification code.txt", "w")
				

		else:
			error_display.config(text = "Your username doesn't exist.")


	## Tkinter UI
	login_window = Tk()
	login_window.title("Login window")

	# Label Image
	bg = PhotoImage(file = "images/Login window/login_bg.png")

	user_string = StringVar(login_window, value = "Username")
	user_emptystring = StringVar()

	password_string = StringVar(login_window, value = "Password")
	password_emptystring = StringVar()

	app_width = 1440
	app_height = 810

	monitor_h = login_window.winfo_screenheight()
	monitor_w = login_window.winfo_screenwidth()

	pos_x = (monitor_w//2) - (app_width//2)
	pos_y = (monitor_h//2) - (app_height//2)

	bg_label = Label(login_window, image = bg)
	bg_label.photo = bg
	bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

	login_window.geometry(f"{app_width}x{app_height}+{pos_x}+{pos_y}")
	login_window.resizable(0,0)

	User_name_entry = Entry(login_window, width = 23, font = ("Consolas", 20),
							bg = "#495269", bd = 0, fg = "#ffffff",
							selectforeground = "#FFFFFF", textvariable = user_emptystring,
							insertbackground = "#FFFFFF")
	User_name_entry.place(x = 130, y = 337)

	password_entry = Entry(login_window, width = 23, font = ("Consolas", 20),
							bg = "#495269", bd = 0, fg = "#ffffff",
							selectforeground = "#FFFFFF", textvariable = password_emptystring, show = "*",
							insertbackground = "#FFFFFF")
	password_entry.place(x = 130, y = 417)
	## Check button image
	check_icon_nonpress = PhotoImage(file = "images/Login window/check_button.png")
	check_icon_nonpress_hover = PhotoImage(file = "images/Login window/check_button_hover.png")
	check_icon_press = PhotoImage(file = "images/Login window/check_button_press.png")
	check_icon_hover_press = PhotoImage(file = "images/Login window/check_button_hover_press.png")

	# Check Button
	Check_button = Button(login_window, image = check_icon_nonpress, bg = "#429f46", bd = 0, command = keep_login)
	Check_button.place(x = 180, y = 474)
	Check_button.bind("<Enter>", on_enter_nonpress)
	Check_button.bind("<Leave>", on_leave_nonpress)

	Check_button_press = Button(login_window, image = check_icon_press, bg = "#429f46", bd = 0, command = dont_keep_login)
	Check_button_press.bind("<Enter>", on_enter_press)
	Check_button_press.bind("<Leave>", on_leave_press)

	Keep_login_label = Label(login_window, text = "KEEP ME LOG IN", font = ("Consolas", 18), bg = "#262a34", fg = "#FFFFFF")
	Keep_login_label.place(x = 220, y = 468)

	## Log in Field
	Error_Label = Label(login_window, text = "Incorrect username or password", font = ("Microsoft Yi Baiti", 20, "bold"), bg = "#262a34", fg = "#ed1e45")

	Login_icon = PhotoImage(file = "images/Login window/Login_Button.png")
	Login_icon_hover = PhotoImage(file = "images/Login window/Login_Button_hover.png")
	Login_icon_press = PhotoImage(file = "images/Login window/Login_Button_press.png")

	Login_buton = CustomButton(login_window,
								Login_icon,
								Login_icon_hover,
								Login_icon_press,
								"#2a5bba", "#3b7cff", "#1d3e80",
								108, 555, 0, check_account)

	### Sign up, Get back password button ###
	### Image ###
	signUp_image = PhotoImage(file = "images/Login window/create_acc_icon.png")
	signUp_hover_image = PhotoImage(file = "images/Login window/create_acc_hover_icon.png")
	signUp_press_image = PhotoImage(file = "images/Login window/create_acc_press_icon.png")

	getPassword_image = PhotoImage(file = "images/Login window/forgot_pw_icon.png")
	getPasword_hover_image = PhotoImage(file = "images/Login window/forgot_pw_hover_icon.png")
	getPassword_press_image = PhotoImage(file = "images/Login window/forgot_pw_press_icon.png")

	## Button widgets ##
	signUp_Button = CustomButton(login_window,
								signUp_image,
								signUp_hover_image,
								signUp_press_image,
								"#0c9d6f", "#0ecc90", "#09805a",
								105, 665, 0, create_account_frame)

	getPassword_Button = CustomButton(login_window,
									getPassword_image,
									getPasword_hover_image,
									getPassword_press_image,
									"#ed1e45", "#fd4064", "#99142c",
									105, 720, 0, get_backAccount)


	#### Create account Frame ####
	CreateAcc_Frame = Frame(login_window, width = 615, height = 805, bg = "#262a34")

	bg_Acc = PhotoImage(file = "images/Login window/Create_acc_frame.png")

	createAcc = Label(CreateAcc_Frame, image = bg_Acc, bg = "#262a34")
	createAcc.photo = bg_Acc
	createAcc.place(x = 0, y = 0)

	### image ###
	create_icon = PhotoImage(file = "images/Login window/CREATE_icon.png")
	create_hover_icon = PhotoImage(file = "images/Login window/CREATE_hover_icon.png")
	create_press_icon = PhotoImage(file = "images/Login window/CREATE_press_icon.png")

	Create_Acc_button = CustomButton(CreateAcc_Frame,
									create_icon,
									create_hover_icon,
									create_press_icon,
									"#185daa", "#248aff", "#124580",
									165, 706, 0, create_account)

	return_icon = PhotoImage(file = "images/Login window/RETURN_icon.png")
	return_hover_icon = PhotoImage(file = "images/Login window/RETURN_hover_icon.png")
	return_press_icon = PhotoImage(file = "images/Login window/RETURN_hover_icon.png")

	Return_login_window_2 = CustomButton(CreateAcc_Frame,
										return_icon,
										return_hover_icon,
										return_press_icon,
										"#ed1e45", "#fd4064", "#801125",
										11, 12, 0, return_login)

	### Entry ###
	display_entry_new = Entry(CreateAcc_Frame, width = 23, font = ("Consolas", 19),
							bg = "#495269", bd = 0, fg = "#ffffff",
							selectforeground = "#FFFFFF", insertbackground = "#FFFFFF")
	display_entry_new.place(x = 153, y = 276)

	username_entry_new = Entry(CreateAcc_Frame, width = 23, font = ("Consolas", 19),
							bg = "#495269", bd = 0, fg = "#ffffff",
							selectforeground = "#FFFFFF", insertbackground = "#FFFFFF")
	username_entry_new.place(x = 153, y = 363)

	email_entry_new = Entry(CreateAcc_Frame, width = 23, font = ("Consolas", 19),
							bg = "#495269", bd = 0, fg = "#ffffff",
							selectforeground = "#FFFFFF", insertbackground = "#FFFFFF")
	email_entry_new.place(x = 153, y = 452)

	password_entry_new = Entry(CreateAcc_Frame, width = 23, font = ("Consolas", 19),
							bg = "#495269", bd = 0, fg = "#ffffff",
							selectforeground = "#FFFFFF", insertbackground = "#FFFFFF", show = "*")
	password_entry_new.place(x = 153, y = 540)

	confirm_password_entry = Entry(CreateAcc_Frame, width = 23, font = ("Consolas", 19),
								bg = "#495269", bd = 0, fg = "#ffffff",
								selectforeground = "#FFFFFF", insertbackground = "#FFFFFF", show = "*")
	confirm_password_entry.place(x = 153, y = 630)


	### Tip box ###
	display_tip = Label(CreateAcc_Frame, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#262a34")
	display_tip.place(x = 272, y = 240)

	username_tip = Label(CreateAcc_Frame, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#262a34")
	username_tip.place(x = 240, y = 327)

	email_tip = Label(CreateAcc_Frame, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#262a34")
	email_tip.place(x = 198, y = 414)

	password_tip = Label(CreateAcc_Frame, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#262a34")
	password_tip.place(x = 237, y = 502)

	## Display name tip ##
	CreateToolTip(display_tip, 'Avoid using "|" as much as possible.', 20, 20)

	## Username tip ##
	CreateToolTip(username_tip, """- Avoid using @#$%*()!/|<>\\-_+=[]{}~., included blank space.
- Your username need to contain both text (A-Z) and number (0-9).
Note: Uppercase word doesn't matter because it will be\nautomatically converted to lowercase.""", 20, 20)

	## Email tip ##
	CreateToolTip(email_tip, """We don't have much to said but don't leave this entry blank
and follow the email format (example@gmail.com).""", 20, 20)

	## Password tip ##
	CreateToolTip(password_tip, """Your password need to meet those requirements:
- Length >= 10.
- Included atleast 1 uppercase word (A-Z) and 1 number (0-9).
- Avoid using @#$%*()!/|<>\\-_+=[]{}~., (blank space is not recommended).""", 20, 20)


	#### Get back account ####
	## choose user ##
	choose_method = Frame(login_window, width = 615, height = 805, bg = "#262a34")
	
	method_bg = PhotoImage(file = "images/Login window/get_acc_frame_1.png")

	method_display = Label(choose_method, image = method_bg, bg = "#262a34")
	method_display.photo = method_bg
	method_display.place(x = 0)

	Return_login_window = CustomButton(choose_method,
										return_icon,
										return_hover_icon,
										return_press_icon,
										"#ed1e45", "#fd4064", "#801125",
										11, 12, 0, return_login)

	### image ###
	next_icon = PhotoImage(file = "images/Login window/NEXT_icon.png")
	next_hover_icon = PhotoImage(file = "images/Login window/NEXT_hover_icon.png")
	next_press_icon = PhotoImage(file = "images/Login window/NEXT_press_icon.png")

	Next_button = CustomButton(choose_method,
								next_icon,
								next_hover_icon,
								next_press_icon,
								"#185daa", "#248aff", "#124580",
								207, 468, 0, confirm_username)

	type_entry = Entry(choose_method, width = 24, font = ("Consolas", 20),
						bg = "#495269", bd = 0, fg = "#ffffff",
						selectforeground = "#FFFFFF", insertbackground = "#FFFFFF")
	type_entry.place(x = 137, y = 394)

	error_display = Label(choose_method, font = ("Consolas", 17, "bold"), bg = "#262a34", fg = "#ed1e45")
	error_display.place(x = 120, y = 565)

	#### get back frame ####
	get_backAcc_frame = Frame(login_window, width = 615, height = 805, bg = "#262a34")	

	getBack_image = PhotoImage(file = "images/Login window/change_password_frame.png")

	getBack_BG = Label(get_backAcc_frame, image = getBack_image, bg = "#262a34")
	getBack_BG.photo = getBack_image
	getBack_BG.place(x = 0)

	Return_login_window_3 = CustomButton(get_backAcc_frame,
										return_icon,
										return_hover_icon,
										return_press_icon,
										"#ed1e45", "#fd4064", "#801125",
										11, 12, 0, return_chooseMethod)

	verification_entry = Entry(get_backAcc_frame, width = 24, font = ("Consolas", 19),
							bg = "#495269", bd = 0, fg = "#ffffff",
							selectforeground = "#FFFFFF", insertbackground = "#FFFFFF")
	verification_entry.place(x = 145, y = 385)

	new_password_entry_2 = Entry(get_backAcc_frame, width = 24, font = ("Consolas", 19),
								bg = "#495269", bd = 0, fg = "#ffffff",
								selectforeground = "#FFFFFF", insertbackground = "#FFFFFF", show = "*")
	new_password_entry_2.place(x = 145, y = 483)	

	confirm_password_entry_2 = Entry(get_backAcc_frame, width = 24, font = ("Consolas", 19),
								bg = "#495269", bd = 0, fg = "#ffffff",
								selectforeground = "#FFFFFF", insertbackground = "#FFFFFF", show = "*")
	confirm_password_entry_2.place(x = 145, y = 584)


	### Tip display ###
	verify_tip = Label(get_backAcc_frame, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#262a34")
	verify_tip.place(x = 337, y = 344)

	password_tip_2 = Label(get_backAcc_frame, text = "*", font = ("Consolas", 13), fg = "#ed1e45", bg = "#262a34")
	password_tip_2.place(x = 302, y = 442)

	## Password tip ##
	CreateToolTip(password_tip_2, """Your password need to meet those requirements:
- Length >= 10.
- Included atleast 1 uppercase word (A-Z) and 1 number (0-9).
- Avoid using @#$%*()!/|<>\\-_+=[]{}~., (blank space is not recommended).""", 20, 20)

	## Verification code tip ##	
	CreateToolTip(verify_tip, """- This is just a beta version so you don't have to check your email.
- Check your desktop and find "Verification code.txt" or you can find it 
in "Project Management/Mail/Verification code.txt to see the code.
- And remember everytime you close this app you will have to get
new verification code because the old one have already been expired.""", 20, 20)


	### image ###
	setPw_image = PhotoImage(file = "images/Login window/set_pw_icon.png")
	setPw_hover_image = PhotoImage(file = "images/Login window/set_pw_icon.png")
	setPw_press_image = PhotoImage(file = "images/Login window/set_pw_press_icon.png")

	setPw_button = CustomButton(get_backAcc_frame,
								setPw_image,
								setPw_hover_image,
								setPw_press_image,
								"#185daa", "#248aff", "#124580",
								200, 687, 0, setNewPassword)

	## default width = 400
	right_Message = Frame(login_window, width = 0, height = 100, bg = "#262a34")
	right_Message.pack(anchor = "e", pady = 30)

	warning_icon = PhotoImage(file = "images/Login window/warning_icon.png")

	warning_image = Label(right_Message, image = warning_icon, bg = "#262a34")
	warning_image.photo = warning_icon
	warning_image.place(x = 10, y = 10)
	
	error_displayText = Label(right_Message, font = ("Consolas", 18), bg = "#262a34", fg = '#FFFFFF', justify = "left")
	error_displayText.place(x = 70, y = 15)


	## Create/ get back accoutn success ###
	succes_frame = Frame(login_window, width = 615, height = 805, bg = "#262a34")

	success_icon = PhotoImage(file = "images/Login window/complete_icon.png")

	succes_label = Label(succes_frame, image = success_icon, bg = "#262a34")
	succes_label.photo = success_icon
	succes_label.place(x = 207, y = 230)

	success_text = Label(succes_frame, font = ("Consolas", 20), bg = "#262a34", fg = "#FFFFFF")

	Return_login_window_4 = CustomButton(succes_frame,
										return_icon,
										return_hover_icon,
										return_press_icon,
										"#ed1e45", "#fd4064", "#801125",
										230, 500, 0, return_login)


	# # Create new account Label
	# New_acc_Label = Label(login_window, text = "New user?", font = ("Microsoft Yi Baiti", 20), bg = "#262a34", fg = "#FFFFFF")
	# New_acc_Label.place(x = 183, y = 648)

	# Create_acc_Label = Label(login_window, text = "Create an account", font = ("Microsoft Yi Baiti", 20, "underline"), bg = "#262a34", fg = "#FFFFFF", cursor = "hand2")
	# Create_acc_Label.place(x = 300, y = 648)
	# Create_acc_Label.bind("<Button-1>", create_account)

	# # Recover password label
	# recov_acc_Label = Label(login_window, text = "Forgot your password?", font = ("Microsoft Yi Baiti", 17), bg = "#262a34", fg = "#FFFFFF")
	# recov_acc_Label.place(x = 183, y = 690)

	# get_acc_Label = Label(login_window, text = "Get it back", font = ("Microsoft Yi Baiti", 17, "underline"), bg = "#262a34", fg = "#FFFFFF", cursor = "hand2")
	# get_acc_Label.place(x = 390, y = 690)
	# get_acc_Label.bind("<Button-1>", create_account)


	login_window.bind("<Return>", login)

if __name__=="__main__":
	pressButton_bool = False

	count_stop = 0
	count_expand = 0
	stop_widget = False

	tag_number_int = ""

	all_string = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
	verification_code = ""

	# Keep login value
	login_bool = False

	### get new email ###
	new_email = ""

	## Temp Variable
	empty_String = ""

	ProjectName_short = ""

	display_name_onScreen = ""
	full_displayname = ""

	username_saved = ""

	username_find_temp = ""

	# Percent string
	percent = "%"

	## Keep project frame
	stayValue = False

	## Total job numbers ##
	job_total = 0

	# Progress state
	progress_value = 0

	### note list ###
	note_list = []

	## Job List - To Do List
	Job_list = []

	## Doing List
	Doing_list = []

	## Complete List
	Complete_List = []

	### Job submitted late ###
	submitted_late = []

	### flag sort - in open project window ###
	flag_sort = False

	## Store og id of value from job list - for knapsack algorithm
	Filter_list_og = []
	## KnapSack List - Use for knapSack Algorithm
	KnapSack_list = []

	## Time limit value store
	time_limit_value = 0

	Title = ('To Do', 'Doing', 'Complete')
	Sign_list = ('None', 'On')

	### Sort by list ###
	sortBy_list = ("Title", "Due Date", "Due Hour", "Time Limit", "Importance")
	sortUp_down = ("Ascending", "Descending")
	sortChild_filter = ("Day", "Month", "Year")

	Filter_List = ('Search by...', 'Title', 'Description', 'Date', 'Hour')
	Filter_In = ('Search in...', 'To Do', 'Doing', 'Complete')

	Edit_mode = ('Read only', 'Edit mode')

	Doing_Complete = ('Doing list', 'Complete list')

	ToDo_Complete = ('To Do list', 'Complete list')

	ToDo_Doing = ("To Do list", "Doing list")

	note_create = """Sorry for inconvenience, but please take note:

- Don't type any Vietnamese words, we haven't supported it yet.
- Avoid \\/:*?"<>| when naming your project.
- Don't delete/rename/move folder, file while program is running.
- This is just the beta, we're currently working on it."""

	error_text = """- Look like you haven't created any project yet.
- Click "Create new..." to start your first project."""

	note_complete = """Note:
- You can only edit title and description
in Complete list.
- To change the others please transfer job
back to Doing or To Do list to edit others
content."""

	invalid_keyword = ('\\','/',':','*','?','"','<','>','|','.')

	upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	lower = ("abcdefghijklmnopqrstuvwxyz")

	symbol = ("@#$%*()!/|<>\\-_+=[]{}~.,")

	number = ("0123456789")

	# # Display To Do listbox
	# TodoList_Bool = False

	## Toggle Button - Expand Frame
	## Size leftside Frame

	Temp_list = []

	# Store temporarily project list
	Project_list = []

	List_account = []
	Login_account = []

	login_state_check()
	mainloop()