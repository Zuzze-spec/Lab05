from database.corso_DAO import Corso_DAO


class Model:
    def __init__(self):
        self._corsoDAO = Corso_DAO()

    def getListCorsiDAO(self):
        return self._corsoDAO.listCorsi
