
#h leksh me to megalytero mhkos


colors = str('red white blue')
print(colors)

words = colors.split()
print max(colors,key=len) #epistrefei th max

def find_longest_word(color_list):
	longest_word=" " 
	
	for word in color_list:
		if len(word) > len(longest_word) 
			longest_word = word
			
	print longest_word
