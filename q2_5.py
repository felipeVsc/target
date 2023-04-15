entrada = input("Qual palavra deseja inverter? ")

class Stack:

    def __init__(self):
        self.stack = []

    def push(self,n):
        self.stack.append(n)
    
    def pop(self):
        return self.stack.pop()

def creatingStack(entrada):
    st = Stack()

    for letra in entrada:
        st.push(letra)

    return st

def reversingString(st):
    reversedString = ""
    for x in range(len(entrada)):
        reversedString+=st.pop()

    return reversedString

print(f"Resultado: {reversingString(creatingStack(entrada))}")