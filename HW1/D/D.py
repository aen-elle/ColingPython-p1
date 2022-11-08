def solution(total):
    hours = total // 60
    if hours > 23:
        hours = hours % 24
    minutes = total % 60
    return str(hours) + ' ' + str(minutes)
