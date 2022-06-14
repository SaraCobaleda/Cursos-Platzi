from double_linked_list import Node, TwoWayNode

if __name__ == '__main__':
    head = TwoWayNode(0, None, None)
    tail = head
    #head.next = head
    #tail.previous = tail
    for data in range (6):
        head.next = TwoWayNode(data, head)
        head = head.next
        tail = head.previous
    probe = tail
    while probe != None:
        print(probe.data)
        probe = probe.previous