from categoria import Categoria
from produto import Produto

def main():
    c1 = Categoria("informatica", "Produtos de informatica")
    c2 = Categoria("Alimentos", "Alimentos em geral")
    p1 = Produto("Iphone", "Telefone rico", "10/10/2025", True, c2)
    print(p1._nome)
    
if __name__ == "__main__": 
    main()