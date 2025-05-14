class GenericTreeNode:  # Clase para representar un nodo del árbol genérico
    def __init__(self, value):  # Constructor que recibe el valor del nodo
        self.value = value  # Guarda el valor del nodo
        self.children = []  # Inicializa la lista de hijos como vacía

class GenericTree:  # Clase para representar un árbol genérico
    def __init__(self, root=None):  # Constructor que puede recibir el nodo raíz
        self.root = root  # Asigna el nodo raíz al árbol

    def height(self):  # Método para calcular la altura del árbol
        def _height(node):  # Función recursiva interna
            if node is None: return -1  # Si el nodo es nulo, retornamos -1 por convención (árbol vacío)
            if not node.children: return 0  # Si no tiene hijos, es una hoja, altura 0
            child_heights = [_height(child) for child in node.children]  # Calculamos la altura de cada hijo
            return 1 + max(child_heights)  # La altura es 1 + la máxima altura de los hijos

        return _height(self.root)  # Llamamos la función desde la raíz del árbol
    
# Creamos los nodos del árbol
root = GenericTreeNode('A')  # Nodo raíz A
b = GenericTreeNode('B')     # Nodo B, hijo de A
c = GenericTreeNode('C')     # Nodo C, hijo de B
d = GenericTreeNode('D')     # Nodo D, hijo de C

# Enlazamos los nodos en forma lineal: A → B → C → D
root.children = [b]          # A tiene un hijo: B
b.children = [c]             # B tiene un hijo: C
c.children = [d]             # C tiene un hijo: D

# Creamos el árbol con raíz A
tree = GenericTree(root)

# Calculamos e imprimimos la altura del árbol
print("Altura del árbol:", tree.height())  # Esperamos 3 porque hay 3 conexiones: A-B-C-D
