class Categoria:
    def __init__(self, nome, descricao):
        self._nome = nome

    def __str__(self):
        return f"{self._nome}: {self._descricao}"