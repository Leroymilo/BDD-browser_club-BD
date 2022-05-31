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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Adding series to database", pos = wx.DefaultPosition, size = wx.Size( 860,240 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 860,240 ), wx.Size( -1,-1 ) )

		vertical_align = wx.BoxSizer( wx.VERTICAL )

		h_align_1 = wx.BoxSizer( wx.HORIZONTAL )

		self.full_name_text = wx.StaticText( self, wx.ID_ANY, u"Series full name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.full_name_text.Wrap( -1 )

		h_align_1.Add( self.full_name_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.full_name_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_1.Add( self.full_name_box, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		vertical_align.Add( h_align_1, 0, wx.EXPAND, 5 )

		h_align_2 = wx.BoxSizer( wx.HORIZONTAL )

		self.id_text = wx.StaticText( self, wx.ID_ANY, u"Series id :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_text.Wrap( -1 )

		h_align_2.Add( self.id_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.id_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_box.SetMinSize( wx.Size( 100,-1 ) )
		self.id_box.SetMaxSize( wx.Size( 100,-1 ) )

		h_align_2.Add( self.id_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		vertical_align.Add( h_align_2, 0, wx.EXPAND, 5 )

		h_align_3 = wx.BoxSizer( wx.HORIZONTAL )

		self.cat_text = wx.StaticText( self, wx.ID_ANY, u"Category :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cat_text.Wrap( -1 )

		h_align_3.Add( self.cat_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cat_choiceChoices = []
		self.cat_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cat_choiceChoices, wx.CB_SORT )
		self.cat_choice.SetSelection( 0 )
		self.cat_choice.SetMinSize( wx.Size( 100,-1 ) )
		self.cat_choice.SetMaxSize( wx.Size( 100,-1 ) )

		h_align_3.Add( self.cat_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kind_text = wx.StaticText( self, wx.ID_ANY, u"Kind :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kind_text.Wrap( -1 )

		h_align_3.Add( self.kind_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		kind_choiceChoices = [ u"BD", u"Comic", u"Manga" ]
		self.kind_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, kind_choiceChoices, 0 )
		self.kind_choice.SetSelection( 0 )
		h_align_3.Add( self.kind_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		vertical_align.Add( h_align_3, 0, wx.EXPAND, 5 )

		h_align_4 = wx.BoxSizer( wx.HORIZONTAL )

		self.auth_text = wx.StaticText( self, wx.ID_ANY, u"Author(s) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.auth_text.Wrap( -1 )

		h_align_4.Add( self.auth_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		first_auth_choiceChoices = []
		self.first_auth_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, first_auth_choiceChoices, wx.CB_SORT )
		self.first_auth_choice.SetSelection( 0 )
		self.first_auth_choice.SetMaxSize( wx.Size( 120,-1 ) )

		h_align_4.Add( self.first_auth_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.add_auth_button = wx.Button( self, wx.ID_ANY, u"Create new author", wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_4.Add( self.add_auth_button, 0, wx.ALL, 5 )


		vertical_align.Add( h_align_4, 0, wx.EXPAND, 5 )

		self.info_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.info_text.Wrap( -1 )

		vertical_align.Add( self.info_text, 1, wx.EXPAND|wx.ALL, 5 )

		self.add_button = wx.Button( self, wx.ID_ANY, u"Add Series", wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical_align.Add( self.add_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( vertical_align )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.first_auth_choice.Bind( wx.EVT_CHOICE, self.change_authors )
		self.add_auth_button.Bind( wx.EVT_BUTTON, self.add_author )
		self.add_button.Bind( wx.EVT_BUTTON, self.add )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def change_authors( self, event ):
		event.Skip()

	def add_author( self, event ):
		event.Skip()

	def add( self, event ):
		event.Skip()


