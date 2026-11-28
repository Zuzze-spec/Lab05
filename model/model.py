from database.corso_DAO import Corso_DAO
from database.studente_DAO import Studente_DAO


class Model:
    def __init__(self):
        self._corsoDAO = Corso_DAO()
        self._studenteDAO = Studente_DAO()

    def getListCorsiDAO(self):
        return self._corsoDAO.listCorsi

    def getListStudentiCorso(self, corso):
        return self._studenteDAO.ottieniStudentiCorso(corso)

    def getStudenteMatricola(self, matricola):
        return self._studenteDAO.ottieniStudenteMatricola(matricola)

    def getCorsiMatricola(self, matricola):
        return self._corsoDAO.ottieniCorsiMatricola2(matricola)

    def putStudente(self, matricola, codins):
        return self._studenteDAO.iscriviStudente(matricola, codins)
