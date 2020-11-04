from tokenizer import sanitize_expression, parse, Token
from visualizer import printContents

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

    def list(self):
        list = [self.value]
        if isinstance(self.left, Node):
            list.append(self.left.list())
        if isinstance(self.right, Node):
            list.append(self.right.list())

        return list

    def evaluate(self):
        try:
            value = float(self.value)
            return value
        except:
            l = float(self.left.evaluate())
            r = float(self.right.evaluate())
            if self.value == "+":
                return l + r
            elif self.value == "-":
                return l - r
            elif self.value == "*":
                return l * r
            elif self.value == "/":
                return l / r

def add_node(stack, operator):
    right = stack.pop()
    left = stack.pop()
    stack.append(Node(operator, left, right))

def build_tree(expression):
    tree = []
    operatorStack = []

    for (token, character) in parse(expression):
        if token is Token.NUMBER:
            tree.append(Node(character))
        elif token is Token.OPEN_BRACKET:
            operatorStack.append(character)
        elif token is Token.CLOSE_BRACKET:
            while operatorStack:
                operator = operatorStack.pop()
                if operator != "(":
                    add_node(tree, operator)
                else:
                    break
        elif token is Token.OPERATOR:
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
    expression = sanitize_expression(input("Expression: "))

    if expression == "exit":
        break
    else:
        root = build_tree(expression)
        print(root.evaluate())
        print(root.description())
        print(root.list())
        printContents(root.list())
