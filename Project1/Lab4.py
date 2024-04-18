class Gift(object):
    def __init__(self, length=0, width=0, height=0):
        self.width = width
        self.height = height
        self.length = length

    def wrapping_paper(self):
        sides = [
            self.width * self.length, self.height * self.length,
            self.width * self.height
        ]
        minimal = min(sides)
        return sum(sides) * 2 + minimal

    def wrapping_ribbon(self):
        sides = [self.width, self.height, self.length]
        sides.sort()
        return (sides[0] +
                sides[1]) * 2 + self.width * self.length * self.height

    def __str__(self):
        return f"{self.length}x{self.width}x{self.height}"


def read_gifts(file):
    # Using readlines()
    input_txt = open(file, 'r')
    Lines = input_txt.readlines()

    input_txt.close()
    gifts = []
    # Strips the newline character
    for line in Lines:
        sizes = line.split('x')
        gifts.append(Gift(int(sizes[0]), int(sizes[1]), int(sizes[2])))

    return gifts


def write_gifts(file, array):
    # Using readlines()
    output_txt = open(file, 'w')

    output_txt.writelines(array)

    output_txt.close()


def to_fstring(gift):
    return f"{gift}\n"


def to_string(gift):
    return f"{gift}"


gifts_array = read_gifts('input.txt')
result = list(map(to_fstring, gifts_array))
terminal_result = list(map(to_string, gifts_array))
print(terminal_result)
write_gifts('output.txt', result)



# Скидывали на занятии с Гита
#*****************************************************************************************
''' Èòåðàòîð. Äëÿ ýòîãî íóæíî íàïèñàòü êëàññ è ðåàëèçîâàòü ìåòîäû __iter__() è __next__(). Ïîñëå ýòîãî òðåáóåòñÿ íàñòðîèòü âíóòðåííèå ñîñòîÿíèÿ è âûçûâàòü èñêëþ÷åíèå StopIteration, êîãäà áîëüøå íå÷åãî âîçâðàùàòü.
class TribonacciGenerator:
    def __init__(self, limit):
        self.prev_prev = 0
        self.prev = 1
        self.cur = 1
        self.limit = limit
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.limit:
            result = self.prev_prev
            self.prev_prev, self.prev, self.cur = self.prev, self.cur, self.prev + self.cur + self.prev_prev
            self.i += 1
            return result
        else:
            raise StopIteration
for i in TribonacciGenerator(35):
    print(i)
'''


# Ãåíåðàòîð - ìåñòî return èñïîëüçóåòñÿ èíñòðóêöèÿ yield. Îíà óâåäîìëÿåò èíòåðïðåòàòîð Python î òîì, ÷òî ýòî ãåíåðàòîð, è âîçâðàùàåò èòåðàòîð.

def tribonacciGenerator(limit):
    prev_prev = 0
    prev = 1
    cur = 1
    count = 0

    while count < limit:
        result = prev_prev
        prev_prev, prev, cur = prev, cur, prev + cur + prev_prev
        count += 1
        yield result


for item in tribonacciGenerator(35):
    print(item)