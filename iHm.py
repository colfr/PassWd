import wx
from CodePassGnerator import getPassWord

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition)
        self.initialize()


    def initialize(self):
        sizer = wx.GridBagSizer(9, 9)
        self.panel = wx.Panel(self,size = self.GetClientSize())
        self.labl = wx.StaticText(self.panel,-1,"Choose Number : ")
        sizer.Add(self.labl ,(0,0),wx.DefaultSpan, wx.ALL,5)

        self.inputNumber = wx.TextCtrl(self.panel,-1)
        sizer.Add(self.inputNumber,(0,1),wx.DefaultSpan,wx.ALL,5)

        self.btn = wx.Button(self.panel,1,'Generate Password')
        self.result = wx.StaticText(self.panel,-1,"")
        sizer.Add(self.result,(1,0),wx.DefaultSpan,wx.ALL,5)
        self.Bind(wx.EVT_BUTTON, self.onClickGenerate, id=1)
        sizer.Add(self.btn,(2,0),(1,2),wx.ALIGN_CENTER,5,5)

        sizer.AddGrowableRow(0)
        sizer.AddGrowableCol(0)

        self.SetSizerAndFit(sizer)
        self.Centre()


    def onClickGenerate(self,event):
        self.result.SetLabel(getPassWord(5))







class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "wxgridbagsizer.py")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


app = MyApp(0)
app.MainLoop()
