  # Import da biblioteca MatPlotLib
import matplotlib.pyplot as plt

# Criando a Classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, qtd):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qtd = qtd

# Definindo os métodos (funções)

# Função cadastrar livro
def cadastrar_livro():
    nome = input("Digite o titulo do livro: ")
    escritor = input("Digite o nome do autor: ")
    categoria = input("Digite o genero do livro: ")
    acervo = int(input("Digite a quantidade de livros disponíveis: "))
    return Livro(nome, escritor, categoria, acervo)

# Função livros na prateleira
def listar_livro(lista):
    print("Livros na prateleira: ")
    if not lista: # Se não lista = Prateleira vazia
        print("A prateleira está vazia!")
    else: # Senão = mostrar livro, autor, gênero e estoque
        for i in lista: # For para percorrer item a item dentro da lista (laço)
            print(f"Livro: {i.titulo} | Autor: {i.autor} | Gênero: {i.genero} | Estoque: {i.qtd}")

# Função buscar livro específico na prateleira
def buscar_livro(lista):
    if not lista:
        return
    
    busca = input("\nDigite o nome do livro deseja procurar: ")
    encontrado = False
    
    for i in lista:
        if busca.lower() == i.titulo.lower():
            print(f"Título: {i.titulo}")
            print(f"Autor: {i.autor}")
            print(f"Gênero: {i.genero}")
            print(f"Estoque: {i.qtd}")
            encontrado = True
            break

    if not encontrado:
        print("Sinto muito, não temos este livro em nosso estoque! ")

# Função de criar o gráfico
def gerar_grafico(lista):
    contagem = {} # Dicionário para agrupar e somar livros por gênero
    
    for i in lista:
        if i.genero in contagem:
            contagem[i.genero] += i.qtd # Contador somando se houver gêneros iguais
        else:
            contagem[i.genero] = i.qtd # Se gênero novo, mostrar valor inicial na tabela
        
    generos = list(contagem.keys()) # Transforma o nome dos gêneros em uma lista para o eixo horizontal (x)
    quantidades = list(contagem.values()) # Transforma a soma da quantidade em uma lista para o eixo vertical (y)

    plt.bar(generos, quantidades, color='tab:blue') # Eixo X e Y na cor Tableau azul
    plt.title('Quantidade de livros por gênero') # Título da tabela
    plt.xlabel('Gêneros') # Eixo X
    plt.ylabel('Total em estoque') # Eixo Y

    plt.show()

# Inicializando lista
biblioteca = []

# Looping de cadastro dos livros
while input("Cadastrar novo livro? (s/n): ").lower() == 's':
    livro_item = cadastrar_livro()
    biblioteca.append(livro_item)
    print(f"Livro {livro_item.titulo} foi cadastrado com sucesso!")

# Livros em estoque
if input("Deseja ver os livros que estão em estoque? (s/n): ").lower() == 's':
    listar_livro(biblioteca)

# Buscador de livros
if input("Deseja buscar um livro específico? (s/n): ").lower() == 's':
    buscar_livro(biblioteca)

# Gráfico por gênero
if input("Deseja visualizar a quantidade de livros por gênero (gráfico)? (s/n): ").lower() == 's':
    gerar_grafico(biblioteca)
