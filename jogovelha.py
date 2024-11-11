from numpy.random import randint

# [FUNÇÕES]
def pedir_num(text: str, min: int, max: int) -> int:
    num = input(text)
    try:
        num = int(float(num))
        if num < min or num > max:
            print("* Este número é invalido!")
        else:
            return num
    except:
        print("* Isto não é um número.")

    return pedir_num(text, min, max)

# [CLASSES]
class Jogador():
    simbolo: str = ""

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def fazer_jogada(Tabuleiro) -> tuple[int, int]:
        pass


class JogadorHumano(Jogador):
    def fazer_jogada(self) -> tuple[int, int]:
        print(f"* Turno de: {self.nome}!")

        linha = pedir_num("* Selecione a linha que quer jogar de 1 a 3: ", 1, 3) - 1
        coluna = pedir_num("* Selecione a coluna que quer jogar de 1 a 3: ", 1, 3) - 1

        return (linha, coluna)


class JogadorComputador(Jogador):
    estrategia: str = ""

    def __init__(self, nome: str, estrategia: str) -> None:
        super().__init__(nome)
        if estrategia.lower() == "aleatoria":
            self.estrategia = estrategia.lower()
        else:
            print("* Estratégia do computador invalída... Tornando-a aleatoria.")
            self.estrategia = "aleatoria"

    def fazer_jogada(self) -> tuple[int, int]:
        print(f"* Turno de: {self.nome}!")

        linha = randint(3)
        coluna = randint(3)
        return (linha, coluna)


class Tabuleiro():
    casas: list[str] = []

    def __init__(self) -> None:
        # Criando os valores vazios das casas
        for i in range(9):
            self.casas.append(" ")

    def pegar_tabuleiro(self) -> list[list[str]]:
        tabuleiro_lista = []

        for linha in range(3):
            tabuleiro_lista.append([])

            for coluna in range(3):
                tabuleiro_lista[linha].append(self.casas[coluna + 3 * linha])

        return tabuleiro_lista

    def marcar_casa(self, pos: tuple[int, int], valor: str) -> None:
        self.casas[pos[0] + 3 * pos[1]] = valor

    def imprimir_tabuleiro(self):
        tabuleiro_lista = self.pegar_tabuleiro()

        for linha in range(len(tabuleiro_lista)):
            linha_lista = tabuleiro_lista[linha]
            for coluna in range(len(linha_lista)):
                if coluna != len(linha_lista) - 1:
                    print(linha_lista[coluna], end=" | ")
                else:
                    print(linha_lista[coluna])

            if linha != len(tabuleiro_lista) - 1:
                print("---------")


class JogoVelha():
    jogadores: list[Jogador] = []
    tabuleiro: Tabuleiro = Tabuleiro()
    turno: int

    def __init__(self, jogador1: Jogador, jogador2: Jogador) -> None:
        self.jogadores = [jogador1, jogador2]
        self.tabuleiro = Tabuleiro()
        self.turno = 0

    def jogar(self) -> None:
        while True:
            self.turno += 1

            atual = self.jogador_atual()
            while True:
                jogada = atual.fazer_jogada()
                if self.tabuleiro.pegar_tabuleiro()[jogada[0]][jogada[1]] == " ":
                    self.tabuleiro.marcar_casa(jogada, atual.simbolo)
                    break

                if type(atual) == JogadorHumano: print("* Jogada incorreta!")

            self.tabuleiro.imprimir_tabuleiro()

            fim_de_jogo = self.checar_fim_de_jogo()
            if fim_de_jogo != None:
                print(f"* O jogo terminou. Motivo: {fim_de_jogo}")
                break

    def checar_fim_de_jogo(self) -> str | None:
        tabuleiro_lista = self.tabuleiro.pegar_tabuleiro()
        texto = f"{self.jogador_atual().nome} ganhou a partida."

        # Verificando as linhas
        for linha in tabuleiro_lista:
            if linha[0] == linha[1] == linha[2] != ' ':
                return texto

        # Verificando colunas
        for col in range(3):
            if tabuleiro_lista[0][col] == tabuleiro_lista[1][col] == tabuleiro_lista[2][col] != ' ':
                return texto

        # Verificando diagonal principal
        if tabuleiro_lista[0][0] == tabuleiro_lista[1][1] == tabuleiro_lista[2][2] != ' ':
            return texto

        # Verificando diagonal secundária
        if tabuleiro_lista[0][2] == tabuleiro_lista[1][1] == tabuleiro_lista[2][0] != ' ':
            return texto

        # Verifica se há espaços vazios ainda
        for linha in tabuleiro_lista:
            if ' ' in linha:
                return

        return 'Empate'

    def jogador_atual(self) -> Jogador:
        return self.jogadores[self.turno % 2]