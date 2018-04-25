from collections import namedtuple
Item = namedtuple('item', 'name price stock')
L = [Item('pears', 2.50, 20),
 Item('plums', 3.25, 40),
 Item('oranges', 3.00, 35),
 Item('peaches', 2.50, 40) ]
def get_Stock(I:Item) -> int:
    return I.stock
L.sort()
print(L)
