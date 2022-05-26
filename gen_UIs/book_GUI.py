# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class Window
###########################################################################

class Window ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Adding book to database", pos = wx.DefaultPosition, size = wx.Size( -1,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,200 ), wx.Size( -1,200 ) )

		vertical_align = wx.BoxSizer( wx.VERTICAL )

		h_align_1 = wx.BoxSizer( wx.HORIZONTAL )

		self.series_text = wx.StaticText( self, wx.ID_ANY, u"Series :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.series_text.Wrap( -1 )

		h_align_1.Add( self.series_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		series_choiceChoices = []
		self.series_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, series_choiceChoices, wx.CB_SORT )
		self.series_choice.SetSelection( 0 )
		h_align_1.Add( self.series_choice, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.series_button = wx.Button( self, wx.ID_ANY, u"Add Series", wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_1.Add( self.series_button, 0, wx.ALL, 5 )


		vertical_align.Add( h_align_1, 0, wx.EXPAND, 5 )

		h_align_2 = wx.BoxSizer( wx.HORIZONTAL )

		self.vol_text = wx.StaticText( self, wx.ID_ANY, u"Volume :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vol_text.Wrap( -1 )

		h_align_2.Add( self.vol_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vol_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_2.Add( self.vol_box, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.vol_name_text = wx.StaticText( self, wx.ID_ANY, u"Volume name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vol_name_text.Wrap( -1 )

		h_align_2.Add( self.vol_name_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vol_name_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_2.Add( self.vol_name_box, 1, wx.ALL, 5 )


		vertical_align.Add( h_align_2, 0, wx.EXPAND, 5 )

		h_align_3 = wx.BoxSizer( wx.HORIZONTAL )

		self.edit_text = wx.StaticText( self, wx.ID_ANY, u"Editor :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edit_text.Wrap( -1 )

		h_align_3.Add( self.edit_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		edit_choiceChoices = []
		self.edit_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, edit_choiceChoices, wx.CB_SORT )
		self.edit_choice.SetSelection( 0 )
		h_align_3.Add( self.edit_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.add_edit_button = wx.Button( self, wx.ID_ANY, u"Add Editor", wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_3.Add( self.add_edit_button, 0, wx.ALL, 5 )

		self.buy_text = wx.StaticText( self, wx.ID_ANY, u"Buy date :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buy_text.Wrap( -1 )

		h_align_3.Add( self.buy_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 110,-1 ), wx.adv.DP_DROPDOWN )
		h_align_3.Add( self.m_datePicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		vertical_align.Add( h_align_3, 0, wx.EXPAND, 5 )

		self.info_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.info_text.Wrap( -1 )

		vertical_align.Add( self.info_text, 1, wx.ALL|wx.EXPAND, 5 )

		self.add_button = wx.Button( self, wx.ID_ANY, u"Add Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical_align.Add( self.add_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( vertical_align )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.series_button.Bind( wx.EVT_BUTTON, self.add_series )
		self.add_edit_button.Bind( wx.EVT_BUTTON, self.add_editor )
		self.add_button.Bind( wx.EVT_BUTTON, self.add )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_series( self, event ):
		event.Skip()

	def add_editor( self, event ):
		event.Skip()

	def add( self, event ):
		event.Skip()


