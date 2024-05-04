n = int(input())
def tribonacci(n):
    tri = [0,0,1]

    if n == 0:
        return [0]
    if n == 1:
        return 0
    if n == 2:
        return 1

    else:
        for i in range(n):
                new_element = tri[-1] + tri[-2]+ tri[-3]
                tri.append(new_element)

        return tri[-1]

print(tribonacci(n)) 

