from collections import deque

if __name__ == '__main__':
    linked_list = deque()
    n = int(input())
    for _ in range(n):
        args = input().split(' ')
        if args[0] == 'insert':
            linked_list.appendleft(int(args[1]))
        elif args[0] == 'delete':
            if int(args[1]) in linked_list:
                linked_list.remove(int(args[1]))
        elif args[0] == 'deleteFirst':
            linked_list.popleft()
        elif args[0] == 'deleteLast':
            linked_list.pop()
    print(*linked_list)