### 📋 Anotações

**Passo a passo do algoritmo:**

1. Definir produtos a serem monitorados
2. Carregar lista de produtos
3. Entrar no site
4. Para cada produto:
   1. Buscar o produto
   2. Se encontrar:
      1. Buscar última informação do produto
      2. Comparar leitura atual com anterior
      3. Se houver mudança:
         1. Exibir mudança
      4. Salvar informações do produto atual
   3. Se não:
      1. Salvar log de erro
5. Gerar relatório do que mudou e o que não mudou
6. Mostrar para o cliente

#### 1. Definir produtos a serem monitorados

* Camiseta Oversized Legacy Azul Marinho
* Camiseta Poliamida Prime Branco
* Camiseta Oversized Plate Marrom Telha
* Camiseta Oversized Plate Off White
* Camiseta Oversized Legacy Marrom Telha
* Regata Machão Oversized Lupus Preto
* Camiseta Oversized Empire Bege Duna
* Camiseta Oversized Cutting Season Branco
* Camiseta Oversized In Motion Off White
* Camiseta Oversized Hunter Preto

#### 2. Entrar no site

[usealphaco.com.br](https://usealphaco.com.br)

#### 3. Buscar o produto

Buscar items de acordo com o **item 4**

#### 4. Salvar informações do produto

Tabela de produtos

| id | product                                  | url                                                                                                                                               |
| -- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Camiseta Oversized Legacy Azul Marinho   | [usealphaco.com.br/products/camiseta-legacy-oversized-azul-marinho](https://usealphaco.com.br/products/camiseta-legacy-oversized-azul-marinho)     |
| 2  | Camiseta Poliamida Prime Branco          | [usealphaco.com.br/products/camiseta-poliamida-prime-branco](https://usealphaco.com.br/products/camiseta-poliamida-prime-branco)                   |
| 3  | Camiseta Oversized Plate Marrom Telha    | [usealphaco.com.br/products/camiseta-oversized-plate-marrom-telha](https://usealphaco.com.br/products/camiseta-oversized-plate-marrom-telha)       |
| 4  | Camiseta Oversized Plate Off White       | [usealphaco.com.br/products/camiseta-oversized-plate-off-white](https://usealphaco.com.br/products/camiseta-oversized-plate-off-white)             |
| 5  | Camiseta Oversized Legacy Marrom Telha   | [usealphaco.com.br/products/camiseta-oversized-legacy-marrom-telha](https://usealphaco.com.br/products/camiseta-oversized-legacy-marrom-telha)     |
| 6  | Regata Machão Oversized Lupus Preto     | [usealphaco.com.br/products/regata-machao-oversized-lupus-preto](https://usealphaco.com.br/products/regata-machao-oversized-lupus-preto)           |
| 7  | Camiseta Oversized Empire Bege Duna      | [usealphaco.com.br/products/camiseta-oversized-empire-bege-duna](https://usealphaco.com.br/products/camiseta-oversized-empire-bege-duna)           |
| 8  | Camiseta Oversized Cutting Season Branco | [usealphaco.com.br/products/camiseta-oversized-cutting-season-branco](https://usealphaco.com.br/products/camiseta-oversized-cutting-season-branco) |
| 9  | Camiseta Oversized In Motion Off White   | [usealphaco.com.br/products/camiseta-oversized-in-motion-off-white](https://usealphaco.com.br/products/camiseta-oversized-in-motion-off-white)     |
| 10 | Camiseta Oversized Hunter Preto          | [usealphaco.com.br/products/camiseta-oversized-hunter-preto](https://usealphaco.com.br/products/camiseta-oversized-hunter-preto)                   |


Tabela de registros (relatorio)

| id | product_id | value | date | didValueChange |
| -- | ---------- | ----- | ---- | -------------- |
|    |            |       |      |                |
|    |            |       |      |                |




#### 5. Mostrar para o cliente

* Montar um CSV com as informações
* Enviar via email

Se quiser versionar um exemplo de dado, use um arquivo separado tipo 'data/.gitkeep' ou um exemplo de amostra.

```python
# Problema 1 - Valor por hora
# *Escreva um programa que retorna o valor hora de um funcionário
# *com base no seu salário mensal e horas trabalhadas por mês.

"""
Método 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais 
informações/investigue mais até você compreender completamente o problema)

1. Quais são os dados de entrada necessários?
- Salário Mensal
- Quantidade de horas trabalhadas

2. O que devo fazer com esses dados?
- Calcular o valor hora

3. Quais são as restrições deste problema?
- Precisa ter um valor do salário mensal
- Precisa ter um valor da quantidade de horas trabalhadas

4. Qual é o resultado esperado?
- Exibir o valor hora da pessoa, com base no cálculo de valor hora

5. Quais são os passos para chegar ao resultado esperado? (pseudocódigo)
- Receber o valor do salário mensal do funcionário
- Receber a quantidade de horas trabalhadas no mês
- Calcular o valor hora dividindo o salário mensal pela quantidade de horas trabalhadas por mês
- Exibir o valor hora calculado
"""
```
