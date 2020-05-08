## mitmproxy 的使用
- 当作抓包工具使用，在终端运行 **mitmweb** 并设置代理
- 当需要抓取 https 请求时，可以访问 mitm.it 地址安装证书

#### mitmproxy 版本问题
安装命令 pip3 install mitmproxy  执行 mitmdump 报错，如 PyAsn1UnicodeDecodeError，python环境为 3.6.5，猜测是版本问题，于是卸载
pip3 uninstall mitmproxy 重新安装 pip3 install mitmproxy==3 即可

#### mitmproxy 的两个组件
- mitmdump 命令行， mitmweb web可视化
- 默认启动的端口是：8080，可以使用 -p 指定
- mitmdump -s python脚本   -s 指定脚本来处理截获的数据
> 参考地址：
> 1. https://juejin.im/post/5ac9ea6d518825364001b5b9
> 2. https://segmentfault.com/a/1190000017956646

#### 教程
博客：https://www.cnblogs.com/H4ck3R-XiX/p/12624072.html