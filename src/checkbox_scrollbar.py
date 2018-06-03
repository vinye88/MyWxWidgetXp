import wx
import wx.lib.scrolledpanel

class ExampleCheckBoxesAndScrollBar(wx.Frame):
    def __init__(self, parent, title):
        super(ExampleCheckBoxesAndScrollBar, self).__init__(parent, title=title)
        self.InitUI()
    
    def InitUI(self):
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        bSizer = wx.WrapSizer(wx.VERTICAL)
        pos_y = 0
        for i in range(50):
            pos_y += 20
            cb = wx.CheckBox(panel2, label="sample checkbox")
            bSizer.Add(cb, 0, wx.ALL, 5)
        panel2.SetSizer(bSizer)
