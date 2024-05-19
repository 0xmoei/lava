# lava points
## install python and screen
```
sudo apt-get update
sudo apt-get install python3.10
sudo apt install screen
sudo apt install git
```
```
sudo apt install python3-pip
```
```
git clone https://github.com/0xmoei/lava
```
## Change ETH RPC & (Wallet: optional)
```
nano eth.py
```
Ctrl+X / Y / Enter

### Run ETH
```
screen -S lava-eth
```
```
python3 eth.py
```
CTRL + A + D

## Change NEAR RPC & (Wallet ID: optional)
```
nano near.py
```
Ctrl+X / Y / Enter

### Run NEAR
```
screen -S lava-near
```
```
python3 near.py
```
CTRL + A + D
