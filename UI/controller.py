import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._durata=None
        self._album=None
        self._Max=None
    def handle_durata(self,e):
        self._durata=e.control.value
    def handleCreaGrafo(self, e):
        if not self._durata:
            self._view.create_alert("inserisci la durata")
            return
        self._model.creaGrafo(float(self._durata))
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {len(self._model.getNodes())} Numero di archi: {self._model.getArchi()}"))

        for element in self._model.getNodes():
            self._view._ddAlbum.options.append(ft.dropdown.Option(text=f"{element.Title}", key=f"{element.AlbumId}", on_click=self.handle_album))
        self._view.update_page()
        pass
    def handle_album(self,e):
        self._album=int(e.control.key)
    def getSelectedAlbum(self, e):
        pass

    def handleAnalisiComp(self, e):
        return self._model.connessa(self._album)
        pass
    def handleMax(self,e):
        self._Max = e.control.value
    def handleGetSetAlbum(self, e):
        self._model.handleRicorsione(self._album,float(self._Max))
        pass