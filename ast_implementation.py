class Integer():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_type(self):
        return "int"

    def __str__(self):
        return f"Integer(name=\"{self.name}\", value=\"{self.value}\")"
    
    def eval(self):
        return int(self.value)


class Float():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_type(self):
        return "float"

    def __str__(self):
        return f"Float(name=\"{self.name}\", value=\"{self.value}\")"

    def eval(self):
        return float(self.value)


class Void():
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_type(self):
        return "void"

    def __str__(self):
        return f"Void(name=\"{self.name}\", value=\"{self.value}\")"

    def eval(self):
        return None


class BinaryOperation():
    def __init__(self, left_operand, right_operand):
        self.left_operand = left_operand
        self.right_operand = right_operand


class Sum(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"Sum(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() + self.right_operand.eval()


class Substraction(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"Substraction(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() - self.right_operand.eval()


class Multiplication(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"Multiplication(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() * self.right_operand.eval()


class Division(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"Division(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() / self.right_operand.eval()


class LessThan(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"LessThan(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() < self.right_operand.eval()


class LessThanOrEqual(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"LessThanOrEqual(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() <= self.right_operand.eval()


class GreaterThan(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"GreaterThan(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() > self.right_operand.eval()


class GreaterThanOrEqual(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"GreaterThanOrEqual(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() >= self.right_operand.eval()


class Equality(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"Equality(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() == self.right_operand.eval()


class Inequality(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"Inequality(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() != self.right_operand.eval()

class AndLogical(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"AndLogical(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() and self.right_operand.eval()
    
class OrLogical(BinaryOperation):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand)

    def __str__(self):
        return f"OrLogical(left_operand=\"{self.left_operand}\", right_operand=\"{self.right_operand}\")"

    def eval(self):
        return self.left_operand.eval() or self.right_operand.eval()


class FunctionDefinition:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def __str__(self):
        params_str = ', '.join(self.params) if self.params else ''
        return f"FunctionDefinition(name={self.name}, params=[{params_str}], body={self.body})"

    def execute(self, environment):
        return self.body.execute(environment)


class Print():
    def __init__(self, value):
        self.value = value
	
	# def eval(self):
	# 	print(self.value.eval())

class IfElseStatement():
    def __init__(self, condition, if_body, else_body=None):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

    def __str__(self):
        if self.else_body is not None:
            return f"IfElseStatement(condition={self.condition}, if_body={self.if_body}, else_body={self.else_body})"
        else:
            return f"IfElseStatement(condition={self.condition}, if_body={self.if_body})"
