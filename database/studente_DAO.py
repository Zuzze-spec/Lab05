# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class Studente_DAO:
    def __init__(self):
        self._dictStudenti = dict()
        self.ottieniStudenti() #SE NON CHIAMO IL METODO NON RIEMPIO EFFETTIVAMENTE IL DIZIONARIO

    def ottieniStudentiCorso(self, codinsCorso):
        cnx= get_connection() #CONNESSIONE AL DATABASE (SEMPRE UGUALE)
        cursor = cnx.cursor(dictionary=True) #SERVE PER LEGGERE DAL DB E LE SALVA OGNI RIGA COME dictionary
        query = ("select s.* from studente s, iscrizione i "
                 "where s.matricola = i.matricola and i.codins = %s") #%s E' VARIABILE A SECONDA DEL codinsCorso
        cursor.execute(query, (codinsCorso,)) #PER REGOLE SINTATTICHE CI VUOLE LA , ALLA FINE

        listStudenti = []
        for row in cursor:
            listStudenti.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        return listStudenti

    def ottieniStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM studente"
        cursor.execute(query)
        for row in cursor:
            matricola = row["matricola"]
            s = Studente(matricola, row["cognome"], row["nome"], row["CDS"])
            self._dictStudenti[matricola] = s

    def ottieniStudenteMatricola(self, matricola):
        matricola = int(matricola)
        if matricola in self._dictStudenti.keys():
            return self._dictStudenti[matricola]
        return None

    def iscriviStudente(self, matricola, codins):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = ("INSERT INTO iscrizione (matricola, codins) "
                 "VALUES (%s, %s)")
        cursor.execute(query, (matricola, codins,))
        cnx.commit()

    @property
    def dictStudenti(self):
        return self._dictStudenti

if __name__ == "__main__":
    s = Studente_DAO()
    s.iscriviStudente(190634, "02PBVPG")
