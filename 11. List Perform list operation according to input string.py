DATA = []


def perform_operation(op_str):
    global DATA
    operation, *key = op_str.split(' ')
    params = tuple(map(int, key))
    if operation != "print":
        eval(f"DATA.{operation}{params}")
    elif operation == "print":
        eval("print(DATA)")


def call_operation(operation_list):
    for op in operation_list:
        perform_operation(op)


if __name__ == '__main__':
    operation_list = []
    N = int(input())
    
    for _ in range(N):
        operation_list.append(input())
    call_operation(operation_list)
