# Filosofos
Solución al problema de los N filósofos de E. Dikjstra (Con hilos)



Cinco filósofos se sientan alrededor de una mesa redonda para comer un plato de fideos. Cada filósofo cuenta con un tenedor a la izquierda de su plato, pero para comer los fideos necesita usar dos tenedores. Cuando un filósofo tiene hambre, éste coge primero el tenedor de la izquierda y luego el tenedor de la derecha.

Los filósofos comerán durante un determinado tiempo y luego de comer se sentirán llenos. Un filósofo lleno no come, sino que piensa hasta que le de hambre de nuevo, entonces intentará tomar ambos tenedores y comer. Después de un tiempo sin comer, un filósofo hambriento muere de hambre.

El problema consiste en encontrar un algoritmo que nos permita resolver el dilema de los filósofos, donde todos los filósofos deben de comer, considerando que primero tomaran el tenedor de la izquierda y despues el de la derecha.


******* Requisitos ********
Contar con Python 3

Al ejecutar el código se debe de escribir el numero de segundos que deseamos dure el programa seguido del numero de filósofos. 
Si no se escriben argumentos, por default se inicia con 30 segundos y 5 filósofos.

py filosofos.py [tiempo en segundos] [numero de filósofos]

****************************

Autor: Corella Pérez Elda
