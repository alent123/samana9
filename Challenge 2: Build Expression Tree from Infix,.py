# Clase que representa un nodo en el árbol de expresiones
class ExpressionNode:
    def __init__(self, value):
        self.value = value  # Guarda el valor del nodo (puede ser operador o operando)
        self.left = None    # Referencia al hijo izquierdo (inicialmente vacío)
        self.right = None   # Referencia al hijo derecho (inicialmente vacío)


# Clase que representa un árbol de expresiones completo
class ExpressionTree:
    def __init__(self, root=None):
        self.root = root  # Guarda la raíz del árbol (puede ser None si está vacío)

    @classmethod
    def from_infix(cls, tokens):
        """Construye un árbol de expresión a partir de una lista de tokens en notación infija"""
        postfix = infix_to_postfix(tokens)  # Convertimos la expresión infija a notación postfija
        stack = []  # Pila para ir construyendo los nodos del árbol

        for token in postfix:  # Recorremos cada token en la expresión postfija
            node = ExpressionNode(token)  # Creamos un nodo con el valor del token actual
            if token in '+-*/':  # Si el token es un operador, necesita dos operandos
                node.right = stack.pop()  # Extraemos el nodo derecho desde la pila (último agregado)
                node.left = stack.pop()   # Extraemos el nodo izquierdo desde la pila (anterior)
            stack.append(node)  # Añadimos el nuevo nodo (operador o valor) a la pila

        return cls(stack[-1])  # El último nodo en la pila es la raíz del árbol completo


# ✅ TEST CASES
# Test 1: Expresión simple "2 + 3"
tree1 = ExpressionTree.from_infix(['2', '+', '3'])
# Se espera que la raíz sea '+' y sus hijos sean '2' y '3'
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')


# Test 2: Expresión con precedencia "2 + 3 * 4"
tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
# Se espera que la raíz sea '+' y el hijo derecho sea '*'
print(tree2.root.value == '+' and tree2.root.right.value == '*')


# Test 3: Paréntesis que alteran precedencia "(2 + 3) * 4"
tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
# Se espera que la raíz sea '*' y su hijo izquierdo sea '+'
print(tree3.root.value == '*' and tree3.root.left.value == '+')

# Test 4: Variables con operación "x + y * z"
tree4 = ExpressionTree.from_infix(['x', '+', 'y', '*', 'z'])
# Se espera que la raíz sea '+' y el hijo derecho sea '*'
print(tree4.root.value == '+' and tree4.root.right.value == '*')

# Test 5: División entre expresiones con paréntesis "(a + b) / (c - d)"
tree5 = ExpressionTree.from_infix(['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'])
# Se espera que la raíz sea '/', hijo izquierdo '+', hijo derecho '-'
print(tree5.root.value == '/' and tree5.root.left.value == '+' and tree5.root.right.value == '-')

