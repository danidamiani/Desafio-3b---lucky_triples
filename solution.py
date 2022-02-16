def solution(l):
    qt = len(l)
    multiplos = [0] * qt
    for i in range(qt):
        for j in range(i+1, qt):
            if l[j] % l[i] == 0:
                multiplos[i] += 1
    luckyOnes = 0
    for i in range(qt):
        for j in range(i+1, qt):
            if l[j] % l[i] == 0:
                luckyOnes += multiplos[j]
    return luckyOnes
