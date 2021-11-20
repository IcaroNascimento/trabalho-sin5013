# TRABALHO 2
# PROBLEMA 1 - Fila de prioridades com heap

class ELEMENTO:
    def __init__(self, id, prior):
        self.id = id
        self.prior = prior
 
class FILADEPRIORIDADE:
    def __init__(self, A, maxElementos):
        self.maxElementos = maxElementos
        if len(A) == 0:
            self.A = [None]
        else:
            self.A = A
        self.m = 0

    def Heap_Max(self):
        if self.m < 1:
            return "-1 -1.0"
        
        max = self.A[1]
        return str(max.id) + ' ' + str(max.prior).replace('.', ',')

    def Heap_Extract_Max(self):
        max = self.A[1]
        self.A[1] = self.A[self.m]
        self.m -= 1
        self.Max_Heapify(1)

        return str(max.id) + ' ' + str(max.prior).replace('.', ',')

    def Heap_Insert(self, elemento):
        heap = self.m + 1
        if heap > self.maxElementos:
            raise "Total de elementos do vetor excedido."
        
        self.m = heap
        self.A.insert(self.m, elemento)
        self.Heap_Increase_Key(heap)

        return 'T'

    def Heap_Print(self):
        imprime = []
        #for elemento in self.A[1:self.m + 1]:
        for elemento in self.A[1:]:
            imprime.append(elemento.id)
            imprime.append(str(elemento.prior).replace('.', ','))

        return " ".join(imprime)

    # corrige descendo
    def Max_Heapify(self, i):
        left_child_index = self.Left_Child(i)
        right_child_index = self.Right_Child(i)

        # finding largest among index, left child and right child
        largest = i

        if left_child_index <= self.m and left_child_index > 0:
            if self.A[left_child_index].prior > self.A[largest].prior:
                largest = left_child_index

        if right_child_index <= self.m and right_child_index > 0:
            if self.A[right_child_index].prior > self.A[largest].prior:
                largest = right_child_index

        # largest is not the node, node is not a heap
        if (largest != i):
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.Max_Heapify(largest)

    # function to get right child of a node of a tree
    def Right_Child(self, index):
        if((((2*index)+1) < len(self.A)) and (index >= 1)):
            return (2*index)+1
        return -1

    # function to get left child of a node of a tree
    def Left_Child(self, index):
        if(((2*index) < len(self.A)) and (index >= 1)):
            return 2*index
        return -1

    # function to get the parent of a node of a tree
    def Get_Parent(self, index):
        if ((index > 1) and (index < len(self.A))):
            return index//2
        return -1

    # corrige subindo
    def Heap_Increase_Key(self, index):
        parent_index = self.Get_Parent(index)
        if index >=2 and self.A[index].prior > self.A[parent_index].prior:
            parent_element = self.A[parent_index]
            self.A[parent_index] = self.A[index]
            self.A[index] = parent_element
            self.Heap_Increase_Key(parent_index)


class MAIN:
    def __init__(self):
        print("################################################")
        print("# Entrada: ")
        fila = FILADEPRIORIDADE([], 4000)
        
        Q = int(input())
        results = []
        # preenche bloco de teste
        while Q > 0:
            entrada = input()

            # devolve
            if entrada == '1':
                results.append(fila.Heap_Max())
            # remove
            elif entrada == '2':
                results.append(fila.Heap_Extract_Max())
            # imprime
            elif entrada == '4':
                results.append(fila.Heap_Print())
            else:
                numeros = entrada.split(" ")
                # insere
                if len(numeros) == 3 and numeros[0] == '3':
                    id = numeros[1]
                    prior = float(numeros[2].replace(',', '.'))
                    elemento = ELEMENTO(id, prior)
                    results.append(fila.Heap_Insert(elemento))

            Q -= 1
        
        print("################################################")
        print("# Saída: ")
        for line in results:
            print(line)

MAIN()
