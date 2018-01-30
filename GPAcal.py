import csv
with open("GPAcal.csv")as csvfile:
	spamreader = csv.reader(csvfile)
	row_list = []
	i = 0  
	for row in spamreader:
		i +=1
		row_list.append(row)

sumGPA = 0
sumGPAterm = 0
sumCredits = 0
sumCreditsterm = 0
arr_gpa = []
arr_gpaterm =[]
for i in range(len(row_list)):
	if (i < 7):
		sumGPA = sumGPA+(float(row_list[i][4]))*(float(row_list[i][6])) 	
		sumCredits = sumCredits+(float(row_list[i][4]))
		sumGPAterm = sumGPAterm+(float(row_list[i][4]))*(float(row_list[i][6]))	
		sumCreditsterm = sumCreditsterm+(float(row_list[i][4]))

		if(i  == 6):
			arr_gpaterm.append(sumGPAterm/sumCreditsterm)
			arr_gpa.append(sumGPA/sumCredits)
			sumGPAterm = 0
			sumCreditsterm = 0

	elif (i >= 7 and i < 14):
		sumGPA = sumGPA+(float(row_list[i][4]))*(float(row_list[i][6])) 	
		sumCredits = sumCredits+(float(row_list[i][4]))
		sumGPAterm = sumGPAterm+(float(row_list[i][4]))*(float(row_list[i][6]))	
		sumCreditsterm = sumCreditsterm+(float(row_list[i][4]))

		if(i  == 13):
			arr_gpaterm.append(sumGPAterm/sumCreditsterm)
			arr_gpa.append(sumGPA/sumCredits)
			sumGPAterm = 0
			sumCreditsterm = 0

	elif (i >= 14 and i < 19):
		sumGPA = sumGPA+(float(row_list[i][4]))*(float(row_list[i][6])) 	
		sumCredits = sumCredits+(float(row_list[i][4]))
		sumGPAterm = sumGPAterm+(float(row_list[i][4]))*(float(row_list[i][6]))	
		sumCreditsterm = sumCreditsterm+(float(row_list[i][4]))
		
		if(i  == 18):
			arr_gpaterm.append(sumGPAterm/sumCreditsterm)
			arr_gpa.append(sumGPA/sumCredits)
			sumGPAterm = 0
			sumCreditsterm = 0
	elif (i >= 19):
		sumGPA = sumGPA+(float(row_list[i][4]))*(float(row_list[i][6])) 	
		sumCredits = sumCredits+(float(row_list[i][4]))
		sumGPAterm = sumGPAterm+(float(row_list[i][4]))*(float(row_list[i][6]))	
		sumCreditsterm = sumCreditsterm+(float(row_list[i][4]))
		
		if(i  == 21):
			arr_gpaterm.append(sumGPAterm/sumCreditsterm)
			arr_gpa.append(sumGPA/sumCredits)
			sumGPAterm = 0
			sumCreditsterm = 0
	
i = 0
while(i < len(arr_gpa)) :
	print('GPA semester ',i+1 ,' : ',arr_gpaterm[i])
	print('GPA ',i+1,' : ',arr_gpa[i])
	i += 1




