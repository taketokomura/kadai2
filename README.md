
# kadai2
ロボットシステム学課題2

## 内容
```
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/　のスライドとプログラムを改変し作成しました。
```

# 動作環境
OS:Ubuntu 20.04

## インストール方法
```
$ git clone https://github.com/taketokomura/kadai2.git
$　cd ~/catkin_ws/src
$　cd ~/catkin_ws
$　catkin_make
$　source ~/.bashrc
端末1$　cd catkin_ws/src
端末2.4$ cd catkin_ws/src
端末3$ cd catkin_ws
```

## 実装機能
```
rosrun mypkg count.py　を実行するとフルネームが出力される。
rosrun mypkg twice.py　を実行すると値が一定に増え、その数値と五倍の値が出力される。
```

## 動作法
```
端末1$ roscore
端末2$ chmod +x count.py
端末2$ rosrun mypkg count.py
端末3$ rosnode list
端末3$ rostopic list
端末3$ rostopic echo /count_up
端末4$ chmod +x twice.py
端末4$ rosrun mypkg twice.py
```

## 協力者
・加藤舞子

## youtube URL
https://youtu.be/OIuk5lM4kCg

## 作成者
上田准教授　小村岳都

## ライセンス
BSD 3-Clause License
