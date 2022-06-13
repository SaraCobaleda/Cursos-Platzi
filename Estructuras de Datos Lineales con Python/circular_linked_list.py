from node import Node

if __name__ == '__main__':
    #el ultimo nodo en la lista apunta al primero
    index = 1
    new_item = 'ham'
    head = Node('hola', None)
    head.next = head
    probe = head
    while index > 0 and probe.next != head:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)
    print(probe.next.data)

    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next