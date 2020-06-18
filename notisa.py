import tkinter as tk

window = tk.Tk()
window.configure(background="grey")
window.title("Test appln")
window.geometry("540x540")

def openit():
	f=open("notes.txt","r")
	for line in f:
		inp1.insert(tk.INSERT,line)
	f.close()
	
def saveit(self):
	input_1=inp1.get("1.0","end-1c")
	f=open("notes.txt","w")
	f.write(input_1)
	f.close()

inp1=tk.Text(window,height=540,width=540 )
inp1.pack()
openit()
inp1.bind("<Leave>",saveit)
inp1.bind("<key>",saveit)

window.mainloop()
