# Jogo da Velha

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/license/mit)

Um simples jogo da velha em python.

## Uso:

Exemplo de Uso:

    from jogovelha import JogoVelha, JogadorHumano, JogadorComputador

    player = JogadorHumano("Nome do jogador")
    player.simbolo = "X"

    cpu = JogadorComputador("Nome da CPU", "aleatoria")
    cpu.simbolo = "O"

    jogo = JogoVelha(player, cpu)
    jogo.jogar()