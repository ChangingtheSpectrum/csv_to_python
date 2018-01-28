import csv
import sys


class Portfolio(object):
	""" Class to represent each Portolio
	
	Attributes:
		portfolio_name (str): Portfolio's name
		portfolio_code (str): Portfolio's code
		portfolio_market_value (str): Portfolio's market value
		share_classes (List of PortfolioShareClasses): All share classes associated with the Portfolio
		
	Methods:
		assign_portfolio_share_classes: Automatically populates the share_classes attribute
		load_portfolios: Creates Portfolio objects with data from .CSV file
		count_portfolios: Counts number of existing Portfolios
		
	"""
	def __init__(self, portfolio_name, portfolio_code, portfolio_market_value):
		self.portfolio_name = portfolio_name
		self.portfolio_code = portfolio_code
		self.portfolio_market_value = portfolio_market_value
		self.share_classes = []

	def assign_portfolio_share_classes(self, share_classes):
		for share_class in share_classes:
			if share_class.portfolio_name == self.portfolio_name:
				self.share_classes.append(share_class)

	@staticmethod
	def load_portfolios(file):
			portfolios = []
			with open(file, 'r') as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					portfolios.append(Portfolio(row[0], row[1], row[2]))
			return portfolios

	def count_portfolios(sample_portfolios):
		return len([p for p in sample_portfolios])


class PortfolioShareClass(object):
	""" Class to represent each Portfolio Share Class
	
	Attributes:
		portfolio_name (str): Parent Portfolio's name
		portfolio_share_class_name (str): Share Class' name
		portfolio_share_class_code (str): Share Class' code
		portfolio_share_class_base_fee (str): Share Class' base fee
		portfolio (Portfolio): The Portfolio the Share Class is associated with
		
	Methods:
		assign_portfolio: Finds the associated Portfolio for each Share Class
		load_portfolio_classes: Creates PortfolioShareClass objects with data from .CSV file
		count_portfolios: Counts number of existing PortfolioShareClasses
		
	"""

	def __init__(self, portfolio_name, portfolio_share_class_name, portfolio_share_class_code,
				 portfolio_share_class_base_fee, portfolio = None):
		self.portfolio_name = portfolio_name
		self.portfolio_share_class_name = portfolio_share_class_name
		self.portfolio_share_class_code = portfolio_share_class_code
		self.portfolio_share_class_base_fee = portfolio_share_class_base_fee

	def assign_portfolio(self, portfolios):
		for portfolio in portfolios:
			if portfolio.portfolio_name == self.portfolio_name:
				self.portfolio = portfolio

	@staticmethod
	def load_portfolio_classes(file):
		portfolio_share_classes = []
		with open(file, 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				portfolio_share_classes.append(PortfolioShareClass(row[0], row[1], row[2], row[3]))
		return portfolio_share_classes

	def count_portfolio_classes(share_classes):
		return len([p for p in share_classes])

# Loads Portfolios and Share Classes from .CSV files
try:
	sample_portfolios = Portfolio.load_portfolios("Portfolio.CSV")
	sample_portfolio_share_classes = PortfolioShareClass.load_portfolio_classes("PortfolioShareClass.CSV")
except IOError as err:
	sys.exit("One or both files could not be loaded.")

# Assigns Portfolios and Share Classes
for portfolio in sample_portfolios:
	portfolio.assign_portfolio_share_classes(sample_portfolio_share_classes)
for share_class in sample_portfolio_share_classes:
	share_class.assign_portfolio(sample_portfolios)


# Prints amount of Portfolios and Share Classes currently loaded
def counts(portfolios, share_classes):
	print("{} Portfolios loaded.".format(Portfolio.count_portfolios(portfolios)))
	print("{} Portfolio Share Classes loaded.\n".format(PortfolioShareClass.count_portfolio_classes(share_classes)))


# Lists each Portfolio and the amount of Share Classes associated
def list_portfolios(portfolios):
	for portfolio in portfolios:
		print("{}, {} Share Classes\n".format(portfolio.portfolio_name, len(portfolio.share_classes)))


# Prompts user for a Portfolio code, then lists the attributes of each Share Class associated
def show_share_class(share_classes):
	share_class_code = input("Code?\n").upper()
	for share_class in share_classes:
		if share_class_code == share_class.portfolio.portfolio_code:
			for attr, value in share_class.__dict__.items():
				print("{}".format(value), end='\t')
			print()


# Menu for user interface
def menu():
	while True:
		method = input("\nHere's a couple commands you can run:\n"
						"COUNTS: Displays the total number of portfolios and portfolio share classes loaded\n"
						"LIST PORTFOLIOS: Displays a list of all portfolios loaded showing the portfolio name and number of share classes associated\n"
						"SHOW SHARE CLASS: Displays all share classes for the entered portfolio code (requires portfolio code)\n"
						"QUIT: Exits the application\n\n").upper()
		if method == 'COUNTS':
			counts(sample_portfolios, sample_portfolio_share_classes)
		elif method == 'LIST PORTFOLIOS':
			list_portfolios(sample_portfolios)
		elif method == 'SHOW SHARE CLASS':
			show_share_class(sample_portfolio_share_classes)
		elif method == 'QUIT':
			sys.exit()
		else:
			print("Input not recognized, try again.")
			menu()

menu()
