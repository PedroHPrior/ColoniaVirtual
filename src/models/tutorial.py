# src/models/tutorial.py

from datetime import datetime

class Tutorial:
    def __init__(self, titulo: str, conteudo: str, autor: str):
        self.titulo = titulo
        self.conteudo = conteudo
        self.autor = autor
        self.tags = [] # Lista de strings
        self.data_publicacao = None # datetime

    def adicionar_tag(self, tag: str):
        self.tags.append(tag)
        print(f"Tag '{tag}' adicionada ao tutorial '{self.titulo}'.")

    def remover_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
            print(f"Tag '{tag}' removida do tutorial '{self.titulo}'.")
        else:
            print(f"Tag '{tag}' não encontrada no tutorial '{self.titulo}'.")

    def marcar_como_concluido(self):
        print(f"Tutorial '{self.titulo}' marcado como concluído.")
        # Lógica para registrar a conclusão do tutorial

    def __str__(self):
        return f"Tutorial(titulo='{self.titulo}', autor='{self.autor}')"