# 💧 Controle de Níveis de Água

## 📌 Sobre o projeto

O **Controle de Níveis de Água** é um projeto desenvolvido em Python para simular o monitoramento do nível de água de um reservatório.

O programa utiliza uma lista para armazenar cinco níveis de água, cada um associado a uma situação e a uma cor específica. Com o auxílio da **biblioteca Colorama**, as mensagens são exibidas no terminal com cores diferentes, facilitando a identificação de cada situação.

## 🚨 Adaptação: nesta versão, os níveis são definidos diretamente no código, sem a necessidade de entrada de dados pelo usuário. O programa percorre os cinco níveis para simular o monitoramento do reservatório.

## 🎯 Objetivo

O objetivo do sistema é demonstrar como utilizar listas, funções, estruturas de repetição e bibliotecas externas em Python para desenvolver um sistema simples de monitoramento.

A utilização de cores permite identificar visualmente cada situação do reservatório, desde o nível muito baixo, considerado crítico, até o nível muito alto, que representa um alerta.

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github&logoColor=white)

- 🐍 Python
- 💻 VS Code
- 📦 Git
- 🐙 GitHub
  
## 🚦 Níveis do reservatório

O sistema trabalha com cinco níveis de água, cada um representando uma situação específica:

Nível

Situação

Cor da mensagem

## Nível 1

Muito baixo (crítico)

🔴 Vermelho

## Nível 2

Baixo

🟡 Amarelo

## Nível 3

Médio

🟢 Verde

## Nível 4

Alto

🩵 Ciano

## Nível 5

Muito alto (alerta)

🔵 Azul

# ⚙️ Funcionamento do sistema

O programa utiliza uma lista chamada niveis_agua para armazenar os níveis, as situações e as cores correspondentes.

A função definir_cor() recebe o nível informado, identifica sua situação e retorna a cor correspondente para a exibição da mensagem.

A biblioteca Colorama é utilizada para aplicar as cores no terminal. Ao final de cada mensagem, o estilo é restaurado utilizando Style.RESET_ALL, evitando que a formatação colorida seja mantida indevidamente nas mensagens seguintes.

## ▶️ Como executar

### 1. Baixe ou clone o projeto

Tenha o projeto `controle-niveis-agua` disponível no seu computador.

### 2. Abra a pasta no VS Code

Abra a pasta do projeto no Visual Studio Code.

### 3. Instale a biblioteca necessária

No terminal do VS Code, execute:


```bash
pip install -r requirements.txt
```

### 4. Execute o arquivo

No terminal, execute:

```bash
python main.py
```

### 5. Visualize os resultados

O programa apresentará os cinco níveis do reservatório, com uma mensagem correspondente a cada situação e a cor definida no código.

Não é necessário informar dados manualmente, pois os níveis são definidos previamente para a simulação.

## 💡 Exemplo de uso

Ao executar o programa, a saída no terminal será semelhante a esta:

=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===

Nível 1: Muito baixo (CRÍTICO)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (ALERTA)

Monitoramento finalizado.

Observação: no terminal, cada mensagem será exibida com sua respectiva cor. As cores não aparecem na representação textual acima, pois dependem da execução do programa.

## 📂 Estrutura do projeto

```text
controle-niveis-agua/
│
├── main.py
├── requirements.txt
└── README.md
```

main.py: contém o código principal do sistema.

requirements.txt: informa a biblioteca necessária para executar o programa.

README.md: apresenta a documentação e as instruções de utilização do projeto.

👨‍💻 Autor

**Alexandre Ferraz**

🎓 Estudante de Desenvolvimento de Sistemas.

🚀 Sempre aprendendo e evoluindo na área de tecnologia.

---

💧 Projeto desenvolvido para fins de estudo e aprendizado em programação. 