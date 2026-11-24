import flet as ft


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
        codinsSelezionato = self._view._ddCorso.value #QUESTO MI RESTITUISCE UN codins PER LA RIGA 14 (key=corso.codins)


    def cercaStudente(self, e):
        pass

    def cercaCorsi(self, e):
        pass

    def iscrivi(self, e):
        pass