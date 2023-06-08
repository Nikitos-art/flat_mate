from flat_mate.flat import Bill, Flatmate
from flat_mate.reports import PdfReport, FileSharer

bill_amount = float(input('Hei user, enter the bill amount: '))
period = input('What is the bill period? Eg. December 2012: ')
name1 = input('Enter your name: ')
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input('Enter your roommates name: ')
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(bill_amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays:", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)


file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())