import xlsxwriter
import functions

def create_file(name):
    excelFile=xlsxwriter.Workbook(f'.\\exports\\{name}.xlsx')
    return excelFile

def create_sheet(excel_file, sheet_name, headers, titles, data_set):
    #HEADER FORMAT
    topHeader_format=excel_file.add_format({'font_name': 'Arial', 'font_size': 8, 'bottom': 1})
    boldHeader_format=excel_file.add_format({'font_name': 'Arial', 'font_size': 8, 'bold': True})
    bottomHeader_format=excel_file.add_format({'font_name': 'Arial', 'font_size': 8, 'top': 5})

    #TITLE FORMATS
    title_format=excel_file.add_format({'font_name': 'Arial', 'font_size': 8, 'bg_color': '#000066', 'font_color': '#FFFFFF', 'bold': True, 'align': 'center', 'valign':'top'})

    #DATA FORMATS
    normalData_format=excel_file.add_format({'font_name': 'Arial', 'font_size': 8})
    
    #SHEET NAME
    worksheet=excel_file.add_worksheet(sheet_name)

    #SHEET DISPLAY
    rowSize=12
    worksheet.hide_gridlines(2)
    worksheet.set_column('A:A', 1)
    worksheet.set_row(0, rowSize, topHeader_format)

    contRow=1
    contCol=1
    
    for header in headers:
        worksheet.set_row(contRow, rowSize, boldHeader_format)
        worksheet.write(contRow, contCol, header)
        contRow+=1

    worksheet.set_row(contRow, rowSize, bottomHeader_format)
    contRow+=1

    for title in titles:
        worksheet.set_row(contRow, rowSize)
        worksheet.write(contRow, contCol, title, title_format)
        contCol+=1
    contCol=1
    contRow+=1

    for datas in data_set:
        worksheet.set_row(contRow, rowSize)
        for data in datas:
            worksheet.write(contRow, contCol, data, normalData_format)
            contCol+=1
        contCol=1
        contRow+=1

    worksheet.autofilter(len(headers)+2, 1, contRow-1, len(titles))
    worksheet.freeze_panes(len(headers)+3, 1)
   
def export_base(datas, sheet_name):
    excel_file=create_file("state")

    headers=[
        'ESTADOS BRASILEIROS',
        'Por: Gustavo Brietzig'
    ]
    titles=functions.extract_keys(datas)
    datas=functions.extract_datas(datas, titles)
    create_sheet(excel_file, sheet_name, headers, titles, datas)

    excel_file.close()
