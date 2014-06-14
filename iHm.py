#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Franck Colombo'


"""
    Merci a SebSauvage
"""
try:
    import wx
except ImportError:
    raise ImportError, b"Veuillez télécharger wxPython"

class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent,id, title):
        wx.Frame.__init__(self, parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.Show(True)


if __name__ == "__main__":

    app = wx.App()
    frame = MyFrame(None,-1,'Générateur de mots de passe')
    app.MainLoop()