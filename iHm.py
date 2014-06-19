# -*- coding: utf-8 -*-
import wx
from CodePassGnerator import getPassWord

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition)
        self.initialize(parent)


    def initialize(self,parent):
        sizer = wx.GridBagSizer(9, 9)
        self.panel = wx.Panel(self,size = self.GetClientSize())

        #line 1
        self.labl = wx.StaticText(self.panel,-1,"Choose Number : ")
        sizer.Add(self.labl ,(0,0),wx.DefaultSpan, wx.ALL,5)
        self.inputNumber = wx.TextCtrl(self.panel,-1)
        sizer.Add(self.inputNumber,(0,1),wx.DefaultSpan,wx.ALL,5)

        # Line 2
        self.result = wx.TextCtrl(self.panel,-1,style = wx.NO_BORDER)

        # """on récupère la couleur de l'élément parent"""

        self.color = wx.ColourDialog(self,parent)
        ## On Set la couleur
        self.result.SetBackgroundColour(str(self.color.GetColourData()))

        # Line 3
        self.btn = wx.Button(self.panel,1,'Generate Password')


        self.result.SetEditable(False)
        sizer.Add(self.result,(1,0),wx.DefaultSpan,wx.ALL,5)
        self.Bind(wx.EVT_BUTTON, self.onClickGenerate, id=1)
        sizer.Add(self.btn,(2,0),(1,2),wx.ALIGN_CENTER,5,5)

        sizer.AddGrowableRow(0)
        sizer.AddGrowableCol(0)

        self.SetSizerAndFit(sizer)
        self.Centre()


    def onClickGenerate(self,event):
        nbCaract = self.inputNumber.GetValue()
        self.result.SetLabel(getPassWord(nbCaract))







class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "Password Generator")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


app = MyApp(0)
app.MainLoop()
