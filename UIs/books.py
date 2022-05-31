import wx

from gen_UIs.book_GUI import Window

from functions.adders import *
from functions.getters import *
from functions.modifiers import *

from UIs.series import Series_UI
from UIs.editors import Editor_UI

class Book_UI(Window) :
    def __init__(self, parent) :
        Window.__init__(self, parent)
        self.update_series()
        self.update_editors()
    
    def update_series(self) :
        self.series = get_series_select()
        self.series_choice.Clear()
        self.series_choice.AppendItems(list(self.series))
    
    def update_editors(self) :
        self.editors = get_edits_select()
        self.edit_choice.Clear()
        self.edit_choice.AppendItems(list(self.editors))
    
    def add(self, event) :
        try :
            nb = int(self.vol_box.GetLineText(0))
        except :
            self.message("Please enter a valid volume number")
            return
        date = self.m_datePicker1.GetValue().Format("%Y-%m-%d")
        
        editor_name = self.edit_choice.GetStringSelection()
        if editor_name == '' :
            editor = None
        else :
            editor = self.editors[editor_name]

        series_title = self.series_choice.GetStringSelection()
        if series_title == '' :
            self.message("Please select series or create some")
            return
        series = self.series[series_title]

        vol_name = self.vol_name_box.GetLineText(0).strip(' ').replace('"', '”')
        add_book(series, nb, vol_name, editor, date)
        self.message("Book added to database")
        db.commit()
        self.Parent.update_books()

    def add_series(self, event) :
        sub_frame = Series_UI(self)
        sub_frame.Show(True)

    def add_editor(self, event) :
        sub_frame = Editor_UI(self)
        sub_frame.Show(True)
    
    def message(self, msg) :
        self.info_text.SetLabelText(msg)

class Book_modif(Book_UI) :
    def __init__(self, parent, item_id):
        super().__init__(parent)
        self.add_button.SetLabel("Apply Edit")
        self.SetTitle("Modifying book in database")

        self.old_item = get_book_data(item_id)

        series_sizer = self.GetSizer().GetChildren()[0].GetSizer()
        series_sizer.GetChildren()[2].GetWindow().Destroy()
        series_sizer.GetChildren()[1].GetWindow().Destroy()
        self.series_choice = wx.StaticText( self, wx.ID_ANY, self.old_item[1], wx.DefaultPosition, wx.DefaultSize, 0 )
        series_sizer.Add(self.series_choice, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        self.Layout()

        self.vol_box.SetValue(str(self.old_item[2]))
        self.vol_box.SetEditable(False)

        self.vol_name_box.SetValue(self.old_item[3])
        if self.old_item[4] is not None :
            self.edit_choice.SetStringSelection(self.old_item[4])
        a, m, j = map(int, self.old_item[5].split('-'))
        self.m_datePicker1.SetValue(wx.DateTime(j, m-1, a))

        self.message("To change series or volume number, please delete and recreate book.")
    
    def add(self, event) :
        try :
            nb = int(self.vol_box.GetLineText(0))
        except :
            self.message("Please enter a valid volume number")
            return
        date = self.m_datePicker1.GetValue().Format("%Y-%m-%d")
        
        editor_name = self.edit_choice.GetStringSelection()
        if editor_name == '' :
            editor = None
        else :
            editor = self.editors[editor_name]

        series_title = self.series_choice.GetLabel()
        if series_title == '' :
            self.message("Please select series or create some")
            return
        series = self.series[series_title]

        vol_name = self.vol_name_box.GetLineText(0).strip(' ').replace('"', '”')

        modif_book(self.old_item[0], vol_name, editor, date)
        self.message("Book modified in database")
        db.commit()
        self.Parent.update_books()
