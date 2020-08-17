if __name__ == '__main__':
    answer = []
    N = int(input())
    
    for i in range(N):
        task = input().split()

        if task[0] == 'append':
            answer.append(int(task[1]))
        elif task[0] == 'insert':
            answer.insert(int(task[1]), int(task[2]))
        elif task[0] == 'pop':
            answer.pop()
        elif task[0] == 'print':
            print(answer)
        elif task[0] == 'remove':
            answer.remove(int(task[1]))
        elif task[0] == 'reverse':
            answer.reverse()
        elif task[0] == 'sort':
            answer.sort()
            
