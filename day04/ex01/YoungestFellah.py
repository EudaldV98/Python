import pandas
from FileLoader import FileLoader as loader

def	youngestFellah(df, year):
	female = df[(df['Year'] == year) & (df['Sex'] == "F")].min()
	male = df[(df['Year'] == year) & (df['Sex'] == "M")].min()
	data = {'F': female['Age'], 'M': male['Age']}
	return data
