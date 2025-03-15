class Cliente:
    def __init__(self, endereco, telefone, email, genero):
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        self._genero = genero
 
    def contato(self):
        return f"Telefone: {self._telefone}\nEmail: {self._email}"
    
