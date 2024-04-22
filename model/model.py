from database import corso_DAO
from database import studente_DAO

class Model:
    def __init__(self):
        self.mappaCorsi = None
        self.mappaStudenti = None

    def getCorsi(self):
        if self.mappaCorsi is None:
            self.mappaCorsi = dict()
            corso_DAO.leggiCorsiDalDB(self.mappaCorsi)
        return self.mappaCorsi

    def getIscrittiCorso(self, codins):
        if self.mappaCorsi[codins].studenti is None:
            self.mappaCorsi[codins].studenti = corso_DAO.getIscritti(codins)
        return self.mappaCorsi[codins].studenti

    def getCorsiStudenteByMatricola(self, matricola):
        corsi = studente_DAO.getCorsi(matricola)
        return corsi

    def getStudenteByMatricola(self, matricola):
        if self.mappaStudenti is None:
            self.mappaStudenti = dict()
            self.mappaStudenti = studente_DAO.leggiStudentiDalDB(self.mappaStudenti)
        return self.mappaStudenti.get(matricola)

    def iscriviCorso(self, matricola, codins):
        self.getIscrittiCorso(codins)
        for studente in self.mappaCorsi[codins].studenti:
            if studente.matricola == matricola:
                return False
        else:
            return corso_DAO.iscriviCorso(matricola, codins)

