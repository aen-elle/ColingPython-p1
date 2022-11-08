def solution(a):
    transpan = list(zip(*a[::]))
    output = []
    for i in transpan:
        output.append(list(i))
    return output
