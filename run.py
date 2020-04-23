from util.excel import Excel

if __name__ == "__main__":

    excel = Excel()

    rows = excel.get_row_nums()

    for i in range(2, rows + 1):
        row_value = excel.get_row_value_from_target_sheet(i)
