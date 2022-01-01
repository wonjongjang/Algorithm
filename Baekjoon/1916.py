import sys
sys.stdin = open('input.txt')
import heapq


N = int(input())    # 도시 개수
M = int(input())    # 버스 개수

v = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, d = map(int, input().split())
    v[s].append([e, d])

A, B = map(int, input().split())

dist = [99999999 for _ in range(N+1)]    # 1

que = []
heapq.heappush(que, [0, A])
dist[A] = 0     # 2

while que:
    d, loc = heapq.heappop(que)

    if loc == B:                # 도착 지점이면
        print(d)
        break

    if dist[loc] < d:           # d가 dist에 저장된 값보다 크면 (최소 비용이기 때문)
        continue                # 다음으로

    for i in v[loc]:            # 3
        nd = d + i[1]
        if dist[i[0]] > nd:     # 4
            dist[i[0]] = nd
            heapq.heappush(que, [nd, i[0]])     # 5