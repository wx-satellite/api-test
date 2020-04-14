from openpyxl import load_workbook


class HandleExcel:
    path = "../case/base.xlsx"
    instance = None

    def set_path(self, path):
        self.path = path
        return self

    def init_excel(self):
        if self.instance is None:
            self.instance = load_workbook(self.path)

    def get_target_sheet(self, index):
        self.init_excel()
        return self.instance[self.instance.sheetnames[index]]

    # 行号row_index从1开始
    def get_row_from_target_sheet(self, row_index=1, target_index=0):
        row_values = []
        sheet = self.get_target_sheet(target_index)
        for v in sheet[row_index]:
            row_values.append(v.value)
        return row_values


if __name__ == "__main__":
    handleExcel = HandleExcel()
    print(handleExcel.get_row_from_target_sheet(1))
