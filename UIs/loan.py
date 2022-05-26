from gen_UIs.loan_GUI import Window

from functions.adders import *
from functions.getters import *

from UIs.books import Book_UI
from UIs.users import User_UI

class Loan_UI(Window) :
    def __init__(self, parent) :
        Window.__init__(self, parent)
        self.update_users()
        self.update_books()
    
    def update_users(self) :
        self.users = get_users_select()
        self.user_choice.Clear()
        self.user_choice.AppendItems(list(self.users))
    
    def update_books(self) :
        self.book_choice.Clear()
        self.book_choice.AppendItems(get_books_select())
    
    def add(self, event) :
        user = self.user_choice.GetStringSelection()
        if len(user) == 0 :
            self.message("Please choose a user")
            return
        book = self.book_choice.GetStringSelection()
        if len(book) == 0 :
            self.message("Please choose a book")
            return
        start_date = self.start_picker.GetValue().Format("%Y-%m-%d")
        end_date = self.end_picker.GetValue().Format("%Y-%m-%d")
        error = add_loan(book, self.users[user], start_date, end_date)
        if error == 0 :
            db.commit()
            self.message(f"{user} took a loan on {book}")
            self.Parent.update_loans()
            return
        elif error == 1 :
            self.message(f"{book} is not available")
            return
        elif error == 2 :
            self.message(f"{user} has to many loans")
            return

    def add_user(self, event) :
        sub_frame = User_UI(self)
        sub_frame.Show(True)

    def add_book(self, event) :
        sub_frame = Book_UI(self)
        sub_frame.Show(True)

    def message(self, msg:str) :
        self.info_text.SetLabelText(msg)