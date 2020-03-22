import sys
import pandas

class	SpatioTemporalData:

	def	__init__(self, df):
		self.df = df

	def	where(self, year):
		return list(self.df.loc[self.df['Year'] == year]['City'].unique())

	def	when(self, location):
		return list(self.df.loc[self.df['City'] == location]['Year'].unique())
