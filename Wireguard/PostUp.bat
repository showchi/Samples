@echo off
setlocal

REM Add the IPV4 route through the WireGuard VPN interface
REM route add 0.0.0.0 mask 0.0.0.0 0.0.0.0 METRIC 95 IF 68
netsh interface ipv4 add route 0.0.0.0/0 "wg0" 0.0.0.0 store= active

REM Add the IPV6 route through the WireGuard VPN interface
REM netsh interface ipv6 add route prefix= ::0/0 interface= wg0 metric= 205 store= active
netsh interface ipv6 add route ::0/0 "wg0" store= active

endlocal