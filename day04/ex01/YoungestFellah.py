import pandas
from FileLoader import FileLoader as loader

def	youngestFellah(df, year):
	data = df.loc[lambda data: data["Year"] == int(year)]
	male = data.loc[lambda data: data["Sex"] == "M"]
	female = data.loc[lambda data: data["Sex"] == "F"]
	result = {"m" : male.min()["Age"], "f": female.min()["Age"]}
	return result
