### 1. Enable DangerousScriptExecution
 ```powershell
 # set the Registry Key HKEY_LOCAL_MACHINE\Software\WireGuard\DangerousScriptExecution to DWORD(1) using regedit.

 reg add HKLM\Software\WireGuard /v DangerousScriptExecution /t REG_DWORD /d 1 /f
 ```


### 2.1 Wireguard config

``` wg0.conf
[Interface]
PrivateKey = ADNh4TO45aMJTMeeimZuIgxtFMvjJpFnFSfcYI3rCH8=
Address = 172.16.0.2/32, 2606:4700:110:85b3:b413:d0b3:6fff:1e4c/128
DNS = 1.0.0.1, 2606:4700:4700::1001, 2001:4860:4860::8844, 8.8.4.4
MTU = 1420
PostUp = "path_to_postup.bat"
PreDown = "path_to_predown.bat"
Table = off

[Peer]
PublicKey = bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = 188.114.96.240:939

```

### 2.2 Clash For Windows config
```yaml
proxy-groups:
  - name: Wireguard
    type: select
    interface-name: wg0
    proxies:
      - DIRECT

rules:
- SCRIPT,quic,REJECT
- RULE-SET,Youtube,Wireguard
```

### Get InterfaceIndex(if needed)
```powershell
Get-NetConnectionProfile -Name wg0

Name                     : wg0
InterfaceAlias           : wg0
InterfaceIndex           : 68
NetworkCategory          : Private
DomainAuthenticationKind : None
IPv4Connectivity         : LocalNetwork
IPv6Connectivity         : NoTraffic
```

### IPV4 Route
##### PowerShell
```powershell
# add IPV4 route
powershell -command "$wgInterface = Get-NetConnectionProfile -Name 'wg0'; route add 0.0.0.0 mask 0.0.0.0 0.0.0.0 METRIC 95 IF $wgInterface.InterfaceIndex"
# OR
netsh interface ipv4 add route prefix= 0.0.0.0/0 interface= wg0 0.0.0.0 metrice= 95 store= active

# remove IPV4 route
powershell -command "$wgInterface = Get-NetConnectionProfile -Name 'wg0'; route delete 0.0.0.0 mask 0.0.0.0 0.0.0.0 METRIC 95 IF $wgInterface.InterfaceIndex"
# OR
netsh interface ipv4 delete route prefix= 0.0.0.0/0 interface= wg0
```
##### CMD
```cmd
REM add IPV4 route
route add 0.0.0.0 mask 0.0.0.0 0.0.0.0 METRIC 95 IF 68
REM OR
netsh interface ipv4 add route 0.0.0.0/0 "wg0" 0.0.0.0 store= active

REM remove IPV4 route
route delete 0.0.0.0 mask 0.0.0.0 0.0.0.0 METRIC 95 IF 68
REM OR
netsh interface ipv4 delete route 0.0.0.0/0 "wg0"
```


### IPV6 Route
##### PowerShell
```powershell
# add IPV6 route
powershell -command "$wgInterface = Get-NetConnectionProfile -Name 'wg0'; netsh interface ipv6 add route prefix= ::0/0 interface= $wgInterface.name metric= 205 store= active"

# OR
netsh interface ipv6 add route prefix= ::0/0 interface= wg0 metric= 205 store= active

# remove IPV6 route
powershell -command "$wgInterface = Get-NetConnectionProfile -Name 'wg0'; netsh interface ipv6 delete route prefix= ::0/0 interface= $wgInterface.name"

# OR
netsh interface ipv6 delete route prefix= ::0/0 interface= wg0
```
##### CMD
```cmd
REM add IPV6 route
netsh interface ipv6 add route prefix= ::0/0 interface= wg0 metric= 205 store= active
REM OR
netsh interface ipv6 add route ::0/0 "wg0" store= active

REM remove IPV6 route
netsh interface ipv6 delete route prefix= ::0/0 interface= wg0
REM OR
netsh interface ipv6 delete route ::0/0 "wg0"
```
