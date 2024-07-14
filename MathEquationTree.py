class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Math_Equation_Tree:
    def __init__(self, expression):
    def __init__(self, expression):
        self.expression = expression
        self.root = None
        self.Create_Tree()

    def Create_Tree(self):
        postfix_expression = self.infix_to_postfix(self.expression)
        self.root = self.Build_Tree(postfix_expression)

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




    def infix_to_postfix(self, expression): #Larger numbers assigned have higher priority in performing operations
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = []
        operators = []

        def greater_precedence(op1, op2): #This section of code ensures that the operators are processed in the correct order according to their priorities
            return precedence[op1] > precedence[op2]

        tokens = expression.split()
        for token in tokens:
            if token.isnumeric():  # if token is an operand
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':  #Inside the while loop, the operators are removed from the stack and added to the output list.
                    output.append(operators.pop())
                operators.pop()  # pop '('
            else:
                while (operators and operators[-1] != '(' and
                       greater_precedence(operators[-1], token)): #This function (greater_precedence) compares precedence and returns True if the operator has greater or equal precedence on the stack.
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output

    def Build_Tree(self, postfix_expression):
        stack = []
        for token in postfix_expression:
            if token.isnumeric():
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
        return stack[0]  # the root of the tree

