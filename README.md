# Finance App

Aplicativo de controle financeiro no terminal, desenvolvido para praticar a base do Python com boas práticas. Usei IA como tutor (explicações e revisão), não para gerar o código pronto.

## Funcionalidades

- Ver saldo
- Despesas (total e maior despesa)
- Receitas (total e maior receita)
- Ver extrato
- Registrar nova transação (com validação de valor e tipo)
- Dados salvos em JSON: as transações continuam lá quando o app é fechado

Com ele, você armazena dados financeiros de forma organizada e consulta, a qualquer momento, tudo o que foi inserido e quanto resta de saldo.

## Como rodar

No terminal, entre na pasta do projeto e execute:

    cd caminho/para/finance_app
    python main.py

## Estrutura dos arquivos

- `main.py`: menu principal em loop (`while`). Importa as funções e conversa com o usuário.
- `financas.py`: regras de negócio (cálculo de saldo, totais, maiores valores, registro de transações).
- `data/armazenamento.py`: salva e carrega as transações em `data/transacoes.json`.

## O que eu aprendi

Desabilitei o autocomplete de IA no editor porque estava atrapalhando meu aprendizado.

Fundamentos praticados: variáveis, `if/elif/else`, `for`, `while`, listas, dicionários, funções, `try/except`, módulos e leitura/escrita de arquivos JSON.

## Próximos passos

- Migrar o armazenamento de JSON para SQL (PostgreSQL)
- Criar uma API com FastAPI
- Integrar um LLM para interpretar lançamentos em linguagem natural (ex: "gastei 45 no almoço") e classificar despesas automaticamente