# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Window
###########################################################################

class Window ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Adding editor to database", pos = wx.DefaultPosition, size = wx.Size( 320,130 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 320,130 ), wx.Size( -1,-1 ) )

		vertical_align = wx.BoxSizer( wx.VERTICAL )

		horizontal_align = wx.BoxSizer( wx.HORIZONTAL )

		self.name_text = wx.StaticText( self, wx.ID_ANY, u"Editor name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_text.Wrap( -1 )

		horizontal_align.Add( self.name_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.name_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal_align.Add( self.name_box, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		vertical_align.Add( horizontal_align, 0, wx.EXPAND, 5 )

		self.info_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.info_text.Wrap( -1 )

		vertical_align.Add( self.info_text, 1, wx.ALL|wx.EXPAND, 5 )

		self.add_button = wx.Button( self, wx.ID_ANY, u"Add Editor", wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical_align.Add( self.add_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.SetSizer( vertical_align )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.add_button.Bind( wx.EVT_BUTTON, self.add )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add( self, event ):
		event.Skip()


