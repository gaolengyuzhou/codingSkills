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