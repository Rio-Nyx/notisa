import tkinter as tk
from jsonparser import *
from tkinter import *
# from platform import processor --> thought of using processor name for encryption , but since there's a chance it might change'

#background=["white","red","black","green","yellow","blue"]
#foreground=["black","green","white","blue","orange","cyan"]
#fontsize=[15,20,25,50,5,10]

settings=jsonread()

class notepad:
	# main window
	def __init__(self):
		self.background=settings['background']
		self.foreground=settings['foreground']
		self.fontsize=settings['fontsize']
		self.window = tk.Tk()
		self.window.configure(background="grey")
		self.window.title("Test appln")
		self.window.geometry("540x540")
		self.inp1=tk.Text(self.window,height=540,width=540 )		# creating a text bx
		self.inp1.config(font=("Courier", self.fontsize),fg=self.foreground,background=self.background)
		self.inp1.pack()        
		#---------------------------------------------

	def do_popup(self,event):			# create a popup when right clicked
		print("Right button clicked")
		# creating a pop up menu
		menu_sub1=Menu(self.window,tearoff=0)
		m = Menu(self.window, tearoff = 0)
		
		menu_sub2=Menu(self.window,tearoff=0)		
		m.add_cascade(label="change background",menu=menu_sub2)
		menu_sub2.add_command(label="  white",command=lambda:self.changebg("white"))
		menu_sub2.add_command(label="  red",command=lambda:self.changebg("red"))
		menu_sub2.add_command(label="  black",command=lambda:self.changebg("black"))
		menu_sub2.add_command(label="  green",command=lambda:self.changebg("green"))
		menu_sub2.add_command(label="  yellow",command=lambda:self.changebg("yellow"))
		menu_sub2.add_command(label="  blue",command=lambda:self.changebg("blue"))
		menu_sub2.add_command(label="  cyan",command=lambda:self.changebg("cyan"))
		
		menu_sub3=Menu(self.window,tearoff=0)
		m.add_cascade(label="change fontcolor",menu=menu_sub3)
		menu_sub3.add_command(label ="  black",command=lambda:self.changefg('black')) 
		menu_sub3.add_command(label ="  green",command=lambda:self.changefg('green')) 
		menu_sub3.add_command(label ="  white",command=lambda:self.changefg('white')) 
		menu_sub3.add_command(label ="  blue",command=lambda:self.changefg('blue')) 
		menu_sub3.add_command(label ="  orange",command=lambda:self.changefg('orange')) 
		menu_sub3.add_command(label ="  cyan",command=lambda:self.changefg('cyan')) 
		
		menu_sub4=Menu(self.window,tearoff=0)
		m.add_cascade(label="change fontsize",menu=menu_sub4)
		menu_sub4.add_command(label ="  5",command=lambda:self.changefs(5)) 
		menu_sub4.add_command(label ="  10",command=lambda:self.changefs(10))
		menu_sub4.add_command(label ="  15",command=lambda:self.changefs(15))
		menu_sub4.add_command(label ="  20",command=lambda:self.changefs(20))
		menu_sub4.add_command(label ="  30",command=lambda:self.changefs(30))
		menu_sub4.add_command(label ="  40",command=lambda:self.changefs(40))
		
		m.add_separator() 
		m.add_command(label ="Close") 
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
	
	def changebg(self,color):
		settings['background']=self.background=color
		self.update()
	
	def changefg(self,color):
		settings['foreground']=self.foreground=color
		self.update()
	
	def changefs(self,size):
		settings['fontsize']=self.fontsize=size
		self.update()
		
	def update(self):
		jsonchange(settings)
		self.inp1.config(font=("Courier", self.fontsize),fg=self.foreground,background=self.background)
		
	def run(self):
		self.inp1.bind("<Leave>",self.saveit)
		#self.inp1.bind("<key>",self.saveit)
		self.inp1.bind('<Button-3>',self.do_popup)
		self.window.protocol("WM_DELETE_WINDOW",self.close)
		self.window.mainloop()
