#!/bin/bash

#-----------------------------------------------------------------------------#
# Pi Pico Pins
#
# Bash script for Raspberry Pi
#
# File     : picopins.sh
# Source   : https://github.com/RPiSpy/pi-pico
#
# Script to display the Pi Pico pinout scheme
#
# Usage    : Make executable with "chmod +x picopins.sh"
#            Run using "./picopins.sh"
#
# Optional : Copy to bin directory to allow it to be run as a command using
#            "sudo cp picopins.sh /bin/picopins"
#            You can then simply use "picopins" in the terminal
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#echo -e "\033[0m"
echo " "
echo -e " \033[1;31m                                       Raspberry Pi Pico Pinout"
echo " "
echo -e " \033[1;97;1;45m[UART0 TX]\033[1;97;46m[I2C0 SDA]\033[1;105m[ SPI0 RX]\033[1;97;1;42m[   GP0  ]\033[0m \033[0;30;47m[01]\033[0m \033[0;97;42m+--\033[0;30;47m|   |\033[0;97;42m--+\033[0m \033[0;30;47m[40]\033[0m \033[1;97;41m[  VBUS  ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[1;97;1;45m[UART0 RX]\033[1;46m[I2C0 SCL]\033[1;105m[SPI0 CSn]\033[1;97;1;42m[   GP1  ]\033[0m \033[0;30;47m[02]\033[0m \033[0;97;42m|  \033[0;30;47m|___|\033[0;97;42m  |\033[0m \033[0;30;47m[39]\033[0m \033[1;97;41m[  VSYS  ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[0;30;40m[--------]\033[30;40m[--------]\033[1;97;1;40m[   GND  ]\033[0m \033[0;30;47m[03]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[38]\033[0m \033[1;97;40m[  GND   ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SDA]\033[1;105m[SPI0 SCK]\033[1;97;1;42m[   GP2  ]\033[0m \033[0;30;47m[04]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[37]\033[0m \033[1;97;43m[ 3V3_EN ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SCL]\033[1;105m[ SPI0 TX]\033[1;97;1;42m[   GP3  ]\033[0m \033[0;30;47m[05]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[36]\033[0m \033[1;97;41m[3V3(OUT)]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[1;97;1;45m[UART1 TX]\033[1;97;46m[I2C0 SDA]\033[1;105m[ SPI0 RX]\033[1;97;1;42m[   GP4  ]\033[0m \033[0;30;47m[06]\033[0m \033[0;97;42m|    P    |\033[0m \033[0;30;47m[35]\033[0m \033[0;30;40m[--------]\033[1;97;104m[ADC_VREF]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[1;97;1;45m[UART1 RX]\033[1;97;46m[I2C0 SCL]\033[1;105m[SPI0 CSn]\033[1;97;1;42m[   GP5  ]\033[0m \033[0;30;47m[07]\033[0m \033[0;97;42m|    I    |\033[0m \033[0;30;47m[34]\033[0m \033[1;97;42m[  GP28  ]\033[1;97;104m[  ADC2  ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[0;30;40m[--------]\033[30;40m[--------]\033[1;97;1;40m[   GND  ]\033[0m \033[0;30;47m[08]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[33]\033[0m \033[1;97;40m[  GND   ]\033[1;97;104m[  AGND  ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SDA]\033[1;105m[SPI0 SCK]\033[1;97;1;42m[   GP6  ]\033[0m \033[0;30;47m[09]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[32]\033[0m \033[1;97;42m[  GP27  ]\033[1;97;104m[  ADC1  ]\033[1;97;46m[I2C1 SCL]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SCL]\033[1;105m[ SPI0 TX]\033[1;97;1;42m[   GP7  ]\033[0m \033[0;30;47m[10]\033[0m \033[0;97;42m|    P    |\033[0m \033[0;30;47m[31]\033[0m \033[1;97;42m[  GP26  ]\033[1;97;104m[  ADC0  ]\033[1;97;46m[I2C1 SDA]\033[0;30;40m[--------]\033[0m"
echo -e " \033[1;97;1;45m[UART1 TX]\033[1;97;46m[I2C0 SDA]\033[1;105m[ SPI1 RX]\033[1;97;1;42m[   GP8  ]\033[0m \033[0;30;47m[11]\033[0m \033[0;97;42m|    I    |\033[0m \033[0;30;47m[30]\033[0m \033[1;97;43m[  RUN   ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[1;97;1;45m[UART1 RX]\033[1;97;46m[I2C0 SCL]\033[1;105m[SPI1 CSn]\033[1;97;1;42m[   GP9  ]\033[0m \033[0;30;47m[12]\033[0m \033[0;97;42m|    C    |\033[0m \033[0;30;47m[29]\033[0m \033[1;97;42m[  GP22  ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[30;40m[--------]\033[0;30;40m[--------]\033[1;97;1;40m[   GND  ]\033[0m \033[0;30;47m[13]\033[0m \033[0;97;42m|    O    |\033[0m \033[0;30;47m[28]\033[0m \033[1;97;40m[  GND   ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SDA]\033[1;105m[SPI1 SCK]\033[1;97;1;42m[  GP10  ]\033[0m \033[0;30;47m[14]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[27]\033[0m \033[1;97;42m[  GP21  ]\033[0;30;40m[--------]\033[1;97;46m[I2C0 SCL]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SCL]\033[1;105m[ SPI1 TX]\033[1;97;1;42m[  GP11  ]\033[0m \033[0;30;47m[15]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[26]\033[0m \033[1;97;42m[  GP20  ]\033[0;30;40m[--------]\033[1;97;46m[I2C0 SDA]\033[0;30;40m[--------]\033[0m"
echo -e " \033[1;97;1;45m[UART0 TX]\033[1;97;46m[I2C0 SDA]\033[1;105m[ SPI1 RX]\033[1;97;1;42m[  GP12  ]\033[0m \033[0;30;47m[16]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[25]\033[0m \033[1;97;42m[  GP19  ]\033[1;97;105m[SPI0 TX ]\033[1;97;46m[I2C1 SCL]\033[0;30;40m[--------]\033[0m"
echo -e " \033[1;97;1;45m[UART0 RX]\033[1;97;46m[I2C0 SCL]\033[1;105m[SPI1 CSn]\033[1;97;1;42m[  GP13  ]\033[0m \033[0;30;47m[17]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[24]\033[0m \033[1;97;42m[  GP18  ]\033[1;97;105m[SPI0 SCK]\033[1;97;46m[I2C1 SDA]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[1;97;1;40m[   GND  ]\033[0m \033[0;30;47m[18]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[23]\033[0m \033[1;97;40m[  GND   ]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0;30;40m[--------]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SDA]\033[1;105m[SPI1 SCK]\033[1;97;1;42m[  GP14  ]\033[0m \033[0;30;47m[19]\033[0m \033[0;97;42m|         |\033[0m \033[0;30;47m[22]\033[0m \033[1;97;42m[  GP17  ]\033[1;97;105m[SPI0 CSn]\033[1;97;46m[I2C0 SCL]\033[1;97;45m[UART0 RX]\033[0m"
echo -e " \033[0;30;40m[--------]\033[1;97;46m[I2C1 SCL]\033[1;105m[ SPI1 TX]\033[1;97;1;42m[  GP15  ]\033[0m \033[0;30;47m[20]\033[0m \033[0;97;42m|_________|\033[0m \033[0;30;47m[21]\033[0m \033[1;97;42m[  GP16  ]\033[1;97;105m[SPI0 RX ]\033[1;97;46m[I2C0 SDA]\033[1;97;45m[UART0 TX]\033[0m"
echo " "
