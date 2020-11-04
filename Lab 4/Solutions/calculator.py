# parsuj(ciąg znaków):
#     idź po znakach
#     jeśli " " pomiń
#     jeśli cyfra dodaj do stosu nodeów node bez dzieci
#     jeśli nawias otwarty dodaj do stosu opertatorów
#     jeśli nawias zamknięty:
#         dopóki nie znajdziesz nawiasu otwierającego weź operator ze stosu operatorów:
#             dodaj_node(stos nodeów, operator)
#             obsłuż error jeśli nie znalazłeś nawiasu otwierającego
#     jeśli operator:
#         dopóki jest jakiś oprator na stosie operatorów:
#             jeśli operator ze stosu jest równy lub ważniejszy od aktualnego:
#                 weź ten operator (wyjmij ze stosu)
#                 dodaj_node(stos nodeów, ten operator)
#         dodaj operator do stosu operatorów
#
#     dopóki stos operatorów nie jest pusty weź operator ze stosu operatorów:
#         dodaj_node(stos nodeów, operator)
#
#     zwróć ostatni element ze stosu nodeów // który będzie rootem drzewa

OPERATORS = ["+", "-", "*", "/"]

def precedence(operator):
    if operator in ["+", "-"]:
        return 1
    elif operator in ["*", "/"]:
        return 2

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def description(self, reverse = True):
        left = self.left.description() if isinstance(self.left, Node) else ""
        right = self.right.description() if isinstance(self.right, Node) else ""

        return f"{left}{right}{self.value}" if reverse else f"{self.value}{left}{right}"

    def evaluate(self):
        if self.value.isnumeric():
            return int(self.value)
        elif self.value == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == "-":
            return self.left.evaluate() - self.right.evaluate()
        elif self.value == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.value == "/":
            return self.left.evaluate() / self.right.evaluate()

def add_node(stack, operator):
    right = stack.pop()
    left = stack.pop()
    print(f"{left.value} {operator} {right.value}")
    stack.append(Node(operator, left, right))

def build_tree(expression):
    tree = []
    operatorStack = []

    for character in expression:
        if character == " ":
            # print("spacja")
            continue
        elif character.isnumeric():
            # print(f"liczba {character}")
            tree.append(Node(character))
        elif character == "(":
            # print("nawias otwarty")
            operatorStack.append(character)
        elif character == ")":
            # print("nawias zamknięty")
            while operatorStack:
                operator = operatorStack.pop()
                if operator != "(":
                    add_node(tree, operator)
                else:
                    break
        elif character in OPERATORS:
            # print(f"operator {character}")
            while operatorStack:
                nextOperator = operatorStack[-1]
                if nextOperator in OPERATORS and precedence(nextOperator) >= precedence(character):
                    add_node(tree, operatorStack.pop())
                else:
                    break
            operatorStack.append(character)

    while operatorStack:
        add_node(tree, operatorStack.pop())

    return tree.pop()

while True:
    expression = input("Expression: ")
    if expression == "exit":
        break
    else:
        root = build_tree(expression)
        print(root.evaluate())
        print(root.description())
