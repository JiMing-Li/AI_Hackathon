#declare variables 
bool takeBreak 
bool moreThanOne
bool ThuOrFri
int probTakeBreak = 0.75
int probNoTake = 0.25
int probHourBreak = (2/3)
int probNoBreakHour = (1/3) 
int probNoHourBreak = 1
int probNoBreakNoHour = 0
int probTFBreak = 0.5
int probTFNoBreak = 0.5
int probNoTFBreak = 0.5
int probNoTFNoBreak = 0.5
int probBreak
int probNoBreak
str outcome 
 
#calculate prediction 
if moreThanOne = True 
	if ThuOrFri = True 
		probBreak = probHourBreak * probThuOrFri * probTakeBreak
		probNoBreak = probNoBreakHour * probTFNoBreak * probNoBreak 
		if (probBreak > probNoBreak)
			outcome = "break"
		else 
			outcome = "don't take a break"
		
	else 
		probBreak = probHourBreak * probNoTFBreak * probTakeBreak
		probNoBreak = probNoBreakHour * probNoTFNoBreak * probNoTake
		if (probBreak > probNoBreak)
			outcome = "break"
		else 
			outcome = "don't take a break"
else 
	if ThuOrFri = True 
		probBreak = probNoHourBreak* probThuOrFri * probTakeBreak
		probNoBreak = probNoBreakNoHour * probTFNoBreak * probNoTake 
		if (probBreak > probNoBreak)
			outcome = "break"
		else 
			outcome = "don't take a break"
	else 
		probBreak = probNoHourBreak * probNoTFNoBreak * probTakeBreak
		probNoBreak = probNoBreakHour * probNoTFNoBreak * probNoTake
		if (probBreak > probNoBreak)
			outcome = "break"
		else 
			outcome = "don't take a break"



