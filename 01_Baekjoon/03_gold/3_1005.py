# ACM CRAFT
import time

start_time = time.time()
from queue import Queue
import sys


def bfs():
    _total_time = [0] * N
    _total_time[start] = time[start]
    _graph_cnt = graph_cnt[:]

    _queue = Queue()
    _queue.put(start)
    while not _queue.empty():
        _cur = _queue.get()
        _graph_cnt[_cur] -= 1
        # print(_cur, _total_time)

        for _idx in range(len(graph[_cur])):
            # 들어오는 화살표가 여러개일 경우를 대비
            # 앞으로 방문할 지점이 가지고있는 총 시간, 현재 지점의 총 시간 + 앞으로 방문할 지점의 건설시간
            _total_time[graph[_cur][_idx]] = max(_total_time[graph[_cur][_idx]],
                                                     _total_time[_cur] + time[graph[_cur][_idx]])
            _queue.put(graph[_cur][_idx])
    # 한번도 방문하지 않았을 경우를 대비
    return str(max(time[goal], _total_time[goal]))



for tc in range(int(sys.stdin.readline())):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(N)]
    graph_cnt = [0] * N
    for i in range(K):
        st, ed = map(int, sys.stdin.readline().split())
        graph[st - 1].append(ed - 1)
        graph_cnt[ed - 1] += 1
    print(graph)
    # 들어오는 화살표가 하나도 없는 지점이 시작점
    start = graph_cnt.index(0)
    goal = int(sys.stdin.readline()) - 1
    sys.stdout.write(bfs() + "\n")



# def topology_sort():
#     _queue = Queue()
#     _topology_list = []
#     _graph_cnt = graph_cnt[:]
#     _queue.put(start)
#     _critical_time = [0] * N
#     _previous_task = [False] * N
#     while not _queue.empty():
#         _cur = _queue.get()
#         print(_cur)
#         _critical_time[_cur] += time[_cur]
#         _topology_list.append(_cur)
#
#         for _idx in range(len(graph[_cur])):
#             temp = graph[_cur][_idx]
#             _graph_cnt[temp] -= 1
#             _critical_time[temp] = max(_critical_time[temp], _critical_time[_cur])
#             _previous_task[temp] = _cur
#             if _graph_cnt[temp] == 0:
#                 _queue.put(temp + 1)
#
#     print(_critical_time)
