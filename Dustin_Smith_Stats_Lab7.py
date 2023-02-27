"""
Program: Dustin_Smith_Stats.py
Author: Dustin Smith
Date: February 24, 2023

This program creates three functions to calculate the mean, median and mode of fruit data from the fruit data file (50DayFruitData.txt).
The text file should contain three columns: days, fruit, and number of fruits eaten.
This program should be in the same directory as (Dustin_Smith_MyProgram_Lab7.py) (Dustin_Smith_Output_Lab7.txt) and (50DayFruitData.txt).
"""

def Mean (fruit_data_file):
	
	#Opens the file path to the fruit_data_file.
	fruit_txt= open(fruit_data_file, "r")
		
	#Reads the lines of fruit data.
	fruit_data = fruit_txt.readlines()
	
	#Initializes variables for apples,bananas, and strawberries.	
	apple_days = 0
	apples_eaten = 0
	apples_eaten_list = []
	
	banana_days = 0
	bananas_eaten = 0
	bananas_eaten_list = []
	
	strawberry_days = 0
	strawberrys_eaten = 0
	strawberrys_eaten_list = []
	
	fruit_days = 0
	fruits_eaten = 0
	fruits_eaten_list = []
	
	#For loop iterates over the fruit data list.
	for i in fruit_data:
		
		#Splits the lines into a list strings.
	    line = i.split()
	    fruit_name = line[1]
	    
	    #Extracts the different fruit names from element two and the integer values from element three.
	    if line[1] == "apple":
			
	        apple_days += 1
	        
	        apples_eaten += int(line[2])
	        apples_eaten_list += [int(line[2])]
	        
	    elif line[1] == "banana":
			
	        banana_days += 1
	        
	        bananas_eaten += int(line[2])
	        bananas_eaten_list += [int(line[2])]
	        
	    elif line[1] == "strawberry":
			
	        strawberry_days += 1
	        
	        strawberrys_eaten += int(line[2])
	        strawberrys_eaten_list += [int(line[2])]
	
	#Creates a list of all fruit names.
	all_fruit_names = ["apple","banana","strawberry"]
	
	#Loops through the fruit data to calculate the mean of all fruits eaten.
	for i in fruit_data:
		
	    line = i.split()
	    
	    fruit_name = line[1]
	    
	    if fruit_name in all_fruit_names:
			
	        fruit_days += 1
	        fruits_eaten += int(line[2])
	        fruits_eaten_list += [int(line[2])]
	          
	#Calculates and defines the mean of apples, bananas, strawberries, and all fruits eaten.              
	mean_apples = apples_eaten / apple_days
	mean_bananas = bananas_eaten / banana_days
	mean_strawberrys = strawberrys_eaten / strawberry_days
	mean_fruits = fruits_eaten / fruit_days
	
	#Returns the mean for each fruit type and all fruits eaten as float point numbers.	
	return  float(mean_apples), float(mean_bananas), float(mean_strawberrys), float(mean_fruits)

def Median (fruit_data_file):
	
	#Opens the fruit_data_file for reading.
	fruit_txt= open(fruit_data_file, "r")
	
	#Reads the lines of fruit data.
	fruit_data = fruit_txt.readlines()
	
	#Intializes a lists for appples, bananas, strawberries.	
	apples_eaten_list = []
	bananas_eaten_list = []
	strawberrys_eaten_list = []
	
	for i in fruit_data:
		
		#Splits the lines into a list of strings.
		line = i.split()
		
		fruit_name = line[1]
		
		#Extracts the fruit name from element two and the amount of fruit eaten from element three.
		if fruit_name == "apple":
	
			apples_eaten_list += [int(line[2])]
			
		elif fruit_name == "banana":
			
			bananas_eaten_list += [int(line[2])]
			
		elif fruit_name == "strawberry":
			strawberrys_eaten_list += [int(line[2])]
	
	#Sort the lists in ascending order.		
	apples_eaten_list.sort()
	bananas_eaten_list.sort()
	strawberrys_eaten_list.sort()
	
	#Initializes different n variables to calculate length of the apple, banana, and strawberry lists (even or odd).
	apple_n = len(apples_eaten_list)
	banana_n = len(bananas_eaten_list)
	strawberry_n= len(strawberrys_eaten_list)
	
	#If statments are executed if the length of the specified list is odd. The median is then set to the respective middle value. 
	#Else statements are executed if the length of the specified list is even. Then the median is set to the average of the respective middle values.
	if apple_n % 2 != 0:
		
	    median_apples = apples_eaten_list[apple_n // 2]
	   
	else:
		
	    median_apples_1 = apples_eaten_list[apple_n // 2 - 1]
	    median_apples_2 = apples_eaten_list[apple_n // 2]
	    median_apples = (median_apples_1 + median_apples_2) / 2
	    
	if banana_n % 2 != 0:
		
	    median_bananas = bananas_eaten_list[banana_n // 2]
	    
	else:
		
	    median_bananas_1 = bananas_eaten_list[banana_n // 2 - 1]
	    median_bananas_2 = bananas_eaten_list[banana_n // 2]
	    median_bananas = (median_bananas_1 + median_bananas_2) / 2
	
	if strawberry_n % 2 != 0:
		
	    median_strawberrys = strawberrys_eaten_list[strawberry_n // 2]
	    
	else:
		
	    median_strawberrys_1 = strawberrys_eaten_list[strawberry_n // 2 - 1]
	    median_strawberrys_2 = strawberrys_eaten_list[strawberry_n // 2]
	    median_strawberrys = (median_strawberrys_1 + median_strawberrys_2) / 2
	    
	#Creates a list of all fruit names.
	all_fruit_names = ["apple","banana","strawberry"]
	
	#Intializes a list for all fruit eaten.
	fruits_eaten_list =[]
	
	#Loops through the fruit data to fill the list of all fruits eaten.
	for i in fruit_data:
		 
		line = i.split()
		
		fruit_name = line[1]
		
		#Checks if the fruit name is in the list of all_fruit_names
		if fruit_name in all_fruit_names:
			
			fruits_eaten_list += [int(line[2])]
	
	#Sort the fruit list in ascending order.		
	fruits_eaten_list.sort()
	
	#The n variable is intialized to check if the length of the fruits eaten list is even or odd.
	n = len(fruits_eaten_list)
	
	if n % 2 != 0:
		
	    median_fruits = fruits_eaten_list[n // 2]
	 
	else:
		
	    median_fruits_1 = fruits_eaten_list[n // 2 - 1]
	    median_fruits_2 = fruits_eaten_list[n // 2]
	    median_fruits = (median_fruits_1 + median_fruits_2) / 2
	
	#Returns the median values as float point numbers.
	return  float(median_apples), float(median_bananas), float(median_strawberrys), float(median_fruits)
	
def Mode (fruit_data_file):
	
	#Opens the file path to the fruit_data_file.
	fruit_txt = open(fruit_data_file, "r")
	
	#Reads the lines of fruit data.
	fruit_data = fruit_txt.readlines()
	
	#Initialize fruit dictionaries.
	apple_count = {}
	banana_count = {}
	strawberry_count = {}
	fruit_count= {}
	
	for i in fruit_data:
		
		#Splits the lines into a list of strings.
		line = i.split()
		
		# Extracts the different fruit names from the third element.
		if line[1] == "apple":
			apple_num = int(line[2])
		    
		    #Stores the frequency of each apple number. Incrimenting the count by one.
			if apple_num in apple_count:
				apple_count[apple_num] += 1
			
			#Adds the integer value to the dictionary with an intial count of one instance.
			else:
				apple_count[apple_num] = 1
	
			apple_max_frequency = 0
			mode_apples = []
			
			#For loop iterates through the items in the apple count dictionary.
			for apple_num, apple_num_frequency in apple_count.items():
				
				#If the frequency of the interation is greater that the max, the max is updated.
				if apple_num_frequency > apple_max_frequency:
					apple_max_frequency = apple_num_frequency
					mode_apples = [apple_num]
				
				#If the frequency of the iteration is equal to the max the list is appended.
				elif apple_num_frequency == apple_max_frequency:
					mode_apples.append(apple_num)
		    
		elif line[1] == "banana":
			banana_num = int(line[2])
		    
			if banana_num in banana_count:
				banana_count[banana_num] += 1
			else:
				banana_count[banana_num] = 1
	
			banana_max_frequency = 0
			mode_bananas = []
	
			for banana_num, banana_num_frequency in banana_count.items():
				if banana_num_frequency > banana_max_frequency:
					banana_max_frequency = banana_num_frequency
					mode_bananas = [banana_num]
				
				elif banana_num_frequency == banana_max_frequency:
					mode_bananas.append(banana_num)
		
		elif line[1] == "strawberry":
			strawberry_num = int(line[2])
		    
			if strawberry_num in strawberry_count:
				strawberry_count[strawberry_num] += 1
			
			else:
				strawberry_count[strawberry_num] = 1
	
			strawberry_max_frequency = 0
			mode_strawberrys = []
	
			for strawberry_num, strawberry_num_frequency in strawberry_count.items():
				
				if strawberry_num_frequency > strawberry_max_frequency:
					strawberry_max_frequency = strawberry_num_frequency
					mode_strawberrys = [strawberry_num]
				
				elif strawberry_num_frequency == strawberry_max_frequency:
					mode_strawberrys.append(strawberry_num)
		
		#Identifies a the list of fruit names.			
		all_fruit_names = ["apple","banana","strawberry"]
		
		fruit_name = line[1]
		
		#If statemnet checks if the fruit name is in the all fruit name list then executes the statment.
		if fruit_name in all_fruit_names:
			
			#Extracts the third element from the line and converts it  an integer		
			fruit_num = int(line[2])
		
			#Stores the frequency of each fruit number. Incrimenting the count by one.
			if fruit_num in fruit_count:
			    fruit_count[fruit_num] += 1
			
			#Adds the integer value to the dictionary with an intial count of one instance.
			else:
			    fruit_count[fruit_num] = 1
			
			fruit_max_frequency = 0
			mode_fruit = []
			
			#For loop iterates through the items in the fruit_count dictionary.
			for fruit_num, fruit_num_frequency in fruit_count.items():
				
				#If the frequency of the interation is greater that the max, the max is updated.
			    if fruit_num_frequency > fruit_max_frequency:
			        
			        fruit_max_frequency = fruit_num_frequency
			        mode_fruit = [fruit_num]
				
				#If the frequency of the iteration is equal to the max appended to the list.
			    elif fruit_num_frequency == fruit_max_frequency:
			        
			        mode_fruit.append(fruit_num)
	        
	#Returns the mode for each fruit type and all fruits eaten.	
	return mode_apples, mode_bananas, mode_strawberrys, mode_fruit,

