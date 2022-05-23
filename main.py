

# import of libraries
import os
import sys
import PySide2
from PySide2 import QtWidgets, QtGui, QtCore
import time
import functools
import pandas as pd

# import of functions
import gui_functions as gf
import CityEnrich_selection as sel
import CityEnrich_enrichment as cee


# setting system environment variable
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path



# positions and dimensions of window
posx = 275
posy = 100
width = 800
height = 800
sizefactor = 0
sizer = True

# path of script
pypath = os.path.dirname(os.path.realpath(__file__))


buildingDict = {}
selAll = True
inpDir = ''

buildingOverWrDict = {-1: {'LoD': None, 'rType': None, 'bFunction': None, 'SAG': None, 'SBG': None, 'YOC': None, 'rHeight': None, 'rHeading': None, 'bHeight': None}}
buildingParamsDict = {-1: {'LoD': None, 'rType': None, 'bFunction': None, 'SAG': None, 'SBG': None, 'YOC': None, 'rHeight': None, 'rHeading': None, 'bHeight': None}}



buildingFunctions = {'': 0, 'residential building': 1000, 'tenement': 1010, 'hostel': 1020, 'residential- and administration building': 1030, 'residential- and office building': 1040,
                     'residential- and business building': 1050, 'residential- and plant building': 1060, 'agrarian- and forestry building': 1070, 'residential- and commercial building': 1080,
                     "forester's lodge": 1090, 'holiday house': 1100, 'summer house': 1110, 'office building': 1120, 'credit institution': 1130, 'insurance': 1140, 'business building': 1150,
                     'department store': 1160, 'shopping centre': 1170, 'kiosk': 1180, 'pharmacy': 1190, 'pavilion': 1200, 'hotel': 1210, 'youth hostel': 1220, 'campsite building': 1230,
                     'restaurant': 1240, 'cantine': 1250, 'recreational site': 1260, 'function room': 1270, 'cinema': 1280, 'bowling alley': 1290, 'casino': 1300, 'industrial building': 1310,
                     'factory': 1320, 'workshop': 1330, 'petrol / gas station': 1340, 'washing plant': 1350, 'cold store': 1360, 'depot': 1370, 'building for research purposes': 1380,
                     'quarry': 1390, 'salt works': 1400, 'miscellaneous industrial building': 1410, 'mill': 1420, 'windmill': 1430, 'water mill': 1440, 'bucket elevator': 1450,
                     'weather station': 1460, 'traffic assets office': 1470, 'street maintenance': 1480, 'waiting hall': 1490, 'signal control box': 1500, 'engine shed': 1510,
                     'signal box or stop signal': 1520, 'plant building for air traffic': 1530, 'hangar': 1540, 'plant building for shipping': 1550, 'shipyard': 1560, 'dock': 1570,
                     'plant building for canal lock': 1580, 'boathouse': 1590, 'plant building for cablecar': 1600, 'multi-storey car park': 1610, 'parking level': 1620, 'garage': 1630,
                     'vehicle hall': 1640, 'underground garage': 1650, 'building for supply': 1660, 'waterworks': 1670, 'pump station': 1680, 'water basin': 1690, 'electric power station': 1700,
                     'transformer station': 1710, 'converter': 1720, 'reactor': 1730, 'turbine house': 1740, 'boiler house': 1750, 'building for telecommunications': 1760, 'gas works': 1770,
                     'heat plant': 1780, 'pumping station': 1790, 'building for disposal': 1800, 'building for effluent disposal': 1810, 'building for filter plant': 1820, 'toilet': 1830,
                     'rubbish bunker': 1840, 'building for rubbish incineration': 1850, 'building for rubbish disposal': 1860, 'building for agrarian and forestry': 1870, 'barn': 1880,
                     'stall': 1890, 'equestrian hall': 1900, 'alpine cabin': 1910, 'hunting lodge': 1920, 'arboretum': 1930, 'glass house': 1940, 'moveable glass house': 1950,
                     'public building': 1960, 'administration building': 1970, 'parliament': 1980, 'guildhall': 1990, 'post office': 2000, 'customs office': 2010, 'court': 2020,
                     'embassy or consulate': 2030, 'district administration': 2040, 'district government': 2050, 'tax office': 2060, 'building for education and research': 2070,
                     'comprehensive school': 2080, 'vocational school': 2090, 'college or university': 2100, 'research establishment': 2110, 'building for cultural purposes': 2120,
                     'castle': 2130, 'theatre or opera': 2140, 'concert building': 2150, 'museum': 2160, 'broadcasting building': 2170, 'activity building': 2180, 'library': 2190,
                     'fort': 2200, 'religious building': 2210, 'church': 2220, 'synagogue': 2230, 'chapel': 2240, 'community center ': 2250, 'place of worship': 2260, 'mosque': 2270,
                     'temple': 2280, 'convent': 2290, 'building for health care': 2300, 'hospital': 2310, 'healing centre or care home': 2320, 'health centre or outpatients clinic': 2330,
                     'building for social purposes': 2340, 'youth centre': 2350, 'seniors centre': 2360, 'homeless shelter': 2370, 'kindergarten or nursery': 2380, 'asylum seekers home': 2390,
                     'police station': 2400, 'fire station': 2410, 'barracks': 2420, 'bunker': 2430, 'penitentiary or prison': 2440, 'cemetery building': 2450, 'funeral parlor': 2460,
                     'crematorium': 2470, 'train station': 2480, 'airport building': 2490, 'building for underground station': 2500, 'building for tramway': 2510, 'building for bus station': 2520,
                     'shipping terminal': 2530, 'building for recuperation purposes': 2540, 'building for sport purposes': 2550, 'sports hall': 2560, 'building for sports field': 2570,
                     'swimming baths': 2580, 'indoor swimming pool': 2590, 'sanatorium': 2600, 'zoo building': 2610, 'green house': 2620, 'botanical show house': 2630, 'bothy': 2640,
                     'tourist information centre': 2650, 'others': 2700}


class mainWindow(QtWidgets.QWidget):
    """mainWindow class"""
    def __init__(self):
        #initiate the parent
        super(mainWindow,self).__init__()
        self.initUI()


    def initUI(self):
        global posx, posy, width, height, sizefactor, sizer
        if sizer:
            posx, posy, width, height, sizefactor = gf.screenSizer(self, posx, posy, width, height, app)
            sizer = False
        gf.windowSetup(self, posx, posy, width, height, pypath, 'CityEnrich - CityGML Enrichment Tool')

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.btn_selFile = QtWidgets.QPushButton('Select file')
        self.uGrid.addWidget(self.btn_selFile, 0, 0, 1, 1)

        self.btn_selDir = QtWidgets.QPushButton('Select folder')
        self.uGrid.addWidget(self.btn_selDir, 0, 1, 1, 1)

        self.txtB_inPath = QtWidgets.QLineEdit()
        self.txtB_inPath.setPlaceholderText('Path to file or folder')
        self.txtB_inPath.setReadOnly(True)
        self.uGrid.addWidget(self.txtB_inPath, 0, 2, 1, 4)

        self.lbl_scanLoD = QtWidgets.QLabel('LoD scan progress:')
        self.uGrid.addWidget(self.lbl_scanLoD, 1, 0, 1, 1)

        self.pB_scanLoD = QtWidgets.QProgressBar(self)
        self.uGrid.addWidget(self.pB_scanLoD, 1, 1, 1, 5)

        self.vbox.addLayout(self.uGrid)

        # for selecting all or individual buildings
        self.gB_buildings = QtWidgets.QGroupBox('')
        self.vbox.addWidget(self.gB_buildings)
        # self.gB_buildings.setToolTip('When unchecked transformation will be done for all buildings in the file(s)')

        self.bGrid = QtWidgets.QGridLayout()
        self.gB_buildings.setLayout(self.bGrid)

        self.rb_allBuildings = QtWidgets.QRadioButton('Enrich all buildings')
        self.bGrid.addWidget(self.rb_allBuildings, 0, 0, 1, 1)
        self.rb_allBuildings.setChecked(selAll)

        self.rb_selectBuildings = QtWidgets.QRadioButton('Enrich individual buildings')
        self.bGrid.addWidget(self.rb_selectBuildings, 0, 3, 1, 1)
        self.rb_selectBuildings.setChecked(not selAll)


        self.tbl_buildings = QtWidgets.QTableWidget()
        self.tbl_buildings.setColumnCount(4)
        self.tbl_buildings.setHorizontalHeaderLabels(['File Name', 'Name of Building', 'Level of Detail (LoD)', ''])
        self.tbl_buildings.verticalHeader().hide()
        # self.tbl_buildings.horizontalHeader().hide()
        self.tbl_buildings.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_buildings.setEnabled(False)
        self.tbl_buildings.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tbl_buildings.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_buildings.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.bGrid.addWidget(self.tbl_buildings, 1, 0, 1, 6)

        # Gridbox for lower grid
        self.lGrid = QtWidgets.QGridLayout()

        self.btn_about = QtWidgets.QPushButton('About')
        self.lGrid.addWidget(self.btn_about, 0, 0, 1, 1)

        self.btn_reset = QtWidgets.QPushButton('Reset')
        self.lGrid.addWidget(self.btn_reset, 0, 1, 1, 1)

        self.btn_exit = QtWidgets.QPushButton('Exit')
        self.lGrid.addWidget(self.btn_exit, 0, 2, 1, 1)

        self.btn_next = QtWidgets.QPushButton('Next')
        self.lGrid.addWidget(self.btn_next, 0, 3, 1, 1)
        self.btn_next.setEnabled(False)

        self.vbox.addLayout(self.lGrid)

        self.btn_selFile.clicked.connect(self.func_selectFile)
        self.btn_selDir.clicked.connect(self.func_selectDir)
        self.rb_selectBuildings.toggled.connect(self.func_selB)

        self.btn_about.clicked.connect(self.func_about)
        self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit.clicked.connect(self.func_exit)
        self.btn_next.clicked.connect(self.func_next)

        # setting some defaults
        self.inpPath = ''
        self.inpDir = inpDir
        self.expPath = ''
        self.buildingDict = {}
        self.completedLoD = 0
        self.cBoxes = []

        # table row index to comboBox index
        self.tableDict = {}

        global buildingDict
        if self.inpDir != '':
            self.txtB_inPath.setText(self.inpDir)
        if buildingDict != {}:
            self.btn_next.setEnabled(True)
            resultsDict = {}
            selected = []
            for i in buildingDict:
                if buildingDict[i]["filename"] not in resultsDict:
                    resultsDict[buildingDict[i]["filename"]] = {}
                else:
                    pass
                resultsDict[buildingDict[i]["filename"]][buildingDict[i]["buildingname"]] = buildingDict[i]["values"]
                selected.append(buildingDict[i]['selected'])
            sel.display_file_lod(self, resultsDict)
            for i, state in enumerate(selected):
                self.cBoxes[i].setChecked(state)
            gf.progressLoD(self, 100)

    def func_selectFile(self):
        res = sel.select_gml(self)
        if res:
            self.inpPath = res
            self.inpDir = os.path.dirname(res)
            sel.get_files(self)
        else:
            pass

    def func_selectDir(self):
        res = sel.select_folder(self)
        if res:
            self.inpPath = res
            self.inpDir = res
            # sel.get_files(self)
        else:
            pass

    def func_selB(self):
        if self.rb_selectBuildings.isChecked():
            self.tbl_buildings.setEnabled(True)
        else:
            self.tbl_buildings.setEnabled(False)

    def func_about(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, about(), False)

    def func_reset(self):
        global posx, posy
        self.reset_variables()
        posx, posy = gf.dimensions(self)
        gf.next_window(self, mainWindow())

    def reset_variables(self):
        self.inpPath = ''
        self.inpDir = ''
        self.buildingDict = {}
        self.completedLoD = 0
        self.cBoxes = []

    def func_exit(self):
        gf.close_application(self)

    def func_next(self):
        global buildingDict, selAll, inpDir, posx, posy
        inpDir = self.inpDir
        selAll = self.rb_allBuildings.isChecked()
        buildingDict = self.buildingDict
        selection = 0
        for key in buildingDict:
            selection += buildingDict[key]["selected"]
        if selAll or selection > 0:
            posx, posy = gf.dimensions(self)
            gf.next_window(self, enrichment_main())
        else:
            gf.messageBox(self, "Important", "Please select at least one building.")

    def onStateChanged(self):
        """gets called when a checkbox for a building is (un)checked to update the buildingDict"""
        ch = self.sender()
        ix = self.tbl_buildings.indexAt(ch.pos())
        self.buildingDict[ix.row()]["selected"] = ch.isChecked()
        curText = self.tbl_buildings.item(ix.row(), 1).text().split('/')[0]
        for i in range(self.tbl_buildings.rowCount()):
            if i != ix.row():
                if self.tbl_buildings.item(i, 1).text().split('/')[0] == curText:
                    self.cBoxes[i].setChecked(ch.isChecked())
                    self.buildingDict[i]["selected"] = ch.isChecked()


# class transformation(QtWidgets.QWidget):
class enrichment_main(QtWidgets.QWidget):
    """window for enrichment options"""

    def __init__(self):
        super(enrichment_main, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor, sizer, buildingParamsDict
        if sizer:
            posx, posy, width, height, sizefactor = gf.screenSizer(self, posx, posy, width, height, app)
            sizer = False
        gf.windowSetup(self, posx, posy, width, height, pypath,
                       'CityEnrich - CityGML Enrichment Tool')

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        ttl = 'Selected buildings- ' + str(len(buildingDict))
        # building parameters
        self.gB_buildingParameters = QtWidgets.QGroupBox(ttl)
        self.vbox.addWidget(self.gB_buildingParameters)
        self.vBox_forBPgB = QtWidgets.QVBoxLayout()
        self.gB_buildingParameters.setLayout(self.vBox_forBPgB)

        # building selection
        self.pGrid = QtWidgets.QGridLayout()

        self.lbl_curBuilding = QtWidgets.QLabel('Current building:')
        self.pGrid.addWidget(self.lbl_curBuilding, 0, 0, 1, 1)

        self.cB_curBuilding = QtWidgets.QComboBox()
        self.cB_curBuilding.addItems(['all (selected) buildings'])
        self.pGrid.addWidget(self.cB_curBuilding, 0, 1, 1, 2)

        # adding selected buildings to the comboBox
        for key in buildingDict:
            if selAll or buildingDict[key]["selected"]:
                self.cB_curBuilding.insertItem(self.cB_curBuilding.count(),
                                               buildingDict[key]["filename"] + "/" + buildingDict[key]["buildingname"])
                buildingDict[key]["thermalzones"] = thermalzones()
                buildingDict[key]["construction"] = construction()
                # if buildingDict[key]["values"]["LoD"] not in presenetLoDs:
                #     presenetLoDs.append(buildingDict[key]["values"]["LoD"])
            else:
                pass
        self.buildingDict = buildingDict

        self.buildingDict_all = {"thermalzones": thermalzones(), "construction": construction()}

        # update title of groubbox according to number of buildings
        ttl = 'Building parameters - ' + str(self.cB_curBuilding.count() - 1) + ' buildings'
        self.gB_buildingParameters.setTitle(ttl)

        self.vBox_forBPgB.addLayout(self.pGrid)

        # geometry properties
        self.gB_geometry = QtWidgets.QGroupBox('Geometry parameters')
        self.vBox_forBPgB.addWidget(self.gB_geometry)

        self.gGrid = QtWidgets.QGridLayout()
        self.gB_geometry.setLayout(self.gGrid)

        self.lbl_buildingHeight = QtWidgets.QLabel('Building height:')
        self.gGrid.addWidget(self.lbl_buildingHeight, 0, 0, 1, 1)

        self.txtB_buildingHeight = QtWidgets.QLineEdit('')
        self.txtB_buildingHeight.setPlaceholderText('Building height in m')
        self.txtB_buildingHeight.setToolTip('Difference in height from base plate to the highest point of the roof')
        self.gGrid.addWidget(self.txtB_buildingHeight, 0, 1, 1, 1)

        self.lbl_roofHeight = QtWidgets.QLabel('Roof height:')
        self.gGrid.addWidget(self.lbl_roofHeight, 0, 2, 1, 1)

        self.txtB_roofHeight = QtWidgets.QLineEdit('')
        self.txtB_roofHeight.setPlaceholderText('Roof height in m')
        self.txtB_roofHeight.setToolTip('Difference in height from lowest to highest point of the roof')
        self.gGrid.addWidget(self.txtB_roofHeight, 0, 3, 1, 1)

        self.lbl_roofType = QtWidgets.QLabel('Roof type:')
        self.gGrid.addWidget(self.lbl_roofType, 1, 0, 1, 1)

        self.cB_roofType = QtWidgets.QComboBox()
        self.cB_roofType.setFont(QtGui.QFont("Consolas"))
        self.cB_roofType.setToolTip('List of available roof types')
        self.cB_roofType.addItems(
            ['', 'flat roof :      1000', 'monopitch roof : 1010', 'dual pent roof : 1020', 'gabled roof :    1030',
             'hipped roof :    1040', 'pavilion roof :  1070'])
        self.gGrid.addWidget(self.cB_roofType, 1, 1, 1, 1)

        self.lbl_roofHeading = QtWidgets.QLabel('Roof heading:')
        self.gGrid.addWidget(self.lbl_roofHeading, 1, 2, 1, 1)

        self.cB_heading = QtWidgets.QComboBox()
        self.cB_heading.setToolTip('Orientation of the roof ridge')
        self.gGrid.addWidget(self.cB_heading, 1, 3, 1, 1)
        self.cB_heading.addItems(['', 'NORTHish', 'EASTish', 'SOUTHish', 'WESTish'])

        # self.lbl_buildingFunction = QtWidgets.QLabel('Building function:')
        # self.gGrid.addWidget(self.lbl_buildingFunction, 2, 0, 1, 1)

        self.lbl_buildingFunction = QtWidgets.QLabel('Building function:')
        self.gGrid.addWidget(self.lbl_buildingFunction, 2, 0, 1, 1)

        self.cB_buildingFunction = QtWidgets.QComboBox()
        self.cB_buildingFunction.setFont(QtGui.QFont("Consolas"))
        self.cB_buildingFunction.setToolTip('List of available building functions')
        self.cB_buildingFunction.addItems(gf.createListForComboBox(buildingFunctions, 40))
        self.gGrid.addWidget(self.cB_buildingFunction, 2, 1, 1, 1)

        self.lbl_yearOfConstruction = QtWidgets.QLabel('Year of construction:')
        self.gGrid.addWidget(self.lbl_yearOfConstruction, 2, 2, 1, 1)

        self.txtB_yearOfConstruction = QtWidgets.QLineEdit()
        self.gGrid.addWidget(self.txtB_yearOfConstruction, 2, 3, 1, 1)

        self.lbl_SAG = QtWidgets.QLabel('Storeys above ground:')
        self.gGrid.addWidget(self.lbl_SAG, 3, 0, 1, 1)

        self.txtB_SAG = QtWidgets.QLineEdit('')
        self.txtB_SAG.setToolTip('Sets the value for the storeysAboveGround CityGML attribute')
        self.gGrid.addWidget(self.txtB_SAG, 3, 1, 1, 1)

        self.lbl_SBG = QtWidgets.QLabel('Storeys below ground:')
        self.gGrid.addWidget(self.lbl_SBG, 3, 2, 1, 1)

        self.txtB_SBG = QtWidgets.QLineEdit('')
        self.txtB_SBG.setToolTip('Sets the value for the storeysBelowGround CityGML attribute')
        self.gGrid.addWidget(self.txtB_SBG, 3, 3, 1, 1)

        # self.lbl_heated = QtWidgets.QLabel('Is heated:')
        # self.gGrid.addWidget(self.lbl_heated, 4, 0, 1, 1)
        #
        # self.cB_heated = QtWidgets.QComboBox()
        # self.cB_heated.setFont(QtGui.QFont("Consolas"))
        # self.cB_heated.setToolTip('Is the building heated?')
        # self.cB_heated.addItems([' ', 'Yes', 'No'])
        # self.gGrid.addWidget(self.cB_heated, 4, 1, 1, 1)
        #
        # self.lbl_cooled = QtWidgets.QLabel('Is cooled:')
        # self.gGrid.addWidget(self.lbl_cooled, 4, 2, 1, 1)
        #
        # self.cB_cooled = QtWidgets.QComboBox()
        # self.cB_cooled.setFont(QtGui.QFont("Consolas"))
        # self.cB_cooled.setToolTip('Is the building cooled?')
        # self.cB_cooled.addItems([' ', 'Yes', 'No'])
        # self.gGrid.addWidget(self.cB_cooled, 4, 3, 1, 1)



        # # enrichment
        self.gB_enrich = QtWidgets.QGroupBox('Enrichment Selection')
        self.vBox_forBPgB.addWidget(self.gB_enrich)
        #
        self.aGrid = QtWidgets.QGridLayout()
        self.gB_enrich.setLayout(self.aGrid)
        #

        self.btn_zone = QtWidgets.QPushButton('Thermal Zones')
        self.aGrid.addWidget(self.btn_zone, 0, 0, 1, 1)

        self.btn_construction = QtWidgets.QPushButton('Construction')
        self.aGrid.addWidget(self.btn_construction, 0, 1, 1, 1)

        # self.btn_occupancy = QtWidgets.QPushButton('Materials')
        # self.aGrid.addWidget(self.btn_occupancy, 1, 0, 1, 1)

        # self.btn_light_app = QtWidgets.QPushButton('Lighting and Appliances')
        # self.aGrid.addWidget(self.btn_light_app, 1, 1, 1, 1)


        # export GUI elements
        self.lGrid = QtWidgets.QGridLayout()

        # self.lbl_export = QtWidgets.QLabel('Save buildings:')
        # self.lGrid.addWidget(self.lbl_export, 0, 0, 1, 3)
        #
        # self.rB_oldAndNew = QtWidgets.QRadioButton('Transformed and remaining buildings')
        # self.lGrid.addWidget(self.rB_oldAndNew, 0, 3, 1, 3)
        #
        # self.rB_onlyTransformed = QtWidgets.QRadioButton('Only transformed buildings')
        # self.lGrid.addWidget(self.rB_onlyTransformed, 0, 6, 1, 3)
        # self.rB_onlyTransformed.setChecked(True)
        #
        # self.rB_individualFiles = QtWidgets.QRadioButton('Individual files per building')
        # self.lGrid.addWidget(self.rB_individualFiles, 0, 9, 1, 3)
        # # self.rB_individualFiles.setEnabled(False)

        self.btn_outDir = QtWidgets.QPushButton('Select output path')
        self.lGrid.addWidget(self.btn_outDir, 0, 0, 1, 1)

        self.txtB_outDir = QtWidgets.QLineEdit()
        self.txtB_outDir.setPlaceholderText('Path to which new file should be written')
        self.lGrid.addWidget(self.txtB_outDir, 0, 1, 1, 4)

        self.expPath = os.path.join(inpDir, 'e3D_CityEnrich')
        self.txtB_outDir.setText(self.expPath)

        self.btn_save_enrichment = QtWidgets.QPushButton('Save as CityGML EnergyADE')
        self.lGrid.addWidget(self.btn_save_enrichment, 1, 0, 1, 1)
        # self.btn_toZero.setToolTip("requires ground surface coordinates")
        # if 1 in presenetLoDs or 2 in presenetLoDs:
        #     self.btn_toZero.setEnabled(True)
        # else:
        #     self.btn_toZero.setEnabled(False)
        #
        # self.btn_toOne = QtWidgets.QPushButton('Transform to LoD 1')
        # self.lGrid.addWidget(self.btn_toOne, 3, 4, 1, 4)
        # self.btn_toOne.setToolTip("requires ground surface coordinates and building height")
        # if 0 in presenetLoDs or 2 in presenetLoDs:
        #     self.btn_toOne.setEnabled(True)
        # else:
        #     self.btn_toOne.setEnabled(False)
        #
        # self.btn_toTwo = QtWidgets.QPushButton('Transform to LoD 2')
        # self.lGrid.addWidget(self.btn_toTwo, 3, 8, 1, 4)
        # self.btn_toOne.setToolTip("requires ground surface coordinates, building height (and roof height)")
        # if 0 in presenetLoDs or 1 in presenetLoDs:
        #     self.btn_toTwo.setEnabled(True)
        # else:
        #     self.btn_toTwo.setEnabled(False)

        self.lbl_enrich = QtWidgets.QLabel('Enrichment Progress')
        self.lGrid.addWidget(self.lbl_enrich, 2, 0, 1, 1)

        self.pB_enrichment = QtWidgets.QProgressBar(self)
        self.lGrid.addWidget(self.pB_enrichment, 2, 1, 1, 4)

        self.vbox.addLayout(self.lGrid)

        self.l2Grid = QtWidgets.QGridLayout()

        self.btn_about = QtWidgets.QPushButton('About')
        self.l2Grid.addWidget(self.btn_about, 0, 0, 1, 1)

        self.btn_reset = QtWidgets.QPushButton('Reset')
        self.l2Grid.addWidget(self.btn_reset, 0, 1, 1, 1)

        self.btn_exit = QtWidgets.QPushButton('Exit')
        self.l2Grid.addWidget(self.btn_exit, 0, 2, 1, 1)

        self.btn_back = QtWidgets.QPushButton('Back')
        self.l2Grid.addWidget(self.btn_back, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid)

        self.btn_construction.clicked.connect(self.func_construction)
        self.btn_save_enrichment.clicked.connect(self.func_enrich)
        self.btn_zone.clicked.connect(self.func_thermalzones)
        self.btn_about.clicked.connect(self.func_about)
        self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit.clicked.connect(self.func_exit)
        self.btn_back.clicked.connect(self.func_back)

        self.cB_curBuilding.currentTextChanged.connect(self.func_curBuildingChanged)

        self.lastBuilding = 'all (selected) buildings'
        self.completedTransform = 0
        self.inpDir = inpDir
        self.buildingParamsDict = buildingParamsDict
        self.buildingOverWrDict = buildingOverWrDict
        self.previousDisabled = []


    def func_getData(self):
        """collects all the data from all posible inputs"""




    def func_curBuildingChanged(self):
        """gets called when the current building changes"""
        # first save info to the last displayed building (at this point the comboBox already changed the text)
        cee.onSave(self, self.lastBuilding)

        # get right classes to hide
        if self.lastBuilding == "all (selected) buildings":
            thermalClass = self.buildingDict_all["thermalzones"]
            construClass = self.buildingDict_all["construction"]
        else:
            index = cee.getIndexFromBuildingDict(self, self.lastBuilding)
            thermalClass = self.buildingDict[index]["thermalzones"]
            construClass = self.buildingDict[index]["construction"]

        # hide windows of last building so the GUI is not everywhere
        thermalClass.hide()
        thermalClass.heating.hide()
        thermalClass.cooling.hide()
        thermalClass.ventilation.hide()
        thermalClass.appliances.hide()
        thermalClass.lighting.hide()
        thermalClass.occupancy.hide()
        construClass.hide()
        

        # then update the index of the last building
        self.lastBuilding = self.cB_curBuilding.currentText()

        if self.cB_curBuilding.currentIndex() != 0:
            try:
                index = cee.getIndexFromBuildingDict(self, self.cB_curBuilding.currentText())
            except:
                index = -1
        else:
            index = -1

        # get SET values from LoDScan
        try:
            sets = self.buildingDict[index]['values']
        except:
            sets = {'LoD': 'N/D', 'rType': 'N/D', 'bFunction': 'N/D', 'SAG': 'N/D', 'SBG': 'N/D', 'YOC': 'N/D',
                    'rHeight': 'N/D', 'rHeading': 'N/D', 'bHeight': 'N/D'}

        # get values from saving
        if index in self.buildingParamsDict:
            # values from previous safe
            values = self.buildingParamsDict[index]
            # adding "all (selected) buildings" values to the values that are going to be displayed
            if index != -1:
                # this compression gets the checks for parameters that have not been save to a building but are safed for all, so that the value is also displayed
                from_minus_one = {k: self.buildingParamsDict[-1][k] for k in self.buildingParamsDict[-1] if (values[k] == None and self.buildingParamsDict[-1][k] != None)}
                for k, v in from_minus_one.items():
                    values[k] = v
        else:
            # values from "all (selected) buildings"
            values = self.buildingParamsDict[-1]

        if sets["bHeight"] != 'N/D':
            self.txtB_buildingHeight.setText(str(sets["bHeight"]))
            self.txtB_buildingHeight.setEnabled(False)
        else:
            self.txtB_buildingHeight.setText('')
            self.txtB_buildingHeight.setEnabled(True)
            if values["bHeight"] != None:
                self.txtB_buildingHeight.setText(str(values["bHeight"]))

        if sets["rHeight"] != 'N/D':
            self.txtB_roofHeight.setText(str(sets["rHeight"]))
            self.txtB_roofHeight.setEnabled(False)
        else:
            self.txtB_roofHeight.setText('')
            self.txtB_roofHeight.setEnabled(True)
            if values["rHeight"] != None:
                self.txtB_buildingHeight.setText(str(values["rHeight"]))

        self.cB_roofType.clear()
        if sets["rType"] != 'N/D':
            self.cB_roofType.addItem(sets["rType"])
            self.cB_roofType.setEnabled(False)
        else:
            self.cB_roofType.addItems(
                ['', 'flat roof :      1000', 'monopitch roof : 1010', 'dual pent roof : 1020', 'gabled roof :    1030',
                 'hipped roof :    1040', 'pavilion roof :  1070'])
            self.cB_roofType.setCurrentIndex(0)
            self.cB_roofType.setEnabled(True)
            if values["rType"] != None:
                helpDict = {'1000': 1, '1010': 2, '1020': 3, '1030': 4, '1040': 5, '1070': 6}
                self.cB_roofType.setCurrentIndex(helpDict[values["rType"]])

        self.cB_heading.clear()
        if sets["rType"] == '1000' or sets["rType"] == '1040' or sets["rType"] == '1070':
            self.cB_heading.setEnabled(False)
        elif sets["rHeading"] == 'N/D':
            self.cB_heading.addItems(['', 'NORTHish', 'EASTish', 'SOUTHish', 'WESTish'])
            self.cB_heading.setEnabled(True)
            if values["rHeading"] != None:
                helpDict = {'NORTHish': 1, 'EASTish': 2, 'SOUTHish': 3, 'WESTish': 4}
                self.cB_heading.setCurrentIndex(helpDict[values["rHeading"]])
        elif type(sets["rHeading"]) == list:
            self.cB_heading.addItems(sets["rHeading"])
            self.cB_heading.setEnabled(True)
        else:
            self.cB_heading.addItem(str(sets["rHeading"]))
            self.cB_heading.setEnabled(False)

        self.cB_buildingFunction.clear()
        if sets["bFunction"] != 'N/D':
            self.cB_buildingFunction.addItem(sets["bFunction"])
            self.cB_buildingFunction.setEnabled(False)
        else:
            self.cB_buildingFunction.addItems(gf.createListForComboBox(buildingFunctions, 40))
            self.cB_buildingFunction.setEnabled(True)
            if values["bFunction"] != None:
                helpDict = {}
                self.cB_buildingFunction.setCurrentIndex(helpDict[values["bFunction"]])

        if sets["YOC"] != 'N/D':
            self.txtB_yearOfConstruction.setText(sets["YOC"])
            self.txtB_yearOfConstruction.setEnabled(False)
        else:
            self.txtB_yearOfConstruction.setText('')
            self.txtB_yearOfConstruction.setEnabled(True)
            if values["YOC"] != None:
                self.txtB_yearOfConstruction.setText(values["YOC"])

        if sets["SAG"] != 'N/D':
            self.txtB_SAG.setText(str(sets["SAG"]))
            self.txtB_SAG.setEnabled(False)
        else:
            self.txtB_SAG.setText('')
            self.txtB_SAG.setEnabled(True)
            if values["SAG"] != None:
                self.txtB_SAG.setText(str(values["SAG"]))

        if sets["SBG"] != 'N/D':
            self.txtB_SBG.setText(str(sets["SBG"]))
            self.txtB_SBG.setEnabled(False)
        else:
            self.txtB_SBG.setText('')
            self.txtB_SBG.setEnabled(True)
            if values["SBG"] != None:
                self.txtB_SAG.setText(str(values["SBG"]))



    def func_enrich(self):
        cee.onSave(self, self.lastBuilding)
        print("Starting Enrichment")
        start = time.time()
        cee.EnrichmentStart(self, selAll)
        end = time.time()
        print(end - start)
    # def func_toZero(self):
    #     print("to zero")
    #     start = time.time()
    #     # ldt.transformationStart(self, 0, selAll)
    #     end = time.time()
    #     print(end - start)
    #
    # def func_toOne(self):
    #     print("to one")
    #     start = time.time()
    #     # ldt.transformationStart(self, 1, selAll)
    #     end = time.time()
    #     print(end - start)
    #
    # def func_toTwo(self):
    #     print("to two")
    #     start = time.time()
    #     # ldt.transformationStart(self, 2, selAll)
    #     end = time.time()
    #     print(end - start)

    def func_about(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, about(), False)


    def get_right_class(self, type):
        """return the right dict to get the right thermalzones or construction class"""
        # get the right class here
        if self.cB_curBuilding.currentIndex() != 0:
            try:
                index = cee.getIndexFromBuildingDict(self, self.cB_curBuilding.currentText())
            except:
                index = -1
                print("error getting index")
        else:
            index = -1

        if index == -1:
            return self.buildingDict_all[type]
        else:
            return self.buildingDict[index][type]


    def func_thermalzones(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.get_right_class("thermalzones"), False)


    def func_construction(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.get_right_class("construction"), False)


    def func_reset(self):
        self.buildingParamsDict = {
            -1: {'LoD': None, 'rType': None, 'bFunction': None, 'SAG': None, 'SBG': None, 'YOC': None, 'rHeight': None,
                 'rHeading': None, 'bHeight': None}}
        self.buildingOverWrDict = {
            -1: {'LoD': None, 'rType': None, 'bFunction': None, 'SAG': None, 'SBG': None, 'YOC': None, 'rHeight': None,
                 'rHeading': None, 'bHeight': None}}
        self.cB_curBuilding.setCurrentIndex(0)
        self.cB_roofType.setCurrentIndex(0)
        self.cB_heading.setCurrentIndex(0)
        self.cB_buildingFunction.setCurrentIndex(0)
        self.txtB_buildingHeight.setText('')
        self.txtB_roofHeight.setText('')
        self.txtB_yearOfConstruction.setText('')
        self.txtB_SAG.setText('')
        self.txtB_SBG.setText('')

        # commenting out because there is no radioButton in this window
        # self.rB_onlyTransformed.setChecked(True)

        self.completedTransform = 0
        self.previousDisabled = []
        self.pB_enrichment.setValue(0)

        self.expPath = os.path.join(inpDir, 'e3D_CityEnrich')
        self.txtB_outDir.setText(self.expPath)

    def func_exit(self):
        gf.close_application(self)


    def func_back(self):
        global posx, posy, buildingParamsDict, buildingOverWrDict
        buildingParamsDict = self.buildingParamsDict
        buildingOverWrDict = self.buildingOverWrDict
        posx, posy = gf.dimensions(self)
        gf.next_window(self, mainWindow())


class thermalzones(QtWidgets.QWidget):
    def __init__(self):
        super(thermalzones, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityEnrich - Thermal Zones')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        self.gB_thermalzone = QtWidgets.QGroupBox('Thermal Zone Enrichment')
        self.vbox.addWidget(self.gB_thermalzone)
        self.vBox_forthermal = QtWidgets.QVBoxLayout()
        self.gB_thermalzone.setLayout(self.vBox_forthermal)

        # selection of parameters
        self.pGrid = QtWidgets.QGridLayout()

        self.lbl_floorarea = QtWidgets.QLabel('Floor Area')
        self.pGrid.addWidget(self.lbl_floorarea, 0, 0, 1, 1)

        self.txt_area = QtWidgets.QLineEdit('')
        self.txt_area.setPlaceholderText("Floor area in m2")
        self.pGrid.addWidget(self.txt_area, 0, 1, 1, 1)

        self.gB_thermalzone.setLayout(self.pGrid)

        self.rB_Grossfloorarea = QtWidgets.QRadioButton('Gross Floor Area')
        self.pGrid.addWidget(self.rB_Grossfloorarea, 0, 2, 1, 1)

        self.rB_netfloorarea = QtWidgets.QRadioButton('Net Floor Area')
        self.pGrid.addWidget(self.rB_netfloorarea, 0, 3, 1, 1)

        self.bG_one = QtWidgets.QButtonGroup()
        self.bG_one.addButton(self.rB_Grossfloorarea)
        self.bG_one.addButton(self.rB_netfloorarea)

        self.lbl_volume = QtWidgets.QLabel('Volume')
        self.pGrid.addWidget(self.lbl_volume, 1, 0, 1, 1)

        self.txt_volume = QtWidgets.QLineEdit('')
        self.txt_volume.setPlaceholderText("Volume in m3")
        self.pGrid.addWidget(self.txt_volume, 1, 1, 1, 1)

        self.rB_Grossvolume = QtWidgets.QRadioButton('Gross Volume')
        self.pGrid.addWidget(self.rB_Grossvolume, 1, 2, 1, 1)

        self.rB_netvolume = QtWidgets.QRadioButton('Net Volume')
        self.pGrid.addWidget(self.rB_netvolume, 1, 3, 1, 1)

        self.bG_two = QtWidgets.QButtonGroup()
        self.bG_two.addButton(self.rB_Grossvolume)
        self.bG_two.addButton(self.rB_netvolume)


        self.lbl_heated = QtWidgets.QLabel('Is heated:')
        self.pGrid.addWidget(self.lbl_heated, 2, 0, 1, 1)

        self.cB_heated = QtWidgets.QComboBox()
        self.cB_heated.setFont(QtGui.QFont("Consolas"))
        self.cB_heated.setToolTip('Is the building heated?')
        self.cB_heated.addItems(['', 'Yes', 'No'])
        self.pGrid.addWidget(self.cB_heated, 2, 1, 1, 1)

        self.lbl_cooled = QtWidgets.QLabel('Is cooled:')
        self.pGrid.addWidget(self.lbl_cooled, 2, 2, 1, 1)

        self.cB_cooled = QtWidgets.QComboBox()
        self.cB_cooled.setFont(QtGui.QFont("Consolas"))
        self.cB_cooled.setToolTip('Is the building cooled?')
        self.cB_cooled.addItems(['', 'Yes', 'No'])
        self.pGrid.addWidget(self.cB_cooled, 2, 3, 1, 1)
        self.vBox_forthermal.addLayout(self.pGrid)

        # usagezone
        self.gB_usagezone = QtWidgets.QGroupBox('Usage Zone - Schedules')
        self.vbox.addWidget(self.gB_usagezone)

        self.aGrid = QtWidgets.QGridLayout()
        self.gB_usagezone.setLayout(self.aGrid)

        self.btn_heating = QtWidgets.QPushButton('Heating')
        self.aGrid.addWidget(self.btn_heating, 0, 0, 1, 1)

        self.btn_cooling = QtWidgets.QPushButton('Cooling')
        self.aGrid.addWidget(self.btn_cooling, 0, 1, 1, 1)

        self.btn_ventilation = QtWidgets.QPushButton('Ventilation')
        self.aGrid.addWidget(self.btn_ventilation, 1, 0, 1, 1)

        self.btn_occupancy = QtWidgets.QPushButton('Occupancy')
        self.aGrid.addWidget(self.btn_occupancy, 1, 1, 1, 1)

        self.btn_lighting = QtWidgets.QPushButton('Lighting')
        self.aGrid.addWidget(self.btn_lighting, 2, 0, 1, 1)

        self.btn_appliances = QtWidgets.QPushButton('Appliances')
        self.aGrid.addWidget(self.btn_appliances, 2, 1, 1, 1)

        self.l2Grid = QtWidgets.QGridLayout()


        self.btn_reset = QtWidgets.QPushButton('Reset')
        self.l2Grid.addWidget(self.btn_reset, 0, 0, 1, 1)

        self.btn_close = QtWidgets.QPushButton('Close')
        self.l2Grid.addWidget(self.btn_close, 0, 1, 1, 1)

        self.vbox.addLayout(self.l2Grid)

        self.btn_heating.clicked.connect(self.func_heating_schedules)
        self.btn_cooling.clicked.connect(self.func_cooling_schedules)
        self.btn_ventilation.clicked.connect(self.func_ventilation_schedules)
        self.btn_occupancy.clicked.connect(self.func_occupancy_schedules)
        self.btn_appliances.clicked.connect(self.func_appliances_schedules)
        self.btn_lighting.clicked.connect(self.func_lighting_schedules)
        self.btn_reset.clicked.connect(self.func_reset)
        self.btn_close.clicked.connect(self.func_close)

        # create classes
        self.heating = base_schedules("Heating Schedules")
        self.cooling = base_schedules("Cooling Schedules")
        self.ventilation = base_schedules("Ventilation Schedules")

        self.appliances = crv_schedules("Appliances Schedules")
        self.lighting = crv_schedules("Lighting Schedules")

        self.occupancy = occupancy_schedules("Occupancy Schedules")
        
    def func_reset(self):
        """reseets GUI to defaults"""
        self.txt_area.setText("")
        self.rB_Grossfloorarea.setChecked(False)
        self.rB_netfloorarea.setChecked(False)
        self.txt_volume.setText("")
        self.rB_Grossvolume.setChecked(False)
        self.rB_netvolume.setChecked(False)
        self.cB_heated.setCurrentIndex(0)
        self.cB_cooled.setCurrentIndex(0)


    def func_heating_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.heating, False)

    def func_cooling_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.cooling, False)

    def func_ventilation_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.ventilation, False)

    def func_occupancy_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.occupancy, False)

    def func_appliances_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.appliances, False)

    def func_lighting_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, self.lighting, False)

    def func_close(self):
        """hides this window"""
        self.hide()




class construction(QtWidgets.QWidget):
    def __init__(self):
        super(construction, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width+100, height+100, pypath, 'CityEnrich - Construction Enrichment')

        # loading materials from file
        self.materials = pd.read_json("files from teaser+\MaterialTemplates.json")
        self.materialDict = {}
        for i in self.materials.columns:
            self.materialDict[self.materials[i]["name"]] = i

        self.num_layers_wall = 0
        self.layers_wall = {}

        self.num_layers_roof = 0
        self.layers_roof = {}

        self.num_layers_ground = 0
        self.layers_ground = {}

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)


        self.scrollArea = QtWidgets.QScrollArea(self)
        self.vbox.addWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QtWidgets.QWidget(self.scrollArea)
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.scrollLayout)


        self.scrollArea.setWidget(self.scrollContent)


        self.gB_enrichment_walls = QtWidgets.QGroupBox('Outer walls')
        self.scrollLayout.addWidget(self.gB_enrichment_walls)
        # #
        self.wallGrid = QtWidgets.QGridLayout()
        self.gB_enrichment_walls.setLayout(self.wallGrid)

        self.lbl_description_walls = QtWidgets.QLabel('Description:') #ToDo: Currently it is just a combobox
        self.wallGrid.addWidget(self.lbl_description_walls, 0, 0, 1, 1)

        self.vbox_wallLayers = QtWidgets.QVBoxLayout()
        self.wallGrid.addLayout(self.vbox_wallLayers, 1, 0, 1, 4)


        self.btn_wall_removeLayer = QtWidgets.QPushButton("remove layer")
        self.wallGrid.addWidget(self.btn_wall_removeLayer, 2, 2, 1, 1)
        
        self.btn_wall_addLayer = QtWidgets.QPushButton("add layer")
        self.wallGrid.addWidget(self.btn_wall_addLayer, 2, 3, 1, 1)


        self.lbl_uvalue_walls = QtWidgets.QLabel('U-value [W/(m^2K)]:')
        self.wallGrid.addWidget(self.lbl_uvalue_walls, 3, 0, 1, 1)

        self.txt_uvalue_walls = QtWidgets.QLineEdit('')
        self.wallGrid.addWidget(self.txt_uvalue_walls, 3, 1, 1, 3)


        #Roof
        self.gB_enrichment_roof = QtWidgets.QGroupBox('Roof')
        self.scrollLayout.addWidget(self.gB_enrichment_roof)
        # #
        self.roofGrid = QtWidgets.QGridLayout()
        self.gB_enrichment_roof.setLayout(self.roofGrid)

        self.lbl_description_roof = QtWidgets.QLabel('Description:')  # ToDo: Currently it is just a combobox
        self.roofGrid.addWidget(self.lbl_description_roof, 0, 0, 1, 1)

        self.vbox_roofLayers = QtWidgets.QVBoxLayout()
        self.roofGrid.addLayout(self.vbox_roofLayers, 1, 0, 1, 4)

        self.btn_roof_removeLayer = QtWidgets.QPushButton("remove layer")
        self.roofGrid.addWidget(self.btn_roof_removeLayer, 2, 2, 1, 1)
        
        self.btn_roof_addLayer = QtWidgets.QPushButton("add layer")
        self.roofGrid.addWidget(self.btn_roof_addLayer, 2, 3, 1, 1)


        self.lbl_uvalue_roof = QtWidgets.QLabel('U-value [W/(m^2K)]:')
        self.roofGrid.addWidget(self.lbl_uvalue_roof, 3, 0, 1, 1)

        self.txt_uvalue_roof = QtWidgets.QLineEdit('')
        self.roofGrid.addWidget(self.txt_uvalue_roof, 3, 1, 1, 3)

        # Ground Slab
        self.gB_enrichment_ground = QtWidgets.QGroupBox('Ground')
        self.scrollLayout.addWidget(self.gB_enrichment_ground)
        # #
        self.groundGrid = QtWidgets.QGridLayout()
        self.gB_enrichment_ground.setLayout(self.groundGrid)

        self.lbl_description_ground = QtWidgets.QLabel('Description:')  # ToDo: Currently it is just a combobox
        self.groundGrid.addWidget(self.lbl_description_ground, 0, 0, 1, 1)

        self.vbox_groundLayers = QtWidgets.QVBoxLayout()
        self.groundGrid.addLayout(self.vbox_groundLayers, 1, 0, 1, 4)

        self.btn_ground_removeLayer = QtWidgets.QPushButton("remove layer")
        self.groundGrid.addWidget(self.btn_ground_removeLayer, 2, 2, 1, 1)
        
        self.btn_ground_addLayer = QtWidgets.QPushButton("add layer")
        self.groundGrid.addWidget(self.btn_ground_addLayer, 2, 3, 1, 1)

        self.lbl_uvalue_ground = QtWidgets.QLabel('U-value [W/(m^2K)]:')
        self.groundGrid.addWidget(self.lbl_uvalue_ground, 3, 0, 1, 1)

        self.txt_uvalue_ground = QtWidgets.QLineEdit('')
        self.groundGrid.addWidget(self.txt_uvalue_ground, 3, 1, 1, 3)


        #Windows
        self.gB_enrichment_windows = QtWidgets.QGroupBox('Windows')
        self.scrollLayout.addWidget(self.gB_enrichment_windows)
        # #
        self.windowsGrid = QtWidgets.QGridLayout()
        self.gB_enrichment_windows.setLayout(self.windowsGrid)

        self.lbl_window2wallRatio = QtWidgets.QLabel("Window to wall ratio [%]:")
        self.windowsGrid.addWidget(self.lbl_window2wallRatio, 0, 0, 1, 1)
        # values between 0 and 100

        self.txt_window2wallRatio = QtWidgets.QLineEdit('')
        self.windowsGrid.addWidget(self.txt_window2wallRatio, 0, 1, 1, 1)

        self.lbl_transmittanceFraction_windows = QtWidgets.QLabel('Transmittance Fraction:')
        self.windowsGrid.addWidget(self.lbl_transmittanceFraction_windows, 0, 2, 1, 1)
        # values between 0 and 1

        self.txt_transmittance_fraction_windows = QtWidgets.QLineEdit('')  # ToDo: Based on the description combo?
        self.windowsGrid.addWidget(self.txt_transmittance_fraction_windows, 0, 3, 1, 1)

        self.lbl_uvalue_windows = QtWidgets.QLabel('U-value [W/(m^2K)]:')  # ToDo: Currently it is just a combobox
        self.windowsGrid.addWidget(self.lbl_uvalue_windows, 1, 0, 1, 1)

        self.txt_uvalue_windows = QtWidgets.QLineEdit('')
        self.windowsGrid.addWidget(self.txt_uvalue_windows, 1, 1, 1, 1)

        self.lbl_glazingratio_windows = QtWidgets.QLabel('Glazing Ratio:')
        self.windowsGrid.addWidget(self.lbl_glazingratio_windows, 1, 2, 1, 1)

        self.txt_glazingratio_windows = QtWidgets.QLineEdit('')
        self.windowsGrid.addWidget(self.txt_glazingratio_windows, 1, 3, 1, 1)


        self.l2Grid = QtWidgets.QGridLayout()


        self.btn_reset = QtWidgets.QPushButton('Reset')
        self.l2Grid.addWidget(self.btn_reset, 0, 0, 1, 1)


        self.btn_close = QtWidgets.QPushButton('Close')
        self.l2Grid.addWidget(self.btn_close, 0, 1, 1, 1)

        self.vbox.addLayout(self.l2Grid)


        self.btn_reset.clicked.connect(self.func_reset)
        self.btn_close.clicked.connect(self.func_close)

        self.btn_wall_addLayer.clicked.connect(functools.partial(self.func_addLayer, "wall"))
        self.btn_wall_removeLayer.clicked.connect(functools.partial(self.func_removeLayer, "wall"))

        self.btn_roof_addLayer.clicked.connect(functools.partial(self.func_addLayer, "roof"))
        self.btn_roof_removeLayer.clicked.connect(functools.partial(self.func_removeLayer, "roof"))

        self.btn_ground_addLayer.clicked.connect(functools.partial(self.func_addLayer, "ground"))
        self.btn_ground_removeLayer.clicked.connect(functools.partial(self.func_removeLayer, "ground"))


        self.func_addLayer("wall")
        self.func_addLayer("roof")
        self.func_addLayer("ground")



    def func_close(self):
        """hides this window"""
        self.hide()



    def func_reset(self):
        """resets window to default"""
        while self.num_layers_wall > 0:
            self.func_removeLayer("wall")
        self.func_addLayer("wall")

        while self.num_layers_roof > 0:
            self.func_removeLayer("roof")
        self.func_addLayer("roof")

        while self.num_layers_ground > 0:
            self.func_removeLayer("ground")
        self.func_addLayer("ground")

        for txtBox in [self.txt_window2wallRatio, self.txt_transmittance_fraction_windows, self.txt_uvalue_windows, self.txt_glazingratio_windows]:
            txtBox.setText('')
            



    def calculate_U_value(self, target, _x) -> None:
        """calculates the u value of a wall roof or ground slab"""

        if target == "wall":
            r_si = 0.13
            r_se = 0.04
            layers = self.layers_wall
            txtBox = self.txt_uvalue_walls
        elif target == "roof":
            r_si = 0.10
            r_se = 0.04
            layers = self.layers_roof
            txtBox = self.txt_uvalue_roof
        elif target == "ground":
            r_si = 0.17
            r_se = 0.04
            layers = self.layers_ground
            txtBox = self.txt_uvalue_ground
        
        sum = 0 # sum of heat transfer resistances of all layers
        for _key, layer in layers.items():
            material = layer["cB_material"].currentText()
            if material == '':
                continue
            id = self.materialDict[material]
            thermal_conduc =  self.materials[id]["thermal_conduc"]
            thickness = layer["sB_thickness"].value()
            sum += thickness / thermal_conduc
        
        if sum == 0:
            u = ''
        else:
            u = str(1 / (r_si + sum + r_se))

        txtBox.setText(u)
        if u != '':
            txtBox.setEnabled(False)
        else:
            txtBox.setEnabled(True)
    


    def func_addLayer(self, target):
        """function adds inputs for an additional target layer"""
        layer = {}

        if target == "wall":
            vbox = self.vbox_wallLayers
            num_of_layers = self.num_layers_wall
        elif target == "roof":
            vbox = self.vbox_roofLayers
            num_of_layers = self.num_layers_roof
        elif target == "ground":
            vbox = self.vbox_groundLayers
            num_of_layers = self.num_layers_ground
        
        layer["gB"] = QtWidgets.QGroupBox(f'Layer {str(num_of_layers + 1)}')
        vbox.insertWidget(-1, layer["gB"])
        
        layer["layout"] = QtWidgets.QGridLayout()
        layer["gB"].setLayout(layer["layout"])

        layer["lbl_material"] = QtWidgets.QLabel('Selected Material:')
        layer["layout"].addWidget(layer["lbl_material"], 0, 0, 1, 1)

        layer["cB_material"] = QtWidgets.QComboBox()
        layer["cB_material"].addItems(self.materialDict.keys())
        layer["cB_material"].currentTextChanged.connect(functools.partial(self.calculate_U_value, target))
        layer["layout"].addWidget(layer["cB_material"], 0, 1, 1, 1)


        layer["lbl_thickness"] = QtWidgets.QLabel('Thickness [m]:')
        layer["layout"].addWidget(layer["lbl_thickness"], 0, 2, 1, 1)

        layer["sB_thickness"] = QtWidgets.QDoubleSpinBox()
        layer["sB_thickness"].setDecimals(3)
        layer["sB_thickness"].setRange(0.001, 2)
        layer["sB_thickness"].setSingleStep(0.001)
        layer["sB_thickness"].setValue(0.01)
        layer["sB_thickness"].valueChanged.connect(functools.partial(self.calculate_U_value, target))
        layer["layout"].addWidget(layer["sB_thickness"], 0, 3, 1, 1)


        if target == "wall":
            self.layers_wall[str(num_of_layers)] = layer
            self.num_layers_wall -=- 1
        elif target == "roof":
            self.layers_roof[str(num_of_layers)] = layer
            self.num_layers_roof -=- 1
        elif target == "ground":
            self.layers_ground[str(num_of_layers)] = layer
            self.num_layers_ground -=- 1



    def func_removeLayer(self, target):
        """removes last layer from target and recalculates the u value"""

        if target == "wall":
            layer_dict = self.layers_wall
            num_of_layers = self.num_layers_wall
        elif target == "roof":
            layer_dict = self.layers_roof
            num_of_layers = self.num_layers_roof
        elif target == "ground":
            layer_dict = self.layers_ground
            num_of_layers = self.num_layers_ground

        if num_of_layers == 0:
            return

        for i in ["sB_thickness", "lbl_thickness", "cB_material", "lbl_material", "gB"]:
            layer_dict[str(num_of_layers-1)][i].setParent(None)

        if target == "wall":
            del self.layers_wall[str(num_of_layers-1)]
            self.num_layers_wall -= 1
        elif target == "roof":
            del self.layers_roof[str(num_of_layers-1)]
            self.num_layers_roof -= 1
        elif target == "ground":
            del self.layers_ground[str(num_of_layers-1)]
            self.num_layers_ground -= 1
        self.calculate_U_value(target, None)
        



class base_schedules(QtWidgets.QWidget):
    """
    base class for schedules
    currently planed to be used with: heating, cooling & ventilation
    """
    def __init__(self, title= "unnamed base_schedules"):
        super().__init__()
        self.title = title

        global posx, posy, width, height, sizefactor
        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, f'CityEnrich - {self.title}')
        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)


        self.gB_schedule = QtWidgets.QGroupBox(self.title)
        self.vbox.addWidget(self.gB_schedule)
        self.mGrid = QtWidgets.QGridLayout()
        self.gB_schedule.setLayout(self.mGrid)


        self.lbl_date_begin = QtWidgets.QLabel('Start Date:')
        self.mGrid.addWidget(self.lbl_date_begin, 0, 0, 1, 1)

        self.dE_date_start = QtWidgets.QDateEdit()
        self.dE_date_start.setCalendarPopup(True)
        self.dE_date_start.setDisplayFormat("yyyy-MM-dd")
        self.dE_date_start.setDate(QtCore.QDate.fromString("2022-01-01", "yyyy-MM-dd"))
        self.mGrid.addWidget(self.dE_date_start, 0, 1, 1, 1)

        self.lbl_date_end = QtWidgets.QLabel('End Date:')
        self.mGrid.addWidget(self.lbl_date_end, 0, 2, 1, 1)

        self.dE_date_end = QtWidgets.QDateEdit()
        self.dE_date_end.setCalendarPopup(True)
        self.dE_date_end.setDisplayFormat("yyyy-MM-dd")
        self.dE_date_end.setDate(QtCore.QDate.fromString("2022-12-31", "yyyy-MM-dd"))
        self.mGrid.addWidget(self.dE_date_end, 0, 3, 1, 1)

        self.lbl_hour_begin = QtWidgets.QLabel('Begin Hour:')
        self.mGrid.addWidget(self.lbl_hour_begin, 1, 0, 1, 1)

        self.tE_time_start = QtWidgets.QTimeEdit()
        self.tE_time_start.setDisplayFormat("hh:mm:ss")
        self.tE_time_start.setTime(QtCore.QTime.fromString("00:00:00", "hh:mm:ss"))
        self.mGrid.addWidget(self.tE_time_start, 1, 1, 1, 1)

        self.lbl_hour_end = QtWidgets.QLabel('End Hour:')
        self.mGrid.addWidget(self.lbl_hour_end, 1, 2, 1, 1)

        self.tE_time_end = QtWidgets.QTimeEdit()
        self.tE_time_end.setDisplayFormat("hh:mm:ss")
        self.tE_time_end.setTime(QtCore.QTime.fromString("23:59:59", "hh:mm:ss"))
        self.mGrid.addWidget(self.tE_time_end, 1, 3, 1, 1)

        self.lbl_interpolation_type = QtWidgets.QLabel('Interpolation Type')  # ToDo: (Max) do we make the unit separate?
        self.mGrid.addWidget(self.lbl_interpolation_type, 2, 0, 1, 1)

        self.cB_interpolation = QtWidgets.QComboBox()  # ToDo: (Max) May be a dropdown?; (Simon) Add selection
        self.cB_interpolation.addItems(["", "averageInPrecedingInterval", "averageInSucceedingInterval", "constantInPrecedingInterval", "constantInSucceedingInterval", "continuous", "discontinuous", "instantaneousTotal", "maximumInPrecedingInterval", "maximumInSucceedingInterval", "minimumInPrecedingInterval", "minimumInSucceedingInterval", "precedingTotal", "succeedingTotal"])
        self.mGrid.addWidget(self.cB_interpolation, 2, 1, 1, 1)

        self.lbl_acquisition_method = QtWidgets.QLabel('Acquisition Method:')
        self.mGrid.addWidget(self.lbl_acquisition_method, 2, 2, 1, 1)

        self.cB_acquisition_method = QtWidgets.QComboBox()  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.cB_acquisition_method.addItems(["", "measurement", "simulation", "calibratedSimulation", "estimation"," unknown"])
        self.mGrid.addWidget(self.cB_acquisition_method, 2, 3, 1, 1)

        self.lbl_thematic_description = QtWidgets.QLabel('Thematic Description:')
        self.mGrid.addWidget(self.lbl_thematic_description, 3, 0, 1, 1)

        self.txt_thematic_description = QtWidgets.QLineEdit('')  # ToDo: (Max) what do wanna add here?
        self.mGrid.addWidget(self.txt_thematic_description, 3, 1, 1, 3)

        self.btn_wkday = QtWidgets.QPushButton("Select file for weekdays")
        self.mGrid.addWidget(self.btn_wkday, 4, 0, 1, 1)

        self.txt_wkday = QtWidgets.QLineEdit("")
        self.txt_wkday.setEnabled(False)
        self.mGrid.addWidget(self.txt_wkday, 4, 1, 1, 3)

        self.btn_wkend = QtWidgets.QPushButton("Select file for weekends")
        self.mGrid.addWidget(self.btn_wkend, 5, 0, 1, 1)

        self.txt_wkend = QtWidgets.QLineEdit("")
        self.txt_wkend.setEnabled(False)
        self.mGrid.addWidget(self.txt_wkend, 5, 1, 1, 3)
        
        self.lbl_unit = QtWidgets.QLabel('Unit:')
        self.mGrid.addWidget(self.lbl_unit, 6, 0, 1, 1)

        self.txt_unit = QtWidgets.QLineEdit('') # ToDo: (Max) Dropdown?
        self.mGrid.addWidget(self.txt_unit, 6, 1, 1, 1)

        self.radio_SIunit = QtWidgets.QRadioButton('SI')
        self.mGrid.addWidget(self.radio_SIunit, 6, 2, 1, 1)

        self.radio_fraction_unit = QtWidgets.QRadioButton('Fraction')
        self.mGrid.addWidget(self.radio_fraction_unit, 6, 3, 1, 1)


        self.lGrid = QtWidgets.QGridLayout()


        self.btn_reset = QtWidgets.QPushButton('Reset') #ToDo: (Simon) Add functionalities to reset
        self.lGrid.addWidget(self.btn_reset, 0, 0, 1, 1)

        self.btn_close = QtWidgets.QPushButton('Close') #ToDo: (Simon) Add functionalities to back
        self.lGrid.addWidget(self.btn_close, 0, 1, 1, 1)

        self.vbox.addLayout(self.lGrid)

        self.btn_reset.clicked.connect(self.func_reset)
        self.btn_close.clicked.connect(self.func_close)

        self.btn_wkday.clicked.connect(functools.partial(self.func_read_schedule, self.txt_wkday))
        self.btn_wkend.clicked.connect(functools.partial(self.func_read_schedule, self.txt_wkend))
    
    def func_read_schedule(self, txtB):
        """reads a file using QFileDialog"""
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Select .gml or .xml file')[0]
        if path != '' and os.path.isfile(path):
            with open(path, "r") as f:
                content = f.read()
            txtB.setText(content)



    def func_reset(self):
        """resets all inputs in window"""
        reset_inputs(self)

    def func_close(self):
        """hides this window"""
        self.hide()


class crv_schedules(base_schedules):
    """
    expanding base_schedules with more inputs:
    Convective fraction
    Radiant fraction
    total Value
    currently planed to be used with: lighting and appliances (and to be extend for occupancy)
    """
    def __init__(self, title= "unnamed crv_schedules"):
        super().__init__(title)

        self.lbl_convectiveFraction = QtWidgets.QLabel('Convective Fraction:')
        self.mGrid.addWidget(self.lbl_convectiveFraction, 7, 0, 1, 1)

        self.txt_convectiveFraction = QtWidgets.QLineEdit('')
        self.mGrid.addWidget(self.txt_convectiveFraction, 7, 1, 1, 1)

        self.lbl_radiantFraction = QtWidgets.QLabel('Radiant Fraction:')
        self.mGrid.addWidget(self.lbl_radiantFraction, 7, 2, 1, 1)

        self.txt_radiantFraction = QtWidgets.QLineEdit('')
        self.mGrid.addWidget(self.txt_radiantFraction, 7, 3, 1, 1)

        self.lbl_totalValue = QtWidgets.QLabel('Total Value:')
        self.mGrid.addWidget(self.lbl_totalValue, 8, 0, 1, 1)

        self.txt_totalValue = QtWidgets.QLineEdit('')
        self.mGrid.addWidget(self.txt_totalValue, 8, 1, 1, 1)



class occupancy_schedules(crv_schedules):
    """
    expanding crv_schedules with more inputs:
    number of occupants
    currently planed to be used with: occupancy
    """
    def __init__(self, title= "unnamed occupancy_schedules"):
        super().__init__(title)

        self.lbl_numberOccupant = QtWidgets.QLabel('Number of Occupants:')
        self.mGrid.addWidget(self.lbl_numberOccupant, 8, 2, 1, 1)

        self.txt_numberOccupant = QtWidgets.QLineEdit('')
        self.mGrid.addWidget(self.txt_numberOccupant, 8, 3, 1, 1)




class about(QtWidgets.QWidget):
    def __init__(self):
        super(about, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityBIT - About')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        self.textwidget = QtWidgets.QTextBrowser()
        self.vbox.addWidget(self.textwidget)
        self.textwidget.setFontPointSize(14)
        with open(os.path.join(pypath, 'about/about.txt'), 'r') as file:
            text = file.read()
        self.textwidget.setText(text)

        self.lGrid = QtWidgets.QGridLayout()

        self.btn_repo = QtWidgets.QPushButton('Open repository')
        self.lGrid.addWidget(self.btn_repo, 0, 0, 1, 1)

        self.btn_close = QtWidgets.QPushButton('Close')
        self.lGrid.addWidget(self.btn_close, 0, 1, 1, 1)

        self.vbox.addLayout(self.lGrid)

        self.btn_repo.clicked.connect(self.open_repo)
        self.btn_close.clicked.connect(self.close_about)

    def open_repo(self):
        os.startfile('www.e3d.rwth-aachen.de')

    def close_about(self):
        self.hide()



def reset_inputs(self):
    """aims to reset all widgets of type: QLineEdit, QComboBox, QRadioButton (also in child elements; sorry for recursion)"""
    for i in self.children():
        if isinstance(i, QtWidgets.QVBoxLayout) or isinstance(i, QtWidgets.QGridLayout) or isinstance(i, QtWidgets.QGroupBox):
            reset_inputs(i)
        elif isinstance(i, QtWidgets.QLineEdit):
            i.setText("")
        elif isinstance(i, QtWidgets.QComboBox):
            i.setCurrentIndex(0)
        elif isinstance(i, QtWidgets.QRadioButton):
            i.setChecked(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("QLabel{font-size: 10pt;} QPushButton{font-size: 10pt;} QRadioButton{font-size: 10pt;} QGroupBox{font-size: 10pt;} QComboBox{font-size: 10pt;} QLineEdit{font-size: 10pt;}")
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec_())

