import Kolejka
from sys import exit, stdin

if __name__ == "__main__":

    Data = int(input())
    Kolejka = Kolejka.Kolejka()
    counter = 0

    for line in stdin:
        counter += 1 
        if counter >=  Data:
            break
        spliter = line.split()
        command = spliter[0]
        toDo = spliter[1:]
        try:
            toDo = [int(x) for x in toDo]
        except ValueError:
            exit('Złe dane')

        if  command == 'insert':
            print('dziala')
            Kolejka.insert(toDo[0], toDo[1])

        elif command == 'empty':
            print('1' if Kolejka.is_empty() else '0')

        elif command == 'top':
            if Kolejka.is_empty():
                print()
            else:
                print(Kolejka.top().key)

        elif command == 'pop':
            if Kolejka.is_empty():
                print()
            else:
                print(Kolejka.pop().key)

        elif command == 'priority':
            Kolejka.priority(toDo[0], toDo[1])

        elif command == 'print':
            for node in Kolejka.heap():
                print('(' + str(node.key) + ', '+ str(node.priority) + ')')