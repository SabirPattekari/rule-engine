class Node:
    def _init_(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left
        self.right = right
        self.value = value  # Only used for operand nodes (e.g., age > 30)

def parse_rule(rule_string):
    """
    Parse the rule string and build the AST.
    Example: "age > 30 AND department = 'Sales'" is converted into an AST.
    """
    tokens = rule_string.replace("(", "").replace(")", "").split()  # Tokenize rule string
    stack = []

    for token in tokens:
        if token in ("AND", "OR"):
            right = stack.pop()
            left = stack.pop()
            stack.append(Node("operator", left, right, token))
        elif token.isdigit() or token.replace(".", "", 1).isdigit():
            # Operand node for numeric comparisons (age, salary, experience)
            stack.append(Node("operand", value=float(token)))
        elif token.isalpha():
            # Operand node for string-based conditions (department)
            stack.append(Node("operand", value=token))

    return stack.pop()  # Return root of the AST

def evaluate_node(node, data):
    """
    Recursively evaluate an AST node against the given data.
    Example: {"age": 35, "department": "Sales"} against a rule AST.
    """
    if node.node_type == "operand":
        return data.get(node.value, False)
    elif node.node_type == "operator":
        left_val = evaluate_node(node.left, data)
        right_val = evaluate_node(node.right, data)
        if node.value == "AND":
            return left_val and right_val
        elif node.value == "OR":
            return left_val or right_val
    return False