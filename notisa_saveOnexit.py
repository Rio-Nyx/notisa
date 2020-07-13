#saves on exit
import tkinter as tk 
window = tk.Tk()
window.configure(background="grey")
window.title("Notiverse")
window.geometry("540x540")
def openit():
	try:
		f=open("notes.txt","r")
		for line in f:
			inp1.insert(tk.INSERT,line)		
	except:
		f=open("notes.txt","x")	
	f.close()	
def saveit():
	input_1=inp1.get("1.0","end-1c")
	f=open("notes.txt","w")
	f.write(input_1)
	f.close()
	window.destroy()
inp1=tk.Text(window,height=540,width=540 )
inp1.pack()
openit()
window.protocol("WM_DELETE_WINDOW",saveit)
window.mainloop()
