timeSchedulingProblem
=====================
import heapq

myHeap = []
#inerting data into heapq
def insertToHeap(rank,Data):
	heapq.heappush(myHeap, tuple([int("-"+str(rank)),Data]))


insertToHeap(30,'C001')
insertToHeap(50,'C001')
insertToHeap(40,'C001')
insertToHeap(80,'C001')
insertToHeap(60,'C001')
insertToHeap(10,'C001')
insertToHeap(90,'C001')

print heapq.heappop(myHeap)
print heapq.heappop(myHeap)
print heapq.heappop(myHeap)
print heapq.heappop(myHeap)
print heapq.heappop(myHeap)
print heapq.heappop(myHeap)
print heapq.heappop(myHeap)
