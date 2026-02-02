# Portfólio de Ciência de Dados

<div align="center">
  <img src="assets/images/Unicap_Icam_Tech-01.png" alt="Logo Unicap Icam Tech" width="300"/>
</div>

<br />

> **Disciplina:** Ciência de Dados  
> **Professor:** Diego Pinheiro, PhD  
> **Aluno:** Roosevelt Bispo dos Santos Júnior  
> **Semestre:** 2025.2

---

## 📌 Sobre o Repositório

Este repositório centraliza todas as atividades práticas, implementações de algoritmos e o projeto final desenvolvidos ao longo da disciplina de Ciência de Dados. 

O foco das atividades é a implementação "do zero" (from scratch) de conceitos fundamentais de Machine Learning e Estatística, além do uso de bibliotecas padrão de mercado para análise de dados.

## 📂 Estrutura do Portfólio

Aqui você encontra o índice do meu aprendizado. Clique no nome da pasta para ver os detalhes de cada implementação.

| Pasta | Tópico Principal | Descrição Resumida |
| :--- | :--- | :--- |
| [**Atividade 01**](./Atividade_01) | **Álgebra Linear** | Implementação de operações matriciais fundamentais, cálculo de matriz inversa e pseudo-inversa para resolução de sistemas lineares. |
| [**Atividade 02**](./Atividade_02) | **Regressão Linear & PLA** | Implementação do algoritmo *Perceptron Learning Algorithm* (PLA) e modelos de regressão linear simples. |
| [**Atividade 03**](./Atividade_03) | **Estatística Inferencial** | Implementação das classes `DataGenerator`, `Bootstrap` (reamostragem) e `ConfidenceInterval` para análise estatística e estimativa de erros. |
| [**Atividade 04**](./Atividade_04) | **Classificação** | Implementação de Regressão Logística e algoritmos de classificação para separação de dados. |
| [**Projeto Final**](./Projeto) | **Análise de Vinhos** | **Dataset:** *Wine Quality*. Análise exploratória, tratamento de dados e modelagem preditiva para determinar a qualidade de vinhos (White/Red). |

---

## 🛠 Tecnologias e Ferramentas

O projeto foi desenvolvido utilizando práticas modernas de Engenharia de Software aplicadas à Ciência de Dados:

* **Linguagem:** Python 3.x
* **Manipulação de Dados:** Pandas, Numpy
* **Visualização:** Matplotlib
* **Ambiente de Desenvolvimento:** VS Code, Docker (DevContainers)
* **Testes Automatizados:** Unittest (garantindo a integridade dos algoritmos implementados)
* **Controle de Versão:** Git & GitHub

## 🚀 Como Executar

Como este repositório utiliza **DevContainers**, o ambiente é padronizado.

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/roosevelt07/Portfolio-Data-Science.git](https://github.com/roosevelt07/Portfolio-Data-Science.git)
    ```
2.  Abra a pasta no **VS Code**.
3.  Quando solicitado, clique em **"Reopen in Container"** (Certifique-se de ter o Docker instalado).
4.  Cada atividade possui sua própria pasta `src` e `tests`. Para rodar os testes de uma atividade específica, navegue até a pasta e execute:
    ```bash
    python -m unittest discover tests
    ```

---

<div align="center">
  <sub>Desenvolvido por Roosevelt Junior no contexto acadêmico da UNICAP (ICAM-TECH).</sub>
</div>
