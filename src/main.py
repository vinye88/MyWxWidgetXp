import wx
import wx.lib.scrolledpanel
import wx.grid as gridlib

class Example_Menu(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example_Menu, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

class Example_Buttons(wx.Frame):

    def __init__(self, parent, title):
        super(Example_Buttons, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()


    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 4, 5, 5)

        gs.AddMany( [(wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Bck'), 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.Button(self, label='Close'), 0, wx.EXPAND),
            (wx.Button(self, label='7'), 0, wx.EXPAND),
            (wx.Button(self, label='8'), 0, wx.EXPAND),
            (wx.Button(self, label='9'), 0, wx.EXPAND),
            (wx.Button(self, label='/'), 0, wx.EXPAND),
            (wx.Button(self, label='4'), 0, wx.EXPAND),
            (wx.Button(self, label='5'), 0, wx.EXPAND),
            (wx.Button(self, label='6'), 0, wx.EXPAND),
            (wx.Button(self, label='*'), 0, wx.EXPAND),
            (wx.Button(self, label='1'), 0, wx.EXPAND),
            (wx.Button(self, label='2'), 0, wx.EXPAND),
            (wx.Button(self, label='3'), 0, wx.EXPAND),
            (wx.Button(self, label='-'), 0, wx.EXPAND),
            (wx.Button(self, label='0'), 0, wx.EXPAND),
            (wx.Button(self, label='.'), 0, wx.EXPAND),
            (wx.Button(self, label='='), 0, wx.EXPAND),
            (wx.Button(self, label='+'), 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

class ExampleRenamer(wx.Frame):

    def __init__(self, parent, title):
        super(ExampleRenamer, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)
        sizer.setsi

        text = wx.StaticText(panel, label="Rename To")
        sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        tc = wx.TextCtrl(panel)
        sizer.Add(tc, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
        buttonNok = wx.Button(panel, label="Nok", size=(90, 28))
        buttonClose = wx.Button(panel, label="Close", size=(90, 28))
        sizer.Add(buttonOk, pos=(3, 3))
        
        sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=10)
        sizer.Add(buttonNok, pos=(3,5))

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)

class ExampleCheckBoxesAndScrollBar(wx.Frame):

    def __init__(self, parent, title):
        super(ExampleCheckBoxesAndScrollBar, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
    
    def InitUI(self):
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        bSizer = wx.WrapSizer( wx.VERTICAL )
        pos_y = 0
        for i in range(50):
            pos_y += 20
            cb = wx.CheckBox(panel2, label="sample checkbox")
            bSizer.Add(cb, 0, wx.ALL, 5)
        panel2.SetSizer(bSizer)

class ExampleTabs(wx.Frame):
    # Define the tab content as classes:
    class TabGeneric(wx.Panel):
        def __init__(self, parent, txt):
            wx.Panel.__init__(self, parent)
            self.t = wx.StaticText(self, -1, txt, (20,20))

    def __init__(self, parent, title):
        super(ExampleTabs, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
    
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
        self.Centre()
    
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

class ExampleDivideWindow(wx.Frame):
    class UpperPanel(wx.Panel):
        def __init__(self, parent):
            wx.Panel.__init__(self, parent=parent)
    
            grid = gridlib.Grid(self)
            grid.CreateGrid(25,12)
    
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(grid, 0, wx.EXPAND)
            self.SetSizer(sizer)
    
    class LowerPanel(wx.Panel):
        def __init__(self, parent):
            wx.Panel.__init__(self, parent=parent)
            txt = wx.TextCtrl(self)

    def __init__(self, parent, title):
        super(ExampleDivideWindow, self).__init__(parent, title=title)
 
        splitter = wx.SplitterWindow(self)
        up = self.UpperPanel(splitter)
        low = self.LowerPanel(splitter)
 
        # split the window
        splitter.SplitHorizontally(up, low)
        splitter.SetSashInvisible(True)
        splitter.SetSashPosition(185, True)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)
 

def main():
    app = wx.App()
    #ex = Example_Menu(None)
    #ex = Example_Buttons(None, title='Calculator')
    #ex = ExampleRenamer(None, title='Renamer')
    #ex = ExampleCheckBoxesAndScrollBar(None, title='Checkboxes')
    #ex = ExampleTabs(None, title='Tabs')
    #ex = ExampleTabWithinTab(None, title='Tabs')
    ex = ExampleDivideWindow(None, title='Tabs')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
