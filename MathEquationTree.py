import re


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Math_Equation_Tree:
    def __init__(self, expression):
        self.expression = self.clean_expression(expression)
        self.root = None
        self.construct_tree()

    def clean_expression(self, expression):
        expression = re.sub(r'([+\-*/^()])', r' \1 ', expression)
        return ' '.join(expression.split())

    def construct_tree(self):
        postfix_expression = self._infix_to_postfix(self.expression)
        self.root = self._build_tree_from_postfix(postfix_expression)

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
Use Shunting Yard Algorithm algorit

        '''

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


def print_tree(node, level=0, prefix="R:   "):
    if node is not None:
        print_tree(node.right, level + 1, "   -> ")
        print(' ' * 5 * level + prefix + str(node.value))
        print_tree(node.left, level + 1, "   -> ")


expression = "(x + 5) * 2 - 8"
math_tree = Math_Equation_Tree(expression)
print_tree(math_tree.root)
