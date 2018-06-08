import xlrd

class ReadExcel:

    def __init__(self,excelfile, sheet,dataid):
        self.excelfile=excelfile
        self.sheet=sheet
        self.dataid=dataid

    def getExcelData(self):
        #print(self.excelfile,self.sheet)
        wb=xlrd.open_workbook(self.excelfile)
        ws=wb.sheet_by_name(self.sheet)
        return ws
            
        
        
        









