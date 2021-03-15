# A representation of a catan board
import networkx as nx
import numpy.random
import numpy as np

# Node 0 is the top node on the board

# Circular edges
Edges = [(i, j) for i, j in zip(range(30), list(range(1, 30)) + [0])]
Edges.extend([(i, j)
              for i, j in zip(range(30, 48), list(range(31, 48)) + [30])])
Edges.extend([(i, j)
              for i, j in zip(range(48, 54), list(range(49, 54)) + [48])])

# First radial edges
outer = 1
inner = 31
while(outer < 30):
    Edges.append((inner, outer))
    inner += 1
    outer += 3
    if not (outer < 30):
        break
    Edges.append((inner, outer))
    inner += 2
    outer += 2

# Second radial edges
inner = 48
outer = 30
while(outer < 48):
    Edges.append((inner, outer))
    inner += 1
    outer += 3

board = nx.Graph()
board.add_edges_from(Edges, owned_by=np.array([1, 0, 0, 0, 0]))
nx.draw(board)

ATTRIBUTES = {
    0: {'hexes': (0)},
    1: {'hexes': (0, 1)},
    2: {'hexes': (1)},
    3: {'hexes': (1)},
    4: {'hexes': (1, 2)},
    5: {'hexes': (2)},
    6: {'hexes': (2, 3)},
    7: {'hexes': (3)},
    8: {'hexes': (3)},
    9: {'hexes': (3, 4)},
    10: {'hexes': (4)},
    11: {'hexes': (4, 5)},
    12: {'hexes': (5)},
    13: {'hexes': (5)},
    14: {'hexes': (5, 6)},
    15: {'hexes': (6)},
    16: {'hexes': (6, 7)},
    17: {'hexes': (7)},
    18: {'hexes': (7)},
    19: {'hexes': (7, 8)},
    20: {'hexes': (8)},
    21: {'hexes': (8, 9)},
    22: {'hexes': (9)},
    23: {'hexes': (9)},
    24: {'hexes': (9, 10)},
    25: {'hexes': (10)},
    26: {'hexes': (10, 11)},
    27: {'hexes': (11)},
    28: {'hexes': (11)},
    29: {'hexes': (11, 0)},
    30: {'hexes': (0, 12, 13)},
    31: {'hexes': (0, 1, 13)},
    32: {'hexes': (1, 2, 13)},
    33: {'hexes': (2, 13, 14)},
    34: {'hexes': (2, 3, 14)},
    35: {'hexes': (3, 4, 14)},
    36: {'hexes': (4, 14, 15)},
    37: {'hexes': (4, 5, 15)},
    38: {'hexes': (5, 6, 15)},
    39: {'hexes': (6, 15, 16)},
    40: {'hexes': (6, 7, 16)},
    41: {'hexes': (7, 8, 16)},
    42: {'hexes': (8, 16, 17)},
    43: {'hexes': (8, 9, 17)},
    44: {'hexes': (9, 10, 17)},
    45: {'hexes': (10, 17, 12)},
    46: {'hexes': (10, 11, 12)},
    47: {'hexes': (11, 0, 12)},
    48: {'hexes': (12, 13, 18)},
    49: {'hexes': (13, 14, 18)},
    50: {'hexes': (14, 15, 18)},
    51: {'hexes': (15, 16, 18)},
    52: {'hexes': (16, 17, 18)},
    53: {'hexes': (17, 12, 18)}
}

hexes = {
    0: (0),
    1: (0, 1),
    2: (1),
    3: (1),
    4: (1, 2),
    5: (2),
    6: (2, 3),
    7: (3),
    8: (3),
    9: (3, 4),
    10: (4),
    11: (4, 5),
    12: (5),
    13: (5),
    14: (5, 6),
    15: (6),
    16: (6, 7),
    17: (7),
    18: (7),
    19: (7, 8),
    20: (8),
    21: (8, 9),
    22: (9),
    23: (9),
    24: (9, 10),
    25: (10),
    26: (10, 11),
    27: (11),
    28: (11),
    29: (11, 0),
    30: (0, 12, 13),
    31: (0, 1, 13),
    32: (1, 2, 13),
    33: (2, 13, 14),
    34: (2, 3, 14),
    35: (3, 4, 14),
    36: (4, 14, 15),
    37: (4, 5, 15),
    38: (5, 6, 15),
    39: (6, 15, 16),
    40: (6, 7, 16),
    41: (7, 8, 16),
    42: (8, 16, 17),
    43: (8, 9, 17),
    44: (9, 10, 17),
    45: (10, 17, 12),
    46: (10, 11, 12),
    47: (11, 0, 12),
    48: (12, 13, 18),
    49: (13, 14, 18),
    50: (14, 15, 18),
    51: (15, 16, 18),
    52: (16, 17, 18),
    53: (17, 12, 18)
}

n_resource_tiles = {
    'ore': 3,
    'brick': 3,
    'wood': 4,
    'wheat': 4,
    'sheep': 4,
    None: 1
}

PORTS = [
    '3f1',
    None,
    '3f1',
    '3f1',
    None,
    'brick',
    'brick',
    None,
    None,
    'wood',
    'wood',
    None,
    '3f1',
    '3f1',
    None,
    'wheat',
    'wheat',
    None,
    None,
    'ore',
    'ore',
    None,
    '3f1',
    '3f1',
    None,
    'sheep',
    'sheep',
    None,
    None,
    '3f1'
]

PORT_TILES = ['ore', 'brick', 'wood', 'wheat', 'sheep'] + ['3f1'] * 4

RESOURCE_TILES = []
for key, value in n_resource_tiles.items():
    RESOURCE_TILES.extend([key] * value)

TILE_NUMBERS = [
    5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11
]

nx.set_node_attributes(board, hexes)


class Board:
    def __init__(self):
        self.hex_resources = RESOURCE_TILES
        random.shuffle(self.hex_resources)

        tile_number_start = random.randint(6) * 2 + 1
        for i in range(12):
            self.hex_numbers.append(TILE_NUMBERS[(i - tile_number_start) % 12])
        for i in range(12, 19):
            self.hex_numbers.append(
                TILE_NUMBERS[(i - tile_number_start) % 6 + 12])
        self.hex_numbers.append(TILE_NUMBERS[-1])

        port_number_start = 5 * np.randint(6)
        ports = [PORTS[(i - port_number_start) % 30]] + [18] * None

        for port, i in enumerate(ports):
            ATTRIBUTES[i]['port'] = port

        for i in range(48):
            hex_numbers = hexes[i]
            node_hexes = [(self.hex_resources[n]: self.hex_numbers[n]) for n in hex_numbers]
            node_ports = ports[i]
            atts = {'hexes':}

    def allocate_resources(self):
        pass


board = Board()
print('hi')
