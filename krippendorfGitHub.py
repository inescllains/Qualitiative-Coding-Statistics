import pandas as pd 
# Pandas is a Python library that analyses data present in csv files.
# This library was created by the Python Package Index which is the 
# official third-party that holds all the Python libraries.

import krippendorff as kp
# Python library that calculates Krippendorff's alpha.

# Meaning of the variables:
# csvCJ / IL = csv file Corinna Jentzsch / Ines Lains.
# dfCJ / IL = DataFrame Corinna Jentzsch / Ines Lains.
# relevanceCJ / IL = The data in the relevance column of the file of Corinna Jentzsch / Ines Lains.
# relevanceData = The list that holds the values of the relevance columns of both coders.

csvCJ = pd.read_csv('Coding of Articles-CJ.csv', index_col=False)
# Gets the file from the computer and gets it ready to be read.
# The file needs to be in csv format, otherwise it wont be able to read it.
# The index_col part is to take out the part that says how many lines the file has.

dfCJ = pd.DataFrame(csvCJ)
# Turns the data into something that can be read by Pandas.
# It gets the csv values and creates a table that it can use in the data analysis.
# It is needed because once it is in this format then it can get the column that holds the values we want to use.
# In this case the Relevance column.

relevanceCJ = dfCJ['Relevance'].tolist()
confidenceCJ = dfCJ['Confidence'].tolist()
# Since it is in the DataFrame format then we ca get the values that are held in the relevance column.
# The .tolist() creates a list from these values.
# For the Krippendorff to do the analyses the values need to be in a list.

print("The csv file.")
print(csvCJ)
print("The DataFrame.")
print(dfCJ)
print("The list of values in the relevance column.")
print(relevanceCJ)
print("The list of values in the confidence column.")
print(confidenceCJ)
# Prints each step that was done above.
# Then it is possible to know exactly the steps made by the computer.

csvIL = pd.read_csv('Coding of Articles-IL.csv', index_col=False)
dfIL = pd.DataFrame(csvIL)
relevanceIL = dfIL['Relevance'].tolist()
confidenceIL = dfIL['Confidence'].tolist()

print("The csv file.")
print(csvIL)
print("The DataFrame.")
print(dfIL)
print("The list of values in the relevance column.")
print(relevanceIL)
print("The list of values in the confidence column.")
print(confidenceIL)
# Exactly the same thing that was done above but for the second coder

relevanceData = relevanceCJ, relevanceIL
print('relevance', relevanceData)
# After collecting the lists that will be compared then another list needs to be created
# that will be inputed in the Krippendorff's alpha.
# The library of the coefficient needs to have both list of values of both coders in the same list.
# Above separate lists were created because otherwise it would not be possible to distinguish which 
# coder the data refered to.

confidenceData = confidenceCJ, confidenceIL
print('confidence', confidenceData)

print("Krippendorff's alpha for nominal metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='nominal'))
print("Krippendorff's alpha for interval metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='interval'))
print("Krippendorff's alpha for ordinal metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='ordinal'))
print("Krippendorff's alpha for ratio metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='ratio'))




#print("Krippendorff's alpha for ordinal metric: ", kp.alpha(reliability_data=confidenceData, level_of_measurement='ordinal'))
# This is the formula using the library that automatically calculates the Krippendorff's alpha.


