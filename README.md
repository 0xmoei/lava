# lava points
### install python and screen
```
sudo apt-get update
sudo apt-get install python3.10
sudo apt install screen
```
```
sudo apt install python3-pip
```
### Change ETH RPC & (Wallet: optional)
```
nano eth.py
```
Ctrl+X / Y / Enter

### Run
```
screen -S lava-eth
```
```
python3 eth.py
```
CTRL + A + D

### Change NEAR RPC & (Wallet ID: optional)
```
nano near.py
```
Ctrl+X / Y / Enter

### Run
```
screen -S lava-near
```
```
python3 near.py
```
CTRL + A + D
