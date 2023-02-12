# YD-ESP32-S3 Core Board 

###### 简介：

YD-ESP32-S3核心板由源地工作室（VCC-GND Studio）设计，有需要可以浏览www.vcc-gnd.com 获取购买。该设备使用ESP32-S3芯片，可以用于物联网应用的测试原型机也就可以用于实际应用，配有两个usb一个是硬件的usb转串口(CH343P WCH 沁恒)，一个是ESP32-S3的usb口。

![](/IMG/img1.PNG)

本指南将帮助您快速上手 YD-ESP32-S3，并提供该款开发板的详细信息。

YD-ESP32-S3 是一款入门级开发板，搭载 Wi-Fi + Bluetooth® LE 模组 ESP32-S3-WROOM-1。

板上模组的大部分管脚均已引出至开发板两侧排针，开发人员可根据实际需求，轻松通过跳线连接多种外围设备，也可将开发板插在面包板上使用。
![img](/IMG/YD-ESP32-S3.PNG)

1、这就是一个ESP32-S3的最小核心板，使用时乐鑫公司的ESP32-S3模块。
2、无线功能专用的LDO电路，不用担心电流（功率）不够用的情况。
3、配有一颗WS2812-RGB LED(注意并不是通过GPIO直接点亮)。
4、RST按键用于外部复位功能，boot按键（配合rst按键可以引导进入bootloard 模式，在复位后可以当做用户按键，就是GPIO0）。
5、你会发现板子有两个TYPE-C接口（一个是直连usb（GPIO19 GPIO20）,另一个是USB转串口的usb口），配有硬件的usb转串口芯片（CH343）。

###### 硬件介绍：

![](/IMG/img2.png)

| 主要组件                                 | 介绍                                                         |
| :--------------------------------------- | ------------------------------------------------------------ |
| ESP32-S3-WROOM-1                         | ESP32-S3-WROOM-1 是通用型 Wi-Fi + 低功耗蓝牙 MCU 模组，具有丰富的外设接口、强大的神经网络运算能力和信号处理能力，专为人工智能和 AIoT 市场打造。ESP32-S3-WROOM-1  采用 PCB 板载天线。 |
| 5 V to 3.3 V LDO（5 V 转 3.3 V LDO）     | 电源转换器，输入 5 V，输出 3.3 V,电流为1A                    |
| Pin Headers（排针）                      | 所有可用 GPIO 管脚（除 flash 的 SPI 总线）均已引出至开发板的排针。 |
| USB-to-UART Port（USB 转 UART 接口）     | Type-c-USB 接口，可用作开发板的供电接口，可烧录固件至芯片，也可作为通信接口，通过板载 USB 转 UART 桥接器与芯片通信。 |
| Boot Button（Boot 键）                   | 下载按键。按住 **Boot** 键的同时按一下 **Reset** 键进入“固件下载”模式，通过串口下载固件。如果启动完毕可以当做普通的输入按键使用，使用到的IO为GPIO0。 |
| Reset Button（Reset 键）                 | 复位按键。                                                   |
| USB Port（USB 接口）                     | ESP32-S3 USB OTG 接口，支持全速 USB 1.1 标准。ESP32-S3 USB 接口可用作开发板的供电接口，可烧录固件至芯片，可通过 USB 协议与芯片通信，也可用于 JTAG 调试。 |
| USB-to-UART Bridge（USB 转 UART 桥接器） | 芯片为CH343P,厂商为沁恒，网址为http://www.wch-ic.com/ 驱动：http://www.wch-ic.com/products/CH343.html? |
| RGB LED                                  | 可寻址 RGB 发光二极管，由 GPIO48 驱动。型号为WS2812。        |
| PWR LED                                  | 电源指示灯，板子供电后，亮起，不可以程序控制。               |
| TX LED                                   | ESP32-S3的串口TXD线路上的led,当有串口数据发出时，LED闪烁，如果不使用串口功能可以当做GPIO使用,GPIO43 |
| RX LED                                   | ESP32-S3的串口RXD线路上的led,当有串口数据接收时，LED闪烁，如果不使用串口功能可以当做GPIO使用，GPIO44 |



###### 备注:

在板载 ESP32-S3-WROOM-1 模组系列（使用 8 线 SPI flash/PSRAM）的开发板，管脚 GPIO35、GPIO36 和 GPIO37 已用于内部 ESP32-S3 芯片与 SPI flash/PSRAM 之间的通信，外部不可使用。



###### 开始开发应用:
通电前，请确保开发板完好无损。



###### 功能框图：
YD-ESP32-S3 的主要组件和连接方式如下图所示：

![](/IMG/img4.png)



###### 电源选项:
您可从以下三种供电方式中任选其一给开发板供电：

USB 转 UART 接口供电或 ESP32-S3 USB 接口供电（选择其一或同时供电），默认供电方式（推荐）

5V 和 G (GND) 排针供电

3V3 和 G (GND) 排针供电

###### 排针:
下表列出了开发板两侧排针（P1 和 P2）的 名称 和 功能，排针的名称如图 YD-ESP32-S3正面 所示，排针的序号与 开发板原理图 (PDF) 一致。

###### P1

| 序号 | 名称 | 类型  | 功能                                                         |
| ---- | ---- | ----- | ------------------------------------------------------------ |
| 1    | 3V3  | P     | 3.3 V 电源                                                   |
| 2    | 3V3  | P     | 3.3 V 电源                                                   |
| 3    | RST  | I     | EN                                                           |
| 4    | 4    | I/O/T | RTC_GPIO4, GPIO4, TOUCH4, ADC1_CH3                           |
| 5    | 5    | I/O/T | RTC_GPIO5, GPIO5, TOUCH5, ADC1_CH4                           |
| 6    | 6    | I/O/T | RTC_GPIO6, GPIO6, TOUCH6, ADC1_CH5                           |
| 7    | 7    | I/O/T | RTC_GPIO7, GPIO7, TOUCH7, ADC1_CH6                           |
| 8    | 15   | I/O/T | RTC_GPIO15, GPIO15, U0RTS, ADC2_CH4, XTAL_32K_P              |
| 9    | 16   | I/O/T | RTC_GPIO16, GPIO16, U0CTS, ADC2_CH5, XTAL_32K_N              |
| 10   | 17   | I/O/T | RTC_GPIO17, GPIO17, U1TXD, ADC2_CH6                          |
| 11   | 18   | I/O/T | RTC_GPIO18, GPIO18, U1RXD, ADC2_CH7, CLK_OUT3                |
| 12   | 8    | I/O/T | RTC_GPIO8, GPIO8, TOUCH8, ADC1_CH7, SUBSPICS1                |
| 13   | 3    | I/O/T | RTC_GPIO3, GPIO3, TOUCH3, ADC1_CH2                           |
| 14   | 46   | I/O/T | GPIO46                                                       |
| 15   | 9    | I/O/T | RTC_GPIO9, GPIO9, TOUCH9, ADC1_CH8, FSPIHD, SUBSPIHD         |
| 16   | 10   | I/O/T | RTC_GPIO10, GPIO10, TOUCH10, ADC1_CH9, FSPICS0, FSPIIO4, SUBSPICS0 |
| 17   | 11   | I/O/T | RTC_GPIO11, GPIO11, TOUCH11, ADC2_CH0, FSPID, FSPIIO5, SUBSPID |
| 18   | 12   | I/O/T | RTC_GPIO12, GPIO12, TOUCH12, ADC2_CH1, FSPICLK, FSPIIO6, SUBSPICLK |
| 19   | 13   | I/O/T | RTC_GPIO13, GPIO13, TOUCH13, ADC2_CH2, FSPIQ, FSPIIO7, SUBSPIQ |
| 20   | 14   | I/O/T | RTC_GPIO14, GPIO14, TOUCH14, ADC2_CH3, FSPIWP, FSPIDQS, SUBSPIWP |
| 21   | 5V   | P     | 5 V 电源                                                     |
| 22   | G    | G     | 接地                                                         |

###### P2

| 序号 | 名称 | 类型  | 功能                                                  |
| ---- | ---- | ----- | ----------------------------------------------------- |
| 1    | G    | G     | 接地                                                  |
| 2    | TX   | I/O/T | U0TXD, GPIO43, CLK_OUT1                               |
| 3    | RX   | I/O/T | U0RXD, GPIO44, CLK_OUT2                               |
| 4    | 1    | I/O/T | RTC_GPIO1, GPIO1, TOUCH1, ADC1_CH0                    |
| 5    | 2    | I/O/T | RTC_GPIO2, GPIO2, TOUCH2, ADC1_CH1                    |
| 6    | 42   | I/O/T | MTMS, GPIO42                                          |
| 7    | 41   | I/O/T | MTDI, GPIO41, CLK_OUT1                                |
| 8    | 40   | I/O/T | MTDO, GPIO40, CLK_OUT2                                |
| 9    | 39   | I/O/T | MTCK, GPIO39, CLK_OUT3, SUBSPICS1                     |
| 10   | 38   | I/O/T | GPIO38, FSPIWP, SUBSPIWP                              |
| 11   | 37   | I/O/T | SPIDQS, GPIO37, FSPIQ, SUBSPIQ                        |
| 12   | 36   | I/O/T | SPIIO7, GPIO36, FSPICLK, SUBSPICLK                    |
| 13   | 35   | I/O/T | SPIIO6, GPIO35, FSPID, SUBSPID                        |
| 14   | 0    | I/O/T | RTC_GPIO0, GPIO0                                      |
| 15   | 45   | I/O/T | GPIO45                                                |
| 16   | 48   | I/O/T | GPIO48, SPICLK_N, SUBSPICLK_N_DIFF, RGB LED           |
| 17   | 47   | I/O/T | GPIO47, SPICLK_P, SUBSPICLK_P_DIFF                    |
| 18   | 21   | I/O/T | RTC_GPIO21, GPIO21                                    |
| 19   | 20   | I/O/T | RTC_GPIO20, GPIO20, U1CTS, ADC2_CH9, CLK_OUT1, USB_D+ |
| 20   | 19   | I/O/T | RTC_GPIO19, GPIO19, U1RTS, ADC2_CH8, CLK_OUT2, USB_D- |
| 21   | G    | G     | 接地                                                  |
| 22   | G    | G     | 接地                                                  |

P：电源；I：输入；O：输出；T：可设置为高阻。

###### 引脚图：

![](/IMG/img11.jpg)

###### CH340芯片的驱动官方链接：

http://www.wch-ic.com/products/CH340.html?        ENGLISH

https://www.wch.cn/products/CH340.html?from=list     中文

Micropython固件下载：

ESP32-S3的下载擦除工具软件flash_download_tool_3.9.2_0在win下downloard tool。
注意：无需安装解压既用，双击小齿轮标志，选择ESP32-S3，develop，USART，剩下看图片，注意起始地址为0x00，前面打对号。如果不能下载可能是USB转串口驱动没有安好，先处理好驱动问题再来下载。

![](/IMG/img3.png)

注意：

不能用thonny自带的所谓的ESP32下载器给ESP32-S3下载micropython固件(thonny自带的是给esp32下载的，型号并不是esp32-s3  地址也并不是S3的0x00而是ESP32的0x1000)，也不能使用micropython官方下载的带SPRAM固件，下载后也不能正常使用，正确的下载方式是使用乐鑫官方的flash tool下载工具，选择ESP32-S3 串口下载（USART）插入板子的COM端口的usb，选择对应的固件（我们源地自己改编的固件）起始地址是0x00 固件选择前打对号，最好先擦除再下载。
固件是1-开头链接的和固件下载软件是2-开头的链接，注意使用前最好更新一下CH343usb转串口的硬件驱动，注意事项在0-开头的资料链接中，在设备管理器中确认出现有……CH343字样COM才行。

如果下载TASMOTA固件，TASMOTA官方有自己的web下载。

https://tasmota.github.io/docs/

如果你下载自己的固件文件可以使用乐鑫的下载工具。

https://www.espressif.com.cn/en/home

这段文字是ESP32-S3的资料。 基础资料包括（硬件串口CH343驱动，源地版本micropython固件，下载固件的软件、micropython的IDE、原理图尺寸图等）：http://124.222.62.86/yd-data/YD-ESP32-S3/ 

如果计划使用官方的idf-C语言编程详细资料链接（例程就是的API参考）： https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/get-started/index.html 

如果计划使用Ardiuno编程资料链接： https://docs.espressif.com/projects/arduino-esp32/en/latest/getting_started.html#about-arduino-esp32 

如果计划使用micropython语言编程资料链接如下（注意快速入门看ESP32就行）： https://docs.micropython.org/en/latest/esp32/quickref.html
