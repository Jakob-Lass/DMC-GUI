
## Definition of states:
#     EMPTY: No DataSet object present
#     RAW:   DataSet object but no DataFiles
#     FULL:  DataSet with DataFiles
from enum import Enum
class States(Enum):
    STARTUP = -1
    EMPTY = 0
    RAW = 1
    FULL = 2

import platform

if platform.system() == 'Windows':
    markerColor = 'lightblue'
else:
    markerColor = 'palette(Link)'

highlightStyle = "background-color: palette(Link); color: white"
normalStyle = "background-color: palette(midlight)"