# Python基础教程  


## Python的下载及安装    
1. Python的下载    
[Python官网](https://www.python.org/)    
[Python Windows安装包的下载](https://www.python.org/downloads/windows/)   
[Python相关文档](https://www.python.org/doc/versions/)    
    > 这里我们使用的是Python3.7.2  

2. Python的安装  
- 直接双击Python的可执行程序安装包   
![](https://github.com/AbsolutelyEmpty/Python-core-technology/blob/develop/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_img/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_001.png)  

    **Install Now**  
    > 这是按照默认的模式进行安装，不需要任何的自定义设置  

    **Customize installation**  
    > 自定义安装  根据自己的需要，个性化的安装  

    **Install launcher for all users(recommended)**  
    > 建议性的选项  选择安装Python是针对计算机的所有用户还是针对当前使用的用户  

    **Add Python 3.7 to PATH**  
    > 选择是否配置Python的PATH环境变量  

    如果选择的是傻瓜式的安装，在安装之前最好选择一下是否针对所有的用户安装和配置PATH环境变量的选项，如果自定义安装，这里可以不用选择，在后面自定义安装设置的时候也可以选择的；这里我们进行自定义安装。  

- 进行自定义的设置  
![](https://github.com/AbsolutelyEmpty/Python-core-technology/blob/develop/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_img/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_002.png)  

    > 这里是选择是否安装Documentation（Python的文档文件），pip（Python的包工具），tcl/tk和IDLE（python自带的一个编辑器）开发环境，Python测试，Python启动器；及选择是否为本机的所有用户使用。  

    ![](https://github.com/AbsolutelyEmpty/Python-core-technology/blob/develop/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_img/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_003.png)  
    - Install for all users 所有用户可使用  
    - Associate files with Python 关联PY相关的文件  
    - Create shortcuts for installed applications 创建桌面的快捷方式  
    - Add Python to environment variables 添加系统变量（windows系统）  
    - Precompile standard library 安装预编译标准库  
    - Download debugging symbols 安装调试模块（开发者可选择，运用于开发环境）  
    - Download debug binaries安装用于VS的调试符号（二进制），如果不使用VS作为开发工具，则不用勾选（支持VS2015以上），适用于.NET开发。

- 安装中  
![](https://github.com/AbsolutelyEmpty/Python-core-technology/blob/develop/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_img/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_004.png)  
- 安装完成  
![](https://github.com/AbsolutelyEmpty/Python-core-technology/blob/develop/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_img/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_005.png)  
    >Disable path length limit  
Changes your machine configuration to allow programs,including Python, 
to bypass the 260 character”MAX_PATH” limitation.  

    这是说明你电脑对Python的一些限制，点击它然后确定权限就可以了。  
    假如你像我一样没有确权，要是遇到问题，可以参考下面两篇文章  
    - http://blog.sciencenet.cn/blog-3373964-1101916.html  
    - https://mspoweruser.com/ntfs-260-character-windows-10/  
- 查看Pythonan安装是否成功  
![](https://github.com/AbsolutelyEmpty/Python-core-technology/blob/develop/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_img/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_006.png)   
- 编写第一个Python程序   
![](https://github.com/AbsolutelyEmpty/Python-core-technology/blob/develop/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_img/Python%E7%9A%84%E4%B8%8B%E8%BD%BD%E5%8F%8A%E5%AE%89%E8%A3%85_007.png) 









 



