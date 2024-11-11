from jogovelha import JogoVelha, JogadorHumano, JogadorComputador

player = JogadorHumano(input("* Digite seu nome de jogador: "))
player.simbolo = "X"

robo = JogadorComputador("CPU", "aleatoria")
robo.simbolo = "O"

jogo = JogoVelha(player, robo)
jogo.jogar()