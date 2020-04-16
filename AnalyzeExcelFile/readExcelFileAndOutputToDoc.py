import xlrd
import docx
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 新建doc文档
doc = docx.Document()

# open the .xlsx file
book = xlrd.open_workbook('resource/helk dashboard visualization_补充完整.xlsx')

sheet1 = book.sheets()[0]


dashboard = ""

for rowNum in range(1, sheet1.nrows):

    curr_dashboard = sheet1.cell(rowNum, 0).value
    if(curr_dashboard is not ""):
        dashboard = curr_dashboard
        doc.add_heading(dashboard, 1)
    
    visualization = sheet1.cell(rowNum, 1).value
    visualization_type = sheet1.cell(rowNum, 2).value
    description = sheet1.cell(rowNum, 3).value

    if(visualization is not ""):
        doc.add_heading(visualization, 2)
        doc.add_paragraph('该visualization的类型为' + visualization_type + ',其作用是' + description + '。其界面如下图所示：')
        pic_path = 'resource/pic/' + visualization + '.png'
        try:
            # 指定图片宽度为 4英寸, 图片高度会自动调整
            doc.add_picture(pic_path, width=Inches(4))
            last_paragraph = doc.paragraphs[-1]
            #图片居中设置
            last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

            # 输出已经分析的visualization名字到指定文件
            with open("resource/visualization.txt", "at", encoding="utf-8") as file:
                file.write(visualization+'\n')
        except FileNotFoundError:
            print(pic_path + "不存在")
            continue

doc.save('resource/output.docx')


