from collections import defaultdict, Counter

def sort_string(text):
    cnt = Counter(text)
    sorted_cnt = reversed(list(cnt.most_common(len(cnt))))
    result = ''
    for i in sorted_cnt:
        result = result + (i[0] * i[1])
    print(result)
        

    