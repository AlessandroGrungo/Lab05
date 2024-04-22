import flet as ft
from UI.view import View
from model.studente import Studente


class Controller:
    def __init__(self, view: View, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # codice del corso selezionato
        self.codins_selezionato = None
    def leggi_corso(self, e): #prende il corso selezionato nel dropdpwn e lo eguaglia al codins selezionato
        self.codins_selezionato = self._view.dropdownCorsi.value # serve .value per prendere il codins cioè la chiave e non l'intero menù options

    def popolaDropdown(self):
        for codin, corso in self._model.getCorsi().items():
            self._view.dropdownCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()

    def getIscritti(self, e):
        if self.codins_selezionato is None:
            self._view.create_alert("Seleziona un corso!")
            return
        iscritti = self._model.getIscrittiCorso(self.codins_selezionato)
        if iscritti is None:
            self._view.create_alert("Errore nella connesione al DB")
            return
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso selezionato."))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} al corso selezionato."))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(studente))
            self._view.update_page()


    def getCorsiStudenteByMatricola(self, e):
        matricola = self._view.txtMatricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return
        else:
            corsi = self._model.getCorsiStudenteByMatricola(int(matricola))
            if corsi is None:
                self._view.create_alert("Non risulta nessun studente con questa matricola!")
            elif len(corsi)==0:
                self._view.create_alert("La matricola non risulta iscritta a nessun corso!")
            else:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi: "))
                for corso in corsi:
                    self._view.txt_result.controls.append(ft.Text(corso))
                self._view.update_page()

        return
    def getStudenteByMatricola(self,e):
        matricola = self._view.txtMatricola.value
        if matricola=="" or matricola is None:
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.getStudenteByMatricola(int(matricola))
        if studente is None:
            self._view.create_alert("Studente non presente nel DB.")
        else:
            self._view.txtNome.value = studente.nome
            self._view.txtCognome.value = studente.cognome
        self._view.update_page()


    def iscriviStudente(self, e):
        matricola = self._view.txtMatricola.value
        if matricola == "" or matricola is None:
            self._view.create_alert("inserire una matricola")
            return
        studente = self._model.getStudenteByMatricola(int(matricola))
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        if self.codins_selezionato is None:
            self._view.create_alert("Selezionare un corso!")
            return
        result = self._model.iscriviCorso(int(matricola), self.codins_selezionato) # booleano
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita, verifica che lo studente non sia già iscritto al corso, altrimenti riprova."))
        self._view.update_page()