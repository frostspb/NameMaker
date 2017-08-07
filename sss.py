import itertools
import numpy as np
matrix = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3']]
#matrix = [['r0c0', 'r1c0', 'r2c0', 'r3c0', 'r4c0', 'r5c0', 'r6c0', 'r7c0', 'r8c0', 'r9c0'], ['r0c1', 'r1c1', 'r2c1', 'r3c1', 'r4c1', 'r5c1', 'r6c1', 'r7c1', 'r8c1', 'r9c1'], ['r0c2', 'r1c2', 'r2c2', 'r3c2', 'r4c2', 'r5c2', 'r6c2', 'r7c2', 'r8c2', 'r9c2'], ['r0c3', 'r1c3', 'r2c3', 'r3c3', 'r4c3', 'r5c3', 'r6c3', 'r7c3', 'r8c3', 'r9c3'], ['r0c4', 'r1c4', 'r2c4', 'r3c4', 'r4c4', 'r5c4', 'r6c4', 'r7c4', 'r8c4', 'r9c4'], ['r0c5', 'r1c5', 'r2c5', 'r3c5', 'r4c5', 'r5c5', 'r6c5', 'r7c5', 'r8c5', 'r9c5'], ['r0c6', 'r1c6', 'r2c6', 'r3c6', 'r4c6', 'r5c6', 'r6c6', 'r7c6', 'r8c6', 'r9c6'], ['r0c7', 'r1c7', 'r2c7', 'r3c7', 'r4c7', 'r5c7', 'r6c7', 'r7c7', 'r8c7', 'r9c7'], ['r0c8', 'r1c8', 'r2c8', 'r3c8', 'r4c8', 'r5c8', 'r6c8', 'r7c8', 'r8c8', 'r9c8'], ['r0c9', 'r1c9', 'r2c9', 'r3c9', 'r4c9', 'r5c9', 'r6c9', 'r7c9', 'r8c9', 'r9c9']]
#matrix = [['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']          ]
#matrix = [["A1","A2","A3","D1","G1","H1","F1","S1","X1","V1"],["B1","B2","B3","D2","G2","H2","F2","S2","X2","V2"],["C1","C2","C3","D3","G3","H3","F3","S3","X3","V3"]]@


#matrix = [ ('G0', 'G1', 'G2'), ('F0', 'F1', 'F2'), ('E0', 'E1', 'E2'), ('D0', 'D1', 'D2'), ('C0', 'C1', 'C2'), ('B0', 'B1', 'B2'), ('A0', 'A1', 'A2')]
permut_iter = itertools.product(*matrix)
permut_result = (itertools.islice((list((''.join(x),) + x) for x in permut_iter), 5))

permut_iter_l = itertools.product(*matrix)
permut_result_l = (itertools.islice((list(x) for x in permut_iter), 5))
#print(permut_result)
prl = list(permut_result)
#prl_l = list(permut_result_l)
#print(prl)
#import sys
#print(sys.getsizeof([]))

#print(sys.getsizeof(prl))
#print (prl_l)
#print(sys.getsizeof(prl_l))
print (prl)
import xlsxwriter

# Start from the first cell. Rows and columns are zero indexed.


# Iterate over the data and write it out row by row.


import os
print ((os.path.dirname(os.path.abspath(__file__))))
