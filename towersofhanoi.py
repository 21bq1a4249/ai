def towers_of_hanoi(numbers,b,m,e):
    if(numbers==1):
        print('move disk1 from pole{} to pole{}'.format(b,e))
        return
    towers_of_hanoi(numbers-1,b,e,m)
    print('move disk1{} from pole{} to pole{}'.format(numbers,b,e))
    towers_of_hanoi(numbers-1,m,b,e)
numbers=3
towers_of_hanoi(numbers,'A','B','C')