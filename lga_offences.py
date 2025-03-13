import data
import pandas as pd

offencesByLGA2016 = pd.DataFrame(columns=["LGA","2016 Type A Percentage", "2016 Type B Percentage", "2016 Type C Percentage", "2016 Type D Percentage", "2016 Type E Percentage", "2016 Offence Rate"])

#Filtering only the 2016 data and the relevant data columns
filteredOffencesData = data.lga_offences.loc[data.lga_offences['Year'] == 2016, ['Year', 'Local Government Area', 'Offence Subdivision', 'LGA Rate per 100,000 population', 'Offence Count']]
filteredOffencesData['Code'] = filteredOffencesData['Offence Subdivision'].str[:1]

#Dictionary for each offence division
codeType = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
results = []

#Calculating rate of offences and their type categorical distribution for each LGA
for lga in filteredOffencesData['Local Government Area'].unique():
    totalOffenceCount = filteredOffencesData[filteredOffencesData["Local Government Area"] == lga]["Offence Count"].sum()
    lgaRateOffences = filteredOffencesData[filteredOffencesData['Local Government Area'] == lga]['LGA Rate per 100,000 population'].sum()

    #Distribution for each type of offence
    for code in codeType:
        codeType[code] =  round(((filteredOffencesData[(filteredOffencesData["Local Government Area"] == lga) & (filteredOffencesData["Code"] == code)]["Offence Count"].sum())/totalOffenceCount)*100,2)

    results.append({'LGA': lga,'2016 Type A Percentage': codeType['A'],'2016 Type B Percentage': codeType['B'],'2016 Type C Percentage': codeType['C'], '2016 Type D Percentage': codeType['D'],'2016 Type E Percentage': codeType['E'],'2016 Offence Rate': round(lgaRateOffences,2)})

offencesByLGA2016 = pd.DataFrame(results)

# Set index to LGA
offencesByLGA2016.set_index("LGA", inplace=True)


#Extending to other years outside of 2019, eg. 2016, 2017, 2018



#2017:
offencesByLGA2017= pd.DataFrame(columns=["LGA","2017 Type A Percentage", "2017 Type B Percentage", "2017 Type C Percentage", "2017 Type D Percentage", "2017 Type E Percentage", "2017 Offence Rate"])
filteredOffencesData = data.lga_offences.loc[data.lga_offences['Year'] == 2017, ['Year', 'Local Government Area', 'Offence Subdivision', 'LGA Rate per 100,000 population', 'Offence Count']]
filteredOffencesData['Code'] = filteredOffencesData['Offence Subdivision'].str[:1]

codeType = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
results = []

for lga in filteredOffencesData['Local Government Area'].unique():
    totalOffenceCount = filteredOffencesData[filteredOffencesData["Local Government Area"] == lga]["Offence Count"].sum()
    lgaRateOffences = filteredOffencesData[filteredOffencesData['Local Government Area'] == lga]['LGA Rate per 100,000 population'].sum()

    for code in codeType:
        codeType[code] =  round(((filteredOffencesData[(filteredOffencesData["Local Government Area"] == lga) & (filteredOffencesData["Code"] == code)]["Offence Count"].sum())/totalOffenceCount)*100,2)

    results.append({'LGA': lga,'2017 Type A Percentage': codeType['A'],'2017 Type B Percentage': codeType['B'],'2017 Type C Percentage': codeType['C'], '2017 Type D Percentage': codeType['D'],'2017 Type E Percentage': codeType['E'],'2017 Offence Rate': round(lgaRateOffences,2)})

offencesByLGA2017 = pd.DataFrame(results)
offencesByLGA2017.set_index("LGA", inplace=True)



#2018:
offencesByLGA2018= pd.DataFrame(columns=["LGA","2018 Type A Percentage", "2018 Type B Percentage", "2018 Type C Percentage", "2018 Type D Percentage", "2018 Type E Percentage", "2018 Offence Rate"])

filteredOffencesData = data.lga_offences.loc[data.lga_offences['Year'] == 2018, ['Year', 'Local Government Area', 'Offence Subdivision', 'LGA Rate per 100,000 population', 'Offence Count']]
filteredOffencesData['Code'] = filteredOffencesData['Offence Subdivision'].str[:1]

codeType = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
results = []

for lga in filteredOffencesData['Local Government Area'].unique():
    totalOffenceCount = filteredOffencesData[filteredOffencesData["Local Government Area"] == lga]["Offence Count"].sum()
    lgaRateOffences = filteredOffencesData[filteredOffencesData['Local Government Area'] == lga]['LGA Rate per 100,000 population'].sum()

    for code in codeType:
        codeType[code] =  round(((filteredOffencesData[(filteredOffencesData["Local Government Area"] == lga) & (filteredOffencesData["Code"] == code)]["Offence Count"].sum())/totalOffenceCount)*100,2)

    results.append({'LGA': lga,'2018 Type A Percentage': codeType['A'],'2018 Type B Percentage': codeType['B'],'2018 Type C Percentage': codeType['C'], '2018 Type D Percentage': codeType['D'],'2018 Type E Percentage': codeType['E'],'2018 Offence Rate': round(lgaRateOffences,2)})

offencesByLGA2018 = pd.DataFrame(results)

offencesByLGA2018.set_index("LGA", inplace=True)



#2019:
offencesByLGA2019= pd.DataFrame(columns=["LGA","2019 Type A Percentage", "2019 Type B Percentage", "2019 Type C Percentage", "2019 Type D Percentage", "2019 Type E Percentage", "2019 Offence Rate"])

filteredOffencesData = data.lga_offences.loc[data.lga_offences['Year'] == 2019, ['Year', 'Local Government Area', 'Offence Subdivision', 'LGA Rate per 100,000 population', 'Offence Count']]
filteredOffencesData['Code'] = filteredOffencesData['Offence Subdivision'].str[:1]

codeType = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
results = []

for lga in filteredOffencesData['Local Government Area'].unique():
    totalOffenceCount = filteredOffencesData[filteredOffencesData["Local Government Area"] == lga]["Offence Count"].sum()
    lgaRateOffences = filteredOffencesData[filteredOffencesData['Local Government Area'] == lga]['LGA Rate per 100,000 population'].sum()

    for code in codeType:
        codeType[code] =  round(((filteredOffencesData[(filteredOffencesData["Local Government Area"] == lga) & (filteredOffencesData["Code"] == code)]["Offence Count"].sum())/totalOffenceCount)*100,2)

    results.append({'LGA': lga,'2019 Type A Percentage': codeType['A'],'2019 Type B Percentage': codeType['B'],'2019 Type C Percentage': codeType['C'], '2019 Type D Percentage': codeType['D'],'2019 Type E Percentage': codeType['E'],'2019 Offence Rate': round(lgaRateOffences,2)})

offencesByLGA2019 = pd.DataFrame(results)

offencesByLGA2019.set_index("LGA", inplace=True)



#2020:
offencesByLGA2020= pd.DataFrame(columns=["LGA","2020 Type A Percentage", "2020 Type B Percentage", "2020 Type C Percentage", "2020 Type D Percentage", "2020 Type E Percentage", "2020 Offence Rate"])

filteredOffencesData = data.lga_offences.loc[data.lga_offences['Year'] == 2020, ['Year', 'Local Government Area', 'Offence Subdivision', 'LGA Rate per 100,000 population', 'Offence Count']]
filteredOffencesData['Code'] = filteredOffencesData['Offence Subdivision'].str[:1]

codeType = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
results = []

for lga in filteredOffencesData['Local Government Area'].unique():
    totalOffenceCount = filteredOffencesData[filteredOffencesData["Local Government Area"] == lga]["Offence Count"].sum()
    lgaRateOffences = filteredOffencesData[filteredOffencesData['Local Government Area'] == lga]['LGA Rate per 100,000 population'].sum()

    for code in codeType:
        codeType[code] =  round(((filteredOffencesData[(filteredOffencesData["Local Government Area"] == lga) & (filteredOffencesData["Code"] == code)]["Offence Count"].sum())/totalOffenceCount)*100,2)

    results.append({'LGA': lga,'2020 Type A Percentage': codeType['A'],'2020 Type B Percentage': codeType['B'],'2020 Type C Percentage': codeType['C'], '2020 Type D Percentage': codeType['D'],'2020 Type E Percentage': codeType['E'],'2020 Offence Rate': round(lgaRateOffences,2)})

offencesByLGA2020 = pd.DataFrame(results)

offencesByLGA2020.set_index("LGA", inplace=True)


#Merging all the sets together
OffencesMerged1 = pd.merge(offencesByLGA2016, offencesByLGA2017, on= 'LGA')
OffencesMerged2 = pd.merge(offencesByLGA2018, offencesByLGA2019, on = 'LGA')
OffencesMerged3 = pd.merge(OffencesMerged1, OffencesMerged2, on = 'LGA')
totalOffencedMerged = pd.merge(OffencesMerged3, offencesByLGA2020, on = 'LGA')

#Output
totalOffencedMerged.to_csv("Offences By LGA.csv")