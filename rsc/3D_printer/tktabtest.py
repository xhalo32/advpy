from tkinter import *

class Tabs(Frame):

    """Tabs for testgen output"""

    def __init__(self, parent):
        super(Tabs, self).__init__()
        self.parent = parent
        self.columnconfigure(10, weight=1)
        self.rowconfigure(3, weight=1)
        self.curtab = None
        self.tabs = {}
        self.addTab()                
        self.pack(fill=BOTH, expand=1, padx=5, pady=5)

    def addTab(self):
        tabslen = len(self.tabs)
        if tabslen < 10:
            tab = {}
            btn = Button(self, text="Tab "+str(tabslen), command=lambda: self.raiseTab(tabslen))
            btn.grid(row=0, column=tabslen, sticky=W+E)

            textbox = Text(self.parent)
            textbox.grid(row=1, column=0, columnspan=10, rowspan=2, sticky=W+E+N+S, in_=self)

            # Y axis scroll bar
            scrollby = Scrollbar(self, command=textbox.yview)
            scrollby.grid(row=7, column=10, rowspan=2, columnspan=1, sticky=N+S+E)
            textbox['yscrollcommand'] = scrollby.set

            tab['id']=tabslen
            tab['btn']=btn
            tab['txtbx']=textbox
            self.tabs[tabslen] = tab
            self.raiseTab(tabslen)

    def raiseTab(self, tabid):
        if self.curtab!= None and self.curtab != tabid and len(self.tabs)>1:
                self.tabs[tabid]['txtbx'].lift(self)
                self.tabs[self.curtab]['txtbx'].lower(self)
        self.curtab = tabid


def main():
    root = Tk()
    root.geometry("600x450+300+300")
    t = Tabs(root)
    t.addTab()
    root.mainloop()

if __name__ == '__main__':
    main()