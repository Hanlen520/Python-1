# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/12 9:40
# FileName: D12_模块__name__.py
# Description: if __name__ == "__main__"
# Question:
#       功能函数一般写完会进行自己测试，执行功能函数
#       如果其他模块调用功能函数模块，调用时也会把功能函数里面的执行函数调用，实际上我们只需要调用功能函数而不调用执行函数部分的代码
#       if __name__ == "__main__"就是为了解决这个问题而生，解决这个问题很简单：
#       只需将功能函数里面的执行函数部分放置在if __name__ == "__main__"模块里即可
#       if __name__ == "__main__":
#           foo()
#       这样做既不影响功能函数的代码测试，也不会在被别的模块调用时执行一些多余的测试代码
# --------------------------------


def foo():
    print("This is foo function")


# foo()
if __name__ == "__main__":
    foo()


# 如果被其他模块调用时，则指的时功能函数模块的文件名：D12_模块__name__
print(__name__)