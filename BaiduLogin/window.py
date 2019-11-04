import tkinter as tk
from baidu_login import baidu_login



class uiwindow:
	def __init__(self):

		# name the window master
		master = tk.Tk()

		# give the master window the tile "automation"
		master.title("Automation")

		# set the default size of the window to 800x400 
		master.geometry("200x200")

		# create two labels, username in the row 0, and password in row 2
		tk.Label(master,
			text="User Name").grid(row=0)
		tk.Label(master,
			text="Password").grid(row=1)

		# create two input fields
		input1 = tk.Entry(master)
		input2 = tk.Entry(master)

		# Put the two input fields at row 0 and 1 of column 1
		input1.grid(row=0,column=1)
		input2.grid(row=1,column=1)

		# assign input to userna and password variable
		def assignvalue():
			global username
			username = input1.get()
#			print(username)
			global password
			password = input2.get()
#			print(password)
			Baidulogin=baidu_login(username,password)
			Baidulogin.action()
			



		#Create submit button
		tk.Button(master,text='submit',command=assignvalue).grid(row=3,column=1)


		# Run the main loop
		master.mainloop()



#		print(username)
#		print(password)

		
		



