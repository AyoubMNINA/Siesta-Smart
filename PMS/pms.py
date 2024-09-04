
#Travail réalisé par : Ayoub Mnina 
#pip install sys, pyqt5, pandas, numpy, sklearn, datetime, uuid, random, joblib, ... 

import sys
import warnings

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pandas as pd
import random as rd  
import datetime as dt
import numpy as np

from sklearn.preprocessing import LabelEncoder, RobustScaler

import uuid
import pycountry
import joblib

pd.set_option('display.max_columns', None)
warnings.filterwarnings("ignore")

class PMS(QWidget):
    def __init__(self):
        super().__init__()
        self.booking_data = pd.DataFrame(columns=["num_reservation",
                                                "hotel",
                                                "lead_time",
                                                "meal",
                                                "country",
                                                "market_segment",
                                                "distribution_channel",
                                                "is_repeated_guest",
                                                "reserved_room_type",
                                                "booking_changes",
                                                "deposit_type",
                                                "days_in_waiting_list",
                                                "customer_type",
                                                "adr",
                                                "required_car_parking_spaces",
                                                "total_of_special_requests",
                                                "total_stays_nights",
                                                "total_people",
                                                "is_reserved_room",
                                                "net_previous_cancelled"])
        self.booking_data = pd.concat([self.booking_data, pd.Series([np.nan]*len(self.booking_data.columns), index=self.booking_data.columns).to_frame().T], ignore_index=True)
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        self.initIU()

    #Home Window
    def initIU(self): 
        screen_geometry = QDesktopWidget().screenGeometry() #Get the screen geometry
        self.setGeometry(150, 40, screen_geometry.width()-300, screen_geometry.height()-100)
        #self.setFixedSize(screen_geometry.width(), screen_geometry.height()) #make the window non-resizable
        self.setWindowTitle("Siesta Smart PMS")
        icon = QIcon('Siesta_Smart_preview.png')
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color : #FFFFF4; color : #0C090A")

        mainBox = QVBoxLayout() 
        font1 = QFont("Times New Roman", 13) #Create the font that we will use for all the text in the app

        #Part deleted because of Confidentiality 🔏

        #Part deleted because of Confidentiality 🔏

        #Part deleted because of Confidentiality 🔏

        tabBox = QHBoxLayout()
        tabs = QTabWidget()
        tabs.setFont(font1)
        tabs.addTab(self.inputUI(), "New Booking (Input data)")
        tabs.addTab(self.uploadUI(), "New Booking (Upload data)")
        tabBox.addWidget(tabs)
        mainBox.addLayout(tabBox) #Add tabs to the main Window

        self.setLayout(mainBox)
        self.show()

    #Create the Widget UI where we can : Inputt Raw Data of New Booking
    def inputUI(self):
        self.inputTab = QWidget()
        grid = QGridLayout()
        
        #---------------------------------------------------- Peoples Group -----------------------------------------
        
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏

        #-------------------------------------------------------------------------------------------------------

        grid.addWidget(groupBox1, 0, 0, 1, 4)
        grid.addWidget(groupBox2, 0, 4, 1, 2)
        grid.addWidget(groupBox4, 1, 0, 1, 2)
        grid.addWidget(groupBox5, 1, 2, 1, 2)
        grid.addWidget(groupBox6, 1, 4, 1, 2)
        grid.addWidget(groupBox7, 2, 0, 1, 2)
        grid.addWidget(groupBox8, 2, 2, 1, 2)
        grid.addWidget(groupBox9, 2, 4, 1, 2)
        grid.addWidget(groupBox10, 3, 0, 1, 3)
        grid.addWidget(groupBox11, 3, 3, 1, 3)
        self.inputTab.setLayout(grid)
        return self.inputTab
    
    #Update the People Group After inserting the number total of peples in the booking
    def updatePeopleFields(self):
        #Clear the previous rows
        #Part deleted because of Confidentiality 🔏

        self.people_countries = ["PRT"] * int(self.nbTotalPeoples.text()) #Create this list to store just the first(main) person who make the booking
        #Add new rows based on the value in the QSpinBox
        for i in range(int(self.nbTotalPeoples.text())):
            #Part deleted because of Confidentiality 🔏
            #Part deleted because of Confidentiality 🔏

    #Update the Days & Dates group After selecting the check-out date
    def updateStaysayLeadtime(self):
        #Part deleted because of Confidentiality 🔏

    #update the Predict Group After clicking the predict button
    def predict_(self):
        #Add data to the Booking_DataFrame 
        #Part deleted because of Confidentiality 🔏
        print("********************************** Encoded & Scaled Data *************************************")

        # Modify the type of certains columns
        #Part deleted because of Confidentiality 🔏
        
        #Label Encoding refers to converting the labels into a numeric form so as to convert them into the machine-readable form
        #Part deleted because of Confidentiality 🔏

        #Concat the new_df with the booking_historic_data to scal the input data
        #Part deleted because of Confidentiality 🔏

        #Scal the encoded data with a RobustScaler
        robustScal = RobustScaler()
        #Part deleted because of Confidentiality 🔏

        #Predict the cancellation using plk trained Models
        #Part deleted because of Confidentiality 🔏

        #Part deleted because of Confidentiality 🔏

        #Part deleted because of Confidentiality 🔏
        

    #Confirming the Booking and send the data to the BDD
    def confirmBooking(self):
        #Part deleted because of Confidentiality 🔏

    #Launch New Booking
    def newBooking(self):
        #----------- TO_DO -------------
        #*******************************
        #Part deleted because of Confidentiality 🔏
        
    #Create the Widget UI where we can : Upload Data of New Booking
    def uploadUI(self):
        self.uploadTab = QWidget()
        grid2 = QGridLayout()

        #--------------------------------------------------------------------------------------------
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #Part deleted because of Confidentiality 🔏
        #---------------------------------------------------------------------------------------------


        grid2.addWidget(group2Box1, 0, 0, 1, 2)
        grid2.addWidget(group2Box2, 1, 0, 1, 2)
        grid2.addWidget(group2Box3, 2, 0, 1, 1)
        grid2.addWidget(group2Box4, 2, 1, 1, 1)
        self.uploadTab.setLayout(grid2)
        return self.uploadTab


#Launching my application
if __name__ == '__main__':
    app = QApplication([])
    fen = PMS()
    sys.exit(app.exec_())