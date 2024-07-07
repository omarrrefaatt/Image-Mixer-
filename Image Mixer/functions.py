from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  pyqtSignal
from imageviewer import  ImageViewer
from PyQt5.QtWidgets import  QLabel
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import numpy as np

class CustomLabel(QLabel):
    doubleClicked = pyqtSignal()
    move_signal = pyqtSignal(int, int)
    released = pyqtSignal()
    
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.setMouseTracking(True)
        self.origin = None
        self.x=0
        self.y=0
        
    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()
        super(CustomLabel, self).mouseDoubleClickEvent(event)


    def mousePressEvent(self, event):
            self.origin = event.pos()
            if self.x!=0 and self.y!=0:
                self.x=0
                self.y=0



    def mouseMoveEvent(self, event):
        global x
        global y
        
        if self.origin:
            delta = event.pos() - self.origin
            if delta.x()>0:
                self.x+=1
            elif delta.x()<0:
                self.x-=1
            elif delta.y()<0:
                self.y+=2
            elif delta.y()>0:
                self.y-=2
            self.origin = event.pos()
            self.move_signal.emit(self.x, self.y)
            

    def mouseReleaseEvent(self, event):
        self.origin = None
        self.released.emit()
        # You can add additional logic here if neededs

    def remove_image(self):
        self.clear()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.createImageLayouts()
        self.windowLayout2 = QtWidgets.QVBoxLayout()
        self.windowLayout2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.windowLayout2.setObjectName("windowLayout2")
        self.windowLayout2.addWidget(self.output_label2)
        self.gridLayout_7.addLayout(self.windowLayout2, 1, 2, 1, 1)
        self.windowLayout1 = QtWidgets.QVBoxLayout()
        self.windowLayout1.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.windowLayout1.setObjectName("windowLayout1")
        self.windowLayout1.addWidget(self.output_label1)
        self.gridLayout_7.addLayout(self.windowLayout1, 1, 0, 1, 1)
        self.windowRadioButton2 = QtWidgets.QRadioButton(self.frame_3)
        self.windowRadioButton2.setObjectName("windowRadioButton2")
        self.gridLayout_7.addWidget(self.windowRadioButton2, 0, 2, 1, 1)
        self.windowRadioButton1 = QtWidgets.QRadioButton(self.frame_3)
        self.windowRadioButton1.setObjectName("windowRadioButton1")
        self.gridLayout_7.addWidget(self.windowRadioButton1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 0, 1, 1, 1)
        self.mixingComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.mixingComboBox.setObjectName("mixingComboBox")
        self.mixingComboBox.addItem("")
        self.mixingComboBox.addItem("")
        self.gridLayout_9.addWidget(self.mixingComboBox, 1, 1, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox = QtWidgets.QGroupBox(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_11.addWidget(self.comboBox, 0, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 1, 0, 1, 1)
        self.regionSizeSlide = QtWidgets.QSlider(self.groupBox)
        self.regionSizeSlide.setOrientation(QtCore.Qt.Horizontal)
        self.regionSizeSlide.setObjectName("regionSizeSlide")
        self.regionSizeSlide.setRange(0,100)
        self.gridLayout_11.addWidget(self.regionSizeSlide, 1, 1, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 1, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 1, 2, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-color: lightblue;")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox3 = QtWidgets.QComboBox(self.frame_8)
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.gridLayout_5.addWidget(self.comboBox3, 0, 1, 1, 2)
        self.imgLayout3 = QtWidgets.QVBoxLayout()
        self.imgLayout3.setObjectName("imgLayout3")
        self.imgLayout3.addWidget(self.img_label3)
        self.gridLayout_5.addLayout(self.imgLayout3, 1, 0, 1, 3)
        self.componentLayout3 = QtWidgets.QVBoxLayout()
        self.componentLayout3.setObjectName("componentLayout3")
        self.componentLayout3.addWidget(self.component_label3)
        self.gridLayout_5.addLayout(self.componentLayout3, 1, 3, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 2)
        self.componentSlider3 = QtWidgets.QSlider(self.frame_8)
        self.componentSlider3.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider3.setObjectName("componentSlider3")
        self.gridLayout_5.addWidget(self.componentSlider3, 2, 2, 1, 2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_8)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_3.display(100)
        self.gridLayout_5.addWidget(self.lcdNumber_3, 2, 4, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 2, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox1 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.gridLayout_3.addWidget(self.comboBox1, 0, 1, 1, 2)
        self.imgLayout1 = QtWidgets.QVBoxLayout()
        self.imgLayout1.setObjectName("imgLayout1")
        self.imgLayout1.addWidget(self.img_label1)
        self.gridLayout_3.addLayout(self.imgLayout1, 1, 0, 1, 3)
        self.componentLayout1 = QtWidgets.QVBoxLayout()
        self.componentLayout1.setObjectName("componentLayout1")
        self.componentLayout1.addWidget(self.component_label1)
        self.gridLayout_3.addLayout(self.componentLayout1, 1, 3, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 2)
        self.componentSlider1 = QtWidgets.QSlider(self.frame_6)
        self.componentSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider1.setObjectName("componentSlider1")
        self.gridLayout_3.addWidget(self.componentSlider1, 2, 2, 1, 2)
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.frame_6)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.lcdNumber_1.display(100)
       
        
        self.gridLayout_3.addWidget(self.lcdNumber_1, 2, 4, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox4 = QtWidgets.QComboBox(self.frame_9)
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.gridLayout_6.addWidget(self.comboBox4, 0, 1, 1, 3)
        self.imgLayout4 = QtWidgets.QVBoxLayout()
        self.imgLayout4.setObjectName("imgLayout4")
        self.imgLayout4.addWidget(self.img_label4)
        self.gridLayout_6.addLayout(self.imgLayout4, 1, 0, 1, 3)
        self.componentLayout4 = QtWidgets.QVBoxLayout()
        self.componentLayout4.setObjectName("componentLayout4")
        self.componentLayout4.addWidget(self.component_label4)
        self.gridLayout_6.addLayout(self.componentLayout4, 1, 3, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 2)
        self.componentSlider4 = QtWidgets.QSlider(self.frame_9)
        self.componentSlider4.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider4.setObjectName("componentSlider4")
        self.gridLayout_6.addWidget(self.componentSlider4, 2, 2, 1, 2)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.frame_9)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_4.display(100)
        self.gridLayout_6.addWidget(self.lcdNumber_4, 2, 4, 1, 1)
        self.gridLayout_2.addWidget(self.frame_9, 1, 2, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox2 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.gridLayout_4.addWidget(self.comboBox2, 0, 1, 1, 3)
        self.imgLayout2 = QtWidgets.QVBoxLayout()
        self.imgLayout2.setObjectName("imgLayout2")
        self.imgLayout2.addWidget(self.img_label2)
        self.gridLayout_4.addLayout(self.imgLayout2, 1, 0, 1, 3)
        self.componentLayout2 = QtWidgets.QVBoxLayout()
        self.componentLayout2.setObjectName("componentLayout2")
        self.componentLayout2.addWidget(self.component_label2)
        self.gridLayout_4.addLayout(self.componentLayout2, 1, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 2)
        self.componentSlider2 = QtWidgets.QSlider(self.frame_7)
        self.componentSlider2.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider2.setObjectName("componentSlider2")
        self.gridLayout_4.addWidget(self.componentSlider2, 2, 2, 1, 2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_7)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.display(100)
        self.gridLayout_4.addWidget(self.lcdNumber_2, 2, 4, 1, 1)
        self.gridLayout_2.addWidget(self.frame_7, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 3)
        self.gridLayout_12.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMagnitude_Phase = QtWidgets.QAction(MainWindow)
        self.actionMagnitude_Phase.setObjectName("actionMagnitude_Phase")
        self.currentmode = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.thereisimage =False
        self.images={
            '':'',
            'image1':None,
            'image2':None,
            'image3':None,
            'image4':None,

        }
        self.mixingdata ={
         'image1':{
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,

        },
        'image2':{
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,
        },
        'image3':{
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,
        },
        'image4':{
            '':'',
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,
        },

        }
        for i in range(1,5):
          slidername = f"componentSlider{i}"
          slider = getattr(self, slidername, None)
          slider.setRange(0,100)
          slider.setValue(100)
          slider.valueChanged.connect(lambda value, range=i: self.adjustratio(value, range))
          
          
        self.mixingComboBox.currentIndexChanged.connect(lambda index: self.changemode(index))
        self.regionSizeSlide.valueChanged.connect(lambda value: self.regionslice(value))
        self.windowRadioButton1.clicked.connect(self.on_windowRadioButton_clicked)
        self.windowRadioButton2.clicked.connect(self.on_windowRadioButton_clicked)
        self.comboBox.currentIndexChanged.connect(lambda index: self.regionchange(index))

    def regionchange(self, index):
        if index == 0:
            self.regionslice(self.regionSizeSlide.value())
        elif index == 1:
            self.regionslice(self.regionSizeSlide.value())

    def adjustratio(self, value, range):
        
        lcd = f"lcdNumber_{range}"
        lcdnumber = getattr(self, lcd, None)
        lcdnumber.display(value)
        image = f"image{range}"
        comboBox = f"comboBox{range}"
        comboBox_instance = getattr(self, comboBox, None)
        componentname = comboBox_instance.currentText()
        ratio = f"Ratio{componentname}"
        self.mixingdata[image][ratio]=value/100
        if self.thereisimage:
           self.recover_image()

    def changemode(self, index):   
        for i in range(1, 5):
            self.currentmode = index
            comboBox = f"comboBox{i}"
            comboBox_instance = getattr(self, comboBox, None)
            image = f"image{i}"
            if index ==0:
                comboBox_instance.setItemText(0, "Real")
                comboBox_instance.setItemText(1,  "Imaginary")
            else:
                comboBox_instance.setItemText(0, "Magnitude")
                comboBox_instance.setItemText(1,  "Phase")
                

            

            

    def on_windowRadioButton_clicked(self):
        # This method will be called when windowRadioButton1 is clicked
        if self.windowRadioButton1.isChecked():
            self.output_label2.remove_image()
            if self.thereisimage:
               self.recover_image()
        elif self.windowRadioButton2.isChecked():
            self.output_label1.remove_image()
            if self.thereisimage:
               self.recover_image()

    def createImageLayouts(self):
         
        self.img_label1 = CustomLabel() 
        self.img_label2 = CustomLabel() 
        self.img_label3 = CustomLabel() 
        self.img_label4 = CustomLabel() 
        

        self.component_label1 = CustomLabel() 
        self.component_label2 = CustomLabel() 
        self.component_label3 = CustomLabel() 
        self.component_label4 = CustomLabel() 

        self.output_label1 = CustomLabel()
        self.output_label2 = CustomLabel()

        

        # Connect the doubleClicked 

        self.img_label1.doubleClicked.connect(lambda: self.onDoubleClick(1))
        self.img_label2.doubleClicked.connect(lambda: self.onDoubleClick(2))
        self.img_label3.doubleClicked.connect(lambda: self.onDoubleClick(3))
        self.img_label4.doubleClicked.connect(lambda: self.onDoubleClick(4))


    def onDoubleClick(self,index):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.xpm *.jpg *.bmp *.gif)", options=options)
        if image_path:

            labelname1 = f"img_label{index}"
            imagelabel1 = getattr(self, labelname1, None)
            labelname2 = f"component_label{index}"
            imagelabel2 = getattr(self, labelname2, None)

            image =ImageViewer(imagelabel1,imagelabel2,image_path)
            imagename = f"image{index}"
            self.mixingdata[imagename]["Magnitude"] = image.getorgcomponents("Magnitude")
            self.mixingdata[imagename]["Phase"] = image.getorgcomponents("Phase")
            self.mixingdata[imagename]["Real"] = image.getorgcomponents("Real")
            self.mixingdata[imagename]["Imaginary"] = image.getorgcomponents("Imaginary")
            self.images[imagename] = image
            
            
            comboBox = f"comboBox{index}"
            comboBox_instance = getattr(self, comboBox, None)
            image.show_ft_component(comboBox_instance.currentText())
            comboBox_instance.currentIndexChanged.connect(lambda index: image.show_ft_component(comboBox_instance.currentText()))
            
            
            imagelabel1.move_signal.connect(lambda x, y: image.adjust_brightness_contrast(x, y))
            self.thereisimage = True
            self.recover_image()

    def recover_image(self):
        if self.windowRadioButton1.isChecked() or self.windowRadioButton2.isChecked(): 
            # Assuming componentsimage is a NumPy array
            if self.currentmode == 0:
                real = 0
                imaginary = 0
                
                for i  in range(1,5):
                    image = f"image{i}"
                    comboBox = f"comboBox{i}"
                    comboBox_instance = getattr(self, comboBox, None)
                    componentname = comboBox_instance.currentText()
                    ratio = f"Ratio{componentname}"
                    if componentname =="Real":
                        real += self.mixingdata[image][componentname]*self.mixingdata[image][ratio] 
                    elif componentname =="Imaginary":
                        imaginary += self.mixingdata[image][componentname]*self.mixingdata[image][ratio] 
                complex_array = real + (1j * imaginary)

            else:
                Magnitude = 0
                phase = 0
                for i  in range(1,5):
                    image = f"image{i}"
                    comboBox = f"comboBox{i}"
                    comboBox_instance = getattr(self, comboBox, None)
                    componentname = comboBox_instance.currentText()
                    ratio = f"Ratio{componentname}"
                    if componentname =="Magnitude":
                        Magnitude += self.mixingdata[image][componentname]*self.mixingdata[image][ratio] 
                    if componentname =="Phase":
                        phase += self.mixingdata[image][componentname]*self.mixingdata[image][ratio] 
                complex_array = Magnitude * np.exp(1j * phase)

            # Perform inverse 2D Fourier Transform
            f_transform_inverse = np.fft.ifft2(np.fft.ifftshift(complex_array))

            # Take the real part to get the recovered image
            componentsimage = np.real(f_transform_inverse)
            recovered_image = (componentsimage - np.min(componentsimage)) / (np.max(componentsimage) - np.min(componentsimage))
            recovered_image = (recovered_image * 255).astype(np.uint8)

            # Resize the image
            resized_image = cv2.resize(recovered_image, (200, 200))

            # Convert the NumPy array to a QImage
            height, width = resized_image.shape
            qt_image = QtGui.QImage(resized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)

            # Convert QImage to QPixmap
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            if self.windowRadioButton1.isChecked():
                # Assuming self.ft_label is a QLabel where you want to display the recovered image
                self.output_label1.setPixmap(pixmap)  
            elif self.windowRadioButton2.isChecked(): 
                self.output_label2.setPixmap(pixmap)  

    def regionslice(self,value):
        if self.comboBox.currentText()== "Inner Region":
            for i in range(1,5):
                imagename = f"image{i}"
                if self.images[imagename] != None:
                    self.images[imagename].regionsliceinner(value,self.currentmode)
                    if self.currentmode==0:
                        self.mixingdata[imagename]["Real"] = self.images[imagename].getcomponents("Real")
                        self.mixingdata[imagename]["Imaginary"] = self.images[imagename].getcomponents("Imaginary")
                    else:
                        self.mixingdata[imagename]["Magnitude"] = self.images[imagename].getcomponents("Magnitude")
                        self.mixingdata[imagename]["Phase"] = self.images[imagename].getcomponents("Phase")
                    
                    self.recover_image()
        elif self.comboBox.currentText() == "Outer Region":
               for i in range(1,5):
                imagename = f"image{i}"
                if self.images[imagename] != None:
                    self.images[imagename].regionsliceouter(value,self.currentmode)
                    if self.currentmode ==0:
                        self.mixingdata[imagename]["Real"] = self.images[imagename].getcomponents("Real")
                        self.mixingdata[imagename]["Imaginary"] = self.images[imagename].getcomponents("Imaginary")
                    else:
                        self.mixingdata[imagename]["Magnitude"] = self.images[imagename].getcomponents("Magnitude")
                        self.mixingdata[imagename]["Phase"] = self.images[imagename].getcomponents("Phase")
                    self.recover_image()
               

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.windowRadioButton2.setText(_translate("MainWindow", "Window 2"))
        self.windowRadioButton1.setText(_translate("MainWindow", "Window 1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Mixing Components"))
        self.label_9.setText(_translate("MainWindow", "Mixing Type:"))
        self.mixingComboBox.setItemText(0, _translate("MainWindow", "Imaginary-Real"))
        self.mixingComboBox.setItemText(1, _translate("MainWindow", "Magnitude-Phase"))
        
        self.groupBox.setTitle(_translate("MainWindow", "Region Mixing"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Outer Region"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Inner Region"))
        self.label_14.setText(_translate("MainWindow", "Region Size:"))
        self.label_3.setText(_translate("MainWindow", "Image 3"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "Imaginary"))
        self.label_7.setText(_translate("MainWindow", "Component Value:"))
        self.label.setText(_translate("MainWindow", "Image 1"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Imaginary"))
        self.label_5.setText(_translate("MainWindow", "Component Value:"))
        self.label_4.setText(_translate("MainWindow", "Image 4"))
        self.comboBox4.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox4.setItemText(1, _translate("MainWindow", "Imaginary"))
        self.label_8.setText(_translate("MainWindow", "Component Value:"))
        self.label_2.setText(_translate("MainWindow", "Image 2"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Imaginary"))
        self.label_6.setText(_translate("MainWindow", "Component Value:"))
        self.actionMagnitude_Phase.setText(_translate("MainWindow", "Magnitude-Phase"))

