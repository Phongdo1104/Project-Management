import csv
from CustomWidgets import *

# Function Algorithm
####### Merge Sort Algorithm ########
def MergeSort(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort(left_side)
		MergeSort(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i]) < int(right_side[j]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

def MergeSort_desc(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc(left_side)
		MergeSort_desc(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i]) > int(right_side[j]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

### Ascending ###
def MergeSort_projectName(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_projectName(left_side)
		MergeSort_projectName(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if str(left_side[i].Project_name.lower()) < str(right_side[j].Project_name.lower()):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort username
def MergeSort_Username(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_Username(left_side)
		MergeSort_Username(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if str(left_side[i].username.lower()) < str(right_side[j].username.lower()):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort password
def MergeSort_Password(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_Password(left_side)
		MergeSort_Password(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if str(left_side[i].password.lower()) < str(right_side[j].password.lower()):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Login State
def MergeSort_login_state(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_login_state(left_side)
		MergeSort_login_state(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if str(left_side[i].login_state.lower()) < str(right_side[j].login_state.lower()):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Title
def MergeSort_title(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_title(left_side)
		MergeSort_title(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if str(left_side[i].title.lower()) < str(right_side[j].title.lower()):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due date
def MergeSort_dueDay(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_dueDay(left_side)
		MergeSort_dueDay(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			day_left = str(left_side[i].DueDay).split("/")
			day_right = str(right_side[j].DueDay).split("/")

			if int(day_left[0]) < int(day_right[0]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due Month
def MergeSort_dueMonth(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_dueMonth(left_side)
		MergeSort_dueMonth(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			day_left = str(left_side[i].DueDay).split("/")
			day_right = str(right_side[j].DueDay).split("/")

			if int(day_left[1]) < int(day_right[1]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due Year
def MergeSort_dueYear(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_dueYear(left_side)
		MergeSort_dueYear(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			day_left = str(left_side[i].DueDay).split("/")
			day_right = str(right_side[j].DueDay).split("/")

			if int(day_left[2]) < int(day_right[2]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due Hour
def MergeSort_dueHour(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_dueHour(left_side)
		MergeSort_dueHour(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i].DueHour) < int(right_side[j].DueHour):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Time limit
def MergeSort_TimeLimit(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_TimeLimit(left_side)
		MergeSort_TimeLimit(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i].Limit_Time) < int(right_side[j].Limit_Time):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort importance
def MergeSort_Importance(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_Importance(left_side)
		MergeSort_Importance(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i].importance) < int(right_side[j].importance):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

#### Descending Order ####
## Sort descending Project Name
def MergeSort__desc_projectName(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort__desc_projectName(left_side)
		MergeSort__desc_projectName(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if str(left_side[i].Project_name.lower()) > str(right_side[j].Project_name.lower()):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort descending Title
def MergeSort_desc_title(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc_title(left_side)
		MergeSort_desc_title(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if str(left_side[i].title.lower()) > str(right_side[j].title.lower()):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due date
def MergeSort_desc_dueDay(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc_dueDay(left_side)
		MergeSort_desc_dueDay(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			day_left = str(left_side[i].DueDay).split("/")
			day_right = str(right_side[j].DueDay).split("/")

			if int(day_left[0]) > int(day_right[0]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due Month
def MergeSort_desc_dueMonth(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc_dueMonth(left_side)
		MergeSort_desc_dueMonth(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			day_left = str(left_side[i].DueDay).split("/")
			day_right = str(right_side[j].DueDay).split("/")

			if int(day_left[1]) > int(day_right[1]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due Year
def MergeSort_desc_dueYear(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc_dueYear(left_side)
		MergeSort_desc_dueYear(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			day_left = str(left_side[i].DueDay).split("/")
			day_right = str(right_side[j].DueDay).split("/")

			if int(day_left[2]) > int(day_right[2]):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Due Hour
def MergeSort_desc_dueHour(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc_dueHour(left_side)
		MergeSort_desc_dueHour(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i].DueHour) > int(right_side[j].DueHour):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort Time limit
def MergeSort_desc_TimeLimit(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc_TimeLimit(left_side)
		MergeSort_desc_TimeLimit(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i].Limit_Time) > int(right_side[j].Limit_Time):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

# Sort importance
def MergeSort_desc_Importance(list_size):
	if len(list_size) > 1 :
		mid = len(list_size)//2
		left_side = list_size[:mid]
		right_side = list_size[mid:]
		MergeSort_desc_Importance(left_side)
		MergeSort_desc_Importance(right_side)
		i = 0
		j = 0
		k = 0
		while i < len(left_side) and j < len(right_side):
			if int(left_side[i].importance) > int(right_side[j].importance):
				list_size[k] = left_side[i]
				i += 1
			else:
				list_size[k] = right_side[j]
				j += 1
			k += 1
		while i < len(left_side):
			list_size[k] = left_side[i]
			k += 1
			i += 1
		while j < len(right_side):
			list_size[k] = right_side[j]
			k += 1
			j += 1

###### Search Algorithm #######
# Binary Search
def binarySearch(arr, start, end, x):
# check condition
    if end >= start:
        mid = start + (end- start)//2
        # If element is present at the middle
        if arr[mid] == x:
            return mid
        # If element is smaller than mid
        elif arr[mid] > x:
            return binarySearch(arr, start, mid-1, x)
        # Else the element greator than mid
        else:
            return binarySearch(arr, mid+1, end, x)
    else:
        # Element is not found in the array
        return -1
        
def ExponentialSearch(arr,n,x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i *= 2
    return binarySearch(arr, i//2, min(i,n), x)


# KnapSack Algorithm
def knapSack(W, wt, val, n,K):
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

def truyvet(n,W,K,wt, result_list):
    i=int(n)
    j=int(W)
    GT = 0
    while i != 0 and j != 0 :
        if K[i][j] != K[i-1][j] :
        	# print(i)
        	result_list.append(i-1)
        	j = j - wt[i-1]
        i -= 1

### Search value in list ###
def search(submitted_late, temp_val):
	for i in range(0, len(submitted_late), 1):
		if temp_val == submitted_late[i]:
			return True
	return False

def search_keyword(submitted_late, temp_val):
	for i in range(0, len(submitted_late), 1):
		if submitted_late[i] in temp_val:
			return True
	return False

def check_valid_email(email):
	if "@" in email and "." in email:
		return True
	else:
		return False

def existed_username(keyword):
	temp_list = []
	with open("user", "r") as user_file:
		reader = csv.reader(user_file, delimiter = "|")
		for row in reader:
			temp_list.append(Account_Info(row[0], row[1], row[2], row[3], row[4]))

	for i in range(0, len(temp_list), 1):
		if keyword == temp_list[i].username:
			return True
	return False

def stringAndNumber(string_list, keyword):
	if search_keyword(string_list, keyword) == True:
		for i in range(0, 9):
			if str(i) in keyword:
				return True
	return False

# Harsh - Password protection
def sha1(data):
    bytes = ""

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    pBits = bits
    #pad until length equals 448 mod 512
    while len(pBits)%512 != 448:
        pBits+="0"
    #append the original length
    pBits+='{0:064b}'.format(len(bits)-1)

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    for c in chunks(pBits, 512): 
        words = chunks(c, 32)
        w = [0]*80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #Main loop
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


#### Use for create appear box ####
def CreateToolTip(widget, text, x_offset, y_offset):
    toolTip = ToolTip(widget, x_offset, y_offset)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)