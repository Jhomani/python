import tkinter as tk

root = tk.Tk()
# Window Settings
root.title('Application Title')
root.geometry('400x200')
root.configure(background = '#000')

a = tk.Label(
  root,
  anchor='nw',
  justify='left', 
  text="Hello, world!",
  fg="white",
  bg="black",
  width= 100,
  height=5
  )
a.pack()

tk.Button(root, text='Exit', width=10, command=root.destroy).pack()

root.mainloop()

print("hello Work")
