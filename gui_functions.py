# import of libraries
import os
from PySide2 import QtWidgets, QtGui, QtCore




def screenSizer(self, posx, posy, width, height, app):
    """func to get size of screen and scale window accordingly"""
    sizefactor = round(app.primaryScreen().size().height()*0.001)   # factor for scaling window, depending on height
    posx *= sizefactor
    posy *= sizefactor
    width *= sizefactor
    height *= sizefactor
    return posx, posy, width, height, sizefactor



def windowSetup(self, posx, posy, width, height, pypath, title, winFac = 1):
    """func for loading icon, setting size and title"""
    try:                                                            # try to load e3d Icon
        self.setWindowIcon(QtGui.QIcon(os.path.join(pypath, r'pictures\e3dIcon.png')))
    except:
        print('error finding file icon')
    self.setGeometry(posx, posy, width * winFac, height * winFac)   # setting window size
    self.setFixedSize(width * winFac, height * winFac)              # fixing window size
    self.setWindowTitle(title)


def load_banner(self, path, sizefactor, banner_size=150):
    """loading image from path to self.vbox"""
    try:
        self.banner = QtWidgets.QLabel(self)
        self.banner.setPixmap(QtGui.QPixmap(path))
        self.banner.setScaledContents(True)
        self.banner.setMinimumHeight(banner_size*sizefactor)
        self.banner.setMaximumHeight(banner_size*sizefactor)
        self.vbox.addWidget(self.banner)
    except:
        print('error finding banner picture')



def messageBox(self, header, message):
    """pop up message box with header and message"""
    self.message_complete = QtWidgets.QMessageBox.information(self, header, message)



def next_window(self, window, close=True):
    """calls next window, closes current if True"""
    self.next_window_jump = window
    self.next_window_jump.show()
    if close == True:
        self.hide()


def dimensions(self):
    """gets current dimensions of window"""
    posx = self.geometry().x()
    posy = self.geometry().y()
    return posx, posy



def close_application(self):
    """quit dialog, to confirm exiting"""
    choice = QtWidgets.QMessageBox.question(self, 'Attention!', 'Do you want to quit?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if choice == QtWidgets.QMessageBox.Yes:
        QtCore.QCoreApplication.instance().quit()
    else:
        pass



def progressLoD(self, max):
    """setting up progress bar"""
    while self.completedLoD < max:
        self.completedLoD += 1
        self.pB_scanLoD.setValue(self.completedLoD)



def progressTransfrom(self, max):
    """setting up progress bar"""
    while self.completedTransform < max:
        self.completedTransform += 1
        self.pB_transformation.setValue(self.completedTransform)



def setTableRowColor(self, colorCode, index):
    """sets the background color of a row with by index"""
    if self.gB_buildings.isChecked() and index >= 0:
        qColor = QtGui.QColor(*colorCode)
        for j in range(self.tbl_buildings.columnCount()-1):
            try:
                self.tbl_buildings.item(index, j).setBackground(qColor)
            except:
                print('error setting background color')

        self.cBoxes[index].setStyleSheet("QCheckBox {background-color: rgb" + str(colorCode) + "}")



def createListForComboBox(dictionary, maxLength):
    """creating list for adding dictionary to combo box"""
    finished = []
    for key in dictionary:
        if key == '':
            finished.append('')
        else:
            finished.append(key + ' : ' + ' ' * (maxLength - len(key)) + str(dictionary[key]))
    return finished