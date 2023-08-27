@echo OFF
title 白屏原神检测软件V1

::申请管理员权限，便于启动原神
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"

call .\venv\Scripts\activate
python GenshinStart.py