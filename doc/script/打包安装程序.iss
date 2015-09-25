; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=发票助手
AppVersion=1.5
DefaultDirName={pf}\FaPiaoHelper
DefaultGroupName=FaPiaoHelper
UninstallDisplayIcon={app}\启动.exe
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output

[Files]
; 主程序
Source: "main.exe"; DestDir: "{app}"
Source: "main.exe.manifest"; DestDir: "{app}"

; 文件夹
Source: "include\*"; DestDir: "{app}\include"
Source: "qt4_plugins\accessible\*"; DestDir: "{app}\qt4_plugins\accessible"
Source: "qt4_plugins\codecs\*"; DestDir: "{app}\qt4_plugins\codecs"
Source: "qt4_plugins\graphicssystems\*"; DestDir: "{app}\qt4_plugins\graphicssystems"
Source: "qt4_plugins\iconengines\*"; DestDir: "{app}\qt4_plugins\iconengines"
Source: "qt4_plugins\imageformats\*"; DestDir: "{app}\qt4_plugins\imageformats"
               
Source: "bz2.pyd"; DestDir: "{app}"
Source: "lxml.etree.pyd"; DestDir: "{app}"
Source: "pyexpat.pyd"; DestDir: "{app}"
Source: "PyQt4.QtCore.pyd"; DestDir: "{app}"
Source: "PyQt4.QtGui.pyd"; DestDir: "{app}"
Source: "python27.dll"; DestDir: "{app}"
Source: "QtCore4.dll"; DestDir: "{app}"
Source: "QtGui4.dll"; DestDir: "{app}"
Source: "QtOpenGL4.dll"; DestDir: "{app}"
Source: "QtSvg4.dll"; DestDir: "{app}"
Source: "QtXml4.dll"; DestDir: "{app}"
Source: "select.pyd"; DestDir: "{app}"
Source: "sip.pyd"; DestDir: "{app}"
Source: "sqlite3.dll"; DestDir: "{app}"
Source: "unicodedata.pyd"; DestDir: "{app}"
Source: "_elementtree.pyd"; DestDir: "{app}"
Source: "_hashlib.pyd"; DestDir: "{app}"
Source: "_socket.pyd"; DestDir: "{app}"
Source: "_sqlite3.pyd"; DestDir: "{app}"
Source: "_ssl.pyd"; DestDir: "{app}"

[Icons]
Name: "{group}\FaPiaoHelper"; Filename: "{app}\main.exe"
