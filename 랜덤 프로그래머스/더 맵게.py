import heapq
heap = []
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    for i in range(len(scoville)-1):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville) * 2
        heapq.heappush(scoville, (first + second))
        answer += 1
        if all(i >= K for i in scoville):
            break
    if all(i < K for i in scoville):
        return -1

    return answer