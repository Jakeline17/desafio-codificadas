import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    sizes = list(map(int, input().split()))

    waiting = set()      
    next_needed = n       
    
    for day in range(n):
        lanche = sizes[day]
        waiting.add(lanche)
        
        placed = [] 
        while next_needed in waiting:
            placed.append(next_needed)
            waiting.remove(next_needed)
            next_needed -= 1
        
        if placed:
            print(*placed)
        else:
            print()

solve()