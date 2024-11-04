class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Lista:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(",".join(map(str, elements)))

    def remove(self, value):
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print(f"Value {value} not found in the list.")

def main():
    Nowa_Lista = Lista()
    Nowa_Lista.add(10)
    Nowa_Lista.add(20)
    Nowa_Lista.add(30)
    Nowa_Lista.remove(20)
    Nowa_Lista.display()
if __name__ == "__main__":
    main()