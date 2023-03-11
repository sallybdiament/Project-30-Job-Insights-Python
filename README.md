# Job Insights - Computer Science Project

Projeto em **Python** com framework **Flask** para obter dados através de um arquivo ```.CSV```!

Habilidades trabalhadas:
- Utilizar o terminal interativo do Python.
- Utilizar estruturas condicionais e de repetição.
- Utilizar funções built-in do Python.
- Utilizar tratamento de exceções.
- Realizar a manipulação de arquivos.
- Escrever funções.
- Escrever testes com Pytest.
- Escrever seus próprios módulos e importá-los em outros códigos.

Projeto 30 da [Trybe](https://wwww.betrybe.com), módulo de Ciência da Computação.

![Score Project](./score-project.png)
## O Projeto

* Implementar função para: abrir, ler e transformar os dados como lista de dicionários, a partir do caminho do arquivo.
* Implementar funções para extração de informações do relatório como: tipos de emprego, tipos de indústria, maior salário e menos salário.
* Implementar funções para filtrar dados: por tipo de emprego, por indústria, por faixa salarial.
* Implementar funções de testes com **Pytest**.

## Instalação 


#### 1- Clonar o repositório

```git clone git@github.com:sallybdiament/Project-30-Job-Insights-Python.git```

#### 2 - Crie o ambiente virtual para o projeto

python3 -m venv .venv && source .venv/bin/activate

#### 3 - Instalar as dependências

python3 -m pip install -r dev-requirements.txt

#### 3 - Para executar as funções:

Abrir o terminal e rodar a função desejada: ```python3 -i src/insights/jobs.py```

#### 4 - Executar os testes:

```python3 -m pytest tests/nomedoarquivo.py -k nome_da_func_de_tests```

ou para executar um teste específico:
```python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste```


## Tecnologias
- Python
- Pytest (unittest.mock, fixture, etc)
- Flask
- Flake8 e Black
- Exceptions (try, except, elsse, finally)
- Data types (int, str, list, dict, tuples, set, etc)
- Conditionals (if, elif, else)
- Loops (for, list comprehension, while, enumerate)
- Functions in Python
- Manipulation of CSV, JSON and XML data (with, open, json, csv, DictReader, etc)
