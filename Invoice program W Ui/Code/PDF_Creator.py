from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date

import fitz  # PyMuPDF

print(date.today().strftime('%d-%m-%Y'))

def create_invoice_pdf(filename,client_info,Invoice_number,rate,all_services):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    personal_data = []
    personal_data_txt = open("Personal\Personal_data.txt","r")
    for i in enumerate(personal_data_txt):
        personal_data.append(i[1].replace("\n",""))

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, height - 50, "Invoice" )

    # Client Info
    c.setFont("Helvetica-Bold",12)
    c.drawString(50, height - 95, "Bill To:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 115, client_info[0])
    c.drawString(50, height - 130, client_info[1])
    c.drawString(50, height - 145, client_info[2]+", "+client_info[3]+", "+client_info[4])
    c.drawString(50, height - 160, "Email: "+client_info[5])

    # User Info
    c.setFont("Helvetica-Bold",12)
    c.drawString(50, height - 185, "From:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 205, personal_data[0])
    c.drawString(50, height - 220, personal_data[1])
    text = personal_data[3]+", "+personal_data[2]+", "+personal_data[4]
    c.drawString(50, height - 235, text)
    c.drawString(50, height - 250, "Email: "+personal_data[5])
    c.drawString(50, height - 265, "Phone Number: "+personal_data[6])

    # invoice info
    c.setFont("Helvetica-Bold",10)
    text_width = c.stringWidth("Invoice Number: ", "Helvetica-Bold", 10)
    c.drawString(490-text_width,height - 115,"Invoice Number: ")
    c.setFont("Helvetica",10)
    text_width = c.stringWidth("Invoice Date: ", "Helvetica", 10)
    c.drawString(490-text_width,height - 130,"Invoice Date: ")

    # Client Info
    c.setFont("Helvetica-Bold",10)
    text_width = c.stringWidth(str(Invoice_number), "Helvetica-Bold", 10)
    c.drawString(550 - text_width, height - 115, str(Invoice_number))
    c.setFont("Helvetica",10)
    text_width = c.stringWidth(str(date.today().strftime('%d-%m-%Y')), "Helvetica", 10)
    c.drawString(550 - text_width, height - 130, str(date.today().strftime('%d-%m-%Y')))

    # break line start of services
    c.line(40,525 , 560,525)

    # service information
    c.setFont("Helvetica-Bold",12)
    c.drawString(50, 540, "Description")
    c.drawString(250, 540, "Date")
    c.drawString(350,540,"Hours/£"+str(float(rate))+"0")
    c.setFont("Helvetica-Bold",12)
    text_width = c.stringWidth("Total", "Helvetica-Bold", 12)
    c.drawString(550 - text_width, 540, "Total")

    # fill in table with data from dates cleaned
    c.setFont("Helvetica",10)
    base_height = 500
    sub_total = 0
    for i in all_services:
        c.drawString(50,base_height,i[4])
        c.drawString(250,base_height,i[3])
        c.drawString(385,base_height,i[2])
        c.drawRightString(550, base_height, "£"+str(float(i[2])*float(rate))+"0")
        base_height -= 20
        sub_total = sub_total + float(i[2])*float(rate)
    c.line(40,base_height , 560,base_height)
    c.setFont("Helvetica-Bold",12)
    c.drawString(50,base_height-20,"Total")
    text_width = c.stringWidth(str(sub_total),"Helvetica",10)
    c.drawRightString(550,base_height-20,"£"+str(float(sub_total))+"0")

    # Bank Info
    c.setFont("Helvetica-Bold",12)
    c.drawString(50, base_height - 60, "Pay By Transfer:")
    c.setFont("Helvetica",10)
    c.drawString(50, base_height - 80, "Account Name: "+personal_data[10])
    c.drawString(50, base_height - 100, "Name Of Bank: "+personal_data[7])
    c.drawString(50, base_height - 120, "Sort Code: "+personal_data[8])
    c.drawString(50, base_height - 140, "Account No: "+personal_data[9])

    # save file
    c.save()

