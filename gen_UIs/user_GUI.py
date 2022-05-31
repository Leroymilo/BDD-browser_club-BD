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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Adding user to database", pos = wx.DefaultPosition, size = wx.Size( -1,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,200 ), wx.DefaultSize )

		vertical_align = wx.BoxSizer( wx.VERTICAL )

		h_align_1 = wx.BoxSizer( wx.HORIZONTAL )

		self.f_name_text = wx.StaticText( self, wx.ID_ANY, u"First Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.f_name_text.Wrap( -1 )

		h_align_1.Add( self.f_name_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.f_name_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_1.Add( self.f_name_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.l_name_text = wx.StaticText( self, wx.ID_ANY, u"Last Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_name_text.Wrap( -1 )

		h_align_1.Add( self.l_name_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.l_name_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_1.Add( self.l_name_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		vertical_align.Add( h_align_1, 0, wx.EXPAND, 5 )

		h_align_2 = wx.BoxSizer( wx.HORIZONTAL )

		self.tel_text = wx.StaticText( self, wx.ID_ANY, u"Tel :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tel_text.Wrap( -1 )

		h_align_2.Add( self.tel_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tel_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_2.Add( self.tel_box, 0, wx.ALL, 5 )

		self.mail_text = wx.StaticText( self, wx.ID_ANY, u"Mail :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mail_text.Wrap( -1 )

		h_align_2.Add( self.mail_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mail_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		h_align_2.Add( self.mail_box, 1, wx.ALL, 5 )


		vertical_align.Add( h_align_2, 0, wx.EXPAND, 5 )

		h_align_3 = wx.BoxSizer( wx.HORIZONTAL )

		self.loan_text = wx.StaticText( self, wx.ID_ANY, u"Loans allowed :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loan_text.Wrap( -1 )

		h_align_3.Add( self.loan_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.loan_spin = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 10 )
		h_align_3.Add( self.loan_spin, 0, wx.ALL, 5 )


		vertical_align.Add( h_align_3, 0, wx.EXPAND, 5 )

		self.info_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.info_text.Wrap( -1 )

		vertical_align.Add( self.info_text, 1, wx.ALL|wx.EXPAND, 5 )

		self.add_button = wx.Button( self, wx.ID_ANY, u"Add User", wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical_align.Add( self.add_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


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


