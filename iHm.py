#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Franck Colombo'


"""
    Merci a SebSauvage
"""
try:
    import wx
except ImportError:
    raise ImportError, b"The wxPython module is required to run this program"

class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent,id, title):
        wx.Frame.__init__(self, parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        self.quote = wx.StaticText(self, -1,label="Select caracters numbers : ")
        sizer.Add(self.quote,(0,0),(1,1),wx.EXPAND)

        button = wx.Button(self,-1,label="Click me !")
        sizer.Add(button, (1,0),(1,2), wx.EXPAND)
        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.Show(True)




if __name__ == "__main__":

    app = wx.App()
    frame = MyFrame(None,-1,'PassWord Generator')
    app.MainLoop()