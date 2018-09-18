# -*- coding: utf-8 -*-

#-------------------------------------- DATA PREPROCESSING ---------------------------------#

#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#Reading the dataset from data
dataset = pd.read_csv(r'C:\Users\phani.thontepu\newbies\data\slr09.csv')

#Creating Dependent and Independent variables
X = dataset['X'].values
y = dataset['Y'].values

#Visualizing the data 
plt.scatter(X,y)
plt.xlabel('pH of well water')
plt.ylabel('Bicarbonate (ppm)')
plt.show()

#Splitting the data into training set and test set
X_train,X_test = np.split(X,indices_or_sections = [28])
y_train,y_test = np.split(y,indices_or_sections = [28])

#------------------------------------ DATA PREPROCESSING ENDS -----------------------------#

#--------------------------------------- TRAINING   ---------------------------------------#

#Computing the values of sigma
sigma_X = sum(X_train)
sigma_y = sum(y_train)
sigma_xy = sum(np.multiply(X_train,y_train))
sigma_X_square = sum(np.square(X_train))
n = len(X_train)

#Computing the values of slope and intercept 
m_numerator = (n*sigma_xy)-(sigma_X*sigma_y)
m_denominator =  n*sigma_X_square - math.pow(sigma_X,2)
m = m_numerator/m_denominator

c_numerator = (sigma_y*sigma_X_square)-(sigma_xy*sigma_X)
c_denominator = (n*sigma_X_square) - math.pow(sigma_X,2)
c = c_numerator/c_denominator

#-------------------------------------- TRAINING ENDS  ------------------------------------#

#------------------------------- PREDICTION AND PLOTING -----------------------------------#

#Predicting the Results
y_pred = X_test*m + c

#Visualizing the Results
plt.scatter(X_test,y_test,c='red')
plt.plot(X_test,y_pred)
plt.xlabel('pH of well water')
plt.ylabel('Bicarbonate (ppm)')
plt.show()

#------------------------------ PREDICTION AND PLOTING ENDS--------------------------------#