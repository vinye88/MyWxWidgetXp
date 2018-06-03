import wx

class ExampleFramePositioningAndStatusBar(wx.Frame):
    class TabGeneric(wx.Panel):
        def __init__(self, parent, txt, size=wx.DefaultSize):
            wx.Panel.__init__(self, parent, size=size)
            self.t = wx.StaticText(self, -1, txt, pos=(20,20))

    def __init__(self, parent, title, size=(600,480)):
        self.size = size
        super(ExampleFramePositioningAndStatusBar, self).__init__(parent, title=title, size=self.size, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.InitUI()
        
    def InitUI(self):
        p = wx.Panel(self, pos=(20,20))
        nb = wx.Notebook(p)
        w,h = self.size
        tab1 = self.TabGeneric(nb, 'This is the first Tab!', (w-50, h-120))
        tab2 = self.TabGeneric(nb, 'This is the second Tab!', (w-50, h-120))

        nb.AddPage(tab1, "Tab 1")
        nb.AddPage(tab2, "Tab 2")

        sizer = self.Enclosure(nb)
        p.SetSizer(sizer)

        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('Welcome to ExampleFramePosition!')       

        nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.TabChanged) 

    def TabChanged(self, evt):
        tabName = evt.EventObject.GetPageText(evt.GetSelection())
        self.statusbar.SetStatusText('Tab changed to ' + tabName)


    def Enclosure(self, el):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(el, 1,wx.ALIGN_CENTER)
        sizer.Layout()
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer2.Add(sizer, 1,wx.ALIGN_CENTER)
        sizer2.Layout()
        return sizer2
