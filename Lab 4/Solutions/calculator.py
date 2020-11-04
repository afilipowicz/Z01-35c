
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
    stack.append(Node(operator, left, right))

def build_tree(expression):
    tree = []
    operatorStack = []

    for character in expression:
        if character == " ":
            continue
        elif character.isnumeric():
            tree.append(Node(character))
        elif character == "(":
            operatorStack.append(character)
        elif character == ")":
            while operatorStack:
                operator = operatorStack.pop()
                if operator != "(":
                    add_node(tree, operator)
                else:
                    break
        elif character in OPERATORS:
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
