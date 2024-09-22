#!/bin/bash
echo "Create users"
sudo useradd -m iit11
sudo useradd -m iit12
sudo useradd -m iit21
sudo useradd -m iit22
echo "Create groups (-f flag return positive if group exists)"
sudo groupadd -f group_iit1
sudo groupadd -f group_iit2

echo "Adding users to groups"

echo "Add to group_iit1"
sudo useradd -G group_iit1 iit11
sudo useradd -G group_iit1 iit12

echo "Add to group_iit2"
sudo useradd -G group_iit2 iit21
sudo useradd -G group_iit2 iit22
echo "Add root access for user"

sudo usermod -aG sudo iit21

echo "Add user iit3"
sudo useradd -m iit3

echo "Create folders with ACL"

mkdir /home/kl1rik/pzs
mkdir -m 700 /home/kl1rik/pzs/pzs11
mkdir -m 070 /home/kl1rik/pzs/pzs12
mkdir -m 007 /home/kl1rik/pzs/pzs13
mkdir -m 777 /home/kl1rik/pzs/pzs14
mkdir -m 700 /home/kl1rik/pzs/pzs15
sudo chown root /home/kl1rik/pzs/pzs15

echo "Add files"

touch file11

echo "For user"
sudo chmod  400 
sudo chmod  600
sudo chmod  200
sudo chmod  700
sudo chmod  400

echo "For group"
sudo chmod  020
sudo chmod  040
sudo chmod  060
sudo chmod  070

echo "For others"
sudo chmod  002
sudo chmod  004
sudo chmod  006
sudo chmod  007

echo "For all"
sudo chmod  444
sudo chmod  222
sudo chmod  666
sudo chmod  777

echo "Add admin files"
sudo chmod  400
sudo chmod  600
sudo chmod  200
sudo chmod  700

