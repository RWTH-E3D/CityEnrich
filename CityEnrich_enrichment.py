# import of libraries
from PySide2 import QtWidgets, QtGui
import os
import pandas as pd
import math
import lxml.etree as ET
import uuid

# import of functions
import gui_functions as gf
import CityEnrich_selection as sel
import twod_operations as twod


def checkIfStringIsNumber(self, string, t=float):
    """checks if string can be converted to a number"""
    try:
        t(string)
        return True
    except:
        msg = 'Unable to safe! "' + string + '" is not a valid input.'
        gf.messageBox(self, 'ERROR', msg)
        return False


def onSave(self):
    """to self user entered building parameters"""
    # get index of comboBox
    if self.cB_curBuilding.currentIndex() != 0:
        index = getIndexFromBuildingDict(self, self.cB_curBuilding.currentText())
    else:
        index = -1
    # gather all data
    params = {}

    # buildingHeight
    if self.txtB_buildingHeight.text() != '' and checkIfStringIsNumber(self, self.txtB_buildingHeight.text()):
        params["bHeight"] = float(self.txtB_buildingHeight.text())
    else:
        params["bHeight"] = None

    # roofHeight
    if self.txtB_roofHeight.text() != '':
        # check if statement ist valid formula
        text = self.txtB_roofHeight.text()
        if '/' in text:
            splits = text.split('/')
            if len(splits) == 2 and splits[0] == "bHeight":
                pass
            else:
                print("wrong formatting of formula")
        elif '*' in text:
            splits = text.split('*')
            if len(splits) == 2 and "bHeight" in splits:
                pass
            else:
                print("wrong formatting of formula")
        elif checkIfStringIsNumber(self, self.txtB_roofHeight.text()):
            params["rHeight"] = float(self.txtB_roofHeight.text())

    else:
        params["rHeight"] = None

    # roofType
    if self.cB_roofType.currentIndex() != 0:
        params["rType"] = self.cB_roofType.currentText()[-4:]
        if params["rHeight"] == 0 and params["rType"] != "1000":
            print(params["rType"])
            print(type(params["rType"]))
            gf.messageBox(self, "Warning", "Roof height can only be 0m when selecting a flat roof")
    else:
        params["rType"] = None

    # roofHeading
    if self.cB_heading.currentIndex() != 0:
        params["rHeading"] = self.cB_heading.currentText()
    else:
        params["rHeading"] = None

    # buildingFunction
    if self.cB_buildingFunction.currentIndex() != 0:
        params["bFunction"] = self.cB_buildingFunction.currentText()[-4:]
    else:
        params["bFunction"] = None

    # YOC
    if self.txtB_yearOfConstruction.text() != '':
        params["YOC"] = self.txtB_yearOfConstruction.text()
    else:
        params["YOC"] = None

    # SAG
    if self.txtB_SAG.text() != '' and checkIfStringIsNumber(self, self.txtB_SAG.text(), int):
        params["SAG"] = int(self.txtB_SAG.text())
    else:
        params["SAG"] = None

    # SBG
    if self.txtB_SBG.text() != '' and checkIfStringIsNumber(self, self.txtB_SBG.text(), int):
        params["SBG"] = int(self.txtB_SBG.text())
    else:
        params["SBG"] = None

    if self.overWriteFlag == True:
        self.buildingOverWrDict[index] = params
    else:
        self.buildingParamsDict[index] = params


def select_expPath(self):
    """func to select folder"""
    path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
    if path:
        self.expPath = path
        self.txtB_outDir.setText(self.expPath)
    else:
        gf.messageBox(self, "Important", "Valid Exportfolder not selected")

def getIndexFromBuildingDict(self, buildingname):
    """gets the index of the building within the buildingDict"""
    for key in self.buildingDict:
        if buildingname.split("/")[1] == self.buildingDict[key]["buildingname"]:
            return key


def getNewTree(self, filename):
    """reads file again to get a new modifiable tree"""
    # parsing file
    parser = ET.XMLParser(remove_blank_text=True)
    ntree = ET.parse(os.path.join(self.inpDir, filename), parser)
    nroot_E = ntree.getroot()
    nnss = nroot_E.nsmap

    # get envelope elements
    envelope_E = nroot_E.find('./gml:boundedBy/gml:Envelope', nnss)
    nLcorner_E = envelope_E.find('gml:lowerCorner', nnss)
    nUcorner_E = envelope_E.find('gml:upperCorner', nnss)

    description_LDT_E = nroot_E.find('gml:description', nnss)
    if description_LDT_E != None:
        if 'transformed using the RWTH e3d City-LDT' not in description_LDT_E.text:
            description_LDT_E.text += "\n                       transfromed using the RWTH e3d City-LDT"
        else:
            # transformed description is already present in element
            pass

    else:
        description_E = ET.SubElement(nroot_E, ET.QName(nnss["gml"], 'description'), nsmap={'gml': nnss["gml"]}, )
        description_E.text = 'created using the e3D CityLDT'
        nroot_E.insert(0, description_E)

    return nroot_E, nnss, nLcorner_E, nUcorner_E, [math.inf, math.inf, math.inf], [-math.inf, -math.inf, -math.inf]


def setBuildingElements(building_E, nss, df):
    """sets some of the default elements"""

    # sBOrder list contains elements in the desired order. running the loop will add their last index if present to the dict, allowing other elements to be appended in the right place
    sBOrder = {'gml:description': -1, 'gml:name': -1, 'core:creationDate': -1, "core:externalReference": -1,
               'core:relativeToTerrain': -1, 'gen:measureAttribute': -1, 'gen:stringAttribute': -1, 'bldg:class': -1,
               'bldg:function': -1, 'bldg:usage': -1, 'bldg:yearOfConstruction': -1, 'bldg:roofType': -1,
               'bldg:measuredHeight': -1, 'bldg:storeysAboveGround': -1, 'bldg:storeysBelowGround': -1,
               'bldg:lod0FootPrint': -1, 'bldg:lod0RoofEdge': -1, 'bldg:lod1Solid': -1, 'bldg:lod2Solid': -1,
               'bldg:boundedBy': -1, 'bldg:lod1TerrainIntersection': -1, 'bldg:lod2TerrainIntersection': -1,
               "bldg:address": -1}
    for tag in sBOrder:
        target = building_E.findall(tag, nss)
        if target != []:
            index = building_E.index(target[-1])
            sBOrder[tag] = index

    # running through all optional elements and adding if necessary
    prefix = "bldg"
    for tagName, dfName in [["function", "function"], ["yearOfConstruction", "YOC"], ["roofType", "roofType"],
                            ["measuredHeight", "buildingHeight"], ["storeysAboveGround", "SAG"],
                            ["storeysBelowGround", "SBG"]]:
        preTag = prefix + ":" + tagName

        found = False
        insertIndex = 0
        for tag in sBOrder:
            if tag == preTag:
                found = True
                sBOrder[tag] = insertIndex + 1
                continue
            if not found:
                if sBOrder[tag] != -1 and sBOrder[tag] > insertIndex:
                    insertIndex = sBOrder[tag]
            else:
                if sBOrder[tag] != -1:
                    sBOrder[tag] -= - 1

        dfValue = df.iloc[0][dfName]
        if (dfValue != None) and (not pd.isna(dfValue)):
            check = building_E.find(preTag, nss)
            if dfName == "SAG" or dfName == "SBG":
                try:
                    dfValue = int(dfValue)
                except:
                    print("ERROR converting value of", tagName, " (", dfValue, ") to int.")
            if check != None:
                check.text = str(dfValue)
            else:
                new_E = ET.Element(ET.QName(nss[prefix], tagName))
                new_E.text = str(dfValue)
                building_E.insert(insertIndex + 1, new_E)


def copyTerrainIntersection(searchElement, nss):
    """copies an existing terrain intersection to the new building model"""
    lod1Intersection_E = searchElement.find('bldg:lod1TerrainIntersection', nss)
    if lod1Intersection_E != None:
        lod1Intersection_E.tag = ET.QName(nss["bldg"], "lod2TerrainIntersection")
        return

    lod2Intersection_E = searchElement.find('bldg:lod2TerrainIntersection', nss)
    if lod2Intersection_E != None:
        lod2Intersection_E.tag = ET.QName(nss["bldg"], "lod1TerrainIntersection")
        return


def getInfoForLoD1(df, searchElement, nss):
    """gathers all required info for LoD1 model creation"""
    # getting building height
    try:
        bHeight = df.iloc[0]['buildingHeight']
    except:
        measuredHeight_E = searchElement.find('bldg:measuredHeight', nss)
        if measuredHeight_E != None:
            bHeight = float(measuredHeight_E.text)
        else:
            print("Error finding building height")

    return bHeight


def getInfoForLoD2(df, searchElement, nss):
    """gathers all required info for LoD2 model creation"""
    # getting building height
    bHeight = getInfoForLoD1(df, searchElement, nss)

    # getting roof height
    rHeight = df.iloc[0]['roofHeight']

    # getting roof type
    rType_E = searchElement.find('bldg:roofType', nss)
    if rType_E != None:
        rType = rType_E.text
    else:
        rType = df.iloc[0]['roofType']

    rHeading = df.iloc[0]['roofHeading']

    return bHeight, rHeight, rType, rHeading


def writeTree(self, rootElement, nss, lcorner, ucorner, minimum, maximum, baseName, exportName):
    """writes tree to file and updates bounding box"""
    lcorner.text = ' '.join(map(str, minimum))
    ucorner.text = ' '.join(map(str, maximum))

    name_E = rootElement.find('gml:name', nss)
    if name_E != None:
        if name_E.text == baseName:
            name_E.text = exportName.split(".gml")[0]


    if os.path.isdir(self.expPath):
        pass
    else:
        os.mkdir(self.expPath)
    tree = ET.ElementTree(rootElement)
    tree.write(os.path.join(self.expPath, exportName), pretty_print = True, xml_declaration=True,
                encoding='utf-8', standalone='yes', method="xml")
    toFZKViewer = True
    if toFZKViewer:
        fullFilename = os.path.join(self.expPath, exportName)
        with open(fullFilename, 'r') as f:
            content = f.read()
        content = content.replace('http://www.opengis.net/citygml/1.0', 'http://www.opengis.net/citygml/2.0')
        with open(fullFilename, 'w') as f:
            f.write(content)


def EnrichmentStart(self, selAll):
    """starting the Enrichment Process"""

    # get data
    dataForFrame = []
    for index in self.buildingDict:
        splits = self.buildingDict[index]["buildingname"].split('/')
        if len(splits) > 1:
            bpname = splits[1]
        else:
            bpname = ''
        row = [self.buildingDict[index]["filename"], splits[0], bpname, self.buildingDict[index]["selected"]]
        sets = self.buildingDict[index]["values"]
        row.append(sets["LoD"])

        # checks which data is present with highest priority on file, then individual building save, then all building save
        for i in ['bHeight', 'rHeight', 'rType', 'rHeading', 'bFunction', 'YOC', 'SAG', 'SBG']:
            if (index in self.buildingOverWrDict) and (self.buildingOverWrDict[index][i] != None):
                print("buildingwise")
                print(self.buildingOverWrDict[index][i])
                row.append(self.buildingOverWrDict[index][i])
            elif (self.buildingOverWrDict[-1][i] != None):
                print("all building over")
                print(self.buildingOverWrDict[-1][i])
                print(type(self.buildingOverWrDict[-1][i]))
                row.append(self.buildingOverWrDict[-1][i])
            elif sets[i] != 'N/D':
                # if already set by building
                row.append(sets[i])
            elif (index in self.buildingParamsDict) and (self.buildingParamsDict[index][i] != None):
                # set by building on individual building
                row.append(self.buildingParamsDict[index][i])
            else:
                # set as default for all buildings
                row.append(self.buildingParamsDict[-1][i])

            # overwrite for rHeading
            if i == 'rHeading':
                if sets[i] != 'N/D':
                    if (index in self.buildingParamsDict) and (self.buildingParamsDict[index][i] != None):
                        # from individual building
                        row[-1] = self.buildingParamsDict[index][i]
                    else:
                        # from all buildings default
                        row[-1] = self.buildingParamsDict[-1][i]

        dataForFrame.append(row)

    df = pd.DataFrame(dataForFrame,
                      columns=['filename', 'buildingID', 'bpID', 'selected', 'LoD', 'buildingHeight', 'roofHeight',
                               'roofType', 'roofHeading', 'function', 'YOC', 'SAG', 'SBG'])
    # only consider buildings which are not in the target LoD
    # df = df.loc[df['LoD'] != targetLoD]
    # print('df after LoD clearing')
    if df.empty:
        msg = 'No buildings to transform'
        gf.messageBox(self, 'Error', msg)
        return

    if not selAll:
        df = df.loc[df["selected"] == True]
    else:
        # all files and buildings
        pass

    """for catching missing data"""
    # dfProblematic = df.loc[df['LoD'] < targetLoD]
    # for index, row in dfProblematic.iterrows():
    #     if targetLoD == 2 and row["LoD"] == 0:
    #         neededParams = ['buildingHeight', 'roofHeight', 'roofType', 'roofHeading']
    #         if checkNeededData(self, row, neededParams) == False:
    #             return
    #     elif targetLoD == 2 and row["LoD"] == 1:
    #         neededParams = ['roofHeight', 'roofType', 'roofHeading']
    #         if checkNeededData(self, row, neededParams) == False:
    #             return
    #     elif targetLoD == 1 and row["LoD"] == 0:
    #         neededParams = ['buildingHeight']
    #         if checkNeededData(self, row, neededParams) == False:
    #             return
    #     else:
    #         # should pretty much be all good in the other cases
    #         pass

    filesToWorkOn = list(dict.fromkeys(df["filename"].to_list()))
    for i, filename in enumerate(filesToWorkOn):
        print("enrich file:", filename)
        dfFile = df.loc[df["filename"] == filename]
        # do the shenanigans here
        enrichFile(self, filename, dfFile)
        gf.progressTransfrom(self, (i + 1) / len(filesToWorkOn) * 100)


def enrichFile(self, filename, dfFile):
    """Enriches 'filename' with "EnergyADE", where 'builidngs' is either a list of building names or set to 'all'"""

    # parsing file
    parser = ET.XMLParser(remove_blank_text=True)
    tree = ET.parse(os.path.join(self.inpDir, filename), parser)
    root_E = tree.getroot()
    nss = root_E.nsmap

    nroot_E, nnss, nLcorner_E, nUcorner_E, minimum, maximum = getNewTree(self, filename)

    # iterate over all buildings in the file
    num_of_buildings = len(root_E.findall('core:cityObjectMember/bldg:Building', nss))
    i = 0
    while i < num_of_buildings:
        building_E = nroot_E.findall('core:cityObjectMember/bldg:Building', nnss)[i]
        building_ID = building_E.attrib['{http://www.opengis.net/gml}id']
        dfBuild = dfFile.loc[dfFile["buildingID"] == building_ID]

        dfMain = dfBuild.loc[dfBuild['bpID'] == '']

        # check if building is selected (dfBuild has an entry -> the file should be transformed)
        if len(dfBuild.index) != 0:
            # adding description
            describ_E = building_E.find("gml:description", nnss)
            if describ_E != None:
                if 'enriched using the RWTH e3d CityEnrich' not in describ_E.text:
                    describ_E.text += "\n                       enriched using the RWTH e3d CityEnrich"
                else:
                    # transformed description is already present in element
                    pass
            else:
                describ_E = ET.SubElement(building_E, ET.QName(nnss["gml"], 'description'))
                describ_E.text = 'enriched using the RWTH e3d CityEnrich'
                building_E.insert(0, describ_E)

            # check if new attributes have been set
            if len(dfMain.index > 1):
                setBuildingElements(building_E, nnss, dfMain)

            # if self.rB_individualFiles.isChecked():
            #     # first save tree to file
            #     baseName = os.path.splitext(filename)[0]
            #     exportName = baseName + "_" + building_ID + "_enriched_e3d_CE.gml"
            #     writeTree(self, nroot_E, nnss, nLcorner_E, nUcorner_E, minimum, maximum, baseName, exportName)
            #     # then create a new root
            #     nroot_E, nnss, nLcorner_E, nUcorner_E, minimum, maximum = getNewTree(self, filename)

            i -= - 1

            # if not self.rB_individualFiles.isChecked():
                # need to safe file here
        baseName = os.path.splitext(filename)[0]
        exportName = baseName + "_enriched_e3d_CE.gml"
        writeTree(self, nroot_E, nnss, nLcorner_E, nUcorner_E, minimum, maximum, baseName, exportName)