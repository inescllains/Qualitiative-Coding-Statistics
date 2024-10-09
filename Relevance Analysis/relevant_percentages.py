#If you need more specific instructions copy paste the entire code to ChatGPT and ask it to explain the code line by line
import pandas
import pandas as pd

#Import the different files in which the relevance is going to be calculated
#   -> To get the files copy the path and add it here
#   -> The print shows the top of the table
domingo = pd.read_excel("Domingo Cabo DelgadoIL.xlsx")
print("Domingo")
print(domingo.head())

#Make relevance and confidence integers and ignore the NaN values - this is needed so that there is no error
domingo["Relevance"] = domingo["Relevance"].fillna(99).astype(int)
domingo["Confidence"] = domingo["Confidence"].fillna(99).astype(int)

noticias_2017_2018 = pd.read_excel("Noticias 2017-2018 Cabo DelgadoIL.xlsx")
print("noticias_2017_2018")
print(noticias_2017_2018.head())
noticias_2017_2018["Relevance"] = noticias_2017_2018["Relevance"].fillna(99).astype(int)
noticias_2017_2018["Confidence"] = noticias_2017_2018["Confidence"].fillna(99).astype(int)

noticias_2019 = pd.read_excel("Noticias 2019 Cabo DelgadoIL.xlsx")
print("noticias_2019")
print(noticias_2019.head())
noticias_2019["Relevance"] = noticias_2019["Relevance"].fillna(99).astype(int)
noticias_2019["Confidence"] = noticias_2019["Confidence"].fillna(99).astype(int)

noticias_2020 = pd.read_excel("Noticias 2020 Cabo DelgadoIL.xlsx")
print("noticias_2020")
print(noticias_2020.head())
noticias_2020["Relevance"] = noticias_2020["Relevance"].fillna(99).astype(int)
noticias_2020["Confidence"] = noticias_2020["Confidence"].fillna(99).astype(int)

savana_2017 = pd.read_excel("Savana 2017 Cabo DelgadoIL.xlsx")
print("savana_2017")
print(savana_2017.head())
savana_2017["Relevance"] = savana_2017["Relevance"].fillna(99).astype(int)
savana_2017["Confidence"] = savana_2017["Confidence"].fillna(99).astype(int)

savana_2018 = pd.read_excel("Savana 2018 Cabo DelgadoIL.xlsx")
print("savana_2018")
print(savana_2018.head())
savana_2018["Relevance"] = savana_2018["Relevance"].fillna(99).astype(int)
savana_2018["Confidence"] = savana_2018["Confidence"].fillna(99).astype(int)

savana_2019 = pd.read_excel("Savana 2019 Cabo DelgadoIL.xlsx")
print("savana_2019")
print(savana_2019.head())
savana_2019["Relevance"] = savana_2019["Relevance"].fillna(99).astype(int)
savana_2019["Confidence"] = savana_2019["Confidence"].fillna(99).astype(int)

savana_2020 = pd.read_excel("Savana 2020 Cabo DelgadoIL.xlsx")
print("savana_2020")
print(savana_2020.head())
savana_2020["Relevance"] = savana_2020["Relevance"].fillna(99).astype(int)
savana_2020["Confidence"] = savana_2020["Confidence"].fillna(99).astype(int)

savana_2021 = pd.read_excel("Savana 2021 Cabo DelgadoIL.xlsx")
print("savana_2021")
print(savana_2021.head())
savana_2021["Relevance"] = savana_2021["Relevance"].fillna(99).astype(int)
savana_2021["Confidence"] = savana_2021["Confidence"].fillna(99).astype(int)

#Calculate the percentage of relevant entries in each file

#This function calculates the percentages, you then specify which dataset(i.e. newspaper) you want to calculate the percentage of relevant articles for
def calculate_relevance(dataframe):
    relevant_entries = ((dataframe["Relevance"] == 1) & (dataframe["Confidence"] >= 5)).sum()
    percentage = (relevant_entries / len(dataframe)) * 100
    return percentage

percentages_data = []

#Calculate the percentages for each newspaper and then add it to a new table with the name of the newspaper and their percentage
domingo_percentagens = calculate_relevance(domingo)
print(domingo_percentagens)
percentages_data.append({"File": "Domingo", "Relevance Percentage": domingo_percentagens})

noticias_2017_2018_percentagens = calculate_relevance(noticias_2017_2018)
print(noticias_2017_2018_percentagens)
percentages_data.append({"File": "Noticias 2017-2018", "Relevance Percentage": noticias_2017_2018_percentagens})

noticias_2019_percentagens = calculate_relevance(noticias_2019)
print(noticias_2019_percentagens)
percentages_data.append({"File": "Noticias 2019", "Relevance Percentage": noticias_2019_percentagens})

noticias_2020_percentagens = calculate_relevance(noticias_2020)
print(noticias_2020_percentagens)
percentages_data.append({"File": "Noticias 2020", "Relevance Percentage": noticias_2020_percentagens})

savana_2017_percentagens = calculate_relevance(savana_2017)
print(savana_2017_percentagens)
percentages_data.append({"File": "Savana 2017", "Relevance Percentage": savana_2017_percentagens})

savana_2018_percentagens = calculate_relevance(savana_2018)
print(savana_2018_percentagens)
percentages_data.append({"File": "Savana 2018", "Relevance Percentage": savana_2018_percentagens})

savana_2019_percentagens = calculate_relevance(savana_2019)
print(savana_2019_percentagens)
percentages_data.append({"File": "Savana 2019", "Relevance Percentage": savana_2019_percentagens})

savana_2020_percentagens = calculate_relevance(savana_2020)
print(savana_2020_percentagens)
percentages_data.append({"File": "Savana 2020", "Relevance Percentage": savana_2020_percentagens})

savana_2021_percentagens = calculate_relevance(savana_2021)
print(savana_2021_percentagens)
percentages_data.append({"File": "Savana 2021", "Relevance Percentage": savana_2021_percentagens})

#Calculate the overall percentage for noticias and savana 
noticias = pd.concat([noticias_2017_2018, noticias_2019, noticias_2020])
noticias_relevance = calculate_relevance(noticias)
print(noticias_relevance)
percentages_data.append({"File": "Noticias Total", "Relevance Percentage": noticias_relevance})

savana = pd.concat([savana_2017, savana_2018, savana_2019, savana_2020, savana_2021])
savana_relevance = calculate_relevance(savana)
print(savana_relevance)
percentages_data.append({"File": "Savana Total", "Relevance Percentage": savana_relevance})

#Merge all the relevant percentages into one file
final_df = pd.concat([domingo, noticias_2017_2018, noticias_2019, noticias_2020, savana_2017, savana_2018, savana_2019, savana_2020, savana_2021])
#calculate overall relevance percentage
final_relevance = calculate_relevance(final_df)
percentages_data.append({"File": "Total Relevance", "Relevance Percentage": final_relevance})

#Keep only the entries (i.e. rows) that are relevant and have a confidence of 5 or more
final_df = final_df[final_df["Relevance"] ==1]
final_df = final_df[final_df["Confidence"] >= 5]

#Store the table of percentages in a dataset
percentages = pd.DataFrame(percentages_data)
print(percentages)

#Save the datasets that have been created to their own excel files
percentages.to_excel("Percentages of Relevant Entries.xlsx", index=False)
final_df.to_excel("Relevant Entries All Newspapers.xlsx", index=False)



