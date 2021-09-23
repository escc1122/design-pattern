# Interpreter Pattern with Python Code
# https://www.runoob.com/design-pattern/interpreter-pattern.html
# 目前想不透這個模式
from abc import abstractmethod, ABCMeta


# 创建一个表达式接口
class Expression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, inContext):
        pass


# 创建实现Expression接口的实体类
class TerminalExpression(Expression):
    _data = ""

    def __init__(self, inData):
        self._data = inData

    def interpret(self, inContext):
        if inContext.find(self._data) >= 0:
            return True
        return False


class OrExpression(Expression):
    _expr1 = None
    _expr2 = None

    def __init__(self, inExpr1, inExpr2):
        self._expr1 = inExpr1
        self._expr2 = inExpr2

    def interpret(self, inContext):
        return self._expr1.interpret(inContext) or self._expr2.interpret(inContext)


class AndExpression(Expression):
    _expr1 = None
    _expr2 = None

    def __init__(self, inExpr1, inExpr2):
        self._expr1 = inExpr1
        self._expr2 = inExpr2

    def interpret(self, inContext):
        return self._expr1.interpret(inContext) and self._expr2.interpret(inContext)


# 调用输出
if __name__ == '__main__':
    # 规则：Robert和John是男性    
    def getMaleExpression():
        robert = TerminalExpression("Robert")
        john = TerminalExpression("John")
        return OrExpression(robert, john)
        # 规则：Julie是一个已婚的女性


    def getMarriedWomanExpression():
        julie = TerminalExpression("Julie")
        married = TerminalExpression("Married")
        return AndExpression(julie, married)


    isMale = getMaleExpression()
    isMarriedWoman = getMarriedWomanExpression()
    print("John is male? " + str(isMale.interpret("John")))
    print("Julie is a married women? " + str(isMarriedWoman.interpret("Married Julie")))
