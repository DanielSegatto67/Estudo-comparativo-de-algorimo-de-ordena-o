import time

def bubbleSort(arr):
    Comparacoes = 0
    Trocas = 0
    tempo_ini = time.time()

    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            Comparacoes +=1
            if arr[j]>arr[j+1]:
                temp = arr[j]
                Trocas +=1
                arr[j] = arr[j+1]
                Trocas +=1
                arr[j+1] = temp
                Trocas +=1
    tempo_fim = time.time()

    tempo_exec = tempo_fim - tempo_ini
    return Comparacoes, Trocas, tempo_exec

def improvedBubbleSort(arr):
    trocou = True
    tam_vetor = len(arr)-1
    Comparacoes = 0
    Trocas = 0
    tempo_ini = time.time()

    while tam_vetor > 0 and trocou:
        trocou = False
        for i in range(tam_vetor):
            Comparacoes +=1
            if arr[i]>arr[i+1]:
                trocou = True
                temp = arr[i]
                Trocas +=1
                arr[i] = arr[i+1]
                Trocas +=1
                arr[i+1] = temp
                Trocas +=1
        tam_vetor = tam_vetor-1
    tempo_fim = time.time()
    
    tempo_exec = tempo_fim - tempo_ini
    return Comparacoes, Trocas, tempo_exec

def selectionSort(arr):
    Comparacoes = 0
    Trocas = 0
    tempo_ini = time.time()

    for i in range(len(arr)-1,0,-1):
        Max=0
        for j in range(1,i+1):
            Comparacoes+=1
            if arr[j]>arr[Max]:
                Max = j
        if i != Max:
            temp = arr[i]
            Trocas+=1
            arr[i] = arr[Max]
            Trocas+=1
            arr[Max] = temp
            Trocas+=1
    tempo_fim = time.time()

    tempo_exec = tempo_fim - tempo_ini
    return Comparacoes, Trocas, tempo_exec

def insertionSort(arr):
    Comparacoes = 0
    Trocas = 0
    tempo_ini = time.time()

    for i in range(1,len(arr)):
        valor_atual = arr[i]
        pos = i
        Comparacoes+=1
        while pos>0 and arr[pos-1]>valor_atual:
            Comparacoes+=1
            arr[pos]=arr[pos-1]
            Trocas+=1
            pos = pos-1

        arr[pos]=valor_atual
        Trocas+=1
    tempo_fim = time.time()

    tempo_exec = tempo_fim - tempo_ini
    return Comparacoes, Trocas, tempo_exec

def mergeSort(arr):
    def merge(arr, esq, meio, dir):
        n1 = meio - esq + 1
        n2 = dir - meio

        L = arr[esq:meio+1]
        R = arr[meio+1:dir+1]

        i = j = 0
        k = esq

        while i < n1 and j < n2:
            comparacoes[0] += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            trocas[0] += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            trocas[0] += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            trocas[0] += 1

    def _merge_sort(arr, l, r):
        if l < r:
            m = (l + r) // 2

            _merge_sort(arr, l, m)
            _merge_sort(arr, m + 1, r)
            merge(arr, l, m, r)

    comparacoes = [0]
    trocas = [0]

    tempo_ini = time.time()

    _merge_sort(arr, 0, len(arr) - 1)

    tempo_fim = time.time()
    tempo_execucao = tempo_fim - tempo_ini

    return comparacoes[0], trocas[0], tempo_execucao

def shellSort(arr):
    Trocas = [0]
    Comparacoes = [0]

    def gapInsertionSort(arr,ini,div):
        for i in range(ini+div,len(arr),div):

            valor_atual = arr[i]
            pos = i
            Comparacoes[0] +=1
            while pos>=div and arr[pos-div]>valor_atual:
                Comparacoes[0] += 1
                arr[pos]=arr[pos-div]
                Trocas[0] +=1
                pos = pos-div

            arr[pos]=valor_atual
            Trocas[0] +=1

    tempo_ini = time.time()
    subarr = len(arr)//2
    while subarr > 0:

      for ini in range(subarr):
        gapInsertionSort(arr,ini,subarr)

      subarr = subarr // 2
    tempo_fim = time.time()

    tempo_exec = tempo_fim - tempo_ini

    return Comparacoes, Trocas, tempo_exec


def quickSort(arr):
    def partition(arr, low, high):
        pivot_index = (low + high) // 2
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        i = low - 1

        for j in range(low, high):
            global comparacoes
            comparacoes += 1

            if arr[j] <= pivot:
                i += 1
                global trocas
                trocas += 1
                arr[i], arr[j] = arr[j], arr[i]

        trocas += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    global trocas, comparacoes
    trocas, comparacoes = 0, 0

    start_time = time.time()
    quick_sort_recursive(arr, 0, len(arr) - 1)
    end_time = time.time()

    tempo_exec = end_time - start_time

    return comparacoes, trocas, tempo_exec