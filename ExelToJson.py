import json
import os
import xlrd


class ExcelToJson:

    def __init__(self, Path):
        """

        :param Path: 路径
        """
        self.json = []
        self.Execl = None
        self.Table = None
        self.Path = Path
        self.Nrows = None
        self.Ncols = None
        self.KeyList = None
        self.TypeList = None
        self.FileName = None
        self.Input()
        self.GetNcols()
        self.GetNrows()
        self.GetKeyList()
        self.GetTypeList()
        self.ListContent()
        self.Save()

    def Input(self):
        self.Execl = xlrd.open_workbook(self.Path)

        self.Table = self.Execl.sheet_by_index(0)

    def Output(self):
        return self.Table

    def GetNrows(self):
        """
        :return: 行数

        """
        self.Nrows = self.Table.nrows
        print("行数", self.Nrows)
        return self.Nrows

    def GetNcols(self):
        """

        :return: 列数
        """
        self.Ncols = self.Table.ncols
        return self.Ncols

    def ListContent(self):
        for i in range(3, self.Nrows):
            values = self.Table.row_values(i, 0)
            valuesLen = len(values)

            jsObj = {}
            for j in range(0, valuesLen):
                key = self.KeyList[j]
                value = values[j]
                if self.TypeList[j] == "int":
                    value = int(value)
                jsObj[key] = value
            self.json.append(jsObj)

    def GetKeyList(self):
        self.KeyList = self.Table.row_values(1, 0)
        print("KeyList", self.KeyList)

    def GetTypeList(self):
        self.TypeList = self.Table.row_values(2, 0)

    def Save(self):
        replace = self.Path.replace("xlsx", "json")

        jsonStr = json.dumps(self.json, ensure_ascii=False)

        with open(replace, "w") as f:
            f.write(jsonStr)


if __name__ == '__main__':

    for root, dirs, files in os.walk("."):
        print(files)
        for i in range(0, len(files)):
            i_ = files[i]
            i__ = i_[-5:]
            if(i__==".xlsx"):
                ExcelToJson(i_)