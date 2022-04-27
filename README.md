# BJTU SSE Hands Freedom Project

> 因为2022年疫情网课的每日打卡令人无聊，所以写了点代码帮忙打卡
>
> 但发现只能打网页问卷，小程序问卷有空再研究下

## 功能

* 只支持网页打卡（不支持小程序打卡）
* 输入目标网页，自动填充内容
* 根据配置文件输入相应信息
* 填充完毕后，需要手动确认才会提交问卷

## 环境

* python 3.10.4

* selenium 4.1.3

  `pip install selenium`

* PyYAML 6.0

  `pip install PyYaml`

* Google Chrome 100.0.4896 及对应版本驱动

  * 仓库中自带此版本的Chrome驱动
  * 如果报错，则需要自己下载本机对应版本的驱动
    * [驱动下载](https://chromedriver.storage.googleapis.com/index.html)

## 使用

1. 安装环境，下载好本机Google Chrome对应版本的驱动
   * 如何查询Chrome版本：右上角三个点 - 帮助 - 关于 Google Chrome
2. 更改`config.yml`中的网页地址和个人信息
3. 执行`hfp.py`
