import wx

class ExampleTabs(wx.Frame):
    # Define the tab content as classes:
    class TabGeneric(wx.Panel):
        def __init__(self, parent, txt):
            wx.Panel.__init__(self, parent)
            self.t = wx.StaticText(self, -1, txt, (20,20))

    def __init__(self, parent, title):
        super(ExampleTabs, self).__init__(parent, title=title)
        self.InitUI()
    
    def InitUI(self):
        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p)
 
        # Create the tab windows
        tab1 = self.TabGeneric(nb, 'This is the first Tab!')
        tab2 = self.TabGeneric(nb, 'This is the second Tab!')
        tab3 = self.TabGeneric(nb, 'This is the third Tab!')
        tab4 = self.TabGeneric(nb, 'This is the last Tab!')
 
        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Tab 1")
        nb.AddPage(tab2, "Tab 2")
        nb.AddPage(tab3, "Tab 3")
        nb.AddPage(tab4, "Tab 4")
 
        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
        sizer.Layout()
    