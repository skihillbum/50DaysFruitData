"""
Program: Dustin_Smith_MyProgram.py
Author: Dustin Smith
Date: February 25, 2023

This programs calls the input file 50DayFruitData.txt then imports the Mean Median, and Mode functions from Dustin_Smith_Stats_Lab7.py file.
The program writes all of the output data in the text file Dustin_Smith_Output_Lab7.txt.
This program should be in the same directory as (Dustin_Smith_Stats_Lab7.py) (Dustin_Smith_Output_Lab7.txt) and (50DayFruitData.txt).
"""

#Assigns fruit_data_file to the text file containing the fruit data.
fruit_data_file = ("50DayFruitData.txt")

#Imports the Mean and Median functions from the Dustin_Smith_Stats.py module.	
from Dustin_Smith_Stats_Lab7 import Mean,Median,Mode

#The called functions are used to calculate the mean, medians, and modes of apples, bananas, strawberries, and all fruit eaten.
mean_apples, mean_bananas, mean_strawberrys, mean_fruits = Mean(fruit_data_file)

median_apples, median_bananas, median_strawberrys, median_fruits = Median(fruit_data_file)

mode_apples, mode_bananas, mode_strawberrys, mode_fruit = Mode(fruit_data_file)

#Defines and opens the Dustin_Smith_Output text file in write mode to accept the output data.
output_file= open("Dustin_Smith_Output_Lab7.txt", "w")

#Writes mean, median, and mode values of fruits eaten to the Dustin_Smith_Output_Lab7.txt file.
#The mean and median values are formatted to the second decimal place.
#The join method is used to construct the mode variable strings. If there is more than one mode value, the printed numbers are seperated by a space.

output_file.write("The mean number of apples eaten is {:.2f}\n".format(mean_apples))	
output_file.write("The median number of apples eaten is {:.2f}\n".format(median_apples))
output_file.write("The mode number of apples eaten is (are) " + " ".join(str(apple) for apple in mode_apples) + "\n\n")

output_file.write("The mean number of bananas eaten is {:.2f}\n".format(mean_bananas))
output_file.write("The median number of bananas eaten is {:.2f}\n".format(median_bananas))
output_file.write("The mode number of bananas eaten is (are) " + " ".join(str(banana) for banana in mode_bananas) + "\n\n")

output_file.write("The mean number of strawberries eaten is {:.2f}\n".format(mean_strawberrys))
output_file.write("The median number of strawberries eaten is {:.2f}\n".format(median_strawberrys))
output_file.write("The mode number of strawberries eaten is (are) " + " ".join(str(strawberry) for strawberry in mode_strawberrys) + "\n\n")

output_file.write("The mean number of all fruit eaten is {:.2f}\n".format(mean_fruits))
output_file.write("The median number of all fruit eaten is {:.2f}\n".format(median_fruits))
output_file.write("The mode number of all fruit eaten is (are) " + " ".join(str(fruit) for fruit in mode_fruit))
