

import Ex6



# Press the green button in the gutter to run the script.
import math

if __name__ == '__main__':

    cycle1 = [[0, 0.38, 0.0, 0],
             [0.38, 0, 1.0, 0],
             [0.0, 1.0, 0, 2],
              [0.0, 0, 2, 0]]

    cycle2 = [[0, 2, 0, 0],
              [0, 0, 3, 0],
              [0, 0, 0, 4],
              [1, 0, 0, 0]]

    cycle3 = [[0, 2, 0, 0],
              [0, 0, 0.38, 0],
              [0, 0, 0, 1],
              [0, 1, 0, 0]]

    d = Ex6.build_digraph_logarithm(cycle3)

    Ex6.find_cycle(d,0)
    #print(d.edges.data())
   # print(math.log(0.38, 2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
