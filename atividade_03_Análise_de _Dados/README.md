[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DR95Hl6l)
# Ativiadade Ciência da Computação
<img src="assets/images/Unicap_Icam_Tech-01.png" alt="drawing" width="200"/>

## Identificação
**Professor**: Diego Pinheiro, PhD

**Disciplina**: Ciência dos Dados

**Atividade**: Atividade - Análise de Dados

## Instruções 
> 1. Sua implementação deve estar dentro da pasta **src** 
> 2. Não modifique nenhum código dentro da pasta **test**
> 3. A submissão **não deve ser feita após o prazo** (nem 1 minuto a mais)

## Descrição da Atividade
### Questão 01
Implemente a classe `DataGenerator` que possui

1. O construtor

```python
def __init__(self, loc, scale, n) -> None:
```
que inicializa os atributos.

2. O método de instância

```python
def get_data(self):
```
que retorna os dados `X`. 

> Faça o testes da classe `TestDataGenerator` passarem.

### Questão 02
Implemente a classe `Bootstrap` que possui 

1. Um construtor 

```python
def __init__(self, X)
```
que inicializa os dados `X`.

2. Um método de instância
```python
def calculate_bootstrap(self, bootstraps, estimator):
```
que calcula os amostras (ie., `bootstraps samples`)

3. Um método de instância 
```python
def mean(self):
```
que retorna a estimativa do valor esperado do estimator considerando as *bootstraps samples*

4. Um método de instância
```python 
def std(self):
```
que retorna o erro padrão do estimator considerando as *bootstraps samples*. 

> Faça os testes da classe `TestBootstrap` passarem.

### Questão 03
Implamente a classe `ConfidenceInterval` que possui 

1. Um construtor 
```python 
def __init__(self, data, alpha) -> None:
```
que inicializa os dados


2. O método de instância 
```python 
def calculate_lower_bound(self):
```

3. O método de instância 
```python 
def calculate_upper_bound(self):
```

Faça os testes da classe `TestConfidenceInterval` passarem.