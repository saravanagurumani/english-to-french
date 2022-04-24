import csv
  

from fileinput import FileInput




	
def replacetext(st):



	
	with FileInput("write.txt", inplace=True,
				backup='.bak') as f:
		for line in f:
			print(line.replace(st[0], st[1]), end='')

	return "Text replaced"









with open('french_dictionary.csv') as file_obj:
      
    reader_obj = csv.reader(file_obj)
      
    for row in reader_obj:
       print(replacetext(row))
