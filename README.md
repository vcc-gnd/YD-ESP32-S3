# YD-ESP32-S3
![img](https://github.com/vcc-gnd/YD-ESP32-S3/blob/dc059405ecdec4672ca9a995eaac1b468d704638/IMG/YD-ESP32-S3.PNG)

这就是一个ESP32-S3的最小核心板，使用时乐鑫公司的ESP32-S3模块，配有硬件的usb转串口芯片（CH343）,无线功能专用的LDO电路，不用担心电流（功率）不够用的情况，配有一颗WS2812-RGB LED(注意并不是通过GPIO直接点亮)，RST按键用于外部复位功能，boot按键（配合rst按键可以引导进入bootloard 模式，在复位后可以当做用户按键，就是GPIO0）,你会发现板子有两个TYPE-C接口（一个是直连usb（GPIO19 GPIO20）,另一个是USB转串口的usb口）。
