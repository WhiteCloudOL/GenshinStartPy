@echo OFF
title ����ԭ�������V1

::�������ԱȨ�ޣ���������ԭ��
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"

call .\venv\Scripts\activate
python GenshinStart.py