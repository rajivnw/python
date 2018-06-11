import xlrd

class ReadExcel:

    def __init__(self,excelfile, sheet,dataid):
        self.excelfile=excelfile
        self.sheet=sheet
        self.dataid=dataid
        self.wb=xlrd.open_workbook(self.excelfile)
        self.ws=self.wb.sheet_by_name(self.sheet)

    def getExcelSheet(self):
        return self.ws
    
    def getExcelWoorkbook(self):
        return self.wb
    
    def getDictOfExecutbleMethods(self):
        executableMethodsDict={}
        
        for rw in range(self.ws.nrows):
            if(self.ws.row(rw)[3].value=='Y' and self.ws.row(rw)[1].value=='Start'):
                
                testCaseId=int(self.ws.row(rw)[0].value)
                firstcond=True
                secondCon=True
                i=1
                methodsDict={}
                
                while(firstcond and secondCon):
                    
                    firstCondition=rw+i<(len(range(self.ws.nrows)))
                    if (not firstCondition):
                        break
                    
                    secondCondition=self.ws.row(rw+i)[1].value !='Start'
                    if (not secondCondition):
                        break
                    
                    methodID=round(float(self.ws.row(rw+i)[0].value),3)
                    methodName=str(self.ws.row(rw+i)[1].value)
                    
#                     print(methodID)
#                     print(methodName)
#                     print(int(methodID))
                    
                    if(testCaseId==int(methodID)):
                        methodsDict.update({methodID:methodName})
                    i=1+i
                executableMethodsDict.update({testCaseId:methodsDict})
#                 print(methodsDict)
#         print(executableMethodsDict)
        return executableMethodsDict
        
        
            
                    
        
    
    
            
        
        
        









