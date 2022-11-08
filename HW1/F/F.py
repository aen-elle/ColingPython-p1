def solution(n):
    power_of_two = 1
    output = []
    while n >= power_of_two:
        output.append(power_of_two)
        power_of_two = power_of_two * 2
    return output