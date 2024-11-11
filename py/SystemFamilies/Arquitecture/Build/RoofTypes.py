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


Roofs = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Roofs)
    .WhereElementIsElementType()
    .ToElements()
)


BasicRoofs = filter(
    lambda roof: str(roof.GetCompoundStructure())
    == "Autodesk.Revit.DB.CompoundStructure",
    Roofs,
)


SlopedGlazingRoofs = filter(
    lambda roof: str(roof.GetCompoundStructure()) == "None", Roofs
)


Fascias = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Fascia)
    .WhereElementIsElementType()
    .ToElements()
)


Gutters = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Gutter)
    .WhereElementIsElementType()
    .ToElements()
)


RoofSoffits = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_RoofSoffit)
    .WhereElementIsElementType()
    .ToElements()
)


TransactionManager.Instance.TransactionTaskDone()
######################################################
# Output
OUT = BasicRoofs, SlopedGlazingRoofs, Fascias, Gutters, RoofSoffits
