import Utilitys.ExcelReader as dr

wb=dr.ReadExcel("/Users/rajiv/Documents/Automation/PythonPractice/newmarks.xls","Instraction","1")
dic=wb.getDictOfExecutbleMethods()
print("my print")
print(dic)