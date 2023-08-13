@echo off
setlocal

REM Remove the IPV4 route through the WireGuard VPN interface
REM route delete 0.0.0.0 mask 0.0.0.0 0.0.0.0 METRIC 95 IF 68
netsh interface ipv4 delete route 0.0.0.0/0 "wg0"

REM Remove the IPV6 route through the WireGuard VPN interface
netsh interface ipv6 delete route ::0/0 "wg0"

endlocal