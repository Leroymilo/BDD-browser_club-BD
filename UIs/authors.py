from gen_UIs.author_GUI import Window

from functions.adders import *
from functions.modifiers import *

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

class Author_modif(Author_UI) :
    def __init__(self, parent, item_id) :
        super().__init__(parent)
        self.item_id = item_id
        cursor.execute(f"SELECT full_name FROM AUTHORS WHERE id={item_id}")
        self.name, = cursor.fetchone()
        self.name_box.SetValue(self.name)
        self.add_button.SetLabel("Apply Edit")
        self.SetTitle("Modifying author in database")

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
        added = modif_author(self.item_id, text)
        if added :
            self.message(f"Author '{text}' edited in database")
            self.Parent.update_authors()
        else :
            self.message("Author already exists")