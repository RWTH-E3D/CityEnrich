

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
# import LDTtransformation as ldt


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

        presenetLoDs = []
        # adding selected buildings to the comboBox
        for key in buildingDict:
            if selAll:
                self.cB_curBuilding.insertItem(self.cB_curBuilding.count(),
                                               buildingDict[key]["filename"] + "/" + buildingDict[key]["buildingname"])
                if buildingDict[key]["values"]["LoD"] not in presenetLoDs:
                    presenetLoDs.append(buildingDict[key]["values"]["LoD"])
            elif buildingDict[key]["selected"]:
                self.cB_curBuilding.insertItem(self.cB_curBuilding.count(),
                                               buildingDict[key]["filename"] + "/" + buildingDict[key]["buildingname"])
                if buildingDict[key]["values"]["LoD"] not in presenetLoDs:
                    presenetLoDs.append(buildingDict[key]["values"]["LoD"])
            else:
                pass
        self.buildingDict = buildingDict

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


        self.p2Grid = QtWidgets.QGridLayout()

        self.spacer = QtWidgets.QLabel('')
        self.p2Grid.addWidget(self.spacer, 0, 0, 1, 2)

        self.btn_overwrite = QtWidgets.QPushButton('Enable overwrite')
        self.p2Grid.addWidget(self.btn_overwrite, 0, 0, 1, 1)
        self.btn_overwrite.setEnabled(True)

        self.btn_saveBuildingParams = QtWidgets.QPushButton('Save building parameters')
        self.p2Grid.addWidget(self.btn_saveBuildingParams, 0, 3, 1, 1)

        self.vBox_forBPgB.addLayout(self.p2Grid)

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

        self.btn_saveBuildingParams.clicked.connect(self.func_save)
        self.btn_overwrite.clicked.connect(self.func_overwrite)
        self.btn_construction.clicked.connect(self.func_construction)
        # self.btn_toZero.clicked.connect(self.func_toZero)
        # self.btn_toOne.clicked.connect(self.func_toOne)
        self.btn_zone.clicked.connect(self.func_thermalzones)
        self.btn_about.clicked.connect(self.func_about)
        self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit.clicked.connect(self.func_exit)
        self.btn_back.clicked.connect(self.func_back)

        self.cB_curBuilding.currentTextChanged.connect(self.func_curBuildingChanged)

        self.completedTransform = 0
        self.inpDir = inpDir
        self.buildingParamsDict = buildingParamsDict
        self.buildingOverWrDict = buildingOverWrDict
        self.overWriteFlag = False
        self.previousDisabled = []

    def func_curBuildingChanged(self):
        """gets called when the current building changes"""
        self.overWriteFlag = False
        if self.cB_curBuilding.currentIndex() != 0:
            try:
                index = sel.getIndexFromBuildingDict(self, self.cB_curBuilding.currentText())
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

        # values from previous overwrite
        if index in self.buildingOverWrDict:
            setX = self.buildingOverWrDict[index]
            for i in setX:
                if setX[i] == None:
                    setX[i] = sets[i]
            sets = setX

        # get values from saving
        if index in self.buildingParamsDict:
            # values from previous safe
            values = self.buildingParamsDict[index]
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

    def overwriteChange(self, state):
        if state:
            self.btn_overwrite.setText('Disable overwrite')
            color = "green"
        else:
            self.btn_overwrite.setText('Enable overwrite')
            color = "light gray"
        txt = "background-color: " + color
        self.btn_overwrite.setStyleSheet(txt)
        self.overWriteFlag = state
        toChange = [self.txtB_buildingHeight, self.txtB_roofHeight, self.txtB_yearOfConstruction, self.txtB_SAG,
                    self.txtB_SBG]

        if state:
            self.previousDisabled = []
            for i in toChange:
                if not i.isEnabled():
                    self.previousDisabled.append(i)
                    i.setEnabled(True)
        else:
            for i in self.previousDisabled:
                i.setEnabled(False)

    def func_overwrite(self):
        self.overwriteChange(not self.overWriteFlag)

    def func_toZero(self):
        print("to zero")
        start = time.time()
        # ldt.transformationStart(self, 0, selAll)
        end = time.time()
        print(end - start)

    def func_toOne(self):
        print("to one")
        start = time.time()
        # ldt.transformationStart(self, 1, selAll)
        end = time.time()
        print(end - start)

    def func_toTwo(self):
        print("to two")
        start = time.time()
        # ldt.transformationStart(self, 2, selAll)
        end = time.time()
        print(end - start)

    def func_about(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, about(), False)

    def func_thermalzones(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, thermalzones(), False)

    def func_construction(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, construction(), False)


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

        self.rB_onlyTransformed.setChecked(True)

        self.completedTransform = 0
        self.overWriteFlag = False
        self.previousDisabled = []
        self.pB_enrichment.setValue(0)

        self.expPath = os.path.join(inpDir, 'e3D_CityEnrich')
        self.txtB_outDir.setText(self.expPath)

    def func_exit(self):
        gf.close_application(self)

    def func_save(self):
        # ldt.onSave(self)
        self.overwriteChange(False)

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

        self.vBox_forthermal.addWidget(self.gB_thermalzone)
        self.gB_thermalzone.setLayout(self.pGrid)
        self.rB_Grossfloorarea = QtWidgets.QRadioButton('Gross Floor Area')
        self.pGrid.addWidget(self.rB_Grossfloorarea, 0, 2, 1, 1)

        self.rB_netfloorarea = QtWidgets.QRadioButton('Net Floor Area')
        self.pGrid.addWidget(self.rB_netfloorarea, 0, 3, 1, 1)

        self.lbl_volume = QtWidgets.QLabel('Volume')
        self.pGrid.addWidget(self.lbl_volume, 1, 0, 1, 1)

        self.txt_volume = QtWidgets.QLineEdit('')
        self.txt_volume.setPlaceholderText("Volume in m3")
        self.pGrid.addWidget(self.txt_volume, 1, 1, 1, 1)

        self.rB_Grossvolume = QtWidgets.QRadioButton('Gross Volume')
        self.pGrid.addWidget(self.rB_Grossvolume, 1, 2, 1, 1)

        self.rB_netvolume = QtWidgets.QRadioButton('Net Volume')
        self.pGrid.addWidget(self.rB_netvolume, 1, 3, 1, 1)

        self.lbl_heated = QtWidgets.QLabel('Is heated:')
        self.pGrid.addWidget(self.lbl_heated, 2, 0, 1, 1)

        self.cB_heated = QtWidgets.QComboBox()
        self.cB_heated.setFont(QtGui.QFont("Consolas"))
        self.cB_heated.setToolTip('Is the building heated?')
        self.cB_heated.addItems([' ', 'Yes', 'No'])
        self.pGrid.addWidget(self.cB_heated, 2, 1, 1, 1)

        self.lbl_cooled = QtWidgets.QLabel('Is cooled:')
        self.pGrid.addWidget(self.lbl_cooled, 2, 2, 1, 1)

        self.cB_cooled = QtWidgets.QComboBox()
        self.cB_cooled.setFont(QtGui.QFont("Consolas"))
        self.cB_cooled.setToolTip('Is the building cooled?')
        self.cB_cooled.addItems([' ', 'Yes', 'No'])
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

        self.btn_about = QtWidgets.QPushButton('About')
        self.l2Grid.addWidget(self.btn_about, 0, 0, 1, 1)

        self.btn_reset = QtWidgets.QPushButton('Reset')
        self.l2Grid.addWidget(self.btn_reset, 0, 1, 1, 1)

        self.btn_exit = QtWidgets.QPushButton('Exit')
        self.l2Grid.addWidget(self.btn_exit, 0, 2, 1, 1)

        self.btn_back = QtWidgets.QPushButton('Back')
        self.l2Grid.addWidget(self.btn_back, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid)

        self.btn_heating.clicked.connect(self.func_heating_schedules)
        self.btn_cooling.clicked.connect(self.func_cooling_schedules)
        self.btn_ventilation.clicked.connect(self.func_ventilation_schedules)
        self.btn_occupancy.clicked.connect(self.func_occupancy_schedules)
        self.btn_appliances.clicked.connect(self.func_appliances_schedules)
        self.btn_lighting.clicked.connect(self.func_lighting_schedules)
        self.btn_about.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

    def func_about(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, about(), False)

    def func_heating_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, heating_schedules(), False)

    def func_cooling_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, cooling_schedules(), False)

    def func_ventilation_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, ventilation_schedules(), False)

    def func_occupancy_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, occupancy_schedules(), False)

    def func_appliances_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, appliances_schedules(), False)

    def func_lighting_schedules(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, lighting_schedules(), False)

    def func_exit(self):
        gf.close_application(self)

class construction(QtWidgets.QWidget):
    def __init__(self):
        super(construction, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width+100, height+100, pypath, 'CityEnrich - Thermal Zones')

        # loading materials from file
        self.materials = pd.read_json("files from teaser+\MaterialTemplates.json")
        self.materialNames = []
        for i in self.materials.columns:
            self.materialNames.append(self.materials[i]["name"])

        self.num_layers_wall = 0
        self.layers_wall = {}

        self.num_layers_roof = 0
        self.layers_roof = {}

        self.num_layers_ground = 0
        self.layers_ground = {}

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        # gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # # grid layout for file selection
        # self.uGrid = QtWidgets.QGridLayout()

        # self.vbox.addLayout(self.uGrid)
        self.gB_construction = QtWidgets.QGroupBox('Construction Enrichment')
        self.vbox.addWidget(self.gB_construction)
        self.vBox_forconstruction = QtWidgets.QVBoxLayout()
        self.gB_construction.setLayout(self.vBox_forconstruction)
        # ToDo: from here much of the buttons are currently as placeholders in this class
        # # walls enrichment

        # self.btn_enrichment_walls = QtWidgets.QPushButton('Walls')
        # self.vBox_forconstruction.addWidget(self)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.vBox_forconstruction.addWidget(self.scrollArea)
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

        # self.gB_layers_walls = QtWidgets.QGroupBox('Layer 1')
        # self.wallGrid.addWidget(self.gB_layers_walls, 1, 0, 1, 4)
        # #
        # self.aGrid_walls = QtWidgets.QGridLayout()
        # self.gB_layers_walls.setLayout(self.aGrid_walls)

        # self.lbl_material_layers_walls = QtWidgets.QLabel('Selected Material:')
        # self.aGrid_walls.addWidget(self.lbl_material_layers_walls, 0, 0, 1, 1)

        # self.txt_material_layers_walls = QtWidgets.QLineEdit('')
        # self.aGrid_walls.addWidget(self.txt_material_layers_walls, 0, 1, 1, 1)

        # self.lbl_thickness_layers_walls = QtWidgets.QLabel('Thickness:')
        # self.aGrid_walls.addWidget(self.lbl_thickness_layers_walls, 0, 2, 1, 1)

        # self.txt_thickness_layers_walls = QtWidgets.QLineEdit('')
        # self.aGrid_walls.addWidget(self.txt_thickness_layers_walls, 0, 3, 1, 1)

        self.btn_wall_removeLayer = QtWidgets.QPushButton("remove layer")
        self.wallGrid.addWidget(self.btn_wall_removeLayer, 2, 2, 1, 1)
        
        self.btn_wall_addLayer = QtWidgets.QPushButton("add layer")
        self.wallGrid.addWidget(self.btn_wall_addLayer, 2, 3, 1, 1)


        self.lbl_uvalue_walls = QtWidgets.QLabel('U-value:')
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


        self.lbl_uvalue_roof = QtWidgets.QLabel('U-value:')
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

        self.lbl_uvalue_ground = QtWidgets.QLabel('U-value:')
        self.groundGrid.addWidget(self.lbl_uvalue_ground, 3, 0, 1, 1)

        self.txt_uvalue_ground = QtWidgets.QLineEdit('')
        self.groundGrid.addWidget(self.txt_uvalue_ground, 3, 1, 1, 3)


        #Windows
        self.gB_enrichment_windows = QtWidgets.QGroupBox('Windows')
        self.scrollLayout.addWidget(self.gB_enrichment_windows)
        # #
        self.windowsGrid = QtWidgets.QGridLayout()
        self.gB_enrichment_windows.setLayout(self.windowsGrid)

        self.lbl_window2wallRatio = QtWidgets.QLabel("Window to wall ratio:")
        self.windowsGrid.addWidget(self.lbl_window2wallRatio, 0, 0, 1, 1)

        self.txt_window2wallRatio = QtWidgets.QLineEdit('')
        self.windowsGrid.addWidget(self.txt_window2wallRatio, 0, 1, 1, 1)

        self.lbl_transmittanceFraction_windows = QtWidgets.QLabel('Transmittance Fraction:')
        self.windowsGrid.addWidget(self.lbl_transmittanceFraction_windows, 0, 2, 1, 1)

        self.txt_transmittance_fraction_windows = QtWidgets.QLineEdit('')  # ToDo: Based on the description combo?
        self.windowsGrid.addWidget(self.txt_transmittance_fraction_windows, 0, 3, 1, 1)

        self.lbl_wavelengthrange_windows = QtWidgets.QLabel('Wave Length Range:')
        self.windowsGrid.addWidget(self.lbl_wavelengthrange_windows, 1, 0, 1, 1)

        self.txt_wavelengthrange_windows = QtWidgets.QLineEdit('')
        self.windowsGrid.addWidget(self.txt_wavelengthrange_windows, 1, 1, 1, 1)

        self.lbl_glazingratio_windows = QtWidgets.QLabel('Glazing Ratio:')
        self.windowsGrid.addWidget(self.lbl_glazingratio_windows, 1, 2, 1, 1)

        self.txt_glazingratio_windows = QtWidgets.QLineEdit('')
        self.windowsGrid.addWidget(self.txt_glazingratio_windows, 1, 3, 1, 1)

        self.lbl_uvalue_windows = QtWidgets.QLabel('U-value:')  # ToDo: Currently it is just a combobox
        self.windowsGrid.addWidget(self.lbl_uvalue_windows, 2, 0, 1, 1)

        self.txt_uvalue_windows = QtWidgets.QLineEdit('')
        self.windowsGrid.addWidget(self.txt_uvalue_windows, 2, 1, 1, 3)

        


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

        self.btn_about.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

        self.btn_wall_addLayer.clicked.connect(functools.partial(self.func_addLayer, "wall"))
        self.btn_wall_removeLayer.clicked.connect(functools.partial(self.func_removeLayer, "wall"))

        self.btn_roof_addLayer.clicked.connect(functools.partial(self.func_addLayer, "roof"))
        self.btn_roof_removeLayer.clicked.connect(functools.partial(self.func_removeLayer, "roof"))

        self.btn_ground_addLayer.clicked.connect(functools.partial(self.func_addLayer, "ground"))
        self.btn_ground_removeLayer.clicked.connect(functools.partial(self.func_removeLayer, "ground"))


        self.func_addLayer("wall")
        self.func_addLayer("roof")
        self.func_addLayer("ground")

    def func_about(self):
        global posx, posy
        posx, posy = gf.dimensions(self)
        gf.next_window(self, about(), False)

    def func_exit(self):
        gf.close_application(self)



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
        layer["cB_material"].addItems(self.materialNames)
        layer["layout"].addWidget(layer["cB_material"], 0, 1, 1, 1)

        layer["lbl_thickness"] = QtWidgets.QLabel('Thickness:')
        layer["layout"].addWidget(layer["lbl_thickness"], 0, 2, 1, 1)

        layer["txt_thickness"] = QtWidgets.QLineEdit('')
        layer["layout"].addWidget(layer["txt_thickness"], 0, 3, 1, 1)


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
        print("want to remove wall layer")

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
        for i in ["txt_thickness", "lbl_thickness", "cB_material", "lbl_material", "gB"]:
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
        

class heating_schedules(QtWidgets.QWidget):
    def __init__(self):
        super(heating_schedules, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityEnrich - Heating Schedules')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        self.gB_heating_schedules = QtWidgets.QGroupBox('Heating Schedules')
        self.vbox.addWidget(self.gB_heating_schedules)
        self.vBox_forheating = QtWidgets.QVBoxLayout()
        self.gB_heating_schedules.setLayout(self.vBox_forheating)

        # # walls enrichment
        self.gB_heating_parameters = QtWidgets.QGroupBox('')
        self.vBox_forheating.addWidget(self.gB_heating_parameters)
        #
        self.heatingGrid = QtWidgets.QGridLayout()
        self.gB_heating_parameters.setLayout(self.heatingGrid)
        #

        self.lbl_date_begin = QtWidgets.QLabel('Start Date:')
        self.heatingGrid.addWidget(self.lbl_date_begin, 0, 0, 1, 1)

        self.txt_date_begin = QtWidgets.QLineEdit('') #ToDo: Add calander selection (Simon)
        self.heatingGrid.addWidget(self.txt_date_begin, 0, 1, 1, 1)

        self.lbl_date_end = QtWidgets.QLabel('End Date:')
        self.heatingGrid.addWidget(self.lbl_date_end, 0, 2, 1, 1)

        self.txt_date_end = QtWidgets.QLineEdit('')  # ToDo: Add calander selection (Simon)
        self.heatingGrid.addWidget(self.txt_date_end, 0, 3, 1, 1)

        self.lbl_hour_begin = QtWidgets.QLabel('Begin Hour:')
        self.heatingGrid.addWidget(self.lbl_hour_begin, 1, 0, 1, 1)

        self.txt_hour_begin = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.heatingGrid.addWidget(self.txt_hour_begin, 1, 1, 1, 1)

        self.lbl_hour_end = QtWidgets.QLabel('End Hour:')
        self.heatingGrid.addWidget(self.lbl_hour_end, 1, 2, 1, 1)

        self.txt_hour_end = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.heatingGrid.addWidget(self.txt_hour_end, 1, 3, 1, 1)

        self.lbl_time_interval = QtWidgets.QLabel('Time Interval and Unit') # ToDo: (Max) do we make the unit separate?
        self.heatingGrid.addWidget(self.lbl_time_interval, 2, 0, 1, 1)

        self.txt_time_interval = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.heatingGrid.addWidget(self.txt_time_interval, 2, 1, 1, 1)

        self.lbl_acquisition_method = QtWidgets.QLabel('Acquisition Method:')
        self.heatingGrid.addWidget(self.lbl_acquisition_method, 2, 2, 1, 1)

        self.txt_acquisition_method = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.heatingGrid.addWidget(self.txt_acquisition_method, 2, 3, 1, 1)

        self.lbl_interpolation_type = QtWidgets.QLabel('Interpolation Type')  # ToDo: (Max) do we make the unit separate?
        self.heatingGrid.addWidget(self.lbl_interpolation_type, 3, 0, 1, 1)

        self.txt_interpolation = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add selection
        self.heatingGrid.addWidget(self.txt_interpolation, 3, 1, 1, 1)

        self.lbl_thematic_description = QtWidgets.QLabel('Thematic Description:')
        self.heatingGrid.addWidget(self.lbl_thematic_description, 3, 2, 1, 1)

        self.txt_thematic_description = QtWidgets.QLineEdit('')  # ToDo: (Max) what do wanna add here?
        self.heatingGrid.addWidget(self.txt_thematic_description, 3, 3, 1, 1)

        # self.lbl_daytype = QtWidgets.QLabel('')  # ToDo: (Max) do we make the unit separate?
        # self.heatingGrid.addWidget(self.lbl_daytype, 4, 0, 1, 1)

        self.radio_weekdaytype = QtWidgets.QRadioButton('Weekday')
        self.heatingGrid.addWidget(self.radio_weekdaytype, 4, 0, 1, 1)

        self.radio_weekendtype = QtWidgets.QRadioButton('Weekend')
        self.heatingGrid.addWidget(self.radio_weekendtype, 4, 1, 1, 1)

        self.btn_select_heating = QtWidgets.QPushButton('Select Values')  # ToDo: (Max) do we make the unit separate?
        self.heatingGrid.addWidget(self.btn_select_heating, 4, 2, 1, 1)

        self.txt_path_select_values = QtWidgets.QLineEdit('')
        self.heatingGrid.addWidget(self.txt_path_select_values, 4, 3, 1, 1)

        self.lbl_unit = QtWidgets.QLabel('Unit:')
        self.heatingGrid.addWidget(self.lbl_unit, 5, 0, 1, 1)

        self.txt_unit = QtWidgets.QLineEdit('') # ToDo: (Max) Dropdown?
        self.heatingGrid.addWidget(self.txt_unit, 5, 1, 1, 1)

        self.radio_SIunit = QtWidgets.QRadioButton('SI')
        self.heatingGrid.addWidget(self.radio_SIunit, 5, 2, 1, 1)

        self.radio_fraction_unit = QtWidgets.QRadioButton('Fraction')
        self.heatingGrid.addWidget(self.radio_fraction_unit, 5, 3, 1, 1)

        #
        # self.lbl_U_Value = QtWidgets.QLabel('U-Value')
        # self.heatingGrid.addWidget(self.lbl_U_Value, 0, 2, 1, 1)
        #
        # self.txt_walluvalue = QtWidgets.QLineEdit('')
        # self.txt_walluvalue.setPlaceholderText('U Value of Wall')
        # self.heatingGrid.addWidget(self.txt_walluvalue, 0, 3, 1, 1)
        #
        # self.btn_material_wall = QtWidgets.QPushButton('Material Selection')
        # self.heatingGrid.addWidget(self.btn_material_wall, 1, 0, 1, 2)
        #
        # # self.btn_walls = QtWidgets.QPushButton('Construction')
        # # self.roofGrid.addWidget(self.btn_walls, 0, 1, 1, 1)
        #
        # # # roof enrichment
        # self.gB_roof = QtWidgets.QGroupBox('Roof')
        # self.vBox_forconstruction.addWidget(self.gB_roof)
        # #
        # self.roofGrid = QtWidgets.QGridLayout()
        # self.gB_roof.setLayout(self.roofGrid)
        # #
        #
        # self.btn_zone = QtWidgets.QPushButton('Thermal Zones')
        # self.roofGrid.addWidget(self.btn_zone, 0, 0, 1, 1)
        #
        # self.btn_walls = QtWidgets.QPushButton('Construction')
        # self.roofGrid.addWidget(self.btn_walls, 0, 1, 1, 1)
        #
        # self.btn_occupancy = QtWidgets.QPushButton('Occupancy')
        # self.roofGrid.addWidget(self.btn_occupancy, 1, 1, 1, 1)
        #
        # self.btn_light_app = QtWidgets.QPushButton('Lighting and Appliances')
        # self.roofGrid.addWidget(self.btn_light_app, 1, 1, 1, 1)
        #
        # # # ground surface enrichment
        # self.gB_ground_surface = QtWidgets.QGroupBox('Ground Surface')
        # self.vBox_forconstruction.addWidget(self.gB_ground_surface)
        # #
        # self.groundGrid = QtWidgets.QGridLayout()
        # self.gB_ground_surface.setLayout(self.groundGrid)
        # #
        # self.btn_zone = QtWidgets.QPushButton('Thermal Zones')
        # self.groundGrid.addWidget(self.btn_zone, 0, 0, 1, 1)
        #
        # self.btn_walls = QtWidgets.QPushButton('Construction')
        # self.groundGrid.addWidget(self.btn_walls, 0, 1, 1, 1)
        #
        # self.btn_occupancy = QtWidgets.QPushButton('Occupancy')
        # self.groundGrid.addWidget(self.btn_occupancy, 1, 1, 1, 1)
        #
        # self.btn_light_app = QtWidgets.QPushButton('Lighting and Appliances')
        # self.groundGrid.addWidget(self.btn_light_app, 1, 1, 1, 1)
        #
        # # # window enrichment
        # self.gB_window = QtWidgets.QGroupBox('Window')
        # self.vBox_forconstruction.addWidget(self.gB_window)
        # #
        # self.windGrid = QtWidgets.QGridLayout()
        # self.gB_window.setLayout(self.windGrid)
        # #
        # self.btn_zone = QtWidgets.QPushButton('Thermal Zones')
        # self.windGrid.addWidget(self.btn_zone, 0, 0, 1, 1)
        #
        # self.btn_walls = QtWidgets.QPushButton('Construction')
        # self.windGrid.addWidget(self.btn_walls, 0, 1, 1, 1)
        #
        # self.btn_occupancy = QtWidgets.QPushButton('Occupancy')
        # self.windGrid.addWidget(self.btn_occupancy, 1, 1, 1, 1)
        #
        # self.btn_light_app = QtWidgets.QPushButton('Lighting and Appliances')
        # self.windGrid.addWidget(self.btn_light_app, 1, 1, 1, 1)
        #
        #
        # # usagezone
        # self.gB_usagezone = QtWidgets.QGroupBox('Usage Zone - Schedules')
        # self.vbox.addWidget(self.gB_usagezone)
        #
        # self.aGrid = QtWidgets.QGridLayout()
        # self.gB_usagezone.setLayout(self.aGrid)
        #
        # self.btn_zone = QtWidgets.QPushButton('Heating')
        # self.aGrid.addWidget(self.btn_zone, 0, 0, 1, 1)
        #
        # self.btn_walls = QtWidgets.QPushButton('Cooling')
        # self.aGrid.addWidget(self.btn_walls, 0, 1, 1, 1)
        #
        # self.btn_occupancy = QtWidgets.QPushButton('Ventilation')
        # self.aGrid.addWidget(self.btn_occupancy, 1, 0, 1, 1)
        #
        # self.btn_light_app = QtWidgets.QPushButton('Occupancy')
        # self.aGrid.addWidget(self.btn_light_app, 1, 1, 1, 1)
        #

        self.l2Grid_heating = QtWidgets.QGridLayout()

        self.btn_save = QtWidgets.QPushButton('Save') #ToDo: (Simon) Add functionalities to save
        self.l2Grid_heating.addWidget(self.btn_save, 0, 0, 1, 1)

        self.btn_reset = QtWidgets.QPushButton('Reset') #ToDo: (Simon) Add functionalities to reset
        self.l2Grid_heating.addWidget(self.btn_reset, 0, 1, 1, 1)

        self.btn_exit = QtWidgets.QPushButton('Exit')
        self.l2Grid_heating.addWidget(self.btn_exit, 0, 2, 1, 1)

        self.btn_back = QtWidgets.QPushButton('Back') #ToDo: (Simon) Add functionalities to back
        self.l2Grid_heating.addWidget(self.btn_back, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid_heating)

        # self.btn_save.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

    # def func_about(self):
    #     global posx, posy
    #     posx, posy = gf.dimensions(self)
    #     gf.next_window(self, about(), False)

    def func_exit(self):
        gf.close_application(self)

class cooling_schedules(QtWidgets.QWidget):
    def __init__(self):
        super(cooling_schedules, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityEnrich - Cooling Schedules')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        self.gB_cooling_schedules = QtWidgets.QGroupBox('Cooling Schedules')
        self.vbox.addWidget(self.gB_cooling_schedules)
        self.vBox_forcooling = QtWidgets.QVBoxLayout()
        self.gB_cooling_schedules.setLayout(self.vBox_forcooling)

        # # walls enrichment
        self.gB_cooling_parameters = QtWidgets.QGroupBox('')
        self.vBox_forcooling.addWidget(self.gB_cooling_parameters)
        #
        self.coolingGrid = QtWidgets.QGridLayout()
        self.gB_cooling_parameters.setLayout(self.coolingGrid)
        #

        self.lbl_date_begin_cooling = QtWidgets.QLabel('Start Date:')
        self.coolingGrid.addWidget(self.lbl_date_begin_cooling, 0, 0, 1, 1)

        self.txt_date_begin_cooling = QtWidgets.QLineEdit('') #ToDo: Add calander selection (Simon)
        self.coolingGrid.addWidget(self.txt_date_begin_cooling, 0, 1, 1, 1)

        self.lbl_date_end_cooling = QtWidgets.QLabel('End Date:')
        self.coolingGrid.addWidget(self.lbl_date_end_cooling, 0, 2, 1, 1)

        self.txt_date_end_cooling = QtWidgets.QLineEdit('')  # ToDo: Add calander selection (Simon)
        self.coolingGrid.addWidget(self.txt_date_end_cooling, 0, 3, 1, 1)

        self.lbl_hour_begin_cooling = QtWidgets.QLabel('Begin Hour:')
        self.coolingGrid.addWidget(self.lbl_hour_begin_cooling, 1, 0, 1, 1)

        self.txt_hour_begin_cooling = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.coolingGrid.addWidget(self.txt_hour_begin_cooling, 1, 1, 1, 1)

        self.lbl_hour_end_cooling = QtWidgets.QLabel('End Hour:')
        self.coolingGrid.addWidget(self.lbl_hour_end_cooling, 1, 2, 1, 1)

        self.txt_hour_end_cooling = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.coolingGrid.addWidget(self.txt_hour_end_cooling, 1, 3, 1, 1)

        self.lbl_time_interval_cooling = QtWidgets.QLabel('Time Interval and Unit') # ToDo: (Max) do we make the unit separate?
        self.coolingGrid.addWidget(self.lbl_time_interval_cooling, 2, 0, 1, 1)

        self.txt_time_interval_cooling = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.coolingGrid.addWidget(self.txt_time_interval_cooling, 2, 1, 1, 1)

        self.lbl_acquisition_method_cooling = QtWidgets.QLabel('Acquisition Method:')
        self.coolingGrid.addWidget(self.lbl_acquisition_method_cooling, 2, 2, 1, 1)

        self.txt_acquisition_method_cooling = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.coolingGrid.addWidget(self.txt_acquisition_method_cooling, 2, 3, 1, 1)

        self.lbl_interpolation_type_cooling = QtWidgets.QLabel('Interpolation Type')  # ToDo: (Max) do we make the unit separate?
        self.coolingGrid.addWidget(self.lbl_interpolation_type_cooling, 3, 0, 1, 1)

        self.txt_interpolation_cooling = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add selection
        self.coolingGrid.addWidget(self.txt_interpolation_cooling, 3, 1, 1, 1)

        self.lbl_thematic_description_cooling = QtWidgets.QLabel('Thematic Description:')
        self.coolingGrid.addWidget(self.lbl_thematic_description_cooling, 3, 2, 1, 1)

        self.txt_thematic_description_cooling = QtWidgets.QLineEdit('')  # ToDo: (Max) what do wanna add here?
        self.coolingGrid.addWidget(self.txt_thematic_description_cooling, 3, 3, 1, 1)

        # self.lbl_daytype = QtWidgets.QLabel('')  # ToDo: (Max) do we make the unit separate?
        # self.heatingGrid.addWidget(self.lbl_daytype, 4, 0, 1, 1)

        self.radio_weekdaytype_cooling = QtWidgets.QRadioButton('Weekday')
        self.coolingGrid.addWidget(self.radio_weekdaytype_cooling, 4, 0, 1, 1)

        self.radio_weekendtype_cooling = QtWidgets.QRadioButton('Weekend')
        self.coolingGrid.addWidget(self.radio_weekendtype_cooling, 4, 1, 1, 1)

        self.btn_select_cooling = QtWidgets.QPushButton('Select Values')  # ToDo: (Max) do we make the unit separate?
        self.coolingGrid.addWidget(self.btn_select_cooling, 4, 2, 1, 1)

        self.txt_path_select_values_cooling = QtWidgets.QLineEdit('')
        self.coolingGrid.addWidget(self.txt_path_select_values_cooling, 4, 3, 1, 1)

        self.lbl_unit_cooling = QtWidgets.QLabel('Unit:')
        self.coolingGrid.addWidget(self.lbl_unit_cooling, 5, 0, 1, 1)

        self.txt_unit_cooling = QtWidgets.QLineEdit('') # ToDo: (Max) Dropdown?
        self.coolingGrid.addWidget(self.txt_unit_cooling, 5, 1, 1, 1)

        self.radio_SIunit_cooling = QtWidgets.QRadioButton('SI')
        self.coolingGrid.addWidget(self.radio_SIunit_cooling, 5, 2, 1, 1)

        self.radio_fraction_unit_cooling = QtWidgets.QRadioButton('Fraction')
        self.coolingGrid.addWidget(self.radio_fraction_unit_cooling, 5, 3, 1, 1)
        self.l2Grid_cooling = QtWidgets.QGridLayout()

        self.btn_save_cooling = QtWidgets.QPushButton('Save')  # ToDo: (Simon) Add functionalities to save
        self.l2Grid_cooling.addWidget(self.btn_save_cooling, 0, 0, 1, 1)

        self.btn_reset_cooling = QtWidgets.QPushButton('Reset')  # ToDo: (Simon) Add functionalities to reset
        self.l2Grid_cooling.addWidget(self.btn_reset_cooling, 0, 1, 1, 1)

        self.btn_exit_cooling = QtWidgets.QPushButton('Exit')
        self.l2Grid_cooling.addWidget(self.btn_exit_cooling, 0, 2, 1, 1)

        self.btn_back_cooling = QtWidgets.QPushButton('Back')  # ToDo: (Simon) Add functionalities to back
        self.l2Grid_cooling.addWidget(self.btn_back_cooling, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid_cooling)

        # self.btn_save.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit_cooling.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

        # def func_about(self):
        #     global posx, posy
        #     posx, posy = gf.dimensions(self)
        #     gf.next_window(self, about(), False)

    def func_exit(self):
        gf.close_application(self)

class ventilation_schedules(QtWidgets.QWidget):
    def __init__(self):
        super(ventilation_schedules, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityEnrich - Ventilation Schedules')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        self.gB_ventilation_schedules = QtWidgets.QGroupBox('Ventilation Schedules')
        self.vbox.addWidget(self.gB_ventilation_schedules)
        self.vBox_forventilation = QtWidgets.QVBoxLayout()
        self.gB_ventilation_schedules.setLayout(self.vBox_forventilation)

        # # walls enrichment
        self.gB_ventilation_parameters = QtWidgets.QGroupBox('')
        self.vBox_forventilation.addWidget(self.gB_ventilation_parameters)
        #
        self.ventilationGrid = QtWidgets.QGridLayout()
        self.gB_ventilation_parameters.setLayout(self.ventilationGrid)
        #

        self.lbl_date_begin_ventilation = QtWidgets.QLabel('Start Date:')
        self.ventilationGrid.addWidget(self.lbl_date_begin_ventilation, 0, 0, 1, 1)

        self.txt_date_begin_ventilation = QtWidgets.QLineEdit('') #ToDo: Add calander selection (Simon)
        self.ventilationGrid.addWidget(self.txt_date_begin_ventilation, 0, 1, 1, 1)

        self.lbl_date_end_ventilation = QtWidgets.QLabel('End Date:')
        self.ventilationGrid.addWidget(self.lbl_date_end_ventilation, 0, 2, 1, 1)

        self.txt_date_end_ventilation = QtWidgets.QLineEdit('')  # ToDo: Add calander selection (Simon)
        self.ventilationGrid.addWidget(self.txt_date_end_ventilation, 0, 3, 1, 1)

        self.lbl_hour_begin_ventilation = QtWidgets.QLabel('Begin Hour:')
        self.ventilationGrid.addWidget(self.lbl_hour_begin_ventilation, 1, 0, 1, 1)

        self.txt_hour_begin_ventilation = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.ventilationGrid.addWidget(self.txt_hour_begin_ventilation, 1, 1, 1, 1)

        self.lbl_hour_end_ventilation = QtWidgets.QLabel('End Hour:')
        self.ventilationGrid.addWidget(self.lbl_hour_end_ventilation, 1, 2, 1, 1)

        self.txt_hour_end_ventilation = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.ventilationGrid.addWidget(self.txt_hour_end_ventilation, 1, 3, 1, 1)

        self.lbl_time_interval_ventilation = QtWidgets.QLabel('Time Interval and Unit') # ToDo: (Max) do we make the unit separate?
        self.ventilationGrid.addWidget(self.lbl_time_interval_ventilation, 2, 0, 1, 1)

        self.txt_time_interval_ventilation = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.ventilationGrid.addWidget(self.txt_time_interval_ventilation, 2, 1, 1, 1)

        self.lbl_acquisition_method_ventilation = QtWidgets.QLabel('Acquisition Method:')
        self.ventilationGrid.addWidget(self.lbl_acquisition_method_ventilation, 2, 2, 1, 1)

        self.txt_acquisition_method_ventilation = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.ventilationGrid.addWidget(self.txt_acquisition_method_ventilation, 2, 3, 1, 1)

        self.lbl_interpolation_type_ventilation = QtWidgets.QLabel('Interpolation Type')  # ToDo: (Max) do we make the unit separate?
        self.ventilationGrid.addWidget(self.lbl_interpolation_type_ventilation, 3, 0, 1, 1)

        self.txt_interpolation_ventilation = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add selection
        self.ventilationGrid.addWidget(self.txt_interpolation_ventilation, 3, 1, 1, 1)

        self.lbl_thematic_description_ventilation = QtWidgets.QLabel('Thematic Description:')
        self.ventilationGrid.addWidget(self.lbl_thematic_description_ventilation, 3, 2, 1, 1)

        self.txt_thematic_description_ventilation = QtWidgets.QLineEdit('')  # ToDo: (Max) what do wanna add here?
        self.ventilationGrid.addWidget(self.txt_thematic_description_ventilation, 3, 3, 1, 1)

        # self.lbl_daytype = QtWidgets.QLabel('')  # ToDo: (Max) do we make the unit separate?
        # self.heatingGrid.addWidget(self.lbl_daytype, 4, 0, 1, 1)

        self.radio_weekdaytype_ventilation = QtWidgets.QRadioButton('Weekday')
        self.ventilationGrid.addWidget(self.radio_weekdaytype_ventilation, 4, 0, 1, 1)

        self.radio_weekendtype_ventilation = QtWidgets.QRadioButton('Weekend')
        self.ventilationGrid.addWidget(self.radio_weekendtype_ventilation, 4, 1, 1, 1)

        self.btn_select_ventilation = QtWidgets.QPushButton('Select Values')  # ToDo: (Max) do we make the unit separate?
        self.ventilationGrid.addWidget(self.btn_select_ventilation, 4, 2, 1, 1)

        self.txt_path_select_values_ventilation = QtWidgets.QLineEdit('')
        self.ventilationGrid.addWidget(self.txt_path_select_values_ventilation, 4, 3, 1, 1)

        self.lbl_unit_ventilation = QtWidgets.QLabel('Unit:')
        self.ventilationGrid.addWidget(self.lbl_unit_ventilation, 5, 0, 1, 1)

        self.txt_unit_ventilation = QtWidgets.QLineEdit('') # ToDo: (Max) Dropdown?
        self.ventilationGrid.addWidget(self.txt_unit_ventilation, 5, 1, 1, 1)

        self.radio_SIunit_ventilation = QtWidgets.QRadioButton('SI')
        self.ventilationGrid.addWidget(self.radio_SIunit_ventilation, 5, 2, 1, 1)

        self.radio_fraction_unit_ventilation = QtWidgets.QRadioButton('Fraction')
        self.ventilationGrid.addWidget(self.radio_fraction_unit_ventilation, 5, 3, 1, 1)
        self.l2Grid_ventilation = QtWidgets.QGridLayout()

        self.btn_save_ventilation = QtWidgets.QPushButton('Save')  # ToDo: (Simon) Add functionalities to save
        self.l2Grid_ventilation.addWidget(self.btn_save_ventilation, 0, 0, 1, 1)

        self.btn_reset_ventilation = QtWidgets.QPushButton('Reset')  # ToDo: (Simon) Add functionalities to reset
        self.l2Grid_ventilation.addWidget(self.btn_reset_ventilation, 0, 1, 1, 1)

        self.btn_exit_ventilation = QtWidgets.QPushButton('Exit')
        self.l2Grid_ventilation.addWidget(self.btn_exit_ventilation, 0, 2, 1, 1)

        self.btn_back_ventilation = QtWidgets.QPushButton('Back')  # ToDo: (Simon) Add functionalities to back
        self.l2Grid_ventilation.addWidget(self.btn_back_ventilation, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid_ventilation)

        # self.btn_save.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit_ventilation.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

        # def func_about(self):
        #     global posx, posy
        #     posx, posy = gf.dimensions(self)
        #     gf.next_window(self, about(), False)

    def func_exit(self):
        gf.close_application(self)

class occupancy_schedules(QtWidgets.QWidget):
    def __init__(self):
        super(occupancy_schedules, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityEnrich - Occupancy Schedules')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        self.gB_occupancy_schedules = QtWidgets.QGroupBox('Occupancy Schedules')
        self.vbox.addWidget(self.gB_occupancy_schedules)
        self.vBox_foroccupancy = QtWidgets.QVBoxLayout()
        self.gB_occupancy_schedules.setLayout(self.vBox_foroccupancy)

        # # walls enrichment
        self.gB_occupancy_parameters = QtWidgets.QGroupBox('')
        self.vBox_foroccupancy.addWidget(self.gB_occupancy_parameters)
        #
        self.occupancyGrid = QtWidgets.QGridLayout()
        self.gB_occupancy_parameters.setLayout(self.occupancyGrid)
        #

        self.lbl_date_begin_occupancy = QtWidgets.QLabel('Start Date:')
        self.occupancyGrid.addWidget(self.lbl_date_begin_occupancy, 0, 0, 1, 1)

        self.txt_date_begin_occupancy = QtWidgets.QLineEdit('') #ToDo: Add calander selection (Simon)
        self.occupancyGrid.addWidget(self.txt_date_begin_occupancy, 0, 1, 1, 1)

        self.lbl_date_end_occupancy = QtWidgets.QLabel('End Date:')
        self.occupancyGrid.addWidget(self.lbl_date_end_occupancy, 0, 2, 1, 1)

        self.txt_date_end_occupancy = QtWidgets.QLineEdit('')  # ToDo: Add calander selection (Simon)
        self.occupancyGrid.addWidget(self.txt_date_end_occupancy, 0, 3, 1, 1)

        self.lbl_hour_begin_occupancy = QtWidgets.QLabel('Begin Hour:')
        self.occupancyGrid.addWidget(self.lbl_hour_begin_occupancy, 1, 0, 1, 1)

        self.txt_hour_begin_occupancy = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.occupancyGrid.addWidget(self.txt_hour_begin_occupancy, 1, 1, 1, 1)

        self.lbl_hour_end_occupancy = QtWidgets.QLabel('End Hour:')
        self.occupancyGrid.addWidget(self.lbl_hour_end_occupancy, 1, 2, 1, 1)

        self.txt_hour_end_occupancy = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.occupancyGrid.addWidget(self.txt_hour_end_occupancy, 1, 3, 1, 1)

        self.lbl_time_interval_occupancy = QtWidgets.QLabel('Time Interval and Unit') # ToDo: (Max) do we make the unit separate?
        self.occupancyGrid.addWidget(self.lbl_time_interval_occupancy, 2, 0, 1, 1)

        self.txt_time_interval_occupancy = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.occupancyGrid.addWidget(self.txt_time_interval_occupancy, 2, 1, 1, 1)

        self.lbl_acquisition_method_occupancy = QtWidgets.QLabel('Acquisition Method:')
        self.occupancyGrid.addWidget(self.lbl_acquisition_method_occupancy, 2, 2, 1, 1)

        self.txt_acquisition_method_occupancy = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.occupancyGrid.addWidget(self.txt_acquisition_method_occupancy, 2, 3, 1, 1)

        self.lbl_interpolation_type_occupancy = QtWidgets.QLabel('Interpolation Type')  # ToDo: (Max) do we make the unit separate?
        self.occupancyGrid.addWidget(self.lbl_interpolation_type_occupancy, 3, 0, 1, 1)

        self.txt_interpolation_occupancy = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add selection
        self.occupancyGrid.addWidget(self.txt_interpolation_occupancy, 3, 1, 1, 1)

        self.lbl_thematic_description_occupancy = QtWidgets.QLabel('Thematic Description:')
        self.occupancyGrid.addWidget(self.lbl_thematic_description_occupancy, 3, 2, 1, 1)

        self.txt_thematic_description_occupancy = QtWidgets.QLineEdit('')  # ToDo: (Max) what do wanna add here?
        self.occupancyGrid.addWidget(self.txt_thematic_description_occupancy, 3, 3, 1, 1)

        # self.lbl_daytype = QtWidgets.QLabel('')  # ToDo: (Max) do we make the unit separate?
        # self.heatingGrid.addWidget(self.lbl_daytype, 4, 0, 1, 1)

        self.radio_weekdaytype_occupancy = QtWidgets.QRadioButton('Weekday')
        self.occupancyGrid.addWidget(self.radio_weekdaytype_occupancy, 4, 0, 1, 1)

        self.radio_weekendtype_occupancy = QtWidgets.QRadioButton('Weekend')
        self.occupancyGrid.addWidget(self.radio_weekendtype_occupancy, 4, 1, 1, 1)

        self.btn_select_occupancy = QtWidgets.QPushButton('Select Values')  # ToDo: (Max) do we make the unit separate?
        self.occupancyGrid.addWidget(self.btn_select_occupancy, 4, 2, 1, 1)

        self.txt_path_select_values_occupancy = QtWidgets.QLineEdit('')
        self.occupancyGrid.addWidget(self.txt_path_select_values_occupancy, 4, 3, 1, 1)

        self.lbl_unit_occupancy = QtWidgets.QLabel('Unit:')
        self.occupancyGrid.addWidget(self.lbl_unit_occupancy, 5, 0, 1, 1)

        self.txt_unit_occupancy = QtWidgets.QLineEdit('') # ToDo: (Max) Dropdown?
        self.occupancyGrid.addWidget(self.txt_unit_occupancy, 5, 1, 1, 1)

        self.radio_SIunit_occupancy = QtWidgets.QRadioButton('SI')
        self.occupancyGrid.addWidget(self.radio_SIunit_occupancy, 5, 2, 1, 1)

        self.radio_fraction_unit_occupancy = QtWidgets.QRadioButton('Fraction')
        self.occupancyGrid.addWidget(self.radio_fraction_unit_occupancy, 5, 3, 1, 1)
        self.l2Grid_occupancy = QtWidgets.QGridLayout()

        self.lbl_ConvectiveFraction_occupancy = QtWidgets.QLabel('Convective Fraction:')
        self.occupancyGrid.addWidget(self.lbl_ConvectiveFraction_occupancy, 6, 0, 1, 1)

        self.txt_ConvectiveFraction_occupancy = QtWidgets.QLineEdit('')
        self.occupancyGrid.addWidget(self.txt_ConvectiveFraction_occupancy, 6, 1, 1, 1)

        self.lbl_radiant_fraction_occupancy = QtWidgets.QLabel('Radiant Fraction:')
        self.occupancyGrid.addWidget(self.lbl_radiant_fraction_occupancy, 6, 2, 1, 1)

        self.txt_radiant_fraction_occupancy = QtWidgets.QLineEdit('')
        self.occupancyGrid.addWidget(self.txt_thematic_description_occupancy, 6, 3, 1, 1)

        self.lbl_totalValue_occupancy = QtWidgets.QLabel('Total Value:')
        self.occupancyGrid.addWidget(self.lbl_totalValue_occupancy, 7, 0, 1, 1)

        self.txt_totalValue_occupancy = QtWidgets.QLineEdit('')
        self.occupancyGrid.addWidget(self.txt_totalValue_occupancy, 7, 1, 1, 1)

        self.lbl_number_occupancy = QtWidgets.QLabel('Number of Occupants:')
        self.occupancyGrid.addWidget(self.lbl_number_occupancy, 7, 2, 1, 1)

        self.txt_number_occupancy = QtWidgets.QLineEdit('')
        self.occupancyGrid.addWidget(self.txt_number_occupancy, 7, 3, 1, 1)


        self.btn_save_occupancy = QtWidgets.QPushButton('Save')  # ToDo: (Simon) Add functionalities to save
        self.l2Grid_occupancy.addWidget(self.btn_save_occupancy, 0, 0, 1, 1)

        self.btn_reset_occupancy = QtWidgets.QPushButton('Reset')  # ToDo: (Simon) Add functionalities to reset
        self.l2Grid_occupancy.addWidget(self.btn_reset_occupancy, 0, 1, 1, 1)

        self.btn_exit_occupancy = QtWidgets.QPushButton('Exit')
        self.l2Grid_occupancy.addWidget(self.btn_exit_occupancy, 0, 2, 1, 1)

        self.btn_back_occupancy = QtWidgets.QPushButton('Back')  # ToDo: (Simon) Add functionalities to back
        self.l2Grid_occupancy.addWidget(self.btn_back_occupancy, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid_occupancy)

        # self.btn_save.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit_occupancy.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

        # def func_about(self):
        #     global posx, posy
        #     posx, posy = gf.dimensions(self)
        #     gf.next_window(self, about(), False)

    def func_exit(self):
        gf.close_application(self)

class appliances_schedules(QtWidgets.QWidget):
    def __init__(self):
        super(appliances_schedules, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityEnrich - Appliances Schedules')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        self.gB_appliances_schedules = QtWidgets.QGroupBox('Appliances Schedules')
        self.vbox.addWidget(self.gB_appliances_schedules)
        self.vBox_forappliances = QtWidgets.QVBoxLayout()
        self.gB_appliances_schedules.setLayout(self.vBox_forappliances)

        # # walls enrichment
        self.gB_appliances_parameters = QtWidgets.QGroupBox('')
        self.vBox_forappliances.addWidget(self.gB_appliances_parameters)
        #
        self.appliancesGrid = QtWidgets.QGridLayout()
        self.gB_appliances_parameters.setLayout(self.appliancesGrid)
        #

        self.lbl_date_begin_appliances = QtWidgets.QLabel('Start Date:')
        self.appliancesGrid.addWidget(self.lbl_date_begin_appliances, 0, 0, 1, 1)

        self.txt_date_begin_appliances = QtWidgets.QLineEdit('') #ToDo: Add calander selection (Simon)
        self.appliancesGrid.addWidget(self.txt_date_begin_appliances, 0, 1, 1, 1)

        self.lbl_date_end_appliances = QtWidgets.QLabel('End Date:')
        self.appliancesGrid.addWidget(self.lbl_date_end_appliances, 0, 2, 1, 1)

        self.txt_date_end_appliances = QtWidgets.QLineEdit('')  # ToDo: Add calander selection (Simon)
        self.appliancesGrid.addWidget(self.txt_date_end_appliances, 0, 3, 1, 1)

        self.lbl_hour_begin_appliances = QtWidgets.QLabel('Begin Hour:')
        self.appliancesGrid.addWidget(self.lbl_hour_begin_appliances, 1, 0, 1, 1)

        self.txt_hour_begin_appliances = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.appliancesGrid.addWidget(self.txt_hour_begin_appliances, 1, 1, 1, 1)

        self.lbl_hour_end_appliances = QtWidgets.QLabel('End Hour:')
        self.appliancesGrid.addWidget(self.lbl_hour_end_appliances, 1, 2, 1, 1)

        self.txt_hour_end_appliances = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.appliancesGrid.addWidget(self.txt_hour_end_appliances, 1, 3, 1, 1)

        self.lbl_time_interval_appliances = QtWidgets.QLabel('Time Interval and Unit') # ToDo: (Max) do we make the unit separate?
        self.appliancesGrid.addWidget(self.lbl_time_interval_appliances, 2, 0, 1, 1)

        self.txt_time_interval_appliances = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.appliancesGrid.addWidget(self.txt_time_interval_appliances, 2, 1, 1, 1)

        self.lbl_acquisition_method_appliances = QtWidgets.QLabel('Acquisition Method:')
        self.appliancesGrid.addWidget(self.lbl_acquisition_method_appliances, 2, 2, 1, 1)

        self.txt_acquisition_method_appliances = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.appliancesGrid.addWidget(self.txt_acquisition_method_appliances, 2, 3, 1, 1)

        self.lbl_interpolation_type_appliances = QtWidgets.QLabel('Interpolation Type')  # ToDo: (Max) do we make the unit separate?
        self.appliancesGrid.addWidget(self.lbl_interpolation_type_appliances, 3, 0, 1, 1)

        self.txt_interpolation_appliances = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add selection
        self.appliancesGrid.addWidget(self.txt_interpolation_appliances, 3, 1, 1, 1)

        self.lbl_thematic_description_appliances = QtWidgets.QLabel('Thematic Description:')
        self.appliancesGrid.addWidget(self.lbl_thematic_description_appliances, 3, 2, 1, 1)

        self.txt_thematic_description_appliances = QtWidgets.QLineEdit('')  # ToDo: (Max) what do wanna add here?
        self.appliancesGrid.addWidget(self.txt_thematic_description_appliances, 3, 3, 1, 1)

        # self.lbl_daytype = QtWidgets.QLabel('')  # ToDo: (Max) do we make the unit separate?
        # self.heatingGrid.addWidget(self.lbl_daytype, 4, 0, 1, 1)

        self.radio_weekdaytype_appliances = QtWidgets.QRadioButton('Weekday')
        self.appliancesGrid.addWidget(self.radio_weekdaytype_appliances, 4, 0, 1, 1)

        self.radio_weekendtype_appliances = QtWidgets.QRadioButton('Weekend')
        self.appliancesGrid.addWidget(self.radio_weekendtype_appliances, 4, 1, 1, 1)

        self.btn_select_appliances = QtWidgets.QPushButton('Select Values')  # ToDo: (Max) do we make the unit separate?
        self.appliancesGrid.addWidget(self.btn_select_appliances, 4, 2, 1, 1)

        self.txt_path_select_values_appliances = QtWidgets.QLineEdit('')
        self.appliancesGrid.addWidget(self.txt_path_select_values_appliances, 4, 3, 1, 1)

        self.lbl_unit_appliances = QtWidgets.QLabel('Unit:')
        self.appliancesGrid.addWidget(self.lbl_unit_appliances, 5, 0, 1, 1)

        self.txt_unit_appliances = QtWidgets.QLineEdit('') # ToDo: (Max) Dropdown?
        self.appliancesGrid.addWidget(self.txt_unit_appliances, 5, 1, 1, 1)

        self.radio_SIunit_appliances = QtWidgets.QRadioButton('SI')
        self.appliancesGrid.addWidget(self.radio_SIunit_appliances, 5, 2, 1, 1)

        self.radio_fraction_unit_appliances = QtWidgets.QRadioButton('Fraction')
        self.appliancesGrid.addWidget(self.radio_fraction_unit_appliances, 5, 3, 1, 1)


        self.lbl_ConvectiveFraction_appliances = QtWidgets.QLabel('Convective Fraction:')
        self.appliancesGrid.addWidget(self.lbl_ConvectiveFraction_appliances, 6, 0, 1, 1)

        self.txt_ConvectiveFraction_appliances = QtWidgets.QLineEdit('')
        self.appliancesGrid.addWidget(self.txt_ConvectiveFraction_appliances, 6, 1, 1, 1)

        self.lbl_radiant_fraction_appliances = QtWidgets.QLabel('Radiant Fraction:')
        self.appliancesGrid.addWidget(self.lbl_radiant_fraction_appliances, 6, 2, 1, 1)

        self.txt_radiant_fraction_appliances = QtWidgets.QLineEdit('')
        self.appliancesGrid.addWidget(self.txt_thematic_description_appliances, 6, 3, 1, 1)

        self.lbl_totalValue_appliances = QtWidgets.QLabel('Total Value:')
        self.appliancesGrid.addWidget(self.lbl_totalValue_appliances, 7, 0, 1, 1)

        self.txt_totalValue_appliances = QtWidgets.QLineEdit('')
        self.appliancesGrid.addWidget(self.txt_totalValue_appliances, 7, 1, 1, 1)

        self.l2Grid_appliances = QtWidgets.QGridLayout()

        self.btn_save_appliances = QtWidgets.QPushButton('Save')  # ToDo: (Simon) Add functionalities to save
        self.l2Grid_appliances.addWidget(self.btn_save_appliances, 0, 0, 1, 1)

        self.btn_reset_appliances = QtWidgets.QPushButton('Reset')  # ToDo: (Simon) Add functionalities to reset
        self.l2Grid_appliances.addWidget(self.btn_reset_appliances, 0, 1, 1, 1)

        self.btn_exit_appliances = QtWidgets.QPushButton('Exit')
        self.l2Grid_appliances.addWidget(self.btn_exit_appliances, 0, 2, 1, 1)

        self.btn_back_appliances = QtWidgets.QPushButton('Back')  # ToDo: (Simon) Add functionalities to back
        self.l2Grid_appliances.addWidget(self.btn_back_appliances, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid_appliances)

        # self.btn_save.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit_appliances.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

        # def func_about(self):
        #     global posx, posy
        #     posx, posy = gf.dimensions(self)
        #     gf.next_window(self, about(), False)

    def func_exit(self):
        gf.close_application(self)

class lighting_schedules(QtWidgets.QWidget):
    def __init__(self):
        super(lighting_schedules, self).__init__()
        self.initUI()

    def initUI(self):
        global posx, posy, width, height, sizefactor

        gf.windowSetup(self, posx + 10, posy + 10, width, height, pypath, 'CityEnrich - Lighting Schedules')

        # creating main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)

        # grid layout for file selection
        self.uGrid = QtWidgets.QGridLayout()

        self.vbox.addLayout(self.uGrid)

        self.gB_lighting_schedules = QtWidgets.QGroupBox('Lighting Schedules')
        self.vbox.addWidget(self.gB_lighting_schedules)
        self.vBox_forlighting = QtWidgets.QVBoxLayout()
        self.gB_lighting_schedules.setLayout(self.vBox_forlighting)

        # # walls enrichment
        self.gB_lighting_parameters = QtWidgets.QGroupBox('')
        self.vBox_forlighting.addWidget(self.gB_lighting_parameters)
        #
        self.lightingGrid = QtWidgets.QGridLayout()
        self.gB_lighting_parameters.setLayout(self.lightingGrid)
        #

        self.lbl_date_begin_lighting = QtWidgets.QLabel('Start Date:')
        self.lightingGrid.addWidget(self.lbl_date_begin_lighting, 0, 0, 1, 1)

        self.txt_date_begin_lighting = QtWidgets.QLineEdit('') #ToDo: Add calander selection (Simon)
        self.lightingGrid.addWidget(self.txt_date_begin_lighting, 0, 1, 1, 1)

        self.lbl_date_end_lighting = QtWidgets.QLabel('End Date:')
        self.lightingGrid.addWidget(self.lbl_date_end_lighting, 0, 2, 1, 1)

        self.txt_date_end_lighting = QtWidgets.QLineEdit('')  # ToDo: Add calander selection (Simon)
        self.lightingGrid.addWidget(self.txt_date_end_lighting, 0, 3, 1, 1)

        self.lbl_hour_begin_lighting = QtWidgets.QLabel('Begin Hour:')
        self.lightingGrid.addWidget(self.lbl_hour_begin_lighting, 1, 0, 1, 1)

        self.txt_hour_begin_lighting = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.lightingGrid.addWidget(self.txt_hour_begin_lighting, 1, 1, 1, 1)

        self.lbl_hour_end_lighting = QtWidgets.QLabel('End Hour:')
        self.lightingGrid.addWidget(self.lbl_hour_end_lighting, 1, 2, 1, 1)

        self.txt_hour_end_lighting = QtWidgets.QLineEdit('')  # ToDo: Add time selection (Simon)
        self.lightingGrid.addWidget(self.txt_hour_end_lighting, 1, 3, 1, 1)

        self.lbl_time_interval_lighting = QtWidgets.QLabel('Time Interval and Unit') # ToDo: (Max) do we make the unit separate?
        self.lightingGrid.addWidget(self.lbl_time_interval_lighting, 2, 0, 1, 1)

        self.txt_time_interval_lighting = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.lightingGrid.addWidget(self.txt_time_interval_lighting, 2, 1, 1, 1)

        self.lbl_acquisition_method_lighting = QtWidgets.QLabel('Acquisition Method:')
        self.lightingGrid.addWidget(self.lbl_acquisition_method_lighting, 2, 2, 1, 1)

        self.txt_acquisition_method_lighting = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add time selection
        self.lightingGrid.addWidget(self.txt_acquisition_method_lighting, 2, 3, 1, 1)

        self.lbl_interpolation_type_lighting = QtWidgets.QLabel('Interpolation Type')  # ToDo: (Max) do we make the unit separate?
        self.lightingGrid.addWidget(self.lbl_interpolation_type_lighting, 3, 0, 1, 1)

        self.txt_interpolation_lighting = QtWidgets.QLineEdit('')  # ToDo: (Max) May be a dropdown?; (Simon) Add selection
        self.lightingGrid.addWidget(self.txt_interpolation_lighting, 3, 1, 1, 1)

        self.lbl_thematic_description_lighting = QtWidgets.QLabel('Thematic Description:')
        self.lightingGrid.addWidget(self.lbl_thematic_description_lighting, 3, 2, 1, 1)

        self.txt_thematic_description_lighting = QtWidgets.QLineEdit('')  # ToDo: (Max) what do wanna add here?
        self.lightingGrid.addWidget(self.txt_thematic_description_lighting, 3, 3, 1, 1)

        # self.lbl_daytype = QtWidgets.QLabel('')  # ToDo: (Max) do we make the unit separate?
        # self.heatingGrid.addWidget(self.lbl_daytype, 4, 0, 1, 1)

        self.radio_weekdaytype_lighting = QtWidgets.QRadioButton('Weekday')
        self.lightingGrid.addWidget(self.radio_weekdaytype_lighting, 4, 0, 1, 1)

        self.radio_weekendtype_lighting = QtWidgets.QRadioButton('Weekend')
        self.lightingGrid.addWidget(self.radio_weekendtype_lighting, 4, 1, 1, 1)

        self.btn_select_lighting = QtWidgets.QPushButton('Select Values')  # ToDo: (Max) do we make the unit separate?
        self.lightingGrid.addWidget(self.btn_select_lighting, 4, 2, 1, 1)

        self.txt_path_select_values_lighting = QtWidgets.QLineEdit('')
        self.lightingGrid.addWidget(self.txt_path_select_values_lighting, 4, 3, 1, 1)

        self.lbl_unit_lighting = QtWidgets.QLabel('Unit:')
        self.lightingGrid.addWidget(self.lbl_unit_lighting, 5, 0, 1, 1)

        self.txt_unit_lighting = QtWidgets.QLineEdit('') # ToDo: (Max) Dropdown?
        self.lightingGrid.addWidget(self.txt_unit_lighting, 5, 1, 1, 1)

        self.radio_SIunit_lighting = QtWidgets.QRadioButton('SI')
        self.lightingGrid.addWidget(self.radio_SIunit_lighting, 5, 2, 1, 1)

        self.radio_fraction_unit_lighting = QtWidgets.QRadioButton('Fraction')
        self.lightingGrid.addWidget(self.radio_fraction_unit_lighting, 5, 3, 1, 1)


        self.lbl_ConvectiveFraction_lighting = QtWidgets.QLabel('Convective Fraction:')
        self.lightingGrid.addWidget(self.lbl_ConvectiveFraction_lighting, 6, 0, 1, 1)

        self.txt_ConvectiveFraction_lighting = QtWidgets.QLineEdit('')
        self.lightingGrid.addWidget(self.txt_ConvectiveFraction_lighting, 6, 1, 1, 1)

        self.lbl_radiant_fraction_lighting = QtWidgets.QLabel('Radiant Fraction:')
        self.lightingGrid.addWidget(self.lbl_radiant_fraction_lighting, 6, 2, 1, 1)

        self.txt_radiant_fraction_lighting = QtWidgets.QLineEdit('')
        self.lightingGrid.addWidget(self.txt_thematic_description_lighting, 6, 3, 1, 1)

        self.lbl_totalValue_lighting = QtWidgets.QLabel('Total Value:')
        self.lightingGrid.addWidget(self.lbl_totalValue_lighting, 7, 0, 1, 1)

        self.txt_totalValue_lighting = QtWidgets.QLineEdit('')
        self.lightingGrid.addWidget(self.txt_totalValue_lighting, 7, 1, 1, 1)

        self.l2Grid_lighting = QtWidgets.QGridLayout()

        self.btn_save_lighting = QtWidgets.QPushButton('Save')  # ToDo: (Simon) Add functionalities to save
        self.l2Grid_lighting.addWidget(self.btn_save_lighting, 0, 0, 1, 1)

        self.btn_reset_lighting = QtWidgets.QPushButton('Reset')  # ToDo: (Simon) Add functionalities to reset
        self.l2Grid_lighting.addWidget(self.btn_reset_lighting, 0, 1, 1, 1)

        self.btn_exit_lighting = QtWidgets.QPushButton('Exit')
        self.l2Grid_lighting.addWidget(self.btn_exit_lighting, 0, 2, 1, 1)

        self.btn_back_lighting = QtWidgets.QPushButton('Back')  # ToDo: (Simon) Add functionalities to back
        self.l2Grid_lighting.addWidget(self.btn_back_lighting, 0, 3, 1, 1)

        self.vbox.addLayout(self.l2Grid_lighting)

        # self.btn_save.clicked.connect(self.func_about)
        # self.btn_reset.clicked.connect(self.func_reset)
        self.btn_exit_lighting.clicked.connect(self.func_exit)
        # self.btn_back.clicked.connect(self.func_back)

        # def func_about(self):
        #     global posx, posy
        #     posx, posy = gf.dimensions(self)
        #     gf.next_window(self, about(), False)

    def func_exit(self):
        gf.close_application(self)




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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("QLabel{font-size: 10pt;} QPushButton{font-size: 10pt;} QRadioButton{font-size: 10pt;} QGroupBox{font-size: 10pt;} QComboBox{font-size: 10pt;} QLineEdit{font-size: 10pt;}")
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec_())

