# Checkpoint 2 - Visão Computacional

## Autoria
Projeto desenvolvido por:
- Ana Carolina - RM93633
- Eloisa Araujo - RM94604
- Luana Ramos dos Santos - RM94670
- Marianne Nocce - RM93255
- Marina Lira - RM95503



# Tema do Projeto
Detecção do estado de saúde de folhas a partir de análise de vídeo com técnicas de visão computacional.

# Problema do Mundo Real
A identificação visual de doenças em folhas é uma tarefa essencial na agricultura para garantir a saúde das plantas e a produtividade. O projeto visa detectar automaticamente se uma folha está:

- **Severamente Doente**: se estiver totalmente marrom/seca
- **Doente**: se for verde, mas contiver manchas
- **Saudável**: se estiver totalmente verde, sem manchas

## Exemplos de Classificação

### Saudável

![saudavel](https://github.com/user-attachments/assets/a5f1d74c-0f3a-4ebd-998a-37207047f50c)


### Doente

![doente](https://github.com/user-attachments/assets/3672c05c-1795-4066-9dce-a05df7b8478c)


### Severamente Doente

![severamente_doente](https://github.com/user-attachments/assets/bfabab1a-549c-497a-9c70-2a9328f7b530)


# Solução Proposta
Foi desenvolvido um algoritmo em Python que lê um vídeo com as folhas e segmenta a região da folha com base em cor (HSV). Assim detecta manchas por threshold e morfologia e analisa a proporção de verde e presença de manchas. Classifica e escreve no vídeo o estado de saúde das folhas.

# Tecnologias Utilizadas
- Python
  
- OpenCV
  ### Biblioteca de visão computacional usada para:
   - Ler vídeos (cv2.VideoCapture)
   - Manipular imagens (conversão de cores, máscaras, contornos)
   - Exibir imagens e vídeos com anotações (como texto e contornos)
     
- NumPy
  ### Biblioteca para manipulação de arrays, usada para:
   - Trabalhar com máscaras e faixas de cor (HSV)
   - Definir intervalos de segmentação
   - Operações matemáticas sobre imagens e matrizes

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

