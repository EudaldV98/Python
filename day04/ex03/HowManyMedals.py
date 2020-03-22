import pandas
from FileLoader import FileLoader as loader

def	howManyMedals(df, name):
	data = df.loc[lambda data: data['Name'] == name]
	result = {}
	for year in data['Year']:
		yearResult = {}
		yearResult['G'] = data.loc[(data['Medal'] == 'Gold') & (data['Year'] == year)].shape[0]
		yearResult['S'] = data.loc[(data['Medal'] == 'Silver') & (data['Year'] == year)].shape[0]
		yearResult['B'] = data.loc[(data['Medal'] == 'Bronze') & (data['Year'] == year)].shape[0]
		result[year] = yearResult
		del yearResult
	return result
