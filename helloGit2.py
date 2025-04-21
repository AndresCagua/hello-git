 #print ("Hello Git 2")
from typing import List

def findMissingOperationIndex(ops: List[str], missingOp: str, currentTop: int) -> int:
    n = len(ops)

    # Intenta insertar la operación faltante en cada posición
    for i in range(n + 1):
        stack = []
        temp_ops = ops[:i] + [missingOp] + ops[i:]  # Inserta missingOp en la posición i

        valid = True
        for op in temp_ops:
            if op.startswith("PUSH"):
                _, x = op.split()
                stack.append(int(x))
            elif op == "POP":
                if not stack:
                    valid = False  # No se puede hacer POP con la pila vacía
                    break
                stack.pop()
        
        if valid and stack and stack[-1] == currentTop:
            return i

    return -1  # No se encontró una posición válida (esto no debería pasar según la consigna)

ops = ["PUSH 5", "POP", "PUSH 10"]
missingOp = "PUSH 7"
currentTop = 10

print(findMissingOperationIndex(ops, missingOp, currentTop))

findMissingOperationIndex(ops, missingOp, currentTop)
