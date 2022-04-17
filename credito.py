class Credito:
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto
        self.estado = "Solicitado"

    def procesar(self):
        self.estado = "En revisión"

    def aceptar(self):
        self.estado = "Autorizado"

    def rechazar(self):
        self.estado = "Cancelado"

    def depositar(self):
        self.estado = "Entregado"
    
    def recibirPago(self):
        self.estado = "Pagado"

    def getEstado(self):
        return self.estado
