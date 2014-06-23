
from __future__ import unicode_literals
#  -*- coding: utf-8 -*-
__author__ = 'Trashy'



import wx

import CodePassGnerator

class windowPass(wx.Frame):

    def __init__(self, parent, title):
        no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER |
                                                wx.RESIZE_BOX |
                                                wx.MAXIMIZE_BOX)

        super(windowPass, self).__init__(parent, title=title,style=no_resize,
            size=(450, 250))

        self.parent =parent
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        self.type=0
        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)


        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Choose number caracters :')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(panel)
        hbox1.Add(self.tc, flag= wx.RIGHT,proportion=1, border=8)
        self.choice =wx.Choice(panel,2,choices = ['','With Special caracters','Alphabetical'])
        hbox1.Add(self.choice,proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.Bind(wx.EVT_CHOICE,self.selectTypePwd, id=2)

        vbox.Add((-1, 10))

        # ---------  Line 2 --------
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        self.result = wx.TextCtrl(panel,-1,style = wx.TE_READONLY|wx.NO_BORDER | wx.TE_CENTRE,size=(345,30))
        self.color = wx.ColourDialog(self,self.parent)
        ## On Set la couleur
        self.result.SetBackgroundColour(str(self.color.GetColourData()))
        hbox2.Add(self.result, flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, border=15)
        btnPaste =wx.Button(panel,-1, label='Copy', size=(50,30))
        hbox2.Add(btnPaste, flag= wx.RIGHT|wx.TOP|wx.EXPAND, border=5)
        self.Bind(wx.EVT_BUTTON,self.onSubmitPaste,btnPaste)

        vbox.Add(hbox2, flag=wx.EXPAND | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel,1, label='Ok', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onClickGenerate, id=1)
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)

    def onClickGenerate(self,event):
        nbCaract = self.tc.GetValue()

        self.result.SetLabel(CodePassGnerator.getPassWord(nbCaract,self.type))

    def selectTypePwd(self,event):

        type = self.choice.GetSelection()

        if(type == 1):
            self.type = 0
        else:
            self.type = 1

    def onSubmitPaste(self,event):

        clipdata = wx.TextDataObject()
        clipdata.SetText(self.result.GetValue())
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()







if __name__ == '__main__':

    app = wx.App()
    windowPass(None, title='Password Generator')
    app.MainLoop()