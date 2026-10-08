
def winner(names: list[str], scores: list[float]) -> str:
    max_i = 0
    for i in range(len(scores)):
        if scores[i] > scores[max_i]:
            max_i = i
    return names[max_i]

def average(scores: list[float]) -> float:
    l_sum = sum(scores)
    if len(scores) > 0:
        return round(l_sum / len(scores), 2)
    else: return None

def above_average(names: list[str], scores: list[float]) -> list[str]:
    ans = []
    for i in range(len(names)):
        if scores[i] > average(scores):
            ans.append(names[i])
    return ans