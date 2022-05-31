# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class Window
###########################################################################

class Window ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DB Browser", pos = wx.DefaultPosition, size = wx.Size( 1000,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 1000,500 ), wx.DefaultSize )
		
		vertical_align = wx.BoxSizer( wx.VERTICAL )
		
		horizontal_align_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.add_button = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		horizontal_align_1.Add( self.add_button, 0, wx.ALL, 5 )
		
		self.remove_button = wx.Button( self, wx.ID_ANY, u"Remove selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal_align_1.Add( self.remove_button, 0, wx.ALL, 5 )
		
		self.edit_button = wx.Button( self, wx.ID_ANY, u"Edit selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal_align_1.Add( self.edit_button, 0, wx.ALL, 5 )
		
		
		vertical_align.Add( horizontal_align_1, 0, wx.EXPAND, 5 )
		
		horizontal_align_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.text_show = wx.StaticText( self, wx.ID_ANY, u"Show :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_show.Wrap( -1 )
		horizontal_align_2.Add( self.text_show, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		table_choiceChoices = [ u"Users", u"Books", u"Loans", u"Series", u"Authors", u"Editors" ]
		self.table_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, table_choiceChoices, 0 )
		self.table_choice.SetSelection( 0 )
		horizontal_align_2.Add( self.table_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_search = wx.StaticText( self, wx.ID_ANY, u"Search :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_search.Wrap( -1 )
		horizontal_align_2.Add( self.text_search, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.search_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal_align_2.Add( self.search_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_on = wx.StaticText( self, wx.ID_ANY, u"on :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_on.Wrap( -1 )
		horizontal_align_2.Add( self.text_on, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		search_choiceChoices = [ u"ID", u"First name", u"Last name", u"tel", u"e-mail", u"Loans", u"Late loans" ]
		self.search_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_choiceChoices, 0 )
		self.search_choice.SetSelection( 0 )
		horizontal_align_2.Add( self.search_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal_align_2.Add( self.search_button, 0, wx.ALL, 5 )
		
		
		vertical_align.Add( horizontal_align_2, 0, wx.EXPAND, 5 )
		
		self.table_display = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical_align.Add( self.table_display, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.text_info = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_info.Wrap( -1 )
		vertical_align.Add( self.text_info, 0, wx.ALL, 5 )
		
		
		self.SetSizer( vertical_align )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.add_button.Bind( wx.EVT_BUTTON, self.add )
		self.remove_button.Bind( wx.EVT_BUTTON, self.remove )
		self.edit_button.Bind( wx.EVT_BUTTON, self.edit )
		self.table_choice.Bind( wx.EVT_CHOICE, self.update_select )
		self.search_button.Bind( wx.EVT_BUTTON, self.search )
		self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_HEADER_CLICK, self.sort, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def add( self, event ):
		event.Skip()
	
	def remove( self, event ):
		event.Skip()
	
	def edit( self, event ):
		event.Skip()
	
	def update_select( self, event ):
		event.Skip()
	
	def search( self, event ):
		event.Skip()
	
	def sort( self, event ):
		event.Skip()
	

