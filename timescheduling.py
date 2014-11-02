timeSchedulingProblem
=====================

import collections
import bisect
import time
from datetime import datetime

"""
Weighted Interval scheduling algorithm.
Runtime complexity: O(n log n)
"""

class Interval(object):
    '''Date weighted interval'''

    def __init__(self, title, start, finish):
        self.title = title
        self.start = start
        self.finish = finish
        #self.start = int(time.mktime(datetime.strptime(start, "%I:%M %p").timetuple()))
        #self.finish = int(time.mktime(datetime.strptime(finish, "%I:%M %p").timetuple()))
        self.weight = self.finish - self.start

    def __repr__(self):
        return str((self.title, self.start, self.finish, self.weight))


def compute_previous_intervals(I):
    '''For every interval j, compute the rightmost mutually compatible interval i, where i < j
       I is a sorted list of Interval objects (sorted by finish time)
    '''
    # extract start and finish times
    start = [i.start for i in I]
    finish = [i.finish for i in I]

    p = []
    for j in xrange(len(I)):
        i = bisect.bisect_right(finish, start[j]) - 1  # rightmost interval f_i <= s_j
        p.append(i)

    return p

def schedule_weighted_intervals(I):
    '''Use dynamic algorithm to schedule weighted intervals
       sorting is O(n log n),
       finding p[1..n] is O(n log n),
       finding OPT[1..n] is O(n),
       selecting is O(n)
       whole operation is dominated by O(n log n)
    '''

    I.sort(lambda x, y: x.finish - y.finish)  # f_1 <= f_2 <= .. <= f_n
    p = compute_previous_intervals(I)

    # compute OPTs iteratively in O(n), here we use DP
    OPT = collections.defaultdict(int)
    OPT[-1] = 0
    OPT[0] = 0
    for j in xrange(1, len(I)):
        OPT[j] = max(I[j].weight + OPT[p[j]], OPT[j - 1])

    # given OPT and p, find actual solution intervals in O(n)
    O = []
    def compute_solution(j):
        if j >= 0:  # will halt on OPT[-1]
            if I[j].weight + OPT[p[j]] > OPT[j - 1]:
                O.append(I[j])
                compute_solution(p[j])
            else:
                compute_solution(j - 1)
    compute_solution(len(I) - 1)

    # resort, as our O is in reverse order (OPTIONAL)
    O.sort(lambda x, y: x.finish - y.finish)

    return O

if __name__ == '__main__':
    I = []
    I.append(Interval("Summer School" , 1, 6))
    I.append(Interval("Semester 1" , 8, 12))
    I.append(Interval("Semester 2" , 13, 15))
    I.append(Interval("Trimester 1" , 17, 23))
    I.append(Interval("Trimester 2" , 1, 8))
    I.append(Interval("Trimester 3" , 11, 22))
    O = schedule_weighted_intervals(I)
    print O
