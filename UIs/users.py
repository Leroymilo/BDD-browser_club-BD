import gen_UIs.user_GUI as gen

from functions.adders import *
from functions.modifiers import *

class User_UI(gen.Window):
    def __init__(self, parent):
        gen.Window.__init__(self, parent)

    def add(self, event):
        f_name = self.f_name_box.GetLineText(0).strip(' ').replace('"', '”')
        if len(f_name) == 0:
            self.message('Please enter a first name')
            return
        l_name = self.l_name_box.GetLineText(0).strip(' ').replace('"', '”')
        tel = self.tel_box.GetLineText(0).strip(' ')
        mail = self.mail_box.GetLineText(0).strip(' ').replace('"', '”')
        # Be carefull of the replacement of quote characters if you decide to automate mails.

        if len(mail) == 0 and len(tel) == 0:
            self.message('Please enter some contact information')
            return

        if len(tel) not in {0, 10} or not tel.isnumeric():
            self.message('Please enter a valid phone number')

        added = add_user(f_name, l_name, tel, mail, self.loan_spin.GetValue())

        if added:
            self.message(f"User {f_name} {l_name} added to database")
            self.Parent.update_users()
        else:
            self.message(f"User {f_name} {l_name} already exists")

    def message(self, msg: str):
        self.info_text.SetLabelText(msg)


class User_modif(User_UI):
    def __init__(self, parent, item_id):
        super().__init__(parent)
        self.item_id = item_id
        cursor.execute(f"SELECT f_name, l_name, tel, mail, max_loan_nb FROM USERS WHERE id={item_id}")
        f_name, l_name, tel, mail, max_loan_nb = cursor.fetchone()

        self.f_name_box.SetValue(f_name)
        self.l_name_box.SetValue(l_name)
        self.tel_box.SetValue(tel)
        self.mail_box.SetValue(mail)
        self.loan_spin.SetValue(max_loan_nb)

        self.SetTitle("Modifying user in database")
        self.add_button.SetLabel("Apply Edit")

    def add(self, event):
        f_name = self.f_name_box.GetLineText(0).strip(' ').replace('"', '”')
        if len(f_name) == 0:
            self.message('Please enter a first name')
            return
        l_name = self.l_name_box.GetLineText(0).strip(' ').replace('"', '”')
        tel = self.tel_box.GetLineText(0).strip(' ')
        mail = self.mail_box.GetLineText(0).strip(' ').replace('"', '”')
        # Be carefull of the replacement of quote characters if you decide to automate mails.

        if len(mail) == 0 and len(tel) == 0:
            self.message('Please enter some contact information')
            return

        if len(tel) not in {0, 10} or not tel.isnumeric():
            self.message('Please enter a valid phone number')

        modified = modif_user(self.item_id, f_name, l_name, tel, mail, self.loan_spin.GetValue())

        if modified:
            self.message(f"User {f_name} {l_name} modified in database")
            self.Parent.update_users()
        else:
            self.message(f"User {f_name} {l_name} is already taken")

    def message(self, msg: str):
        self.info_text.SetLabelText(msg)