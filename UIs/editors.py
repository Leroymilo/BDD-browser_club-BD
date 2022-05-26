from gen_UIs.editor_GUI import Window

from functions.adders import *

class Editor_UI(Window) :
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
      
        self.message("")
        added = add_editor(text)
        if added :
            db.commit()
            self.message(f"Editor '{text}' added to database")
            self.Parent.update_editors()
        else :
            self.message("Editor already exists")
   
    def message(self, msg) :
        self.info_text.SetLabelText(msg)