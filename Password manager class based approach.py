#Password manager class based approach EXAMPLE
import tkinter as tk

CONNECT_APP_DIMENSIONS=("400", "200")
PASSWORD_APP_DIMENSIONS=("800", "500")


USERNAME_PASSWORD_IN_DB=[
    ['banane_user', 'banane_password'],
    ['kiwi_user', 'kiwi_password'],
    ['patate_user', 'patate_password'],
]

class PasswordApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_geometry(PASSWORD_APP_DIMENSIONS[0]+"x"+PASSWORD_APP_DIMENSIONS[1])

        # ---- ADDING GESTION ----

        # username entry
        self.username_entry=tk.Entry(self, width=20)
        self.username_entry.focus_set()
        self.username_entry.insert(tk.END, "new_username")
        self.username_entry.grid(row=0,column=0)
        # password entry
        self.password_entry=tk.Entry(self, width=20)
        self.password_entry.focus_set()
        self.password_entry.insert(tk.END, "new_password")
        self.password_entry.grid(row=0,column=1)
        # add username/password button
        self.add_button = tk.Button(self, text="add", command=self.add_account)
        self.add_button.grid(row=0,column=2)
        # status label
        self.status_text=tk.StringVar(self)
        self.status = tk.Label(self, textvariable=self.status_text)
        self.status.grid(row=0,column=3)

        # ---- END ADDING GESTION ----

        # intiliaze some list
        self.display_buttons=[]
        self.password_status_texts=[]
        self.password_labels=[]

        # make a copy of DB
        self.database = USERNAME_PASSWORD_IN_DB.copy()

        # display username/password list
        self.refresh_list()

    def refresh_list(self):
        cpt_row = 1
        simple_cpt = 0

        for username_password in self.database:
            # new password was added
            if simple_cpt < len(self.display_buttons):
                cpt_row += 1
                simple_cpt += 1
                continue
            # display password button
            self.display_buttons.append(
                tk.Button(
                    self,
                    text=username_password[0], 
                    command= lambda simple_cpt=simple_cpt: self.display_password(db_id=simple_cpt)
                )
            )
            self.display_buttons[simple_cpt].grid(row=cpt_row,column=0)
            # status label
            self.password_status_texts.append(tk.StringVar(self, '******'))
            self.password_labels.append(tk.Label(self, textvariable=self.password_status_texts[simple_cpt]))
            self.password_labels[simple_cpt].grid(row=cpt_row,column=1)

            cpt_row += 1
            simple_cpt += 1

    def display_password(self, db_id):
        # updating label associated to username
        self.password_status_texts[db_id].set(self.database[db_id][1])

    def add_account(self):
        # getting user inputs
        username=self.username_entry.get()
        password=self.password_entry.get()
        # check minimum size
        if len(username) < 4 or len(password) < 4:
            self.status_text.set("Incorrect username/password")
            return
        # check username not already in self.database
        for username_password in self.database:
            if username_password[0] == username:
                self.status_text.set("Username already in DB")
                return
        # adding username/password to DB
        self.database.append([username, password])
        # refreshing list
        self.refresh_list()

class ConnectionApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_geometry(CONNECT_APP_DIMENSIONS[0]+"x"+CONNECT_APP_DIMENSIONS[1])

        # username entry
        self.entry=tk.Entry(self, width=20)
        self.entry.focus_set()
        self.entry.insert(tk.END, "username")
        self.entry.grid(row=0,column=0)

        # connect button
        self.connect_button = tk.Button(text="connect", command=self.connect)
        self.connect_button.grid(row=0,column=1)

        # status label
        self.status_text=tk.StringVar()
        self.status = tk.Label(textvariable=self.status_text)
        self.status.grid(row=0,column=2)

    def connect(self):
        if self.entry.get() == "steve":
            self.status_text.set("Connected")
            self.password_app=PasswordApp()
            self.destroy()
        else:
            self.status_text.set("Unknown user")


if __name__ == '__main__':
    connect_app=ConnectionApp()
    connect_app.mainloop()