# Computer Vision Final Project



### 0 提交规范

每次开始修改前先从分支里pull最新的代码，提交后在`log.md`中标注提交的时间、修改文件和修改内容。



### 1 成员

520030910393 马逸川
520030910396 温海林


### 2 环境配置

```python
git clone # 克隆到本地

# 使用的库
python==3.9.15
pip install torch torchvision 
```

可以先尝试一下有没有push, pull的权限，如果没有的话按照下面的方式添加。

添加push, pull权限的流程:

(以VScode为例。)

先将git添加到环境变量中。

打开VScode终端，按照以下的链接创建SSH key。[链接 ](https://segmentfault.com/a/1190000018826722) 

（不用打开git bash， 直接在终端里面输入就好。）

添加后在终端中输入git remote -v ，如果返回的结果为 git@github.com:Entarochuan/CV_Final_Proj.git 则不用修改。

否则输入:

`git remote set-url origin git@github.com:Entarochuan/CV_Final_Proj.git`

修改链接。

结束后可以随便新建一个文件尝试push, pull操作(记得删掉新建的文件并再push一遍你的删除操作)。



### 3 文件目录

