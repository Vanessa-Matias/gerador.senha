# **Sobre o Projeto**

Esse é o meu primeiro projeto em Python.

Um gerador de senhas simples e eficaz, criado para ajudar você a criar senhas seguras e aleatórias.

# **Funcionalidades**
* **Personalização:** Permite ao usuário escolher o tamanho da senha.
* **Complexidade:** Inclui letras, números e caracteres especiais para criar senhas robustas.
* **Validação:** Verifica se a senha gerada possui o comprimento mínimo recomendado.
* **Feedback:** Informa o usuário sobre a força da senha gerada.
* **Interface amigável:** Utiliza cores para destacar informações importantes.

# **Conceitos-chave e bibliotecas**
O script utiliza a função `password_generator` para gerar senhas aleatórias. A função recebe como parâmetro o comprimento da senha (`len_pass`). Se nenhum valor for fornecido, a função assume o valor padrão de 8 caracteres.
A biblioteca `random` é utilizada para selecionar aleatoriamente caracteres de um conjunto pré-definido. O módulo `string` fornece constantes que representam o conjunto de letras maiúsculas, minúsculas, dígitos e caracteres de pontuação, que são combinados para formar a senha.

# **Como Funciona?**
1 - Ao iniciar o programa, o usuario deverá colocar a quantidade de digitos que deseja em sua senha.

2- Se o usuário não digitar nenhum número válido, ou um número que seja menor que 8 ou maior que 32 digitos, o programa apresentará mensagens de alerta para a correção.

3 - Caso o usuário digiti a quantidade correta de digitos dentro do padrão configurado, o programa vai gerar sua senha.

# **Imagem**
* **Exemplo 1:**

![Image](https://github.com/user-attachments/assets/96e59a06-17e3-40a7-acfe-5cdb49441e55)

* **Exemplo 2:**

![Image](https://github.com/user-attachments/assets/de390e4f-dfe3-4b2c-b9cd-944396a952f0)

* **Exemplo 3:**
  
![Image](https://github.com/user-attachments/assets/818803c6-5729-4cec-98a5-dc9b1e2490c1)
