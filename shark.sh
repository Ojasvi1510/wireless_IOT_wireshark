#!/bin/sh

REQUIRED_PKG="pyshark"
echo Checking for $REQUIRED_PKG: $PKG_OK
if ! (( $(python3 -c "import pyshark" &> /dev/null) )); then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get update
  git clone https://github.com/KimiNewt/pyshark.git
  cd pyshark/src
  python3 setup.py install
  cd ../../
fi

REQUIRED_PKG="python-numpy"
#PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if ! (( $(python3 -c "import numpy" &> /dev/null) )); then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get update
  sudo apt install python-numpy
fi

REQUIRED_PKG="python3-matplotlib"
#echo Checking for $REQUIRED_PKG: $PKG_OK
if ! (( $(python3 -c "import matplotlib" &> /dev/null) )); then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get update
  sudo apt-get install python3-matplotlib
fi

REQUIRED_PKG="tshark"
#PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get update
  sudo add-apt-repository -y ppa:wireshark-dev/stable
  sudo apt install -y tshark
fi

REQUIRED_PKG="python3-pandas"
#PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if ! (( $(python3 -c "import pandas" &> /dev/null) )); then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get update
  sudo apt install python3-pandas
fi


python3 wireshark.py
