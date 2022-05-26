from gen_UIs.series_GUI import Window

from functions.adders import *
from functions.modifiers import *
from functions.getters import *

from UIs.authors import Author_UI

class Series_UI(Window) :
    def __init__(self, parent) :
        Window.__init__(self, parent)
        self.auth_choices = []
        self.update_authors()
        self.update_categories()

    def update_authors(self) :
        self.auths = get_auths_select()
        selected_auths = [auth_choice.GetStringSelection() for auth_choice in self.auth_choices]
        self.first_auth_choice.SetStr
        for i in range(len(self.auth_choices)) :
            choice = self.auth_choices[i]
            choice.Clear()
            choice.Append(' ')
            choice.AppendItems(list(self.auths))
            choice.SetStringSelection(selected_auths[i])
        
    def change_authors(self, event):
        if self.first_auth_choice.GetSelection() != 0 :
            pass

        i = 0
        while i < len(self.auth_choices) :
            if self.auth_choices[i].getStringSelection() == ' ' :
                self.auth_choices.pop(i)
                continue
            i += 1
        return
   
    def update_categories(self) :
        self.cats = get_cats_select()
        self.cat_choice.Clear()
        self.cat_choice.Append(' ')
        self.cat_choice.AppendItems(list(self.cats))
        self.cat_choice.SetSelection(0)

    def add(self, event) :
        name = self.full_name_box.GetLineText(0).strip(' ').replace('"', '”')
        if len(name) == 0 :
            self.message("Please enter a name")
            return
        elif len(name) > 64 :
            self.message("Name is too long")
            return
        
        s_id = self.id_box.GetLineText(0)
        if len(s_id) != 3 :
            self.message("Id must be 3 characters")
            return
        elif not s_id.isupper() or not s_id.isalpha() :
            self.message("Id must be made of uppercase letters")
            return

        auth_names = [choice.GetStringSelection() for choice in self.auth_choices if choice.GetSelection() > 0]
        
        self.message("")
        auth_ids = [self.auths[name] for name in auth_names if name != '']
        kind = self.kind_choice.GetStringSelection()
        cat= self.cats[self.cat_choice.GetStringSelection()]
        added = add_series(s_id, name, cat, kind, auth_ids)
        if added :
            db.commit()
            self.message(f"Series '{s_id}' added to database")
            self.Parent.update_series()
        else :
            self.message("Series ID or full name already used")

    def add_author(self, event) :
        sub_frame = Author_UI(self)
        sub_frame.Show(True)

    def message(self, msg:str) :
        self.info_text.SetLabelText(msg)

class Series_modif(Series_UI) :
    def __init__(self, parent, item_id):
        super().__init__(parent)
        self.id_box.SetEditable(False)
        self.id_box.SetLabel(item_id)
        self.add_button.SetLabel("Apply Edit")

        item = get_series(["ID", item_id])[0]

        self.old_name = item[1]
        self.full_name_box.SetLabel(item[1])

        authors = item[2].split(", ")
        for auth_nb in range(len(authors)) :
            self.auth_choices[auth_nb].SetStringSelection(authors[auth_nb])
        
        self.cat_choice.SetStringSelection(item[3])
        self.kind_choice.SetStringSelection(item[4])
    
    def add(self, event) :
        name = self.full_name_box.GetLineText(0).strip(' ').replace('"', '”')
        if len(name) == 0 :
            self.message("Please enter a name")
            return
        elif len(name) > 64 :
            self.message("Name is too long")
            return
        
        s_id = self.id_box.GetLineText(0)
        if len(s_id) != 3 :
            self.message("Id must be 3 characters")
            return
        elif not s_id.isupper() or not s_id.isalpha() :
            self.message("Id must be made of uppercase letters")
            return

        auth_names = [choice.GetStringSelection() for choice in self.auth_choices if choice.GetSelection() > 0]
        
        self.message("")
        auth_ids = [self.auths[name] for name in auth_names if name != '']
        kind = self.kind_choice.GetStringSelection()
        cat= self.cats[self.cat_choice.GetStringSelection()]
        modified = modif_series(s_id, self.old_name, name, cat, kind, auth_ids)
        if modified :
            db.commit()
            self.message(f"Series '{s_id}' edited in database")
            self.Parent.update_series()
        else :
            self.message("Series full name already used")
