
# cnxn = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server};' 
#     'SERVER=LAPTOP-I7J2DJUB;' 
#     'DATABASE=Sprint1Practise;'
#     'Trusted_Connection=yes;'
# )

# cnxn = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server};' 
#     'SERVER=LAPTOP-I7J2DJUB;' 
#     'DATABASE=Sprint1Practise;'
#     'Trusted_Connection=yes;'
# )

# connection_string = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:userdatainsert.database.windows.net,1433;Database=userdata;Uid=dhruvk18;Pwd={Dhruv1802};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
# cnxn: pyodbc.Connection = pyodbc.connect(connection_string)


#create a new cursor object from the connection
# cur: pyodbc.Cursor = cnxn.cursor()

'''
import lines
    initialise the flask app

connection lines

--routing methods for home and search

routing method for home
    create cursor accordingly
    get the details from the form 

    create a cursor for inserting
    traditional insert sql query

create a routing method for search
    get the mobile number from the form
    create a cursor

    perform select query traditional manner
    return result in html file



'''

#importing the needed packages and modules
# from flask import Flask, render_template, request, redirect
# import textwrap
import pymssql
# app = Flask(__name__)
 
conn = pymssql.connect('webappdbaccess.eastus.cloudapp.azure.com','sa','Dhruv@18',"TestDB")
cursor = conn.cursor()

cursor.execute("""select * from Person""")

# cursor.executemany(
#     "INSERT INTO persons VALUES (%d, %s, %s)",
#     [(1, 'John Smith', 'John Doe'),
#      (2, 'Jane Doe', 'Joe Dog'),
#      (3, 'Mike T.', 'Sarah H.')])

# you must call commit() to persist your data if you don't set autocommit to True
# conn.commit()

# cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print(row)
    # row = cursor.fetchone()

conn.close()




# @app.route('/', methods=['GET','POST'])
# def hello():
#     if request.method == 'POST':
#         #Fetch form data
#         userDetails = request.form
#         firstName = userDetails['firstName']
#         lastName = userDetails['lastName']
#         email = userDetails['email']
#         phoneNumber = userDetails['phoneNumber']
#         try:
#             cur = cnxn.cursor()
#             insert_query= textwrap.dedent('''INSERT INTO Person(firstName, lastName, email, phoneNumber) VALUES(?, ?, ?, ?);''')
#             values = (str(firstName),str(lastName),str(email), str(phoneNumber))
#             cur.execute(insert_query,values)
#             cur.commit()
#         except Exception as err:
#             raise err

#         # cur.close()
#         return redirect('/users')
#     return render_template('index.html')
 
# @app.route('/users',methods=['GET','POST'])
# def users():
#     if request.method == 'GET':
#         #Fetch form data
#         try:
#             cur = cnxn.cursor()
#             cur.execute('SELECT * FROM Person')
#             # for row in cur:
#             #     print(row)
    
    
#             userDetails = cur.fetchall()
#             print(userDetails)
#             return render_template('users.html',posted=True, noResult=False,userDetails=userDetails)
#         except Exception as err:
#             return render_template('users.html',posted=False, noResult=True,userDetails=userDetails)
#     else:
#         return render_template('users.html',posted=False, noResult=True,userDetails=userDetails)
        
    

# if __name__ == '__main__':
#     app.run(debug=True)


