# src/models/avaliacao.py

from datetime import datetime

class Avaliacao:
    def __init__(self, nota: int, comentario: str, data: datetime = None):
        self.nota = nota
        self.comentario = comentario
        self.data = data if data else datetime.now()

    def get_nota(self) -> int:
        return self.nota

    def get_comentario(self) -> str:
        return self.comentario

    def get_data(self) -> datetime:
        return self.data

    def __str__(self):
        return f"Avaliacao(nota={self.nota}, comentario='{self.comentario}', data={self.data.strftime('%Y-%m-%d')})"