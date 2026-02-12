rm -Recurse speed_indicator.build
rm -Recurse speed_indicator.dist 
python -m nuitka --standalone --windows-console-mode=disable .\speed_indicator.py
$nsisDir = Get-ItemProperty -Path "HKLM:\SOFTWARE\WOW6432Node\NSIS", "HKLM:\SOFTWARE\NSIS" -Name "(default)" -ErrorAction SilentlyContinue | 
           Select-Object -ExpandProperty "(default)" -First 1

if ($nsisDir) {
    $exePath = Join-Path $nsisDir "makensis.exe"

    # 2. Set for CURRENT SESSION only (Temporary)
    $env:MAKE_NSIS = $exePath
    Write-Host "Success: `$env:MAKE_NSIS is set to $env:MAKE_NSIS" -ForegroundColor Green

    # 3. Set for USER scope (Persistent across reboots)
    [Environment]::SetEnvironmentVariable("MAKE_NSIS", $exePath, "User")
    Write-Host "Persistent variable MAKE_NSIS has been saved to User Profile." -ForegroundColor Cyan
} else {
    Write-Error "NSIS registry key not found. Is it installed?"
    $env:MAKE_NSIS = 'makensis.exe'
}
makensis.exe scripts/installer/mysetup.nsi
