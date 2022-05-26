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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Adding loan to database", pos = wx.DefaultPosition, size = wx.Size( 500,162 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,162 ), wx.Size( -1,162 ) )

		vertical_align = wx.BoxSizer( wx.VERTICAL )

		h_align_1 = wx.BoxSizer( wx.HORIZONTAL )

		self.user_text = wx.StaticText( self, wx.ID_ANY, u"User :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user_text.Wrap( -1 )

		h_align_1.Add( self.user_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		user_choiceChoices = []
		self.user_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, user_choiceChoices, 0 )
		self.user_choice.SetSelection( 0 )
		h_align_1.Add( self.user_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.add_user_button = wx.Button( self, wx.ID_ANY, u"Add User", wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_1.Add( self.add_user_button, 0, wx.ALL, 5 )

		self.book_text = wx.StaticText( self, wx.ID_ANY, u"Book :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.book_text.Wrap( -1 )

		h_align_1.Add( self.book_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		book_choiceChoices = []
		self.book_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, book_choiceChoices, 0 )
		self.book_choice.SetSelection( 0 )
		h_align_1.Add( self.book_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.add_book_button = wx.Button( self, wx.ID_ANY, u"Add Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_1.Add( self.add_book_button, 0, wx.ALL, 5 )


		vertical_align.Add( h_align_1, 0, wx.EXPAND, 5 )

		h_align_2 = wx.BoxSizer( wx.HORIZONTAL )

		self.start_text = wx.StaticText( self, wx.ID_ANY, u"Start of the loan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.start_text.Wrap( -1 )

		h_align_2.Add( self.start_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.start_picker = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 110,-1 ), wx.adv.DP_DROPDOWN )
		h_align_2.Add( self.start_picker, 0, wx.ALL, 5 )

		self.end_text = wx.StaticText( self, wx.ID_ANY, u"End of the loan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.end_text.Wrap( -1 )

		h_align_2.Add( self.end_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.end_picker = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 110,-1 ), wx.adv.DP_DROPDOWN )
		h_align_2.Add( self.end_picker, 0, wx.ALL, 5 )


		vertical_align.Add( h_align_2, 0, wx.EXPAND, 5 )

		self.info_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.info_text.Wrap( -1 )

		vertical_align.Add( self.info_text, 0, wx.ALL, 5 )

		self.add_button = wx.Button( self, wx.ID_ANY, u"Add Loan", wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical_align.Add( self.add_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( vertical_align )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.add_user_button.Bind( wx.EVT_BUTTON, self.add_user )
		self.add_book_button.Bind( wx.EVT_BUTTON, self.add_book )
		self.add_button.Bind( wx.EVT_BUTTON, self.add )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_user( self, event ):
		event.Skip()

	def add_book( self, event ):
		event.Skip()

	def add( self, event ):
		event.Skip()


