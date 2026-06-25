from openpyxl import Workbook
def save(df,path):
    wb=Workbook();ws=wb.active
    ws.append(["Day"]+list(df.columns))
    for d,row in df.iterrows():
        ws.append([d]+list(row))
    wb.save(path)
