
# Análise e predição de Churn
- Python 3.9.19

Um projeto de ciência de dados que analisa dados de clientes e prevê a probabilidade de churn com base em seu perfil de compra em uma empresa de telecomunicações

- Você encontrará a modelagem e análise exploratória dos dados na pasta de notebooks. Ao inserir os dados no diretório descrito nas etapas abaixo e preparar o ambiente, o usuário pode executar todas as células e checar as anotações.

- No projeto, tem-se outras pastas como a de reports que está com as figuras das referentes análises salvas, como também o pipeline de treinamento que é importado no arquivo main.py


## Rodando localmente

Clone o projeto

```bash
  git clone https://link-para-o-projeto
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

- ## **Crie o diretório DATA apresentado na estrutura abaixo e insira os [dados utilizados](https://docs.google.com/spreadsheets/d/1hyNndE4QVhjVLmB37ePBURRUkBlFUMJ3g6wlH2UenJY/edit#gid=516785925) no diretório data/raw e os chame de customer-churn.xlsx**

Execute o arquivo main.py no diretório do projeto

```bash
  python main.py
```


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  pytest
```
- Para mais informações: [pytest](https://docs.pytest.org/en/8.0.x/)


Organização do Projeto
------------

    ├── README.md          <- O README para desenvolvedores que usarem este projeto.
    ├── data
    │   ├── external       <- Dados de fontes de terceiros.
    │   ├── interim        <- Dados intermediários que foram transformados.
    │   ├── processed      <- Os conjuntos de dados finais e canônicos para modelagem.
    │   └── raw            <- O dump de dados original e imutável.
    │
    ├── models             <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
    │
    ├── notebooks          <- Notebooks Jupyter. A convenção de nomenclatura é um número (para ordenação),
    │                         as iniciais do criador, e uma descrição curta delimitada por `-`, por exemplo,
    │                         `1.0-jqp-exploracao-inicial-dos-dados`.
    │
    ├── references         <- Dicionários de dados, manuais e todos os outros materiais explicativos.
    │
    ├── reports            <- Análises geradas como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos e figuras geradas para serem usadas nos relatórios
    │
    ├── requirements.txt   <- O arquivo de requisitos para reproduzir o ambiente de análise, por exemplo, gerado com `pip freeze > requirements.txt`
    │
    ├── src                <- Código fonte para uso neste projeto.
    │   ├── __init__.py    <- Torna src um módulo Python
    │   │
    │   ├── data           <- Scripts para baixar ou gerar dados
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para transformar dados brutos em recursos para modelagem
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para treinar modelos e, em seguida, usar modelos treinados para fazer
    │   │   │                 previsões
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para criar visualizações exploratórias e orientadas a resultados
    │       └── visualize.py
    │
    └── tests    <- testes para verificar a consistência do fluxo de trabalho


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
