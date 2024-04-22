import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dropdownCorsi = None
        self.btnCercaIscritti = None
        self.txtMatricola = None
        self.txtCognome = None
        self.txtNome = None
        self.btnCercaCorsiStudente = None
        self.btnCercaStudente = None
        self.btnIscriviStudente = None
        self.txt_name = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        ###
        # ROW 1
        ###
        # DROPDOWN MENU
        self.dropdownCorsi = ft.Dropdown(label="Corso", width=490, hint_text="Seleziona un corso",
                                         options=[], #inizializza l'elenco
                                         on_change=self._controller.leggi_corso ) #chiama il metodo quando viene cambiata selezione nel dropdown
        self._controller.popolaDropdown()
        # btn cerca iscritti del corso scelto nel menu
        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti", width=130, on_click=self._controller.getIscritti,
                                                  tooltip="Cerca gli iscritti del corso selezionato") # verrà visualizzato quando l'utente passa il mouse sopra il pulsante.
        # SCRIVO LA ROW
        row1 = ft.Row([self.dropdownCorsi, self.btnCercaIscritti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        ###
        # ROW 2
        ###
        #caselle
        self.txtMatricola = ft.TextField(label="Matricola", width=200, hint_text="Inserire matricola")
        self.txtNome = ft.TextField(label="Nome", width=200, read_only=True)
        self.txtCognome = ft.TextField(label="Cognome", width=200, read_only=True)
        # scrivo la row2
        row2= ft.Row([self.txtMatricola, self.txtNome, self.txtCognome],
                     alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        ###
        # ROW 3
        ###
        #bottoni
        self.btnCercaStudente =ft.ElevatedButton(text="Cerca studente", on_click=self._controller.getStudenteByMatricola)
        self.btnCercaCorsiStudente = ft.ElevatedButton(text="Cerca corsi che frequenta lo studente", on_click=self._controller.getCorsiStudenteByMatricola)
        self.btnIscriviStudente = ft.ElevatedButton(text="Iscrivi studente al corso", on_click=self._controller.iscriviStudente)
        #SCRIVO LA ROW 3
        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsiStudente, self.btnIscriviStudente], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
