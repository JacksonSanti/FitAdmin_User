# FitAdmin (User)

## Introdução

Este projeto é um MVP (Minimum Viable Product) desenvolvido para a PUC-Rio, com o objetivo de colocar em prática os conhecimentos adquiridos no semestre atual. 
Ele representa a terceira parte do projeto com arquitura em microserviço, após a instalação da terceira parte deve ser feita a instalação da [parte 4](https://github.com/JacksonSanti/FitAdmin_financial_grpc).

---

## Informativo

### 1. **Sobre a proposta**
Nos últimos anos, tem havido um aumento expressivo de brasileiros buscando uma melhor qualidade de vida, com foco na saúde e bem-estar. Com isso, o número de academias abertas em diversas regiões do Brasil cresceu significativamente.

Contudo, muitas academias — especialmente as que não pertencem a grandes redes — ainda oferecem uma experiência ruim para o aluno, desde o cadastro de dados até o gerenciamento financeiro.

Este projeto tem como objetivo desenvolver um sistema completo que resolva esse problema, proporcionando uma experiência mais agradável e dinâmica tanto para o aluno quanto para a academia.

---

### 2. **Sobre a documentação**

**Tecnologias utilizadas:** 
- GRPC SERVER
- SQLite

**Fluxograma:**

![FitAdmin Fluxograma](./docs/FitAdmin_Fluxograma.png)


---

## Instalação

1. **Clone este repositório**
   ```bash
   git clone git@github.com:JacksonSanti/FitAdmin_User.git
2. **Após criar o ambiente virtual,instale as dependências necessárias**
   ```bash
   pip install -r requirements.txt
3. **Rodar o comando abaixo para subir este container (é necessário ter o docker instalado)**
   ```bash
   docker compose up -d
