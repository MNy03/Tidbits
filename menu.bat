@echo off
REM Some shortcuts for basic management of the PC. To be updated when more items become available and are interesting enough
:begin
SET Workingdir="C:\Users\Johan\Documents\Tools\"
for /f %%a in ('hostname') DO (for /f "tokens=3" %%b in ('net statistics Workstation ^|findstr "Stat"') DO set Uptime=%%a up since %%b)
TITLE Workingdir == %Workingdir% and %Uptime%
cd /d %Workingdir%
cls
echo Select a task:
echo =============
echo -
echo 2) Run CMD as admin
echo 3) Boot Wekan (Headless) + chrome
echo 4) Shutdown Wekan (60sec delay)
echo 5) SpaceSniffer
echo 6) ProcessExplorer
echo 7) Tcpvcon
echo 8) Tcpview
echo 9) Boot OpenVAS (Headless)
echo 10) Shutdown OpenVAS(60sec delay)
echo 11) Some system info
echo e) Edit
echo x) eXit
echo -
set /p menu_option=Please pick an option:
goto op%menu_option%
goto begin


REM TODO: Convert all to powershell for more powers.
REM TODO: Also, runas /noprofile /user:jroot doesn't always work. 
REM powershell "Get-PnpDevice | Where-Object {$_.FriendlyName -like '*touchscreen*'} | Disable-PnpDevice -Confirm:$false"
REM powershell "Get-PnpDevice | Where-Object {$_.FriendlyName -like '*touchscreen*'} | Enable-PnpDevice -Confirm:$false"


:ope
notepad "menu.bat"
goto begin

:opx
@exit

:op2 
runas /noprofile /user:jroot cmd
goto begin

:op3
start "" "%Workingdir%Wekan - Boot.lnk"
TIMEOUT /T 90
start "" "C:\Program Files (x86)\SRWare Iron\chrome.exe" http://192.168.56.101
goto begin

:op4
start "" "%Workingdir%Wekan - Shutdown.lnk"
goto begin

:op5
start "" %Workingdir%SpaceSniffer.exe "scan C:\Users\Johan"
goto begin

:op6
start "" %Workingdir%Sysinternals\procexp.exe
goto begin

:op7
start "" %Workingdir%Sysinternals\Tcpvcon.exe
goto begin

:op8
start "" %Workingdir%Sysinternals\Tcpview.exe
goto begin

:op9
start "" "%Workingdir%OpenVAS - Boot.lnk"
goto begin

:op10
start "" "%Workingdir%OpenVAS - Shutdown.lnk"
goto begin

:op11
cls
echo =============
echo Extra info - %Uptime%
echo =============
echo Active IPs:
ipconfig |findstr IPv4
echo Local DNS cache:
ipconfig /displaydns |findstr Name
echo =============
pause
goto begin
