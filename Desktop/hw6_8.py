def C(m, n):
    result = 1
    x = y = 1
    min_num = min(n, m - n)
    for i in range(min_num):
        x *= (m - i)
        y *= (min_num - i)
        result = x // y
    
    return result
    
N = [25, 30, 35, 40]

for i in N:
    # prob = 1 - C(1126, N') / H(1126, N')
    prob = 1 - (C(1126, i) / C(1126 + i - 1, i))
    print("When N' = %d," %i, end = ' ')
    print("prob of getting at least one duplicated example is %.5f"
          %prob)
 

    
