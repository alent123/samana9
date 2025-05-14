

def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
    # Tu código aquí 🛠️
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = [] #lista donde  se almanecera el resultado 
    stack = [] #  pila donde se guardara los operadores 

    for token in tokens: # recorrido en cada  token 
        if token.isalnum():  ## isalnum() devuelve True si es letra o número
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] != '(' and # Mientras haya operadores en la pila con mayor o igual precedenci los sacamos al resultado
                   precedence.get(stack[-1], 0) >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)   # Luego ponemos el operador actual en la pila
        elif token == '(': # Si encontramos un paréntesis de apertura lo colocamos en la pila
            stack.append(token)
        elif token == ')':# Si encontramos un paréntesis de cierre
            while stack and stack[-1] != '(':  # Extraemos de la pila hasta encontrar el paréntesis de apertura
                output.append(stack.pop())
            stack.pop()  # Quitamos el paréntesis de apertura '('
    while stack:
        output.append(stack.pop())

    return output  # Retornamos la expresión

# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Output: 2 3 +
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # ➕ Simple operation

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Output: 2 3 4 * +
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # 📊 Precedence test

# Test 3: Parentheses override precedence
# Input: (2 + 3) * 4
# Output: 2 3 + 4 *
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # 🔗 Parentheses

# Test 4: Complex expression
# Input: (1 + 2) * (3 - 4)
# Output: 1 2 + 3 4 - *
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # 🧮 Complex

# Test 5: Multiple operators
# Input: a + b * c / d
# Output: a b c * d / +
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # 🔤 Variables
