# from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Node
# from pathfinding.finder.a_star import AStarFinder
#
# matrix = [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 1, 1]
# ]
# grid = Grid(matrix=matrix)
#
# start = grid.node(0, 0)
# end = grid.node(2, 2)
#
# finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
# path, runs = finder.find_path(start, end, grid)
#
# print('operations:', runs, 'path length:', len(path))
# print(grid.grid_str(path=path, xsstart=start, end=end))

from map import Map

# test = '''####################
# ##_____T____##___###
# ####___X_#_______###
# ######_T_##______###
# #___TXTT~~##__++__##
# #___T_#~~~~##+++++_#
# ____T_#~~~~~#++++___
# #______~~~~##+++___#
# #_______~~#________#
# ___HHHH*HH*HHHHH*___
# ###__________#######'''


m = Map(open('1_victoria_lake.txt','r'))
for c in m.customers:
    print(c.location, c.reward)
