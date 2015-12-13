; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=发票助手
AppVersion=2.1
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
Source: "image\*"; DestDir:"{app}\image"
Source: "logs\*"; DestDir:"{app}\logs"
Source: "include\*"; DestDir:"{app}\include"

Source: "tcl\*"; DestDir:"{app}\tcl"
Source: "tk\*"; DestDir:"{app}\tk"

Source: "resources\*"; DestDir:"{app}\resources"
Source: "resources\i18n\*"; DestDir:"{app}\resources\i18n"

Source: "qt4_plugins\accessible\*"; DestDir: "{app}\qt4_plugins\accessible"
Source: "qt4_plugins\codecs\*"; DestDir: "{app}\qt4_plugins\codecs"
Source: "qt4_plugins\graphicssystems\*"; DestDir: "{app}\qt4_plugins\graphicssystems"
Source: "qt4_plugins\iconengines\*"; DestDir: "{app}\qt4_plugins\iconengines"
Source: "qt4_plugins\imageformats\*"; DestDir: "{app}\qt4_plugins\imageformats"
               
Source: "*"; DestDir: "{app}"

[Icons]
Name: "{group}\FaPiaoHelper"; Filename: "{app}\main.exe"
