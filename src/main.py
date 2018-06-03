from button             import ExampleButtons
from checkbox_scrollbar import ExampleCheckBoxesAndScrollBar
from divide_window      import ExampleDivideWindow
from framepos_statusbar import ExampleFramePositioningAndStatusBar
from menu               import ExampleMenu
from renamer            import ExampleRenamer
from tabs               import ExampleTabs
from tabsintab          import ExampleTabWithinTab

import wx

def main():
    app = wx.App()

    ex = list()
    ex.append(ExampleMenu(None, title='Simple menu'))
    ex.append(ExampleButtons(None, title='Skel of a Calculator'))
    ex.append(ExampleRenamer(None, title='Renamer - a GrindBox example'))
    ex.append(ExampleCheckBoxesAndScrollBar(None, title='Checkbox positioning'))
    ex.append(ExampleTabs(None, title='Tabs'))
    ex.append(ExampleTabWithinTab(None, title='Tabs in Tab'))
    ex.append(ExampleDivideWindow(None, title='Dividing window'))
    ex.append(ExampleFramePositioningAndStatusBar(None, title='Frame Position and Status Bar', size=(550,350)))
    
    for e in ex:
        e.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
