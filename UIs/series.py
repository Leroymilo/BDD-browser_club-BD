import wx

from gen_UIs.series_GUI import Window

from functions.adders import *
from functions.modifiers import *
from functions.getters import *

from UIs.authors import Author_UI

class Series_UI(Window) :
    def __init__(self, parent) :
        Window.__init__(self, parent)
        self.auth_BoxSizer = self.GetSizer().GetChildren()[3].GetSizer()
        self.auth_choices = []
        self.auths = []
        self.first_auth_choice.Append(' ')
        self.update_authors()
        self.update_categories()

    def update_authors(self) :
        auths = get_auths_select()
        new_auths = list(set(auths).difference(set(self.auths)))
        self.auths = auths
        self.first_auth_choice.Append(new_auths)
        for choice in self.auth_choices :
            choice.Append(new_auths)
        
    def change_authors(self, event):
        if self.first_auth_choice.GetSelection() != 0 and len(self.auth_choices) < 5 :
            new_auth_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.first_auth_choice.GetStrings(), wx.CB_SORT)
            new_auth_choice.SetMaxSize(wx.Size(120, -1)) 
            self.auth_BoxSizer.Insert(1+len(self.auth_choices), new_auth_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
            self.Layout()

            new_auth_choice.SetStringSelection(self.first_auth_choice.GetStringSelection())
            new_auth_choice.Bind( wx.EVT_CHOICE, self.change_authors )
            self.first_auth_choice.SetSelection(0)
            self.auth_choices.append(new_auth_choice)

        i = 0
        while i < len(self.auth_choices) :
            if self.auth_choices[i].GetSelection() == 0 :
                self.auth_choices.pop(i)
                self.auth_BoxSizer.GetChildren()[i+1].GetWindow().Destroy()
                continue
            i += 1

        if len(self.auth_choices) >= 5 :
            self.first_auth_choice.Hide()
        else :
            self.first_auth_choice.Show()
        
        self.Layout()
   
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

        auth_names = [choice.GetStringSelection() for choice in self.auth_choices]
        
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
        self.id_box.SetValue(item_id)
        self.add_button.SetLabel("Apply Edit")
        self.SetTitle("Modifying series in database")

        self.old_item = get_series(["ID", item_id])[0]

        self.full_name_box.SetValue(self.old_item[1])

        authors = self.old_item[2].split(", ")
        for auth_nb in range(len(authors)) :
            self.first_auth_choice.SetStringSelection(authors[auth_nb])
            self.change_authors(None)
        
        self.cat_choice.SetStringSelection(self.old_item[3])
        self.kind_choice.SetStringSelection(self.old_item[4])
    
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

        auth_names = [choice.GetStringSelection() for choice in self.auth_choices]
        

        self.message("")
        auth_ids = [self.auths[name] for name in auth_names if name != '']
        kind = self.kind_choice.GetStringSelection()
        cat= self.cats[self.cat_choice.GetStringSelection()]

        if s_id != self.old_item[0] or cat != self.old_item[3] :
            conf = wx.MessageDialog(self, "", "", wx.CANCEL | wx.OK)
            conf.SetExtendedMessage("""Warning : changing id or category will change the reference of all books from these series.
Old books references will be remembered if they are changed.""")
            conf.SetYesNoLabels("Continue", "Cancel")
            if conf.ShowModal() == 5101 :
                return

        modified = modif_series(self.old_item[0], s_id, name, cat, kind, auth_ids)
        if modified == 0 :
            db.commit()
            self.message(f"Series '{s_id}' edited in database")
            self.Parent.update_series()
        elif modified == 1 :
            self.message("Series new id already used")
        elif modified == 2 :
            self.message("Series new name already used")
        else :
            self.message("Unknown error")
