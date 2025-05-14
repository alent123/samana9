class GenericTreeNode:  # Clase para representar un nodo del árbol
    def __init__(self, value):  # Constructor con valor
        self.value = value       # Guarda el valor del nodo
        self.children = []       # Inicializa la lista de hijos vacía

class GenericTree:  # Clase para representar un árbol genérico
    def __init__(self, root=None):  # Constructor con nodo raíz opcional
        self.root = root  # Asigna el nodo raíz

    def find_leaves(self):  # Método para encontrar todas las hojas
        def _collect_leaves(node):  # Función recursiva interna
            if node is None: return []  # Si el nodo es nulo, retornamos lista vacía
            if not node.children: return [node.value]  # Si no tiene hijos, es hoja
            leaves = []  # Lista para almacenar las hojas encontradas
            for child in node.children: leaves.extend(_collect_leaves(child))  # Recorremos hijos
            return leaves  # Retornamos la lista completa de hojas

        return _collect_leaves(self.root)  # Llamamos desde la raíz del árbol

# --- TEST CASE EXPLICADO ---
root = GenericTreeNode('A')  # Nodo raíz
b = GenericTreeNode('B')     # Nodo B
c = GenericTreeNode('C')     # Nodo C
d = GenericTreeNode('D')     # Nodo D
e = GenericTreeNode('E')     # Hijo de B
f = GenericTreeNode('F')     # Hijo de B

root.children = [b, c, d]    # A tiene 3 hijos
b.children = [e, f]          # B tiene 2 hijos

tree = GenericTree(root)  # Creamos el árbol
print("Hojas del árbol:", tree.find_leaves())  # Esperamos: ['C', 'E', 'F', 'D']
