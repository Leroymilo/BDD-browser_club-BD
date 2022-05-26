import wx
import wx.dataview

from functions.adders import *
from functions.getters import *
from functions.removers import *

from UIs.authors import Author_UI
from UIs.editors import Editor_UI
from UIs.series import Series_UI
from UIs.books import Book_UI
from UIs.users import User_UI
from UIs.loan import Loan_UI

from UIs.series import Series_modif

attributes = {"Users":["ID", "First name", "Last name", "tel", "e-mail", "Loans", "Late loans"],
"Books":["ID", "Series", "Volume", "Volume name", "Copy", "Category", "Type", "Editor", "Buy date", "Disponibility", "Old ID"],
"Loans":["First name", "Last name", "ID book", "Book name", "Volume", "Start date", "End date"],
"Series":["ID", "Full name", "Authors", "Category", "Type"],
"Authors":["ID", "Name"],
"Editors":["ID", "Name"]}
#Attributes displayed

search_att = {"Users":["First name", "Last name"],
"Books":["Series", "Category", "Editor"],
"Loans":["First name", "Last name", "Book name"],
"Series":["ID", "Full name", "Authors"],
"Authors":["Name"],
"Editors":["Name"]}
#Attributes the user can search on

getters = {"Users":get_users, "Books":get_books, "Loans":get_loans,
"Series":get_series, "Authors":get_authors, "Editors":get_editors}

adders = {"Users":User_UI, "Books":Book_UI, "Loans":Loan_UI,
"Series":Series_UI, "Authors":Author_UI, "Editors":Editor_UI}

modifiers = {"Series":Series_modif}

removers = {"Users":remove_users, "Books":remove_book, "Series":remove_series,
"Authors":remove_author, "Editors":remove_editor}

from main_window import Window
class main(Window) : 
    def __init__(self,parent) : 
        Window.__init__(self,parent)
        self.Show()
        self.Maximize()
        self.table = []
        self.update_select()
        self.message("Click a column to sort the table by this attribute")
    
    def update_select(self, event=None) :
        table = self.table_choice.GetStringSelection()
        self.search_choice.Clear()
        self.search_choice.AppendItems(search_att[table])
        self.search_choice.SetSelection(0)
        self.search_box.SetLabelText('')
        self.add_button.SetLabel("Add "+table.lower())
        self.update_table()
        self.display_table()
    
    def update_authors(self) :
        if self.table_choice.GetStringSelection() == "Authors" :
            self.update_table()
            self.display_table()
    
    def update_editors(self) :
        if self.table_choice.GetStringSelection() == "Editors" :
            self.update_table()
            self.display_table()
    
    def update_series(self) :
        if self.table_choice.GetStringSelection() == "Series" :
            self.update_table()
            self.display_table()
    
    def update_books(self) :
        if self.table_choice.GetStringSelection() == "Books" :
            self.update_table()
            self.display_table()
    
    def update_users(self) :
        if self.table_choice.GetStringSelection() == "Users" :
            self.update_table()
            self.display_table()
    
    def update_loans(self) :
        if self.table_choice.GetStringSelection() == "Loans" :
            self.update_table()
            self.display_table()
    
    def update_table(self) :
        table_name = self.table_choice.GetStringSelection()
        self.table_display.ClearColumns()
        for column_name in attributes[table_name] :
            self.table_display.AppendTextColumn(column_name)
        self.table = getters[table_name]()

    def display_table(self) :
        self.table_display.DeleteAllItems()
        for line in self.table :
            self.table_display.AppendItem(line)
    
    def sort(self, event) :
        column_pos = self.table_display.GetColumnPosition(event.GetDataViewColumn())
        self.table.sort(key=lambda t:t[column_pos])
        self.display_table()
    
    def search(self, event) :
        table_name = self.table_choice.GetStringSelection()
        string = self.search_box.GetLineText(0)
        if string.strip() == '' :
            self.table = getters[table_name]()
        else :
            self.table = getters[table_name]((self.search_choice.GetStringSelection(), string))
        self.display_table()
    
    def add(self, event) :
        sub_frame = adders[self.table_choice.GetStringSelection()](self)
        sub_frame.Show(True)
    
    def remove(self, event) :
        if self.table_display.GetSelectedRow() == -1 :
            self.message("No item selected")
            return

        conf = wx.MessageDialog(self, "", "", wx.CANCEL | wx.OK)
        conf.SetExtendedMessage("""You are about to delete the selected item from the database.
This action will also delete all items refering to the selected item, are you sure?""")
        conf.SetYesNoLabels("Continue", "Cancel")
        if conf.ShowModal() == 5101 :
            return
        
        row = self.table_display.GetSelectedRow()
        table_name = self.table_choice.GetStringSelection()

        if table_name == "Loans" :
            f_name = self.table_display.GetValue(row, 0)
            l_name = self.table_display.GetValue(row, 1)
            book_id = self.table_display.GetValue(row, 2)
            end_loan(f_name, l_name, book_id)
            self.message("Loan succesfully ended.")
        
        else :
            removers[table_name](self.table_display.GetValue(row, 0))
        
        self.update_table()
        self.display_table()
    
    def edit(self, event):
        row = self.table_display.GetSelectedRow()
        if row == -1 :
            self.message("No item selected")
            return
        
        table_name = self.table_choice.GetStringSelection()
        if table_name not in modifiers :
            self.message("Cannot modify these items")
            return
        item_id = self.table_display.GetValue(row, 0)
        
        sub_frame = modifiers[table_name](self, item_id)
        sub_frame.Show(True)
        

    def message(self, msg:str) :
        self.text_info.SetLabelText(msg)

app = wx.App(False) 
frame = main(None) 
#start the applications 
app.MainLoop()

db.close()
