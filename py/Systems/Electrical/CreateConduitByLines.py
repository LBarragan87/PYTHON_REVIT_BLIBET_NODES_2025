import System
import clr

# import DSCoreNodes
clr.AddReference("DSCoreNodes")
from DSCore import *

# Import ProtoGeometry
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

# Import RevitNodes
clr.AddReference("RevitNodes")
from Revit import *
import Revit

# Import Revit elements
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from Revit.Elements import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
import Autodesk.Revit.DB.Electrical

# Import DocumentManager
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


# functions
def makeList(elements):
    NewList = []
    if isinstance(elements, list):
        NewList = elements
    else:
        NewList.append(elements)
    return NewList


# Get Document
doc = DocumentManager.Instance.CurrentDBDocument
######################################################
# Inputs

conduit_type_id = UnwrapElement(IN[0])[0].Id
Level_id = UnwrapElement(IN[1]).Id
start_point = UnwrapElement(IN[2])
end_point = UnwrapElement(IN[3])
middle_elevation = UnwrapElement(IN[4])


######################################################
# Start Code
TransactionManager.Instance.EnsureInTransaction(doc)

conduits = []
index = 0
for point in start_point:
    sp = start_point[index]
    ep = end_point[index]
    create_conduit = Electrical.Conduit.Create(doc, conduit_type_id, sp, ep)
    conduits.append(create_conduit)
    index += 1
TransactionManager.Instance.TransactionTaskDone()
######################################################
# Output
OUT = ConduitWithFittingTypes, ConduitWithOutFittingTypes
