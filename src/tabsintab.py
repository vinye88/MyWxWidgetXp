import wx

class ExampleTabWithinTab(wx.Frame):
    class TabWithTabs(wx.Panel):
        class TabGeneric(wx.Panel):
            def __init__(self, parent, txt):
                wx.Panel.__init__(self, parent)
                self.t = wx.StaticText(self, -1, txt, (20,20))
        def __init__(self, parent, txt):
            wx.Panel.__init__(self, parent)
            nb = wx.Notebook(self)
    
            # Create the tab windows
            tab1 = self.TabGeneric(nb, 'This is the first Tab from ' + txt + '!')
            tab2 = self.TabGeneric(nb, 'This is the second Tab from ' + txt + '!')
            tab3 = self.TabGeneric(nb, 'This is the third Tab from ' + txt + '!')
            tab4 = self.TabGeneric(nb, 'This is the last Tab from ' + txt + '!')
    
            # Add the windows to tabs and name them.
            nb.AddPage(tab1, "Tab " + txt + ' 1')
            nb.AddPage(tab2, "Tab " + txt + ' 2')
            nb.AddPage(tab3, "Tab " + txt + ' 3')
            nb.AddPage(tab4, "Tab " + txt + ' 4')
    
            # Set noteboook in a sizer to create the layout
            sizer = wx.BoxSizer()
            sizer.Add(nb, 1, wx.EXPAND)
            self.SetSizer(sizer)
            sizer.Layout()

    def __init__(self, parent, title):
        super(ExampleTabWithinTab, self).__init__(parent, title=title)
        self.InitUI()
    
    def InitUI(self):
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        tab1 = self.TabWithTabs(nb, 'A')
        tab2 = self.TabWithTabs(nb, 'B')

        nb.AddPage(tab1, "Tab A")
        nb.AddPage(tab2, "Tab B")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
        sizer.Layout()
        return p
