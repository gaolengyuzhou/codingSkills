# 一、开机自启
## 1、创建run_python.sh
```
sudo vi run_python.sh
```
### a.打开串口
```
#!/bin/bash

sudo chmod 777 /dev/ttyACM0
echo "/dev/ttyACM0 chmod done"
# sleep 10
# echo "50,90\r\n" > /dev/ttyACM0

exit 0
```
### b.执行python文件
```
# source /home/xitong/Yolo-Deepsort/yolo36/bin/activate
cd /home/xitong/Yolo-Deepsort/Yolov5_DeepSort_Pytorch/
/home/xitong/Yolo-Deepsort/yolo36/bin/python /home/xitong/Yolo-Deepsort/moter_test.py
```
### c.打开权限
```
sudo chmod 777 run_python.sh
```
## 2、创建run_python.service
```
/etc/systemd/system[Unit]
Description=Run a Custom Script at Startup
After=default.target

[Service]
ExecStart=/home/xitong/run_python.sh

[Install]
WantedBy=default.target
```
### a.打开权限
```
sudo chmod 777 run_python.service
```
### b.移动到service
```
sudo mv run_python.service /etc/systemd/system
```
### c.开启服务
```
systemctl daemon-reload
systemctl enable run_python.service
```
## 3、检验
```
systemctl start rc-local.service  #启动服务
systemctl stop rc-local.service  #暂停服务
systemctl status rc-local.service #查看状态
systemctl daemon-reload # 重新加载自启服务
```
```
systemd-analyze plot > boot.svg
```
# 二、sudo 无密码
>sudo visudo
```
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
xitong ALL=(ALL) NOPASSWD:ALL
```
# 三、开启风扇
## 创建rc.local文件
```
sudo vi /etc/rc.local
```
```
#!/bin/sh
# echo " /etc/rc.local"
sudo sh -c 'echo 180 > /sys/devices/pwm-fan/target_pwm'
echo "target_pwm_fan = 180"

exit 0
```
## 修改rc-local.service
```
sudo vi /lib/systemd/system/rc-local.service
```
```
# 最后添加这两行
[Install]
WantedBy=multi-user.target
Alias=rc-local.service
```
## 软链接到service
```
ln -s /lib/systemd/system/rc.local.service /etc/systemd/system/
```
## 打开权限
```
sudo chmod 777 /lib/systemd/system/rc-local.service
sudo chmod 777 /etc/rc.local
```

# 其他
```
# sudo systemctl isolate multi-user.target # 关闭图形化界面
# sudo systemctl stop todeskd.service # 关闭todesk
```

<video src="/videos/your-video-filename.mp4" autoplay="true" controls="controls" width="800" height="600">
</video>