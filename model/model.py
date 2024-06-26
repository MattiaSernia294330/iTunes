import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._dizionarionodi={}
        self._bestSol=[]
        self._distanzaBest=0
        pass
    def creaGrafo(self,durata):
        self._grafo.clear()
        self._dizionarionodi={}
        for element in DAO.getNodi(durata):
            self._grafo.add_node(element)
            self._dizionarionodi[element.AlbumId]=element
        for nodo1 in self._grafo.nodes:
            for nodo2 in self._grafo.nodes:
                if nodo1!=nodo2 and DAO.getArchi(nodo1.AlbumId,nodo2.AlbumId)>0:
                    self._grafo.add_edge(nodo1,nodo2)
    def getNodes(self):
        return self._grafo.nodes()
    def getArchi(self):
        return len(self._grafo.edges())
    def connessa(self,id):
        numero=len(nx.node_connected_component(self._grafo, self._dizionarionodi[id]))
        somma=0
        for element in nx.node_connected_component(self._grafo, self._dizionarionodi[id]):
            somma+=element.durata
        print(numero)
        print(somma)
    def _ricorsione(self,nodo,parziale,pesomax,numeronodi):
        successori=list(self._grafo.neighbors(nodo))
        for element in successori.copy():
            if element in parziale or element.durata>=pesomax:
                successori.remove(element)
        if len(successori)==0:
            if numeronodi>self._distanzaBest:
                self._bestSol=parziale
                self._distanzaBest=numeronodi
                print(self._distanzaBest)
            return
        else:
            for item in successori:
                nuovo_nodo = item
                parziale_nuovo = list(parziale)
                parziale_nuovo.append(nuovo_nodo)
                numeronodi_nuovo=numeronodi+1
                nuovopesomax=pesomax-float(item.durata)
                self._ricorsione(nuovo_nodo,parziale_nuovo,nuovopesomax,numeronodi_nuovo)
    def handleRicorsione(self,nodo,pesomax):
        self._bestSol=[]
        self._distanzaBest=0
        self._ricorsione(self._dizionarionodi[nodo],[self._dizionarionodi[nodo]],pesomax,0)
        print(self._distanzaBest)
