
# from email.policy import default
# from turtle import width
from fpdf import FPDF

# create object
# Layout ('P','l')
# unit('mm','cm','in')
# format('A3'.'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
# pdf = FPDF('L','mm','A4')

# Add a page
# pdf.add_page()

# specify font
# Fonts ('times','courier','helvetica','symbol','zpfdingbats')
# 'B'  (bold), 'U' (underline), 'I'(italic), ''(ragular), combination(i.e. ('BU')) 
# pdf.set_font('helvetica','B',18) # font size

# # add text
# w ==width h = height
# pdf.cell(40,10,'hello')
# pdf.output('pdf_1.pdf')


# simple_table.py

# from fpdf import FPDF
import sqlite3

def simple_table(spacing=4):
    con = sqlite3.connect("projectDB.db")
    cur = con.cursor()
    q = "select SID,BookID,SubjectName,BookName,AuthorName,Edition,IssueDate,ReturnDate from issueBook where ReturnDate = ?"
    cur.execute(q,("NULL",))
    res= cur.fetchall()
    # data = [('PYTHON/001', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-11', '2023-07-15', '2023-07-27', 'F101'), ('JAVA/002', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-25', '2023-08-08', '2023-07-27', 'NULL'), ('PYTHON/003', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-25', '2023-08-08', '2023-07-25', 'NULL'), ('JAVA/001','Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-20', '2023-08-26', '2023-07-27', 'NULL'), ('JAVA/002', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-20', '2023-07-26', '2023-07-27', 'F103'), ('gf', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-25', '2023-08-08', 'NULL', 'NULL'), ('ghg', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-25', '2023-08-08', 'NULL', 'NULL'), ('abv', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-26', '2023-08-08', 'NULL', 'NULL')]
    data = [[str(i) for i in j] for j in res]
    # data.insert(0,('A','b','c','d','e','f','g','h'))
    data.insert(0,('SID','BookID','SubjectName','BookName','AuthorName','Edition','IssueDate','ReturnDate'))
    pdf = FPDF('L','mm','A4')
    pdf.set_font('helvetica','B',9)
    pdf.add_page()

    col_width = pdf.w / 8.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing, txt=item, border=2)
        pdf.ln(row_height*spacing)
        
    pdf.output('simple_table_2.pdf')

simple_table()

"""from reportlab.pdfgen import canvas
path = 'D:\Python_pdf\my_pdf.pdf'
c = canvas"""
