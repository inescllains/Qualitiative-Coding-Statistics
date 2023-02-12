import pandas as pd 
import krippendorff as kp

csvCJ = pd.read_csv('NameOfcsvFile1.csv', index_col=False)
dfCJ = pd.DataFrame(csvCJ)
relevanceCJ = dfCJ['Relevance'].tolist()

csvIL = pd.read_csv('NameOfcsvFile2.csv', index_col=False)
dfIL = pd.DataFrame(csvIL)
relevanceIL = dfIL['Relevance'].tolist()
confidenceIL = dfIL['Confidence'].tolist()

relevanceData = relevanceCJ, relevanceIL

confidenceData = confidenceCJ, confidenceIL

print("Krippendorff's alpha for nominal metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='nominal'))
print("Krippendorff's alpha for interval metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='interval'))
print("Krippendorff's alpha for ordinal metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='ordinal'))
print("Krippendorff's alpha for ratio metric: ", kp.alpha(reliability_data=relevanceData, level_of_measurement='ratio'))
