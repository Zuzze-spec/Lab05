import flet as ft

from model.studente import Studente


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def riempiDD(self):
        listCorsiOption = []
        for corso in self._model.getListCorsiDAO():
            corsoOption = ft.dropdown.Option(key=corso.codins, text=corso.__str__())
            listCorsiOption.append(corsoOption)
        return listCorsiOption


    def cercaIscritti(self, e):
        self._view._lv.clean()
        codinsSelezionato = self._view._ddCorso.value #QUESTO MI RESTITUISCE UN codins PER LA RIGA 14 (key=corso.codins)
        if not codinsSelezionato: #COMPRENDE I CASI CHE IL codinsSelezionato sia None (inizialmente) O '' LE VOLTE SUCCESSIVE
            self._view.create_alert("Corso non selezionato!")
            messaggioErrore = ft.Text(value="Corso non selezionato!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return #SERVE PER TERMINARE LA FUNZIONE IN CASO IL CODICE CHE NE SEGUE VADA ESEGUITO RISPETTANDO LA CONDIZIONE SOPRASTANTE
        listStudenti = self._model.getListStudentiCorso(codinsSelezionato)
        qtaStudenti = len(listStudenti)
        textLv = ft.Text(value=f"Ci sono {qtaStudenti} iscritti al corso:")
        self._view._lv.controls.append(textLv)
        for s in listStudenti:
            textLv = ft.Text(value=s)
            self._view._lv.controls.append(textLv)
        self._view.update_page()

    def cercaStudente(self, e):
        self._view._lv.clean()
        matricola = self._view._matricola.value
        if not matricola:
            self._view.create_alert("Matricola non inserita!")
            messaggioErrore = ft.Text(value="Matricola non inserita!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        try:
            int(matricola)
        except ValueError:
            self._view.create_alert("Matricola non valida!")
            messaggioErrore = ft.Text(value="Matricola non valida!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        studente = self._model.getStudenteMatricola(matricola)
        if studente is None:
            self._view.create_alert("Studente non trovato!")
            messaggioErrore = ft.Text(value="Studente non trovato!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        self._view._cognome.value = studente.cognome
        self._view._nome.value = studente.nome
        self._view.update_page()

    def cercaCorsi(self, e):
        self._view._lv.clean()
        matricola = self._view._matricola.value
        if not matricola:
            self._view.create_alert("Matricola non inserita!")
            messaggioErrore = ft.Text(value="Matricola non inserita!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        try:
            int(matricola)
        except ValueError: #SE SI VERIFICA QUESTO ERRORE FAI CIO' CHE SEGUE
            self._view.create_alert("Matricola non valida!")
            messaggioErrore = ft.Text(value="Matricola non valida!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        if not self._model.getStudenteMatricola(matricola):
            self._view.create_alert("Studente non trovato!")
            messaggioErrore = ft.Text(value="Studente non trovato!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        listCorsi = self._model.getCorsiMatricola(matricola)
        qtaCorsi = len(listCorsi)
        textLv = ft.Text(f"Risultano {qtaCorsi} corsi:")
        self._view._lv.controls.append(textLv)
        for c in listCorsi:
            textLv = ft.Text(c)
            self._view._lv.controls.append(textLv)
        self._view.update_page()

    def iscrivi(self, e):
        self._view._lv.clean()
        #1^CHECK: CORSO SELEZIONATO DAL DD
        codins = self._view._ddCorso.value
        if not codins:
            self._view.create_alert("Corso non selezionato!")
            messaggioErrore = ft.Text(value="Corso non selezionato!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        #2^CHECK: MATRICOLA INSERITA
        matricola = self._view._matricola.value
        if not matricola:
            self._view.create_alert("Matricola non inserita!")
            messaggioErrore = ft.Text(value="Matricola non inserita!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        #3^CHECK: MATRICOLA INTERA
        try:
            int(matricola)
        except ValueError: #SE SI VERIFICA QUESTO ERRORE FAI CIO' CHE SEGUE
            self._view.create_alert("Matricola non valida!")
            messaggioErrore = ft.Text(value="Matricola non valida!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        #4^CHECK: MATRICOLA ESISTENTE
        if not self._model.getStudenteMatricola(matricola):
            self._view.create_alert("Studente non trovato!")
            messaggioErrore = ft.Text(value="Studente non trovato!", color="red")
            self._view._lv.controls.append(messaggioErrore)
            self._view.update_page()
            return
        #5^CHECK: CORSO NON GIA' FREQUENTATO DALLO STUDENTE
        for c in self._model.getCorsiMatricola(matricola):
            if c.codins == codins:
                self._view.create_alert("Studente già iscritto!")
                messaggioErrore = ft.Text(value="Studente già iscritto!", color="red")
                self._view._lv.controls.append(messaggioErrore)
                self._view.update_page()
                return
        self._model.putStudente(matricola, codins)
        esito = ft.Text(value="Studente iscritto correttamente!", color="blue")
        self._view._lv.controls.append(esito)
        self._view.update_page()