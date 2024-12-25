# 查看电脑的ssh用户名和IP
```
ifconfig | grep inet
```
> 192.168.0.129
```
whoami
```
> xitong
## 最强查看
```
uname -m && cat /etc/*release
```
## ssh登录
```
ssh xitong@192.168.0.129
```

# 使用git下载
```
export GIT_SSL_NO_VERIFY=1
```

# scp传输
```
scp -r Yolov5_DeepSort_Pytorch xitong@192.168.0.129:/home/xitong
```

# 查看文件、文件夹大小
```
ls  -lht
```

# 带权限删除回收站
```
sudo rm -rf ~/.local/share/Trash/Yolov5_DeepSort_Pytorch
```

# 面对新的环境可以使用以下命令了解python环境
```python
#-- coding:UTF-8 --

import pkg_resources
import site


print(site.getsitepackages())

installed_packages = pkg_resources.working_set

installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])

for package_info in installed_packages_list:
    print(package_info)
```

