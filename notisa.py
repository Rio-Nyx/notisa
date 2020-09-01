import tkinter as tk
from tkinter import *
# from platform import processor --> thought of using processor name for encryption , but since there's a chance it might change'

background=["white","red","black","green","yellow","blue"]
foreground=["black","green","white","blue","orange","cyan"]
fontsize=[15,20,25,50,5,10]
#fonts=["Arial Bold","Times","Helvetica","Symbol"]

class notepad:
	# main window
	def __init__(self):
		self.ind_bg=self.ind_fg=self.ind_fs=0
		self.window = tk.Tk()
		self.window.configure(background="white")
		self.window.title("Notiverse")
		self.window.geometry("540x540")
		self.inp1=tk.Text(self.window,height=540,width=540 )		# creating a text bx
		self.inp1.config(font=("Courier", fontsize[0]),fg=foreground[0],background=background[0])		
		self.inp1.pack()        
		#---------------------------------------------

	def do_popup(self,event):			# create a popup when right clicked
		print("Right button clicked")
		# creating a pop up menu
		my=Menu(self.window,tearoff=0)
		m = Menu(my, tearoff = 0) 
		m.add_command(label ="change background",command=self.changebg) 
		m.add_command(label ="change fontcolor",command=self.changefg) 
		m.add_command(label ="change fontsize",command=self.changefs) 
		m.add_separator() 
		m.add_command(label ="Close") 
		#labelfont = ('courier', 20, 'bold')
		
		try: 
			m.tk_popup(event.x_root, event.y_root) 
		finally: 
			m.grab_release()          
		                              
	def openit(self):			# fn to open text file	
		try:											
			f=open("notes.txt","r")
			for line in f:
				self.inp1.insert(tk.INSERT,line)
		except:
			f=open("notes.txt","x")
		f.close()
		
	def saveit(self,event):		# fn to save text file
		input_1=self.inp1.get("1.0","end-1c")
		f=open("notes.txt","w")
		f.write(input_1)
		f.close()

	def close(self):		# fn to close current window
		#if messagebox.askokcancel("Quit", "Do you want to quit?"):
		self.window.destroy()
	
	def changebg(self):
		self.ind_bg+=1
		if(self.ind_bg>=len(background)):
			self.ind_bg=0
		self.update()
	
	def changefg(self):
		self.ind_fg+=1
		if(self.ind_fg>=len(foreground)):
			self.ind_fg=0
		self.update()
	
	def changefs(self):
		self.ind_fs+=1
		if(self.ind_fs>=len(fontsize)):
			self.ind_fs=0
		self.update()
		
	def update(self):
		self.inp1.config(font=("Courier", fontsize[self.ind_fs]),fg=foreground[self.ind_fg],background=background[self.ind_bg])
		
	def run(self):
		self.inp1.bind("<Leave>",self.saveit)
		#self.inp1.bind("<key>",self.saveit)
		self.inp1.bind('<Button-3>',self.do_popup)
		self.window.protocol("WM_DELETE_WINDOW",self.close)
		self.window.mainloop()
notiverse=notepad()
notiverse.openit()
notiverse.run()
