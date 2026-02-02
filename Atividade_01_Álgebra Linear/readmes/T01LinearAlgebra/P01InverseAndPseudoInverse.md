
## Descrição da Atividade 

### Questão 1
Uma das aplicações da matriz inversa é na resolução de sistemas de equações. Suponha que você esteja procurando comprar um apartamento. Após você ter visitado 3 apartamentos, percebeu que:
-	O primeiro apartamento tinha 4 quartos, 4 banheiros, 120 metros quadrados e custava R$110,000;
-	O segundo apartamento tinha 6 quartos, 2 banheiro, 180 metros quadrados e custava R$ R$135,000;
-	O terceiro apartamento tinha 2 quarto, 4 banheiros, 80 metros quadrados, e custava R$75,000. 

Você se perguntou se o custo de um apartamento pode ser definido em função do número de quartos, do número de banheiros, e de seu tamanho.  Então, escreveu o sistema de equações a seguir. 

<img src="../../assets/T01LinearAlgebra/P01InverseAndPseudoInverse/eqs1.png"  width="400"/>

Para isso, você deve 
1.	Armazenar os coeficientes na matriz `X`;
2.	Armazenar as constantes na matriz `y`;
3. Encontrar a matriz inversa X<sup>-1</sup>
4. Multiplicar a matriz inversa X<sup>-1</sup> pela matriz de coeficientes `y`. 


### Questão 2

Uma das aplicações da matriz inversa é na resolução de sistemas de equações. Porém, não pode ser utilizada quando a matriz não é quadrada. Por exemplo, quando o número de linhas é maior que o número de colunas, o que é bem comum em Ciência dos Dados. 

Suponha que você esteja procurando comprar um apartamento. Após você ter visitado 3 apartamentos em um bairro não muito procurado, você percebeu que:
-	O primeiro apartamento tinha 1 quarto, 1 banheiro, 50 metros quadrados e custava R$75,000;
-	O segundo apartamento tinha 2 quartos, 1 banheiro, 50 metros quadrados e custava R$ R$125,500;
-	O terceiro apartamento tinha 2 quartos, 1 banheiro, 100 metros quadrados e custava R$126,000;

Após visitar os mesmos apartamentos em um bairro muito procurado, você percebeu que os mesmos 3 apartamentos custavam, respectivamente R$175,000, R$225,500 e R$226,000

Você se perguntou se o custo de um apartamento pode ser definido em função do número de quartos (x), do número de banheiros(y), de seu tamanho (z), e da sua localização em um bairro muito procurado (w).  Então, escreveu o sistema de equações a seguir para os 6 apartamentos visitados. 

<img src="../../assets/T01LinearAlgebra/P01InverseAndPseudoInverse/eqs2.png"  width="400"/>

Porém, como a matriz A não é quadrada, a sua inversa não está definida. Porém, como você está se tornando um Cientista dos Dados, você sabe que pode utilizar o Método dos Mínimos Quadrados (MMQ), ou Mínimos Quadrados Ordinários (MQO) ou OLS (do inglês Ordinary Least Squares). 

Para isso, você deve

1. Calcular a transposta X<sup>T</sup>;
2. Multiplicar a transposta X<sup>T</sup> por X para encontrar a matriz (X<sup>T</sup>X);
3. Calcular a inversa da matriz (X<sup>T</sup>X) ou seja (X<sup>T</sup>X)<sup>-1</sup>;
4. Calcular a pseudo-inversa (X<sup>T</sup>X)<sup>-1</sup>X<sup>T</sup>;
5. Multiplicar a pseudo-inversa pelo vetor de constantes.