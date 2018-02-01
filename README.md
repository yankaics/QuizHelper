# QuizHelper
手机答题辅助工具,提取搜狗汪仔答题助手api,无需手机截图OCR,显示搜狗推荐答案及参考/百度搜索结果总数及词频计数,支持冲顶/芝士/西瓜/花椒/一直播
![Screenshots](https://github.com/joanwe/QuizHelper/blob/master/Screenshots.png)
# Tips
1. 安装python3以及pip
2. 安装所需python包

```
pip3 install prettytable  
pip3 install aiohttp
pip3 install bs4
```
3. 安装lxml解析器 [知乎里搜索具体安装方法吧](https://www.zhihu.com/question/30047496/answer/108902875)
4. 终端先转到文件所在目录再输入以下命令

```
python3 QuizHelper.py
```
5. 开始时数字键输入选择答题app

# Update
* 2018.01.26
  - 采用了异步IO(asyncio&aiohttp)的方式并发搜索数据
  - 重构代码模块,修改了词频计数方式
  - 添加了一直播黄金十秒入口
* 2018.01.31
  * 修改了数据获取方式,使搜索结果和词频计数更加精确
  * 修复了推荐答案无法与搜狗同步显示的bug
* 2018.02.02
  * 更新了搜狗json数据的提取方式
  * 修复了因404响应导致程序奔溃的bug

# Next

- 优化算法,通过google获取词频计数


