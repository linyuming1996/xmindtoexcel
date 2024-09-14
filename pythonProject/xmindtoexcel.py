from typing import List, Any
import xlwt
from xmindparser import xmind_to_dict
import xmindparser


class xmind_to_xls:
    def __init__(self):
        self.max = 0
        self.index = 0
        self.markers = []

    def resolve_path(self, dict_, lists, title):
        """
        通过递归取出每个主分支下的所有小分支并将其作为一个列表
        :param dict_:
        :param lists:
        :param title:
        :return:
        """
        # print(dict_)
        # print(lists)
        # print(title)
        # 去除title首尾空格
        title = title.strip()
        # print(title)
        # 若title为空，则直接取value
        if len(title) == 0:
            concat_title = dict_["title"].strip()
        else:
            concat_title = title + "\t" + dict_["title"].strip()
        if not dict_.__contains__("topics"):
            lists.append(concat_title)
            # print(lists)
        else:
            for d in dict_["topics"]:
                self.resolve_path(d, lists, concat_title)

    def find_markers(self, dict_):
        mark = None
        if dict_.get('makers'):
            # print(dict_)
            mark = int(dict_.get('makers')[0][-1])
            # print(mark)
            self.markers.append(mark)
            # print(self.markers)
        elif mark is None and not dict_.__contains__("topics"):
            mark = 2
            self.markers.append(mark)
        else:
            for d in dict_["topics"]:
                self.find_markers(d)

    def xmind_to_excel(self, list_, excel_path):
        f = xlwt.Workbook()
        # 生成单sheet的Excel文件，sheet名自取
        sheet = f.add_sheet("测试用例", cell_overwrite_ok=True)

        # 第一行固定的表头标题
        row_header = ["序号", "一级模块", "二级模块", "三级模块"]
        for i in range(0, len(row_header)):
            # print(len(row_header))
            sheet.write(0, i, row_header[i])

        # 增量索引

        for x in range(0, len(list_)):
            # 获取最深的用例长度
            lists: List[Any] = []
            self.resolve_path(list_[x], lists, "")
            for j in range(0, len(lists)):
                lists[j] = lists[j].split('\t')
                if len(lists[j]) > self.max:
                    self.max = len(lists[j])

        for h in range(0, len(list_)):
            lists: List[Any] = []
            # print(list_)
            self.resolve_path(list_[h], lists, "")
            self.find_markers(list_[h])
            # print(lists)
            # print(h)
            # print('\n'.join(lists))  # 主分支下的小分支
            for j in range(0, len(lists)):
                # 将主分支下的小分支构成列表
                lists[j] = lists[j].split('\t')
                # print(lists[j])
                for i in range(self.max - len(lists[j])):
                    lists[j].insert(-3, '')
                # print(lists[j])
                for n in range(0, len(lists[j])):
                    # 生成第一列的序号
                    sheet.write(j + self.index + 1, 0, j + self.index + 1)
                    sheet.write(j + self.index + 1, n + 1, lists[j][n])
                    # 自定义内容，比如：测试点/用例标题、预期结果、实际结果、操作步骤、优先级……
                    # 这里为了更加灵活，除序号、模块、功能点的标题固定，其余以【自定义+序号】命名，如：自定义1，需生成Excel表格后手动修改
                    if n == len(lists[j]) - 1:
                        sheet.write(0, n + 1, "预期结果")
                    elif n == len(lists[j]) - 2:
                        sheet.write(0, n + 1, "测试步骤")
                    elif n == len(lists[j]) - 3:
                        sheet.write(0, n + 1, "用例名称")
                    elif n >= 3:
                        sheet.write(0, n + 1, "自定义" + str(n - 1))
                # 遍历完lists并给增量索引赋值，跳出for j循环，开始for h循环
                if j == len(lists) - 1:
                    self.index += len(lists)
        sheet.write(0, self.max + 1, "优先级")
        self.index = 1
        for i in self.markers:
            sheet.write(self.index, self.max + 1, i)
            self.index += 1
        f.save(excel_path)

    def run(self, xmind_path):
        xmind_dict = xmind_to_dict(xmind_path)  # 将xmind转换成字典
        # print(xmind_dict)  # print("将XMind中所有内容提取出来并转换成列表：", xmind_dict)
        excel_name = xmind_path.split('\\')[-1].split(".")[0] + '.xls'  # Excel文件与XMind文件保存在同一目录下
        excel_path = "\\".join(xmind_path.split('\\')[:-1]) + "\\" + excel_name
        # print(excel_path)
        # print("通过切片得到所有分支的内容：", xmind_dict[0]['topic']['topics'])
        self.xmind_to_excel(xmind_dict[0]['topic']['topics'], excel_path)  # 获取用例树转换成Excel
        # self.find_makers(data=xmind_dict[0]['topic']['topics'])
        # print(xmind_dict[0]['topic']['topics'])


if __name__ == '__main__':
    xmind_path_ = r"C:\Users\ymlinf\Downloads\需求.xmind"
    xmind_to_xls().run(xmind_path_)
