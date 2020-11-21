class ListNode:
     def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
      
class Solution:
               
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        integerL1 = ""
        integerL2 = ""
        curL1 = l1
        curL2 = l2
        while curL1 is not None or curL2 is not None:
            if curL1 is not None:
                integerL1 += str(curL1.val)
                curL1 = curL1.next
            if curL2 is not None:
                integerL2 += str(curL2.val)
                curL2 = curL2.next
        integerL1 = integerL1[::-1]
        integerL2 = integerL2[::-1]
        integerL1 = int(integerL1)
        integerL2 = int(integerL2)
        combine = integerL1 + integerL2
        combine = str(combine)
        combine = combine[::-1]
        main = l1
        headOne = True
        for i in range(len(combine)):
            if headOne:
                l1 = ListNode(int(combine[i]))
                main = l1
                headOne = False
                continue
            if main.next is None:
                main.next = ListNode(int(combine[i]))
                main = main.next

        return l1
    def printlist(self, node: ListNode):
        print(node.val)
        while node.next is not None :
            node = node.next
            print(node.val)
       
    
list1 = ListNode(2);
list1.next = ListNode(4)
list1.next.next = ListNode(3)
list2 = ListNode(5);
list2.next = ListNode(6)
list2.next.next = ListNode(4) 
s = Solution()  
merge = s.addTwoNumbers(list1, list2)
s.printlist(merge)





    
    
