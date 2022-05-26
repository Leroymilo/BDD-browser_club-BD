import gen_UIs.user_GUI as gen

from functions.adders import *

class User_UI(gen.Window) :
   def __init__(self, parent) :
      gen.Window.__init__(self, parent)
   
   def add(self, event) :
      f_name = self.f_name_box.GetLineText(0).strip(' ').replace('"', '”')
      if len(f_name) == 0 :
         self.message('Please enter a first name')
         return
      l_name = self.l_name_box.GetLineText(0).strip(' ').replace('"', '”')
      tel = self.tel_box.GetLineText(0).strip(' ')
      mail = self.mail_box.GetLineText(0).strip(' ').replace('"', '”')
      #Be carefull of the replacement of quote characters if you decide to automate mails.

      if len(mail) == 0 and len(tel) == 0 :
         self.message('Please enter some contact information')
         return
      
      if len(tel) not in {0, 10} or not tel.isnumeric() :
         self.message('Please enter a valid phone number')
      
      added = add_user(f_name, l_name, tel, mail, self.loan_spin.GetValue())
      if added :
         self.message(f"User {f_name} {l_name} added to database")
         self.Parent.update_users()
      else :
         self.message(f"User {f_name} {l_name} already exists")

   def message(self, msg:str) :
      self.info_text.SetLabelText(msg)