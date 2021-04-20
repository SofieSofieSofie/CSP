import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="podcast"
)

mycursor = mydb.cursor()

epNum = 499
epNam =  "America Isn't Real"
epPath = "transcribe/cth_text/cth499.txt"
epLink = "display_cth.php?id=499"

parsedText = open("transcribe/cth_text/cth499.txt", "r").read()

sql = "INSERT INTO cth (id, epNam, epPath, epLink, parsedtext) VALUES (%s, %s, %s, %s, %s)"
val = (epNum, epNam, epPath, epLink, parsedText)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")