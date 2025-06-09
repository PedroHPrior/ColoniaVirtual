# src/models/comentario.py

from datetime import datetime

class Comentario:
    def __init__(self, texto: str, autor: str, data: datetime = None):
        self.texto = texto
        self.autor = autor
        self.data = data if data else datetime.now()

    def get_texto(self) -> str:
        return self.texto

    def get_autor(self) -> str:
        return self.autor

    def get_data(self) -> datetime:
        return self.data

    def __str__(self):
        return f"Comentario(autor='{self.autor}', texto='{self.texto}', data={self.data.strftime('%Y-%m-%d')})"