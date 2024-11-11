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
# Start Code
TransactionManager.Instance.EnsureInTransaction(doc)

Ceilings = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Ceilings)
    .WhereElementIsElementType()
    .ToElements()
)


CompoundCeilings = filter(
    lambda ceiling: str(ceiling.GetCompoundStructure())
    == "Autodesk.Revit.DB.CompoundStructure",
    Ceilings,
)


BasicCeilings = filter(
    lambda ceiling: str(ceiling.GetCompoundStructure()) == "None", Ceilings
)
TransactionManager.Instance.TransactionTaskDone()
######################################################
# Output
OUT = CompoundCeilings, BasicCeilings
