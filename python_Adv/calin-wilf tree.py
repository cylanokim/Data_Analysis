"""  
In number theory, the Calkkin-Wilf tree is a tree in which the vertices correspond 
one-to-one to the positive rational numbers. Every positive rational number appears
exactly once in the tree.
"""

def calkin_wilf(A):
    a = 1 
    b = 1
    for i in A:
        if i == 'L':
            b += a 
        if i == 'R':
            a += b  
    return (a, b)

T = int(input())

for test_case in range(1, T+1):
    Nodes = [i for i in input()]

    a, b = calkin_wilf(Nodes)

    print(f'#{test_case} {a} {b}')

T = int(input())

for test_case in range(1, T+1):
    Nodes = [i for i in input()]
    a, b = 1,1 
    for i in Nodes:
        if i == 'L':
            b += a 
        else:
            a += b  
    print(f'#{test_case} {a} {b}')

