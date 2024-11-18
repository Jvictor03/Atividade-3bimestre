class Supermercado:
    def __init__(self, numero_produtos: int):
        self.numero_produtos = numero_produtos

    def get_numero_produtos(self) -> int:
        return self.numero_produtos

    def set_numero_produtos(self, numero_produtos: int) -> None:
        self.numero_produtos = numero_produtos

    def calcular_total(self) -> None:
        total = 0.0
        for i in range(self.numero_produtos):
            valor_produto = float(input(f"Digite o valor do produto {i + 1}: "))
            total += valor_produto
        print(f"O valor total das compras no supermercado é: {total:.2f}")


class TestarSupermercado:
    @staticmethod
    def main():
        num_produtos = int(input("Digite o número de produtos: "))
        
        
        supermercado = Supermercado(num_produtos)

        
        supermercado.calcular_total()

       
        novo_num_produtos = int(input("Digite um novo número de produtos: "))
        supermercado.set_numero_produtos(novo_num_produtos)

       
        supermercado.calcular_total()



if __name__ == "__main__":
    TestarSupermercado.main()
