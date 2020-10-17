class ExcelFile:
    def __init__(self, workbook, worksheet):
        self.workbook = workbook
        self.worksheet = worksheet

    def get_data(self):
        return [self.workbook, self.worksheet]