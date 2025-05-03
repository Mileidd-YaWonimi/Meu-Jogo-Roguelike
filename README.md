Meu Jogo Roguelike (Nome do seu repositório - ajuste se necessário)

Este é um jogo roguelike simples criado utilizando a biblioteca Pygame Zero para Python. O jogador controla um herói com o objetivo de sobreviver em um ambiente repleto de inimigos.

## Funcionalidades Atuais

* **Menu Principal Interativo:** Permite iniciar o jogo, ligar/desligar a música de fundo e sair do jogo.
* **Controle do Herói:** Movimente o herói pelo cenário utilizando as teclas direcionais (setas do teclado). O herói possui animações de movimento e de espera (idle).
* **Inimigos com Patrulha:** Inimigos se movem autonomamente dentro de áreas predefinidas.
* **Sistema de Colisão:** Detecção de colisão entre o herói e os inimigos.
* **Sistema de Dano:** Ao colidir com um inimigo, o herói perde vida. Há um breve período de invulnerabilidade após receber dano (cooldown).
* **Game Over:** O jogo termina quando a vida do herói chega a zero.
* **Música e Sons:** Música de fundo para imersão e um efeito sonoro para colisões.
* **Interface de Vida:** A vida atual do herói é exibida no canto superior direito da tela.

## Como Jogar

1.  **Requisitos:**
    * Python 3 instalado no seu sistema.
    * Pygame Zero instalado (`pip install pgzero`).
    * (Opcional) Se você não tiver o Pygame instalado via Pygame Zero, pode precisar instalá-lo separadamente (`pip install pygame`).

2.  **Execução:**
    * Clone este repositório para o seu computador.
    * Navegue até a pasta do projeto no seu terminal ou prompt de comando.
    * Execute o jogo com o comando: `pgzrun main.py`

## Controles

* **Teclas Direcionais (Seta para Cima, Seta para Baixo, Seta para Esquerda, Seta para Direita):** Movimentam o herói.
* **Enter:** No menu principal, seleciona a opção destacada.
* **Clique do Mouse:** No menu principal, também permite selecionar as opções.

## Créditos

* Este jogo foi criado utilizando a incrível biblioteca [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/).
* (Adicione aqui os créditos de quaisquer assets de música, sons ou gráficos que você utilizou, se aplicável.)

## Status do Projeto

Este é um projeto em desenvolvimento para aprendizado e diversão. Funcionalidades futuras podem incluir:

* Geração procedural de níveis.
* Mais tipos de inimigos com diferentes comportamentos.
* Itens colecionáveis e power-ups.
* Um sistema de pontuação.
* E muito mais!

## Contribuições

(Se você estiver aberto a contribuições)

Contribuições são bem-vindas! Se você tiver ideias para melhorar o jogo, encontrou bugs ou gostaria de adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.
