import mysql.connector as c
mydb = c.connect(
  host="localhost",
  user="root",
  password="system",
  database="supriya"
)
mycursor = mydb.cursor()
            # # create table
# mycursor.execute('CREATE TABLE fam(number INT, name VARCHAR(20), age INT);')
# print("table created")
# mydb.commit()

           # # insert values
# num=input("Enter your number\n")
# name= input("Enter your name\n")
# age=input("Enter your age\n")
# mycursor.execute("insert into fam values(%s,%s,%s)",(num,name,age))

           # # delete values
# mycursor.execute("DELETE FROM fam WHERE number = 1;")
# print("Deleted successfully")

          # # update fam details
# mycursor.execute("UPDATE fam SET name = 'Adi', age = 18 WHERE number = 2")
          # # display table details
# mycursor.execute("select * from fam")
# students=mycursor.fetchall();
# for std in students:
#   print(std)
#
          # # diplay fam details based on name
# mycursor.execute("SELECT * FROM fam ORDER BY name DESC")
# fam_details = mycursor.fetchall()
# # Display the fetched records
# if fam_details:
#     print("Displaying 'fam' details based on name 'Thomas':")
#     for record in fam_details:
#         print(record)
# else:
#     print("No records found for the name 'Thomas'.")

        # # display fam details whose age is between 10-20
# mycursor.execute("SELECT * FROM fam WHERE age BETWEEN 10 AND 20;")
# fam_details = mycursor.fetchall()
# if fam_details:
#     print("Displaying 'fam' details where age is between 10 and 20:")
#     for record in fam_details:
#         print(record)
# else:
#     print("No records found where age is between 10 and 20.")

mydb.commit()
