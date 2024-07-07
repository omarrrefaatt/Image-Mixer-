import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor,QBrush,QPainterPath
from PyQt5.QtCore import Qt, QRect
from PIL import ImageEnhance
from PIL import Image as PilImage
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



class ImageViewer:
    def __init__(self,imagelabel1, imagelabel2,path):
        self.path = path

        # Initialize variables
        self.image = None
        self.adjustedimage = None
        self.currentviewedcomp="Magnitude"
        self.currentpixmap =QPixmap(self.path) 

        self.image_label = imagelabel1
        self.ft_label = imagelabel2
        self.load_image()
        f_transform = np.fft.fft2(self.image)
        f_transform_shifted = np.fft.fftshift(f_transform)
        # Display the selected FT component
        self.magnitude = np.abs(f_transform_shifted)

        self.phase = np.angle(f_transform_shifted)


        self.real_part = np.real(f_transform_shifted)


        self.imaginary_part = np.imag(f_transform_shifted)
        new_size = (200, 200)

        self.orgcomponents = {
            '':'',
            'Magnitude':cv2.resize(self.magnitude, new_size),
            'Phase':cv2.resize(self.phase, new_size),
            'Real':cv2.resize(self.real_part, new_size),
            'Imaginary':cv2.resize(self.imaginary_part, new_size),
        }
        self.components = {
            '':'',
            'Magnitude':cv2.resize(self.magnitude, new_size),
            'Phase':cv2.resize(self.phase, new_size),
            'Real':cv2.resize(self.real_part, new_size),
            'Imaginary':cv2.resize(self.imaginary_part, new_size),
        }
        self.show_image()
        self.show_ft_component("Magnitude")
        
        
    def getorgcomponents(self,text):
        return self.orgcomponents[text]
    
    def getcomponents(self,text):
        return self.components[text]
        
    def load_image(self):
        
        if self.path:
            # Read the image using OpenCV
            original_image = cv2.imread(self.path)
            self.image =original_image
            if original_image is not None:
                # Convert to grayscale
                gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

                # Resize to the smallest size
                min_size = min(original_image.shape[:2])
                resized_image = cv2.resize(gray_image, (200, 200))

                # Update the image and display it
                self.image = resized_image
                self.adjustedimage = resized_image
                
                

    def show_image(self):
        desired_size = (200, 200)

        
        resized_image = cv2.resize(self.adjustedimage, (desired_size[1], desired_size[0]))

        # Resize the image to the desired size
        

        qt_image = QtGui.QImage(resized_image.data, resized_image.shape[1], resized_image.shape[0], resized_image.shape[1], QtGui.QImage.Format_Grayscale8)

        # Create a QPixmap with the desired size
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        
    
        # Set the QPixmap on the QLabel
        self.image_label.setPixmap(pixmap)




        # Convert the resized image to a QImage
    
    def show_ft_component(self,text):
        if self.image is not None:
            self.currentviewedcomp=text
            component = self.components[text]
            desired_size = (200, 200)
            # Display the FT component in the label
            recovered_image = (component - np.min(component)) / (np.max(component) - np.min(component))
            img_pil = (recovered_image * 255).astype(np.uint8)
            img = np.array(img_pil)
            resized_image = cv2.resize(img, (desired_size[1], desired_size[0]))
            qt_image = QtGui.QImage(resized_image.data, resized_image.shape[1], resized_image.shape[0], resized_image.shape[1], QtGui.QImage.Format_Grayscale8)
            
            self.currentpixmap = QtGui.QPixmap.fromImage(qt_image)

            self.ft_label.setPixmap(self.currentpixmap)

    def regionsliceinner(self,value,mode):
        pixmap = self.currentpixmap.copy()
        newpixmap = self.currentpixmap.copy()
        percentage = value / 100
        
        rectanglewidth = int(pixmap.width()* percentage)
        rectangleheight = int(pixmap.height()* percentage)
        start_x = int((pixmap.width() - rectanglewidth) // 2)    
        start_y = int((pixmap.height() -  rectangleheight) // 2)
        painter = QPainter(pixmap)
        painter.setPen(Qt.blue)
        brush = QBrush(QColor(0, 0, 255, 128))  # RGB values: 0 for red, 0 for green, 255 for blue, 128 for alpha (transparency)
        painter.setBrush(brush)
        painter.drawRect(start_x, start_y, rectanglewidth, rectangleheight)
        painter.end()
        self.ft_label.setPixmap(pixmap)

        newrectangle = QRect(start_x, start_y, rectanglewidth, rectangleheight)
        newpixmap = newpixmap.copy(newrectangle)
        newpixmap.save("insliced.png")
        cropped = cv2.imread("insliced.png", cv2.IMREAD_GRAYSCALE)
        dimensions = cropped.shape
        outerdimensions = (200,200)
        outer =[outerdimensions[0],outerdimensions[1]]
        sliceing_array =np.zeros(outer)
        start_r =(outerdimensions[0] - dimensions[0])//2
        start_c = (outerdimensions[1] - dimensions[1])//2
        sliceing_array[start_r:start_r+dimensions[0], start_c:start_c+dimensions[1]] = 1
        if mode==1:
            self.components["Magnitude"] = self.orgcomponents["Magnitude"]*sliceing_array
            self.components["Phase"] = self.orgcomponents["Phase"]*sliceing_array
        else:
            self.components["Real"] = self.orgcomponents["Real"]*sliceing_array
            self.components["Imaginary"] = self.orgcomponents["Imaginary"]*sliceing_array
    
    def regionsliceouter(self,value,mode):
        pixmap = self.currentpixmap.copy()
        newpixmap = self.currentpixmap.copy()
        percentage = value / 100
        rectanglewidth = int(pixmap.width()* percentage)
        rectangleheight = int(pixmap.height()* percentage)
        start_x = int((pixmap.width() - rectanglewidth) // 2)    
        start_y = int((pixmap.height() -  rectangleheight) // 2)

        path = QPainterPath()
        path.addRect(0,0,pixmap.width(),pixmap.height())
        path.addRect(start_x,start_y,rectanglewidth,rectangleheight)

        painter = QPainter(pixmap)
        painter.setPen(Qt.blue)
        brush = QBrush(QColor(0, 0, 255, 128))  # RGB values: 0 for red, 0 for green, 255 for blue, 128 for alpha (transparency)
        painter.setBrush(brush)
        painter.drawPath(path)

        painter.end()
        self.ft_label.setPixmap(pixmap) 
        newrectangle = QRect(start_x, start_y, rectanglewidth, rectangleheight)
        
        cropedpaint = QPainter(newpixmap)
        cropedpaint.fillRect(newrectangle,Qt.black)
        cropedpaint.drawRect(start_x, start_y, rectanglewidth, rectangleheight)
        cropedpaint.end()
        newpixmap.save("outsliced.png")
        sliced = cv2.imread("outsliced.png", cv2.IMREAD_GRAYSCALE)
        sliced[sliced>=1] = 1
        if mode==1:
            self.components["Magnitude"] = self.orgcomponents["Magnitude"]*sliced
            self.components["Phase"] = self.orgcomponents["Phase"]*sliced
        else:
            self.components["Real"] = self.orgcomponents["Real"]*sliced
            self.components["Imaginary"] = self.orgcomponents["Imaginary"]*sliced



    def adjust_brightness_contrast(self, x, y):
        # Normalize x and y values
        x_normalized = (x + 60) / 60
        y_normalized = (y + 60) / 60

        # Convert the image to PIL format
        pil_image = PilImage.fromarray(self.image)

        # Apply contrast adjustment using ImageEnhance.Contrast
        contrast_enhancer = ImageEnhance.Contrast(pil_image)
        pil_image_contrasted = contrast_enhancer.enhance(x_normalized)

        # Apply brightness adjustment using ImageEnhance.Brightness
        brightness_enhancer = ImageEnhance.Brightness(pil_image_contrasted)
        pil_image_adjusted = brightness_enhancer.enhance(y_normalized)

        # Convert the adjusted PIL image back to NumPy array
        self.adjustedimage = np.array(pil_image_adjusted)

        self.show_image() 

    # def getorgcomponents(self,text,rows_percentage,col_percentage,type="inner"):
    #     component=self.orgcomponents[text]
    #     number_of_rows=rows_percentage*component.shape[0]/100
    #     number_of_col=col_percentage*component.shape[1]/100
    #     # // => floor division
    #     starting_row=(component.shape[0]//2)-(number_of_rows//2)
    #     ending_row=starting_row+(number_of_rows)

    #     starting_col=(component.shape[1]//2)-(number_of_col//2)
    #     ending_col=starting_col+(number_of_col)
    #     if type=="inner":
    #         bounding_arr=np.zeros(component.shape)
    #         bounding_arr[starting_row:ending_row, starting_col:ending_col] = 1
    #     else:
    #         bounding_arr=np.ones(component.shape)
    #         bounding_arr[starting_row:ending_row, starting_col:ending_col] = 0
        
    #     return np.multiply(component,bounding_arr) 

