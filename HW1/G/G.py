def solution(a, b):
    output = []
    for i in a:
        output.append(i)
    for i in b:
        if i not in a:
            output.append(i)
    return sorted(output)
