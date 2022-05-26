from gen_UIs.author_GUI import Window

from functions.adders import *

class Author_UI(Window) :
    def __init__(self, parent) :
        Window.__init__(self, parent)
   
    def add(self, event) :
        text = self.name_box.GetLineText(0).strip(' ').replace('"', '”')
        if len(text) == 0 :
            self.message("Please enter a name")
            return
        elif len(text) > 64 :
            self.message("Name is too long")
            return
        if ", " in text :
            self.message("Name cannot contain the string \", \"")
            return
      
        self.message("")
        added = add_author(text)
        if added :
            self.message(f"Author '{text}' added to database")
            self.Parent.update_authors()
        else :
            self.message("Author already exists")
   
    def message(self, msg) :
        self.info_text.SetLabelText(msg)