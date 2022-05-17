# import of libraries
from PySide2 import QtWidgets, QtGui
import os
import pandas as pd
import math
import lxml.etree as ET
import uuid
import copy
# import of functions
import gui_functions as gf
import CityEnrich_selection as sel
import twod_operations as twod

"""Testing Dataframe"""
d = {'volume': [700], 'area': [250]}
thermal_zone = pd.DataFrame(data=d)


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
    """to save user entered building parameters"""
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

    """add EnergyADE Namespace and schemaLocation"""
    tree_copy = copy.deepcopy(tree)
    nroot_E = add_namespace(tree_copy, 'energy', 'http://www.sig3d.org/citygml/2.0/energy/1.0')
    nnss = nroot_E.nsmap

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
                _set_gml_volume_lxml(building_E, nnss, thermal_zone)
                _set_gml_floor_area_lxml(building_E, nnss, thermal_zone)
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
        print("comes through here!")
        baseName = os.path.splitext(filename)[0]
        exportName = baseName + "_enriched_e3d_CE.gml"
        writeTree(self, nroot_E, nnss, nLcorner_E, nUcorner_E, minimum, maximum, baseName, exportName)


def _set_gml_volume_lxml(building_E, nsClass, thermal_zone):

    # declaring Volume Object

    gml_volume = ET.SubElement(building_E, ET.QName(nsClass['energy'], 'volume'))
    gml_volume_type = ET.SubElement(gml_volume, ET.QName(nsClass['energy'], 'VolumeType'))
    ET.SubElement(gml_volume_type, ET.QName(nsClass['energy'], 'type')).text = "grossVolume"
    ET.SubElement(gml_volume_type, ET.QName(nsClass['energy'], 'value'), attrib={'uom': "m3"}).text \
        = str(thermal_zone.volume[0].item())


def _set_gml_floor_area_lxml(building_E, nsClass,thermal_zone):

    # declaring Floor Area Object

    gml_floor_area = ET.SubElement(building_E, ET.QName(nsClass['energy'], 'floorArea'))
    gml_floor_area_type = ET.SubElement(gml_floor_area, ET.QName(nsClass['energy'], 'FloorArea'))
    ET.SubElement(gml_floor_area_type, ET.QName(nsClass['energy'], 'type')).text = "grossFloorArea"
    ET.SubElement(gml_floor_area_type, ET.QName(nsClass['energy'], 'value'), attrib={'uom': "m2"}).text \
        = str(thermal_zone.area[0].item())


def _set_gml_thermal_zone_lxml(building_E, nsClass, thermal_zone):

    thermal_zone_id = str("GML_" + str(thermal_zone.internal_id))
    usage_zone_id = str("GML_" + str(thermal_zone.use_conditions.internal_id))
    gml_thermal_zone = ET.SubElement(building_E, ET.QName(nsClass.energy, 'thermalZone'))
    gml_Thermal_Zone = ET.SubElement(gml_thermal_zone, ET.QName(nsClass.energy, 'ThermalZone'),
                                     attrib={ET.QName(nsClass.gml, 'id'): thermal_zone_id})
    ET.SubElement(gml_Thermal_Zone, ET.QName(nsClass.energy, 'contains'),
                  attrib={ET.QName(nsClass.xlink, 'href'): str('#'+usage_zone_id)})
    _set_gml_floor_area_lxml(gml_Thermal_Zone, nsClass, thermal_zone, ET)
    _set_gml_volume_lxml(gml_Thermal_Zone, nsClass, thermal_zone, ET)
    ET.SubElement(gml_Thermal_Zone, ET.QName(nsClass.energy, 'isCooled')).text = "false"
    ET.SubElement(gml_Thermal_Zone, ET.QName(nsClass.energy, 'isHeated')).text = "true"
    gml_volume_geometry = ET.SubElement(gml_Thermal_Zone, ET.QName(nsClass.energy, 'volumeGeometry'))
    # solid = ET.SubElement(gml_volume_geometry, ET.QName(nsClass.gml, 'Solid'),
    #                                  attrib={ET.QName(nsClass.gml, 'id'): str(thermal_zone_id + "_solid")})

    polyIDs, exteriorSurfaces = _set_composite_surface(gml_volume_geometry, nsClass, thermal_zone, ET)

    """Set Usage zone for thermal zone"""
    _set_usage_zone_lxml(thermal_zone, building_E, usage_zone_id)

    """Set boundary Surfaces"""

    construction_id_windows = None
    material_ids = []

    for i in range(len(exteriorSurfaces)):
        if i == 0:
            surfaceType = 'WallSurface'
            construction_id = None

        elif i == 1:
            surfaceType = 'RoofSurface'
            construction_id = None

        elif i == 2:
            surfaceType = 'GroundSurface'
            construction_id = None


        for surface in exteriorSurfaces[i]:
            thermal_openings = []

            for win_count in thermal_zone.windows:
                if surface.orientation == win_count.orientation and surface.tilt == win_count.tilt:
                    thermal_openings.append(win_count)
            construction_id, construction_id_windows = \
                _set_gml_thermal_boundary_lxml(gml_Thermal_Zone, surface, thermal_openings, nsClass, construction_id,
                                               construction_id_windows, material_ids, thermal_zone_id)

    return polyIDs


def _set_composite_surface(solid, nsClass, thermal_zone, ET):

    exteriorSurfaces = [thermal_zone.outer_walls, thermal_zone.rooftops, thermal_zone.ground_floors]
    polyIDs = []
    n = 0
    UUID = uuid.uuid1()
    for dictionary in exteriorSurfaces:
        for key in dictionary:
            ID = "PolyID" + str(UUID) + '_' + str(n)
            polyIDs.append(ID)
            hashtagedID = '#' + ID
            # ET.SubElement(solid, ET.QName(nsClass.gml, 'surfaceMember'),
            #               attrib={ET.QName(nsClass.xlink, 'href'): hashtagedID})
            n -= - 1
    return polyIDs, exteriorSurfaces


def _set_gml_thermal_boundary_lxml(gml_zone, wall, thermal_openings, nsClass, construction_id,
                                   construction_id_windows, material_ids, thermal_zone_id):
    """Control function to add a thermal boundary surface to the thermal zone

    The thermal zone instance of citygml is modified and thermal boundary
    surfaces are added. The thermal boundaries are chosen according to their
    type (OuterWall, InnerWall, Roof, etc.). For outer walls (including roof)
    the thermal boundary is returned to add windows (Thermal Openings).

    Parameters
    ----------

    gml_zone : energy.thermalZones() object
        A thermalZone object, where energy is a reference to
        `pyxb.bundles.opengis.citygml.energy`.

    wall : TEASER instance of Wall()
        Teaser instance of Wall or its inherited classes

    thermal_openings: List of TEASER instances of Window() or Door()
        Teaser instance of BuildingElement or its inherited classes
    Returns
    ----------

    _current_tb : energy.ThermalBoundarySurface()
        A ThermalBoundarySurface object with semantic information
        (area, azimuth, inclination etc.)

    """
    _current_tb = None
    if type(wall).__name__ == "OuterWall":

        thermal_boundary_type_value = "outerWall"


    elif type(wall).__name__ == "Rooftop":
        thermal_boundary_type_value = "roof"


    elif type(wall).__name__ == "GroundFloor":

        thermal_boundary_type_value = "groundSlab"

    elif type(wall).__name__ == "InnerWall":
        thermal_boundary_type_value = "intermediaryFloor"


    elif type(wall).__name__ == "Ceiling" or type(wall).__name__ == "Floor":

        thermal_boundary_type_value = "interiorWall"

    else:
        print("Strange Wall Surface detected!")

    boundedBy_E = ET.SubElement(gml_zone, ET.QName(nsClass.energy, 'boundedBy'))
    thermal_boundary_E = ET.SubElement(boundedBy_E, ET.QName(nsClass.energy, 'ThermalBoundary'),
                                       attrib={ET.QName(nsClass.gml, 'id'): str("GML_" + str(wall.internal_id))})
    ET.SubElement(thermal_boundary_E, ET.QName(nsClass.energy, "thermalBoundaryType")).text = \
        thermal_boundary_type_value
    ET.SubElement(thermal_boundary_E, ET.QName(nsClass.energy, "azimuth"), attrib={'uom': "deg"}).text = \
        str(wall.orientation)
    ET.SubElement(thermal_boundary_E, ET.QName(nsClass.energy, "inclination"), attrib={'uom': "deg"}).text = \
        str(wall.tilt)
    ET.SubElement(thermal_boundary_E, ET.QName(nsClass.energy, "area"), attrib={'uom': "m2"}).text = \
        str(wall.area)
    if construction_id is None:
        construction_id = _set_gml_construction_lxml(wall, material_ids)
    else:
        pass
    ET.SubElement(thermal_boundary_E, ET.QName(nsClass.energy, "construction"), attrib={ET.QName(nsClass.xlink, 'href'):
                                                                                        str("#" + str(construction_id))})

    if thermal_openings is not None:
        for thermal_opening in thermal_openings:
            contains = ET.SubElement(thermal_boundary_E, ET.QName(nsClass.energy, "contains"))
            thermal_opening_E = ET.SubElement(contains, ET.QName(nsClass.energy, "ThermalOpening"),
                                              attrib={ET.QName(nsClass.gml, 'id'): str("GML_" + str(thermal_opening.internal_id))})
            ET.SubElement(thermal_opening_E, ET.QName(nsClass.energy, "area"), attrib={'uom': "m2"}).text = \
                str(thermal_opening.area)
            if construction_id_windows is None:
                construction_id_windows = _set_gml_construction_lxml(thermal_opening, material_ids)
            else:
                pass
            ET.SubElement(thermal_opening_E, ET.QName(nsClass.energy, "construction"),
                          attrib={ET.QName(nsClass.xlink, 'href'): str("#" + construction_id_windows)})

    ET.SubElement(thermal_boundary_E, ET.QName(nsClass.energy, "delimits"),
                  attrib={ET.QName(nsClass.xlink, 'href'): str("#" + str(str(thermal_zone_id)))})

    return construction_id, construction_id_windows


def _set_gml_construction_lxml(element, material_ids):
    construction_id = str("GML_" + str(uuid.uuid1()))
    feature_member = ET.SubElement(nroot_E, ET.QName(nsClass.gml, 'featureMember'))
    construction_gml = ET.SubElement(feature_member, ET.QName(nsClass.energy, 'Construction'),
                                     attrib={ET.QName(nsClass.gml, 'id'): str(construction_id)})
    ET.SubElement(construction_gml, ET.QName(nsClass.gml, "description")).text = \
        str(type(element).__name__ +"_construction")
    ET.SubElement(construction_gml, ET.QName(nsClass.gml, "name")).text = \
        str(type(element).__name__ + "_construction")
    ET.SubElement(construction_gml, ET.QName(nsClass.energy, "uValue"), attrib={'uom': "W/K*m2"}).text = \
        str(element.ua_value / element.area)



    for layer_count in element.layer:
        layer_gml = ET.SubElement(construction_gml, ET.QName(nsClass.energy, "layer"))
        Layer_gml = ET.SubElement(layer_gml, ET.QName(nsClass.energy, "Layer"),
                                  attrib={ET.QName(nsClass.gml, 'id'): str("GML_" + str(layer_count.internal_id))})
        layer_comp = ET.SubElement(Layer_gml, ET.QName(nsClass.energy, "layerComponent"))
        Layer_comp = ET.SubElement(layer_comp, ET.QName(nsClass.energy, "LayerComponent"),
                                  attrib={ET.QName(nsClass.gml, 'id'):
                                              str("GML_" + str(layer_count.internal_id) + "_1")})
        ET.SubElement(Layer_comp, ET.QName(nsClass.energy, "areaFraction"), attrib={'uom': "scale"}).text = str(1)
        ET.SubElement(Layer_comp, ET.QName(nsClass.energy, "thickness"), attrib={'uom': "m"}).text = \
            str(layer_count.thickness)
        ET.SubElement(Layer_comp, ET.QName(nsClass.energy, 'material'),
                      attrib={ET.QName(nsClass.xlink, 'href'):
                                  str("#" + "GML_" + layer_count.material.material_id)})

        if layer_count.material.material_id in material_ids:
            pass
        else:
            material_ids.append(layer_count.material.material_id)

            feature_member_material = ET.SubElement(nroot_E, ET.QName(nsClass.gml, 'featureMember'))
            material_gml = ET.SubElement(feature_member_material, ET.QName(nsClass.energy, 'SolidMaterial'),
                                             attrib={ET.QName(nsClass.gml, 'id'):
                                                         str("GML_" + layer_count.material.material_id)})
            ET.SubElement(material_gml, ET.QName(nsClass.gml, "description")).text = \
                str(layer_count.material.name)
            ET.SubElement(material_gml, ET.QName(nsClass.gml, "name")).text = \
                str(layer_count.material.name)
            ET.SubElement(material_gml, ET.QName(nsClass.energy, "conductivity"), attrib={'uom': "W/K*m"}).text = \
                str(layer_count.material.thermal_conduc)
            ET.SubElement(material_gml, ET.QName(nsClass.energy, "density"), attrib={'uom': "kg/m3"}).text = \
                str(layer_count.material.density)
            ET.SubElement(material_gml, ET.QName(nsClass.energy, "specificHeat"), attrib={'uom': "kJ/K*kg"}).text = \
                str(layer_count.material.heat_capac)

    return construction_id


def _set_usage_zone_lxml(thermal_zone, gml_bldg, usage_zone_id):
    usage_zone = thermal_zone.use_conditions
    gml_usage_zone = ET.SubElement(gml_bldg, ET.QName(nsClass.energy, 'usageZone'))
    gml_Usage_Zone = ET.SubElement(gml_usage_zone, ET.QName(nsClass.energy, 'UsageZone'),
                                   attrib={ET.QName(nsClass.gml, 'id'): usage_zone_id})

    """Heating"""
    heating_schedule = ET.SubElement(gml_Usage_Zone, ET.QName(nsClass.energy, 'heatingSchedule'))
    _set_schedule(heating_schedule, usage_zone,  usage_zone_id, "heating")

    """type"""
    ET.SubElement(gml_Usage_Zone, ET.QName(nsClass.energy, 'usageZoneType')).text = str(usage_zone.usage)

    """Cooling"""
    # TODO: Check together with isCooled if AHU is used and set cooling

    """Ventilation"""
    # ventilation_schedule = ET.SubElement(gml_Usage_Zone, ET.QName(nsClass.energy, 'ventilationSchedule'))
    # _set_schedule(usage_zone, ventilation_schedule, usage_zone_id, "ventilation")

    """Occupiedby"""
    occupied_by = ET.SubElement(gml_Usage_Zone, ET.QName(nsClass.energy, 'occupiedBy'))
    occupants = ET.SubElement(occupied_by, ET.QName(nsClass.energy, 'Occupants'),
                              attrib={ET.QName(nsClass.gml, 'id'): (usage_zone_id + "_Occupants")})
    heat_dissipation = ET.SubElement(occupants, ET.QName(nsClass.energy, 'heatDissipation'))
    heat_exchange_type = ET.SubElement(heat_dissipation, ET.QName(nsClass.energy, 'HeatExchangeType'))
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'convectiveFraction'), attrib={'uom': "scale"}).text = \
        str(usage_zone.ratio_conv_rad_persons)
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'radiantFraction'), attrib={'uom': "scale"}).text = \
        str(1 - usage_zone.ratio_conv_rad_persons)
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'totalValue'), attrib={'uom': "W"}).text = \
        str(usage_zone.fixed_heat_flow_rate_persons)
    ET.SubElement(occupants, ET.QName(nsClass.energy, 'numberOfOccupants')).text = str(int(usage_zone.persons*thermal_zone.area))
    occupancy_rate = ET.SubElement(occupants, ET.QName(nsClass.energy, 'occupancyRate'))
    _set_schedule(occupancy_rate, usage_zone, usage_zone_id, "persons")

    """Machines"""
    equipped_with = ET.SubElement(gml_Usage_Zone, ET.QName(nsClass.energy, 'equippedWith'))
    electrical_app = ET.SubElement(equipped_with, ET.QName(nsClass.energy, 'ElectricalAppliances'),
                              attrib={ET.QName(nsClass.gml, 'id'): (usage_zone_id + "_Machines")})

    opperation_schedule = ET.SubElement(electrical_app, ET.QName(nsClass.energy, 'operationSchedule'))
    _set_schedule(opperation_schedule, usage_zone, usage_zone_id, "machines")

    heat_dissipation = ET.SubElement(electrical_app, ET.QName(nsClass.energy, 'heatDissipation'))
    heat_exchange_type = ET.SubElement(heat_dissipation, ET.QName(nsClass.energy, 'HeatExchangeType'))
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'convectiveFraction'), attrib={'uom': "scale"}).text = \
        str(usage_zone.ratio_conv_rad_machines)
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'radiantFraction'), attrib={'uom': "scale"}).text = \
        str(1 - usage_zone.ratio_conv_rad_machines)
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'totalValue'), attrib={'uom': "W/m2"}).text = \
        str(usage_zone.machines)



    """Lighting"""
    equipped_with = ET.SubElement(gml_Usage_Zone, ET.QName(nsClass.energy, 'equippedWith'))
    electrical_app = ET.SubElement(equipped_with, ET.QName(nsClass.energy, 'LightingFacilities'),
                              attrib={ET.QName(nsClass.gml, 'id'): (usage_zone_id + "_Lighting")})

    opperation_schedule = ET.SubElement(electrical_app, ET.QName(nsClass.energy, 'operationSchedule'))
    _set_schedule(opperation_schedule, usage_zone, usage_zone_id, "lighting")

    heat_dissipation = ET.SubElement(electrical_app, ET.QName(nsClass.energy, 'heatDissipation'))
    heat_exchange_type = ET.SubElement(heat_dissipation, ET.QName(nsClass.energy, 'HeatExchangeType'))
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'convectiveFraction'), attrib={'uom': "scale"}).text = \
        str(usage_zone.ratio_conv_rad_lighting)
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'radiantFraction'), attrib={'uom': "scale"}).text = \
        str(1 - usage_zone.ratio_conv_rad_lighting)
    ET.SubElement(heat_exchange_type, ET.QName(nsClass.energy, 'totalValue'), attrib={'uom': "W/m2"}).text = \
        str(usage_zone.lighting_power)


    # _set_gml_floor_area_lxml(gml_Usage_Zone, nsClass, thermal_zone, ET)


def _set_schedule(schedule_type, usage_zone, usage_zone_id, type_name):
    daily_pattern = ET.SubElement(schedule_type, ET.QName(nsClass.energy, 'DailyPatternSchedule'),
                                  attrib={ET.QName(nsClass.gml, 'id'): str(usage_zone_id + f"_{type_name}_schedule")})
    ET.SubElement(daily_pattern, ET.QName(nsClass.gml, "name")).text = str(type_name)
    period_of_year = ET.SubElement(daily_pattern, ET.QName(nsClass.energy, 'periodOfYear'))
    Period_of_year = ET.SubElement(period_of_year, ET.QName(nsClass.energy, 'PeriodOfYear'))
    period = ET.SubElement(Period_of_year, ET.QName(nsClass.energy, 'period'))

    time_period = ET.SubElement(period, ET.QName(nsClass.gml, 'TimePeriod'))
    ET.SubElement(time_period, ET.QName(nsClass.gml, 'beginPosition')).text = str("2023-01-01T00:00:00")
    ET.SubElement(time_period, ET.QName(nsClass.gml, 'endPosition')).text = str("2023-12-31T00:00:00")

    for day_type in ["weekDay", "weekEnd"]:
        daily_schedule = ET.SubElement(Period_of_year, ET.QName(nsClass.energy, 'dailySchedule'))
        Daily_schedule = ET.SubElement(daily_schedule, ET.QName(nsClass.energy, 'DailySchedule'))
        ET.SubElement(Daily_schedule, ET.QName(nsClass.energy, 'dayType')).text = str(day_type)
        schedule = ET.SubElement(Daily_schedule, ET.QName(nsClass.energy, 'schedule'))
        regular_ts = ET.SubElement(schedule, ET.QName(nsClass.energy, 'RegularTimeSeries'))

        variable_props = ET.SubElement(regular_ts, ET.QName(nsClass.energy, 'variableProperties'))
        time_value_prop = ET.SubElement(variable_props, ET.QName(nsClass.energy, 'TimeValuesProperties'))
        ET.SubElement(time_value_prop, ET.QName(nsClass.energy, 'acquisitionMethod')).text = str("estimation")
        ET.SubElement(time_value_prop, ET.QName(nsClass.energy, 'interpolationType')).text = \
            str("averageInSucceedingInterval")
        ET.SubElement(time_value_prop, ET.QName(nsClass.energy, 'thematicDescription')).text = str("Nominal" + type_name)

        temporal_extant = ET.SubElement(regular_ts, ET.QName(nsClass.energy, 'temporalExtent'))
        time_period = ET.SubElement(temporal_extant, ET.QName(nsClass.gml, 'TimePeriod'))
        ET.SubElement(time_period, ET.QName(nsClass.gml, 'beginPosition')).text = str("00:00:00")
        ET.SubElement(time_period, ET.QName(nsClass.gml, 'endPosition')).text = str("00:00:23")

        ET.SubElement(regular_ts, ET.QName(nsClass.energy, 'timeInterval'), attrib={'unit': "hour"}).text = str(1)

        if type_name == "heating" or "type"=="cooling":
            uom = "K"
        if type_name == "ventilation":
            uom = "1/h"
        else:
            uom = "scale"

        if day_type is "weekDay":

            ET.SubElement(regular_ts, ET.QName(nsClass.energy, 'values'), attrib={'uom': uom}).text = str(usage_zone.schedules[f"{type_name}_profile"].iloc[0:23].values).strip('[]')

        if day_type is "weekEnd":

            ET.SubElement(regular_ts, ET.QName(nsClass.energy, 'values'), attrib={'uom': uom}).text = str(usage_zone.schedules[f"{type_name}_profile"].iloc[120:143].values).strip('[]')

    return


def add_namespace(tree, alias, uri):
    """
    taken and adopted from Stackoverflow. "Adds" new Namespace (EnergyADE - energy) and Schema location to
    original file. For this it takes the original root and copies the elements to the newly created root.
    :param tree:
    :param alias:
    :param uri:
    :return:
    """
    root = tree.getroot()
    nsmap = root.nsmap
    nsmap[alias] = uri
    new_root = ET.Element(root.tag, attrib=root.attrib, nsmap=nsmap)
    schemaLocation = "http://www.opengis.net/citygml/2.0 http://www.sig3d.org/citygml/2.0/energy/1.0/EnergyADE.xsd"
    new_root = ET.Element(ET.QName(nsmap['core'], 'CityModel'),
                         attrib={"{" + nsmap['xsi'] + "}schemaLocation": schemaLocation}, nsmap=nsmap)
    for elem in root:
        new_root.append(elem)
    return new_root
