import tkinter as tk

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', borderwidth=0):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.borderwidth = borderwidth

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
        self['highlightthickness'] = 0
        self['borderwidth'] = self.borderwidth

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

if __name__ == "__main__": 
    root = tk.Tk() 
    username = EntryWithPlaceholder(root, "username")
    password = EntryWithPlaceholder(root, "password", 'blue')
    username.pack()
    password.pack()  
    root.mainloop()