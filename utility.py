from Utilitys import XMLReader

wb=XMLReader.ReadExcel("newmarks.xls","Sheet1","1")
ws=wb.getExcelData()

for rw in range(ws.nrows):
    print (ws.row(rw))
