# Checkpoint 2 - Visão Computacional

## Autoria
Projeto desenvolvido por:
- Ana Carolina - RM93633
- Eloisa Araujo - RM94604
- Luana Ramos dos Santos - RM94670
- Marianne Nocce - RM93255
- Marina Lira - RM95503

Como parte da avaliação do Checkpoint 2 da disciplina de Sistemas Inteligentes da FIAP.

# Tema do Projeto
Detecção do estado de saúde de folhas a partir de análise de vídeo com técnicas de visão computacional.

# Problema do Mundo Real
A identificação visual de doenças em folhas é uma tarefa essencial na agricultura para garantir a saúde das plantas e a produtividade. O projeto visa detectar automaticamente se uma folha está:

- **Severamente Doente**: se estiver totalmente marrom/seca
- **Doente**: se for verde, mas contiver manchas
- **Saudável**: se estiver totalmente verde, sem manchas

# Solução Proposta
Foi desenvolvido um algoritmo em Python que lê um vídeo com folhas em movimento e segmenta a região da folha com base em cor (HSV). Assim detecta manchas por threshold e morfologia e analisa a proporção de verde e presença de manchas. Classifica e escreve no vídeo o estado de saúde.

# Tecnologias Utilizadas
- Python
- OpenCV (cv2)
- NumPy

# Como Executar
1. Instale as dependências:
   ```bash
   pip install opencv-python numpy
   ```
2. Salve seu vídeo como `video_folhas.mp4` na mesma pasta do script.
3. Execute no terminal:
   ```bash
   python visaoComputacional.py
   ```
4. O vídeo será exibido como `video_folhas.mp4`

# Estrutura do Projeto
```
|- visaoComputacional.py
|- video_folhas.mp4
|- README.md
```

# Professor Responsável
Prof. Yan Gabriel Coelho

