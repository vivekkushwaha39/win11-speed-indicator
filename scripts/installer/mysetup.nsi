; --- Basic Info ---
Name "Win11SpeedIndicator"
OutFile "Win11SISetup.exe"
InstallDir "$PROGRAMFILES64\Win11SpeedIndicator"
RequestExecutionLevel admin ; Required for Program Files access

; --- Interface Settings ---
!include "MUI2.nsh" ; Modern UI
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Section "Install"
    SetOutPath "$INSTDIR"
    
    ; Add all files from your Nuitka .dist folder
    ; Change 'your_script.dist' to your actual folder name
    File /r "..\..\speed_indicator.dist\*.*" 
    
    ; Create Uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
    
    ; Create Start Menu Shortcut
    CreateShortcut "$SMPROGRAMS\Win11SpeedIndicator.lnk" "$INSTDIR\speed_indicator.exe"

    ; register startup
    ; Add to Startup (Registry)
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Run" "Win11SpeedIndicator" "$\"$INSTDIR\speed_indicator.exe$\""

SectionEnd

Section "Uninstall"
    ; Remove files (NSIS requires explicit file/folder deletion)
    Delete "$INSTDIR\uninstall.exe"
    RMDir /r "$INSTDIR"
    
    ; Remove Shortcut
    Delete "$SMPROGRAMS\Win11SpeedIndicator.lnk"
    ; Remove from Startup
    DeleteRegValue HKCU "Software\Microsoft\Windows\CurrentVersion\Run" "Win11SpeedIndicator"

SectionEnd
