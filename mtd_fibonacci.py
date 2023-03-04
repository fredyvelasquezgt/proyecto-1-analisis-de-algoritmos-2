import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def mtd_fibonacci(n):
    start_time = time.time()
    
    state = 'q0'
    tape = ['B'] * (n+2)
    tape[1] = '1'
    head_pos = 1
    count = 1
    
    while state != 'qf':
        print(state + ': ' + ' '.join(tape[:head_pos]) + ' [' + tape[head_pos] + '] ' + ' '.join(tape[head_pos+1:]))
        
        if state == 'q0':
            state = 'q1'
        
        elif state == 'q1':
            if tape[head_pos] == 'B':
                state = 'qf'
            else:
                tape[head_pos+1] = '1'
                head_pos += 1
                count += 1
                if count == n:
                    state = 'qf'
                else:
                    state = 'q2'
        
        elif state == 'q2':
            if tape[head_pos] == 'B':
                state = 'qf'
            else:
                tape[head_pos-1] = '1'
                head_pos -= 1
                count += 1
                if count == n:
                    state = 'qf'
                else:
                    state = 'q3'
        
        elif state == 'q3':
            if tape[head_pos] == 'B':
                state = 'qf'
            else:
                tape[head_pos] = 'B'
                head_pos += 1
                count += 1
                if count == n:
                    state = 'qf'
                else:
                    state = 'q4'
        
        elif state == 'q4':
            if tape[head_pos] == 'B':
                state = 'qf'
            else:
                tape[head_pos-1] = 'B'
                head_pos -= 1
                count += 1
                if count == n:
                    state = 'qf'
                else:
                    state = 'q1'
    
    end_time = time.time()
    print('Elapsed time:', end_time - start_time)
    
    fib = fibonacci(n)
    print('El', n, 'ésimo número de la secuencia de Fibonacci es:', fib)
    
    values_on_tape = [x for x in tape if x != 'B']
    print('Valores finales en la cinta:', values_on_tape)

n = int(input('Ingrese un número para calcular el número correspondiente en la secuencia de Fibonacci: '))
mtd_fibonacci(n)
