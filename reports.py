import webbrowser
import os
from fpdf import FPDF
from filestack import Client
from dotenv import load_dotenv
load_dotenv()
my_api_key = os.getenv("FILE_SHARE_API_KEY")

BORDER = 0


class PdfReport:
    """
    Creates a PDF file that contains data about a flatmate, such as their names, their due
    amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates bill', border=BORDER, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt='Period:', border=BORDER)
        pdf.cell(w=150, h=25, txt=bill.period, border=BORDER, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=BORDER)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=BORDER, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=BORDER)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=BORDER, ln=1)

        # Change directory to files
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
        ### on mac and linux need some tinkering because it wont open the path automatically
        ### webbrowser.open('file'://+os.path.realpath(self.filename))


class FileSharer:
    def __init__(self, filepath, api_key=my_api_key):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url