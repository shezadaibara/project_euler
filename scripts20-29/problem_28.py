def sum_of_diagonal(N):
    ele = 1
    d = [ele,]
    total = ele
    layer = 1
    while ele < N*N:
        for x in range(0, 4):
            ele = ele + 2 * layer
            d.append(ele)
            total += ele
        layer += 1
    return total
