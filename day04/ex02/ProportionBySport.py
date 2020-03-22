import pandas
from FileLoader import FileLoader as loader

def	proportionBySport(df, year, sport, gender):
	total = df[(df['Year'] == year) & (df['Sex'] == gender)].drop_duplicates('Name').count()['Sex']
	num = df[(df['Year'] == year) & (df['Sport'] == sport) & (df['Sex'] == gender)].drop_duplicates('Name').count()['Sex']
	return num / total
