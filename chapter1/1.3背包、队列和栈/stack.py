"""
在stack栈数据结构中，数据像积木那样一层层堆起来，后面加入的数据就放在最上层。
使用的时候，最上层的数据第一个被用掉，这就叫做”后进先出”,英文叫LIFO 
ADT Stack:
    Stack(self)     # 创建空栈
    is_empty(self)  # 判断栈是否为空
    push(self, elem)    # 将元素elem加入栈
    pop(self)       # 删除栈中最后加入的元素并将其返回
    top(self)           # 取得栈中最后压入的元素，不删除
"""
class Stack():
    def __init__(self):
        self._elements = []
    
    def is_empty(self):
        if len(self._elements) == 0:
            return True
        return False

    def push(self, x):
        self._elements.append(x)

    def pop(self):
        if len(self._elements) != 0:
            self._elements.pop(-1)
    
    def top(self):
        return self._elements[-1]
    
    def __repr__(self):
        return "Stack(%s)" % self._elements

"""
用栈来实现算术表达式的求解
程序接受一个字符串输入表达式，输出结果

表达式由括号，运算符和操作数组成。按以下4中情况从左到右诸葛将这些实体送入栈处理：
1. 将操作数压入操作数栈
2. 将运算符压入运算符栈
3. 忽略左括号
4. 在遇到右括号时弹出一个运算符，弹出所需数量的操作数，并将运算符和操作数的结果压入操作数栈
"""
class Evaluate():
    def __init__(self, x):
        if not isinstance(x, str):
            raise Exception("input must be a string")
        self.x = x
    
    def eval(self):
        operator_stack =Stack()
        number_stack = Stack()
        operator = ["+", "-", "*", "/", "(", ")"]
        i = 0
        while i < len(self.x):
            if self.x[i] in operator:
                if self.x[i] == "(":
                    i += 1
                elif self.x[i] == ")":
                    num1 = number_stack.top()
                    number_stack.pop()
                    num2 = number_stack.top()
                    number_stack.pop()
                    opear = operator_stack.top()
                    operator_stack.pop
                    number_stack.push(str(eval(num1+opear+num2)))
                    i += 1
                else:
                    operator_stack.push(self.x[i])
                    i += 1
            else:
                j = i + 1
                while self.x[j] not in operator:
                    j += 1
                number_stack.push(self.x[i:j])
                i = j
        return int(number_stack.top())


if __name__ == "__main__":
    a = Evaluate("(1+((2+3)*(4*5)))")
    print(a.eval())