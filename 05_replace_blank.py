# 面试题5：替换空格
# 此题用C语言实现起来很麻烦，但是python实在太方便了
def replace_blank(str):
    return str.replace(" ", "%20")

if __name__ == '__main__':
    print(replace_blank("We are happy."))