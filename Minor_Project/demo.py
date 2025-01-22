# # import os
# # p = os.environ.get("demo_pass")
# # print(p)


# # body = """
# #     Dear name,
# #     Your request for
# # """
# # print(body)
# # name = "abc"
# # book = "pyton"
# # b = f"Dear {name}\nyour request for {book} has been issued"
# # print(b)


# # from datetime import timedelta,date
# import sqlite3

# # to = date.today()
# # a3 = to + timedelta(days=3)

# # con = sqlite3.connect("projectDB.db")
# # cur = con.cursor()
# # q = "select SID, BookID, SubjectName, BookName, AuthorName, Edition from issueBook where DueDate = ? and ReturnDate = ?"
# # cur.execute(q,(a3,'NULL'))
# # res = cur.fetchall()
# # print(res)

# # dt = '2023-08-08'
# # y,m,d = map(int,dt.split('-'))
# # rem = date(y,m,d)
# # 
# # print(a3)
# # if a3 == rem:
# #     print("Ok")
# # else:
#     # print("Not Ok")


# # from datetime import datetime
# # # import time
# # ct = datetime.now().time()
# # print(ct)
# # # st = datetime.strptime("2026-07-06 23:30:00", "%Y-%m-%d %H:%M:%S").time()
# # st = datetime.strptime("23:30:00", "%H:%M:%S").time()
# # print(st)
# # if ct >= st :
# #     print("cT")
# # else:
# #     print("sT")

# # import time

# # # Get the current time
# # current_time = time.localtime()

# # # Define a specific time (hour, minute, and second)
# # specific_time = (2023, 7, 29, 15, 30, 0)  # Format: (year, month, day, hour, minute, second)

# # # Convert both times to seconds since the epoch
# # current_time_seconds = time.mktime(current_time)
# # print(current_time_seconds)
# # specific_time_seconds = time.mktime(specific_time)
# # print(specific_time_seconds)

# # Compare the two times
# # if current_time_seconds > specific_time_seconds:
# #     print("The current time is later than the specific time.")
# # elif current_time_seconds < specific_time_seconds:
# #     print("The current time is earlier than the specific time.")
# # else:
# #     print("The current time is the same as the specific time.")


# con = sqlite3.connect("projectDB.db")
# cur = con.cursor()
# q = "select SID,BookID,SubjectName,BookName,AuthorName,Edition,IssueDate,ReturnDate from issueBook where ReturnDate = ?"
# cur.execute(q,("NULL",))
# res= cur.fetchall()
# # data = [('PYTHON/001', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-11', '2023-07-15', '2023-07-27', 'F101'), ('JAVA/002', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-25', '2023-08-08', '2023-07-27', 'NULL'), ('PYTHON/003', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-25', '2023-08-08', '2023-07-25', 'NULL'), ('JAVA/001','Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-20', '2023-08-26', '2023-07-27', 'NULL'), ('JAVA/002', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-20', '2023-07-26', '2023-07-27', 'F103'), ('gf', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-25', '2023-08-08', 'NULL', 'NULL'), ('ghg', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-25', '2023-08-08', 'NULL', 'NULL'), ('abv', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-26', '2023-08-08', 'NULL', 'NULL')]
# data = [[str(i) for i in j] for j in res]
# print(res)
# print(data)
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
e = "ssss@gmail.com"
# if re.fullmatch(regex, e)== True:
if re.fullmatch(regex, e):
    # print(re.fullmatch(regex, e))
    print("ok")
else:
    print("mot ok")

a = "54"
print(a.isnumeric())

