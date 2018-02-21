#!/urs/bin/env python3
import os
import sys
import glob
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_directory = sys.argv[1]
output_file = sys.argv[2]
#
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("sums_and_averages")

all_data = []
sales_column_index = 3

header = ["Workbook", "Worksheet", "Worksheet_total", "Worksheet_average", "Workbook_total", "Workbook_average"]
all_data.append(header)

for input_file in glob.glob(os.path.join(input_directory, "*.xls*")) :
    with open_workbook(input_file) as workbook :
        total_sales_list = []
        total_num_of_sales = []
        workbook_output = []
        for worksheet in workbook.sheets() :
            total_sales = 0
            num_of_sales = 0
            worksheet_output = []
            worksheet_output.append(glob.glob(os.path.basename(input_file)))
            worksheet_output.append(worksheet.name)
            for row_index in range(1, worksheet.nrows) :
                try :
                    total_sales += worksheet.cell_value(row_index, sales_column_index)
                    # total_sales += float(str(worksheet.cell_value(row_index, sales_column_index)).strip('$').replace(',',''))
                    num_of_sales += 1
                except :
                    total_sales += 0
                    num_of_sales += 0
            # print("sheet by sheet : %.2f" %total_sales)
            total_num_of_sales.append(num_of_sales)
            average_sale = "%.2f" %(total_sales / num_of_sales)
            total_sales_list.append(total_sales)
            worksheet_output.append(total_sales)
            worksheet_output.append(float(average_sale))
            workbook_output.append(worksheet_output)
        workbook_total = sum(total_sales_list)
        workbook_average = sum(total_sales_list) / sum(total_num_of_sales)

        for list_element in workbook_output :
            list_element.append(workbook_total)
            list_element.append(workbook_average)
        all_data.extend(workbook_output)

for list_index, output_list in enumerate(all_data) :
    for element_index, element in enumerate(output_list) :
        output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)

print("End.")



# -------------------------------------------------------------------------------------------------------------------------
# #!/urs/bin/env python3
# import os
# import sys
# import glob
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
#
# input_directory = sys.argv[1]
# output_file = sys.argv[2]
#
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet("sums_and_averages")
#
# all_data = []
# sales_column_index = 3
#
# header = ["Workbook", "Worksheet", "Worksheet_total", "Worksheet_average", "Workbook_total", "Workbook_average"]
# all_data.append(header)
#
# for input_file in glob.glob(os.path.join(input_directory, "*.xls*")) :
#     with open_workbook(input_file) as workbook :
#         list_of_totals = []
#         list_of_numbers = []
#         workbook_output = []
#         for worksheet in workbook.sheets() :
#             total_sales = 0
#             num_of_sales = 0
#             worksheet_list = []
#             worksheet_list.append(os.path.basename(input_file))
#             worksheet_list.append(worksheet.name)
#             for row_index in range(1, worksheet.nrows) :
#                 try :
#                     total_sales += worksheet.cell_value(row_index, sales_column_index)
#                     # total_sales += float(str(worksheet.cell_value(row_index, sales_column_index)).strip('$').replace(',',''))
#                     num_of_sales += 1
#                 except :
#                     total_sales += 0
#                     num_of_sales += 0
#             # print("sheet by sheet : %.2f" %total_sales)
#             average_sale = "%.2f" %(total_sales / num_of_sales)
#             worksheet_list.append(total_sales)
#             worksheet_list.append(float(average_sale))
#             list_of_totals.append(total_sales)
#             list_of_numbers.append(float(num_of_sales))
#             workbook_output.append(worksheet_list)
#         workbook_total = sum(list_of_totals)
#         workbook_average = sum(list_of_totals) / sum(list_of_numbers)
#         for list_element in workbook_output :
#             list_element.append(workbook_total)
#             list_element.append(workbook_average)
#         all_data.extend(workbook_output)
#
# for list_index, output_list in enumerate(all_data) :
#     for element_index, element in enumerate(output_list) :
#         output_worksheet.write(list_index, element_index, element)
#
# output_workbook.save(output_file)
#
# print("End.")