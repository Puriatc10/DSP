import re
import math

DYADIC_OPERATIONS = ['+', '-', '*', '/']

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def calculate_postfix(self):

        if self is not None and self.value in DYADIC_OPERATIONS:
            if self.left is not None and self.right is not None:
                p = f'{self.left.calculate_postfix()} {self.value} {self.right.calculate_postfix()}'
                return eval(p)
        else:
            return self.value

    def calculate_infix(self):
        if self.value in DYADIC_OPERATIONS:
            return eval(f'{self.right.calculate_infix()} {self.value} {self.left.calculate_infix()}')
        else:
            return self.value

    def set_input(self, input_var):
        if self.value in input_var.keys():
            self.value = input_var[self.value]
        if self.right is not None:
            self.right.set_input(input_var)
        if self.left is not None:
            self.left.set_input(input_var)

class Math_Equation_Tree:
    def __init__(self, expressions):
        self.expressions = self.clean_expression(expressions)
        self.roots = {}
        self.construct_tree()

    def clean_expression(self, expressions):
        exps = []
        for exp in expressions:
            exp = re.sub(r'([+\-*/^()])', r' \1 ', exp)
            cleaned_expression = ' '.join(exp.split())
            exps.append(cleaned_expression)
        return exps

        ''' Infix expression: The expression of the form "a operator b" (a + b) i.e., when an operator is in-between every pair of operands.
            Postfix expression: The expression of the form "a b operator" (ab+) i.e., When every pair of operands is followed by an operator.
            Defining the priority of operators:
            The priority of each operator is specified.
            Using a stack (stack):
            The stack is used to store operators and manage their priority.
            The infix phrase from left to right:
            If the operand is (a number or a variable), it is added to the output.
            If it is an operation or parentheses, it is added to the stack or output based on priority and specific conditions.
            Move the rest of the operators from the stack to the output:
            Finally, all remaining operators on the stack are added to the output.
            Use Shunting Yard Algorithm algorithm
        '''

    def construct_tree(self):
        for exp in self.expressions:
            postfix_expression = self._infix_to_postfix(exp)
            self.roots[exp] = self._build_tree_from_postfix(postfix_expression)

    def _infix_to_postfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = []
        operators = []

        def greater_precedence(op1, op2):
            return precedence[op1] > precedence[op2]

        tokens = expression.split()
        for token in tokens:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()
            else:
                while (operators and operators[-1] != '(' and
                       (greater_precedence(operators[-1], token) or
                        precedence[operators[-1]] == precedence[token])):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output

    def _build_tree_from_postfix(self, postfix_expression):
        stack = []
        for token in postfix_expression:
            if token.isalnum():
                stack.append(TreeNode(token))
            else:
                right_node = stack.pop()
                left_node = stack.pop()
                root_node = TreeNode(token)
                root_node.left = left_node
                root_node.right = right_node
                left_node.parent = root_node
                right_node.parent = root_node
                stack.append(root_node)
        return stack[0]




def calculate_postfix(math_tree, input_var):
    for exp in math_tree.expressions:
        math_tree.roots[exp].set_input(input_var)
        print(math_tree.roots[exp].calculate_postfix())

def print_tree(node, level=0, prefix="R:   "):
    if node is not None:
        print_tree(node.right, level + 1, "   -> ")
        print(' ' * 5 * level + prefix + str(node.value))
        print_tree(node.left, level + 1, "   -> ")

def print_formal_tree(node):
    q = [(node, 1)]
    current_level = 1
    while q:
        u, level = q.pop()
        if level > current_level:
            current_level = level
            print()
        print(u.value, end='\t')
        if u.left is not None:
            q.append((u.left, level + 1))
        if u.right is not None:
            q.append((u.right, level + 1))
    print()


expressions = ["(x + 5) * y - 8",
               "x + y",
               "y + 3"]
math_tree = Math_Equation_Tree(expressions)
for exp in math_tree.expressions:
    print_tree(math_tree.roots[exp])
    print('##########')
calculate_postfix( math_tree, {'x': 5, 'y': 4})
