class ExpressionNode:  # Clase para nodos del árbol de expresión
    def __init__(self, value):  # Constructor que recibe el valor del nodo
        self.value = value  # Asigna valor (operador, número o variable)
        self.left = None  # Inicializa el hijo izquierdo como None
        self.right = None  # Inicializa el hijo derecho como None

class ExpressionTree:  # Clase del árbol de expresión
    def __init__(self, root=None):  # Constructor que acepta nodo raíz opcional
        self.root = root  # Asigna el nodo raíz

    def simplify(self):  # Método para simplificar el árbol de expresión
        def _simplify(node):  # Función recursiva interna
            if node is None: return None  # Si el nodo es nulo, retornamos None
            node.left = _simplify(node.left)  # Simplificamos el subárbol izquierdo
            node.right = _simplify(node.right)  # Simplificamos el subárbol derecho

            if node.left and node.right:  # Si ambos hijos existen
                if node.left.value.isdigit() and node.right.value.isdigit():  # Y ambos son números
                    a = int(node.left.value)  # Convertimos el valor izquierdo a entero
                    b = int(node.right.value)  # Convertimos el valor derecho a entero
                    if node.value == '+': result = a + b  # Si el operador es suma
                    elif node.value == '-': result = a - b  # Si es resta
                    elif node.value == '*': result = a * b  # Si es multiplicación
                    elif node.value == '/': result = a // b  # Si es división, usamos entera
                    else: return node  # Si el operador no se reconoce, no se modifica
                    return ExpressionNode(str(result))  # Retornamos un nuevo nodo con el resultado

            return node  # Si no se pudo simplificar, retornamos el nodo original

        self.root = _simplify(self.root)  # Llamamos a simplificar desde la raíz
        
# Creamos el árbol de expresión: (2 + 3) * x

root = ExpressionNode('*')         # Nodo raíz con operador '*'
add = ExpressionNode('+')          # Nodo interno con operador '+'
add.left = ExpressionNode('2')     # Hijo izquierdo de '+' es 2
add.right = ExpressionNode('3')    # Hijo derecho de '+' es 3

root.left = add                    # Lado izquierdo de '*' es la suma (2 + 3)
root.right = ExpressionNode('x')   # Lado derecho de '*' es la variable x

tree = ExpressionTree(root)        # Construimos el árbol

tree.simplify()                    # Simplificamos: (2 + 3) = 5 → árbol se convierte en: 5 * x

# Imprimimos los valores
print("Valor raíz:", tree.root.value)        # Esperamos '*' (el operador principal)
print("Izquierdo:", tree.root.left.value)    # Esperamos '5' (resultado de 2 + 3)
print("Derecho:", tree.root.right.value)     # Esperamos 'x' (se mantiene porque es variable)
