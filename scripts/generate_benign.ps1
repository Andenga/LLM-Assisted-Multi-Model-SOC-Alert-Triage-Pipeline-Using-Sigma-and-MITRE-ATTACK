# Benign admin-style activity. Safe to run repeatedly.
$cmds = @(
  { whoami /all }, { ipconfig /all }, { systeminfo }, { net user },
  { net localgroup administrators }, { tasklist }, { netstat -ano },
  { reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" },
  { Get-Process }, { Get-Service }, { Get-ScheduledTask },
  { Get-CimInstance Win32_OperatingSystem },
  { certutil -hashfile "$env:windir\system32\notepad.exe" SHA256 }
)
1..5 | ForEach-Object {
  foreach ($c in $cmds) { & $c | Out-Null; Start-Sleep -Seconds (Get-Random -Min 2 -Max 10) }
}

# Legitimate "scary-looking" things admins really do
$enc = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes('Get-Date'))
powershell -NoProfile -EncodedCommand $enc | Out-Null
schtasks /create /tn "LabBenignTask" /tr "notepad.exe" /sc daily /st 09:00 /f | Out-Null
schtasks /delete /tn "LabBenignTask" /f | Out-Null
Invoke-WebRequest https://www.microsoft.com -UseBasicParsing | Out-Null
Compress-Archive -Path "$env:USERPROFILE\Documents" -DestinationPath "$env:TEMP\docs.zip" -Force