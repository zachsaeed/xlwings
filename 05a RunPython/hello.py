
import xlwings as xw



def hello_python():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    sheet.range("A1").value = "Hello Python!" 

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    sheet.range("A2").value = "This is easy!"   

