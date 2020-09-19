import xlrd
def readExcelDataAsperTestCase(TCName,ColumnName):
    # TCName = "TC001_OpenFacebook"
    # ColumnName = "URL"
    file_location = "C:/Users/prodebna/PycharmProjects1/BDD/TestData/PythonDemo.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_name("Sheet1")

    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            if sheet.cell(i, j).value == ColumnName:
                cellNumber = j
                break
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            if sheet.cell(i, j).value == TCName:
                value = sheet.cell(i, cellNumber).value
                print(value)
                return value
                break







