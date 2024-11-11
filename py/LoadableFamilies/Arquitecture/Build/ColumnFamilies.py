# imports
from RevitServices.Transactions import TransactionManager
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import *
import Autodesk
from Revit.Elements import *
import Revit
from Revit import *
from Autodesk.DesignScript.Geometry import *
from DSCore import *
import System
import clr
clr.AddReference('DSCoreNodes')
clr.AddReference('ProtoGeometry')
clr.AddReference("RevitNodes")
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitAPI")
clr.AddReference("RevitServices")
# Get Document
doc = DocumentManager.Instance.CurrentDBDocument
######################################################
# Inputs
columns_collector = FilteredElementCollector(doc).OfCategory(
    BuiltInCategory.OST_Columns).WhereElementIsElementType().ToElements()


structural_columns_collector = FilteredElementCollector(doc).OfCategory(
    BuiltInCategory.OST_StructuralColumns).WhereElementIsElementType().ToElements()
######################################################
# Start Code
TransactionManager.Instance.EnsureInTransaction(doc)
column_families = []
column_family_names = []
for column in columns_collector:
    this_column = column.Family
    if this_column.Name not in column_family_names:
        column_family_names.append(this_column.Name)
        column_families.append(this_column)
family_structural_columns = []
family_structural_column_names = []
for structural_column in structural_columns_collector:
    thisStructuralColumn = structural_column.Family
    if thisStructuralColumn.Name not in family_structural_column_names:
        family_structural_column_names.append(thisStructuralColumn.Name)
        family_structural_columns.append(thisStructuralColumn)
TransactionManager.Instance.TransactionTaskDone()


######################################################
# Output
OUT = column_families, family_structural_columns
