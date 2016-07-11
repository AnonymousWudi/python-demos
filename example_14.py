# coding=utf-8


class ListNode():

    def __init__(self, value):
        self.value = value
        self.node_next = None


if __name__ == '__main__':
    numbers = int(raw_input())
    if numbers == 1:
        print raw_input()

    value = int(raw_input())
    head = ListNode(value)
    numbers -= 1
    while numbers:
        value = int(raw_input())
        temp_node = ListNode(value)
        temp_head = head
        temp = head
        while temp_head:
            if temp_node.value < temp_head.value:
                temp_node.node_next = temp_head
                break
            elif temp_node.value == temp_head.value:
                break
            elif temp_head.node_next and temp_head.value < temp_node.value < temp_head.node_next.value:
                temp_node.node_next = temp_head.node_next
                temp_head.node_next = temp_node
                break
            elif temp_head.node_next and temp_node.value > temp_head.value:
                temp_head = temp_head.node_next
            elif not temp_head.node_next and temp_node.value > temp_head.value:
                temp_head.node_next = temp_node
                break
        numbers -= 1
    while head:
        print head.value
        head = head.node_next
