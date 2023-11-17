from Sorts import *
from Vetor import *

vetor = preencheVetor(1000)
#randomizaVetor(vetor)
#vetor = preencheVetorDesc(1000)
comparacoes, trocas, tempo_exec = bubbleSort(vetor)

print(f"Comparacoes: {comparacoes}")
print(f"Trocas: {trocas}")
print(f"Tempo de execucao: {tempo_exec} segundos")
