from gen_UIs.book_GUI import Window

from functions.adders import *
from functions.getters import *

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