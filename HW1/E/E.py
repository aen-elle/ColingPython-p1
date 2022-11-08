def solution(x1, y1, x2, y2):
    xaxis = abs(x1 - x2)
    yaxis= abs(y1 - y2)
    return False if xaxis > 1 or yaxis > 1 else True
