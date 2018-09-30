import random 
import datetime

testLessThanOne = 0
testMoreThanOne = 0
ThuOrFri = 0
moreThanOne = 0
testNoThuOrFri = 0 
testBreak = 0
testNoThuOrFri = 0 
testBreak = 0
testNoThuOrFri = 0
takeBreak = 0
testNoBreak = 0
testThuOrFri = 0
list_rand_hour = [1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]
list_rand_ampm = [1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0]
list_rand_break = [1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1]
#declare variables 
testTotal = 100000
testHourAndBreak = 0
testNoHourAndBreak = 0
testHourAndNoBreak = 0
testNoBreakAndNoHour = 0
testTFAndBreak = 0
testNoTFAndBreak = 0
testNoTFAndBreak = 0
testNoTFAndNoBreak = 0


#run test cases 
for i in range(len(list_rand_break)):
	if (list_rand_break[i] == 1):
		testBreak = testBreak + 1
	else:
		testNoBreak = testNoBreak + 1
for j in range(len(list_rand_hour)):
	if (list_rand_break[i] == 1):
		testMoreThanOne = testMoreThanOne + 1
	else:
		testLessThanOne = testLessThanOne + 1
for k in range(len(list_rand_ampm)):
	if (list_rand_ampm[k] == 1):
		testThuOrFri = testThuOrFri + 1
	else:
		testNoThuOrFri = testNoThuOrFri + 1
for m in range(len(list_rand_ampm)):
 	if (list_rand_break[m]==1 and list_rand_break[m]==1):
 		testHourAndBreak = testHourAndBreak+1
 	elif (list_rand_break[m]==0 and list_rand_break[m]==1):
 		testNoHourAndBreak = testNoHourAndBreak+1
 	elif (list_rand_break[m]==1 and list_rand_break[m]==0):
 		testHourAndNoBreak = testHourAndNoBreak+1
 	else:
 		testNoBreakAndNoHour = testNoBreakAndNoHour+1
for n in range(len(list_rand_ampm)):
	if (list_rand_ampm[n]==1 and list_rand_break[n]==1):
 		testTFAndBreak = testTFAndBreak+1
	elif (list_rand_ampm[n]==0 and list_rand_break[n]==1):
 		testNoTFAndBreak = testNoTFAndBreak+1
	elif (list_rand_ampm[n]==1 and list_rand_break[n]==0):
 		testNoTFAndBreak = testNoTFAndBreak+1
	else:
 		testNoTFAndNoBreak = testNoTFAndNoBreak+1 

#declare more 
probTakeBreak = testBreak/testTotal 
probNoTake = testNoBreak/testTotal
probHourBreak = testHourAndBreak/testBreak 
probNoBreakHour = testHourAndNoBreak/testBreak
probNoHourBreak = testNoHourAndBreak/testBreak
probNoBreakNoHour = testNoBreakAndNoHour/testNoBreak
probTFBreak = testTFAndBreak/testBreak
probTFNoBreak = testNoTFAndNoBreak/testNoBreak
probNoTFBreak = testNoTFAndBreak/testBreak
probNoTFNoBreak = testNoTFAndNoBreak/testBreak

#calculate prediction 
if moreThanOne == 1: 
	if ThuOrFri == 1: 
		probBreak = probHourBreak * probThuOrFri * probTakeBreak
		probNoBreak = probNoBreakHour * probTFNoBreak * probNoBreak 
		if probBreak > probNoBreak:
			outcome = "1"
		else: 
			outcome = "0"
		
	else :
		probBreak = probHourBreak * probNoTFBreak * probTakeBreak
		probNoBreak = probNoBreakHour * probNoTFNoBreak * probNoTake
		if probBreak > probNoBreak:
			outcome = "1"
		else:
			outcome = "0"
else:
	if ThuOrFri == 1: 
		probBreak = probNoHourBreak* probThuOrFri * probTakeBreak
		probNoBreak = probNoBreakNoHour * probTFNoBreak * probNoTake 
		if probBreak > probNoBreak:
			outcome = "1"
		else :
			outcome = "0"
	else :
		probBreak = probNoHourBreak * probNoTFNoBreak * probTakeBreak
		probNoBreak = probNoBreakHour * probNoTFNoBreak * probNoTake
		if probBreak > probNoBreak:
			outcome = "1"
		else:
			outcome = "0"

 print(outcome, datetime.datetime.now())

