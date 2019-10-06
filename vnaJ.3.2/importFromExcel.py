import xlrd
import MySQLdb
import os
import sys

if len(sys.argv) < 2:
	print("Vous devez fournir un chemin vers lequel recuperer le xls")
	sys.exit(1)
path=os.path.abspath(sys.argv[1])

# Open the workbook and define the worksheet 
book = xlrd.open_workbook(path)
nom_des_feuilles=book.sheet_names()
sheet = book.sheet_by_name(nom_des_feuilles[0])

# Establish a MySQL connection 

##database = MySQLdb.connect(host="10.42.0.1", user="Junior", passwd="cnd", db = "exemple")

# Get the cursor, which is used to traverse the database, line by line
##cursor = database.cursor()

# Create the table

##query0 = 'CREATE TABLE ' + path[25:(len(path)-4)] + ' LIKE mesure'
##cursor.execute(query0)

# Create the INSERT INTO sql query 

##query = 'INSERT INTO ' + path[25:(len(path)-4)]+ ' (frequency, returnloss, returnphase, transmissionloss, transmissionphase, rs, xs, z, magnitude, rhoreal, rhoimag, swr, theta, groupdelay) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
##for r in range(2,sheet.nrows):
##	frequency = sheet.cell(r,0).value
##	returnloss = sheet.cell(r,1).value
##	returnphase = sheet.cell(r,2).value
##	transmissionloss = sheet.cell(r,3).value
##	transmissionphase = sheet.cell(r,4).value
##	rs = sheet.cell(r,5).value
##	xs = sheet.cell(r,6).value
##	z = sheet.cell(r,7).value
##	magnitude = sheet.cell(r,8).value
##	rhoreal = sheet.cell(r,9).value
##	rhoimag = sheet.cell(r,10).value
##	swr = sheet.cell(r,11).value
##	theta = sheet.cell(r,12).value
##	groupdelay = sheet.cell(r,13).value
	
	# Assign values from each row 
##	values = (frequency, returnloss, returnphase, transmissionloss, transmissionphase, rs, xs, z, magnitude, rhoreal, rhoimag, swr, theta, groupdelay)

	# Execute sql quety 
##	cursor.execute(query,values)

# Close the cursor 
##cursor.close()

# Commit the transaction
##database.commit()

# Print results 
##print( " ")
##print( "All Done! Bye, for now.")
##print( " ")
##columns = str(sheet.ncols)
##rows = str(sheet.nrows)
##print ("I just imported "+ columns +" columns and "+ rows + "rows to MySQL!")


# Send data via a .txt file

fichier = open("/home/pi/vnaJ.3.2/export/"+path[25:(len(path)-4)]+".txt","w")
for r in range(2,sheet.nrows):
	fichier.write(str(sheet.cell(r,0).value))
	fichier.write(",")
	fichier.write(str(sheet.cell(r,1).value))
	fichier.write(",")
	fichier.write(str(sheet.cell(r,2).value))

fichier.close()
