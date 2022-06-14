from node import Node

if __name__ == "__main__":
    buscar = "F"
    head = None
    for i in range(1, 5):
        head = Node(i, head)

    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next

    #buscar
    probe = head
    buscar = 2
    while probe != None and buscar != probe.data:
        probe = probe.next

    if probe != None:
        print(f" elemento {buscar} encontrado")

    #reemplazar
    probe = head
    reemplazar = 3
    nuevo_item = "z"

    while probe != None and reemplazar != probe.data:
        probe = probe.next

    if probe != None:
        probe.data = nuevo_item
        print(f" elemento {reemplazar} reemplazado por {nuevo_item}")

    #insertar nuevo nodo al inicio
    head = Node("F", head)

    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next

    #nuevo nodo al final

    nuevo_nodo = Node("K")

    if head is None:
        head = nuevo_nodo
    else:
        probe = head
        while probe.next != None:
            probe = probe.next
        probe.next = nuevo_nodo

    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next

    #eliminar nodo cabeza
    eliminar = head.data
    head = head.next
    print("///" + eliminar)

    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next
