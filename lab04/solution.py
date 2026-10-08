
def winner(names: list[str], scores: list[float]) -> str:
    max_i = 0
    for i in range(len(scores)):
        if scores[i] > scores[max_i]:
            max_i = i
    return names[max_i]
