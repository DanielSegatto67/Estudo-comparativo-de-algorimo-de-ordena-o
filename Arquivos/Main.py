from Sorts import *
from Vetor import *
import sys

sys.setrecursionlimit(100000) 

vetor_melhor_caso = preencheVetor(1000) #Preenche um vetor com numeros de 0 até o parametro passado - 1, representa o melhor caso

vetor_caso_medio = preencheVetor(1000)
randomizaVetor(vetor_caso_medio)  #Aleatoriza os elementos de um vetor para representar o caso médio

vetor_pior_caso = preencheVetorDesc(1000) #Preenche um vetor a partir do parametro passado-1 até o 0, representa o pior caso


comparacoes, trocas, tempo_exec = bubbleSort(vetor_melhor_caso)
comparacoes, trocas, tempo_exec = bubbleSort(vetor_caso_medio)
comparacoes, trocas, tempo_exec = bubbleSort(vetor_pior_caso)
print(f"Bubble Sort:")
print(f"Comparações:{comparacoes}")
print(f"Trocas:{trocas}")
print(f"Tempo de execução:{tempo_exec} segundos\n")


# comparacoes, trocas, tempo_exec = improvedBubbleSort(vetor_melhor_caso)
# comparacoes, trocas, tempo_exec = improvedBubbleSort(vetor_caso_medio)
# comparacoes, trocas, tempo_exec = improvedBubbleSort(vetor_pior_caso)
# print(f"Improved Bubble Sort")
# print(f"Comparações:{comparacoes}")
# print(f"Trocas:{trocas}")
# print(f"Tempo de execução:{tempo_exec} segundos\n")

# comparacoes, trocas, tempo_exec = insertionSort(vetor_melhor_caso)
# comparacoes, trocas, tempo_exec = insertionSort(vetor_caso_medio)
# comparacoes, trocas, tempo_exec = insertionSort(vetor_pior_caso)
# print(f"Insertion Sort:")
# print(f"Comparações:{comparacoes}")
# print(f"Trocas:{trocas}")
# print(f"Tempo de execução:{tempo_exec} segundos\n")

# comparacoes, trocas, tempo_exec = selectionSort(vetor_melhor_caso)
# comparacoes, trocas, tempo_exec = selectionSort(vetor_caso_medio)
# comparacoes, trocas, tempo_exec = selectionSort(vetor_pior_caso)
# print(f"Selection Sort:")
# print(f"Comparações:{comparacoes}")
# print(f"Trocas:{trocas}")
# print(f"Tempo de execução:{tempo_exec} segundos\n")

# comparacoes, trocas, tempo_exec = mergeSort(vetor_melhor_caso)
# comparacoes, trocas, tempo_exec = mergeSort(vetor_caso_medio)
# comparacoes, trocas, tempo_exec = mergeSort(vetor_pior_caso)
# print(f"Merge Sort:")
# print(f"Comparações:{comparacoes}")
# print(f"Trocas:{trocas}")
# print(f"Tempo de execução:{tempo_exec} segundos\n")

# comparacoes, trocas, tempo_exec = quickSort(vetor_melhor_caso)
# comparacoes, trocas, tempo_exec = quickSort(vetor_caso_medio)
# comparacoes, trocas, tempo_exec = quickSort(vetor_pior_caso)
# print(f"Quick Sort:")
# print(f"Comparações:{comparacoes}")
# print(f"Trocas:{trocas}")
# print(f"Tempo de execução:{tempo_exec} segundos\n")

# comparacoes, trocas, tempo_exec = shellSort(vetor_melhor_caso)
# comparacoes, trocas, tempo_exec = shellSort(vetor_caso_medio)
# comparacoes, trocas, tempo_exec = shellSort(vetor_pior_caso)
# print(f"Shell Sort:")
# print(f"Comparações:{comparacoes}")
# print(f"Trocas:{trocas}")
# print(f"Tempo de execução:{tempo_exec} segundos\n")