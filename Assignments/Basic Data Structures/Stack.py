

class Stack():
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return self.items == []


    def push(self, data):
        self.items.append(data)


    def pop(self):
        return self.items.pop()


    def peek(self):
        self.items[len(self.items) - 1]


    def size(self):
        return len(self.items)


# uses a stack to reverse the characters in a string
def revstring(mystr):
    stack = Stack()
    for c in mystr:
        stack.push(c)

    str = ""
    while not stack.isEmpty():
        str += stack.pop()

    return  str


# Simple Balanced Parentheses
def parChecker1(symbolstring):
    s = Stack()
    balanced = True
    index = 0

    while index<len(symbolstring) and balanced:
        symbol = symbolstring[index]

        if symbol == '(':
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


# Balanced Symbols(A General Case)
def parChecker2(symbolstring):
    s = Stack()
    balanced = True
    index = 0

    while index<len(symbolstring) and balanced:
        symbol = symbolstring[index]

        if symbol in '([{':
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def main():
    s = Stack()

    print(s.isEmpty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

    # exercise
    print revstring("apple")

    # Simple Balanced Parentheses
    print (parChecker1('((()))'))
    print (parChecker1('(()'))

    # Balanced Symbols(A General Case)
    print(parChecker2('{{([][])}()}'))
    print(parChecker2('[{()]'))


if __name__ == "__main__":
    main()

