#!/bin/bash

echo -n "Enter resolution > "
read text
info = cvt $text
sudo xrandr --newmode info