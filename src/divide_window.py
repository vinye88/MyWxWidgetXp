import wx
import wx.grid as gridlib

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
 