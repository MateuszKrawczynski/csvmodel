# Read this to the end to understand how to use the framework
# CsvModelTraining
 CsvModel is a framework witten for python to easly train models over a .csv file. These models are able to predict the result when given parameters and trainiing csv
#  Importing
To import this framework you need to have the pandas lib installed. Python code: import csvmodel
# Training your model
To train you write csvmodel.train.save(PATH TO YOUR .CSV FILE , NAME OF MODEL YOU ARE TRAINING) .
Every trained model will be in the same directory as your main.py file 
# Loading your model
To load your trained model write csvmodel.load.model(NAME OF YOUR MODEL)
# Predicting with your model
After loading your model it can predict from given parameters.
To do that you write csvmodel.prompt(PARAMETERS)
# What are PARAMETERS?
Paramaters is a list of parametrs , like: ["abc","def","xyz"] .
# Bulid of the .csv file for training
First column of the .csv file is a result , it is what can be predicted. 
Rest of the columns are parameters.
If your .csv file isn't seperated by ";" , then you need do set csvmodel.DELIMETER to your seperator ex. ","



