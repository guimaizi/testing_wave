import tkinter
 
root = tkinter.Tk()
te = tkinter.Text(root)
sl = tkinter.Scrollbar(root)
sl.pack(side='right', fill='y')
te['yscrollcommand'] = sl.set
for i in range(10):
    string = str(i) + '\n'
    te.insert('end', string)
te.pack(side='left')
sl['command'] = te.yview
te.insert('end', 'xsssssss')
te.update()
root.mainloop()
