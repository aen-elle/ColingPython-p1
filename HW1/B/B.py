def solution(n):
    part_1 = "   _~_   "
    part_2 = "  (o o)  "
    part_3 = " /  V  \ "
    part_4 = "/(  _  )\\"
    part_5 = "  ^^ ^^  " 
    output = part_1 * n + '\n' + part_2 * n + '\n' + part_3 * n + '\n' + part_4 * n + '\n' + part_5 * n
    return output if n >0 else ""

print(solution(3))