"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
source: https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None


import heapq
import itertools


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists1(self, lists):
        counter = itertools.count()
        result = []
        temp_node = None
        target_node = None
        node = None
        for item in lists:
            if item:
                heapq.heappush(result, (item.val, counter.next(), item))
        head = current = ListNode(0)
        while result:
            val, count, node  = heapq.heappop(result)
            next_node = node.next
            if next_node:
                 heapq.heappush(result, (next_node.val, counter.next(), next_node))
            current.next = node
            current = current.next
        return head.next

    def mergeKLists2(self, lists):
        def list2iter(L):
            p = L
            while p:
                yield p.val, p
            p = p.next

        def iter2list(it):
             head = p = ListNode(0)
             for val, node in it:
                  p.next = node
                  p = p.next
             return head.next
       its = [list2iter(i) for i in lists]
       it = heapq.merge(*its)
       return iter2list(it)

    def mergeKLists3(self, lists):
        if not lists:
            return None

        h = []
        for i in range(len(lists)):
            l = lists[i]
            while l:
                heapq.heappush(h, l.val)
                l = l.next

        if not h:
            return None

        head = ListNode(-1)
        head.next = None
        cur = head

        v = [heapq.heappop(h) for i in range(len(h))]
        for i in v:
            t = ListNode(i)

            cur.next = t
            cur = cur.next

        return head.next

    def mergeKLists4(self, lists):
        h = []
        for i in lists:
            if i:
                h.append([i.val, i])

        heapq.heapify(h)

        dummy_head = pos = ListNode(0)

        while h:
            _value, top = h[0]
            if top.next:
                heapq.heapreplace(h, [top.next.val, top.next])
            else:
                heapq.heappop(h)

            pos.next = top
            pos = pos.next

        return dummy_head.next
