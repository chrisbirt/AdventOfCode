def eval_wire(signals, wires, wire, path=''):

    if wire in signals:
        return signals [wire]

    if wire.isdigit():
        signal = int(wire)
    else:
        cmd = wires[wire].split(' ')

        if len(cmd) == 1:
            signal = eval_wire(signals, wires, cmd[0])

        elif len(cmd) == 2:
            signal = ~eval_wire(signals, wires, cmd[1]) & 0xFFFF

        elif len(cmd) == 3:
            if cmd[1] == 'LSHIFT':
                signal = eval_wire(signals, wires, cmd[0], path) << int (cmd [2])
        
            elif cmd[1] == 'RSHIFT':
                signal = eval_wire(signals, wires, cmd[0], path) >> int (cmd [2])
        
            elif cmd[1] == 'AND':
                signal = eval_wire(signals, wires, cmd[0], path) & eval_wire(signals, wires, cmd[2], path)

            elif cmd[1] == 'OR':
                signal = eval_wire(signals, wires, cmd[0], path) | eval_wire(signals, wires, cmd[2], path)

    signals[wire] = signal
    return signal


def solve():

    p1, p2, day = 0, 0, 7

    with open('input07') as f:
        input = f.read().splitlines()

    rows = [row.split(' -> ') for row in input]
    wires = {row[-1]:row[0] for row in rows}

    signals = {}
    p1 = eval_wire(signals, wires, 'a')

    signals = {'b': p1}
    p2 = eval_wire(signals, wires, 'a')

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()