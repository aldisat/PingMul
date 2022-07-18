# PingMul

Multiple Ping menggunakan Python

## How to
1. Masukkan ip target pada file `ip_list.txt`
2. Jalankan `python3 pingmul.py`

## Example
- Ip target
```
$ cat ip_list.txt 
google.com
wikipedia.com
gasdasf.com
111.111.111.111
192.168.18.1
192.168.18.257
```
- Running pingmul
```
$ python3 pingmul.py 
 ['google.com', 'wikipedia.com', 'gasdasf.com', '111.111.111.111', '192.168.18.1', '192.168.18.257']  

PING google.com (142.251.12.100): 56 data bytes
64 bytes from 142.251.12.100: icmp_seq=0 ttl=56 time=43.789 ms

--- google.com ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 43.789/43.789/43.789/0.000 ms
0
PING wikipedia.com (103.102.166.226): 56 data bytes
64 bytes from 103.102.166.226: icmp_seq=0 ttl=53 time=19.824 ms

--- wikipedia.com ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 19.824/19.824/19.824/0.000 ms
0
ping: cannot resolve gasdasf.com: Unknown host
17408
PING 111.111.111.111 (111.111.111.111): 56 data bytes

--- 111.111.111.111 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss
512
PING 192.168.18.1 (192.168.18.1): 56 data bytes
64 bytes from 192.168.18.1: icmp_seq=0 ttl=64 time=7.152 ms

--- 192.168.18.1 ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 7.152/7.152/7.152/0.000 ms
0
ping: cannot resolve 192.168.18.257: Unknown host
17408
google.com is up!
wikipedia.com is up!
gasdasf.com is down!
111.111.111.111 is down!
192.168.18.1 is up!
192.168.18.257 is down!
```
