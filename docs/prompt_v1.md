(.venv) PS C:\Users\Estelle\Documents\GitHub\LLM-Assisted-Multi-Model-SOC-Alert-Triage-Pipeline-Using-Sigma-and-MITRE-ATTACK> python scripts/try_five.py mock mock
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: python  winpwnage.py -u execute -i 9 -p c:\Windows\system32\cmd.exe
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 1332
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC3046
--> verdict: suspicious 0.5 | failed parse: False | tok/s: None | wall s: 0
mock
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: suspicious 0.5 | failed parse: False | tok/s: None | wall s: 0
mock
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: suspicious 0.5 | failed parse: False | tok/s: None | wall s: 0
mock
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: suspicious 0.5 | failed parse: False | tok/s: None | wall s: 0
mock
============================================================
Rule: Windows Shell/Scripting Processes Spawning Suspicious Programs (level: high)
ATT&CK: T1059.005 Visual Basic (tactic: execution); T1059.001 PowerShell (tactic: execution); T1218 System Binary Proxy Execution (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\mshta.exe
RuleName: 
Description: Microsoft (R) HTML Application host
TerminalSessionId: 1
ParentCommandLine: rundll32.exe  url.dll,FileProtocolHandler file:///C:/programdata/calc.hta
Product: Internet Explorer
Company: Microsoft Corporation
ParentProcessId: 3856
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hash
--> verdict: suspicious 0.5 | failed parse: False | tok/s: None | wall s: 0
mock
(.venv) PS C:\Users\Estelle\Documents\GitHub\LLM-Assisted-Multi-Model-SOC-Alert-Triage-Pipeline-Using-Sigma-and-MITRE-ATTACK> python scripts/try_five.py local foundation-sec:8b-instruct
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: python  winpwnage.py -u execute -i 9 -p c:\Windows\system32\cmd.exe
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 1332
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC3046
--> verdict: suspicious 0.7 | failed parse: False | tok/s: 2.0134374743580006 | wall s: 295.9
The alert indicates that rundll32.exe is being executed from a suspicious command line, which includes a Python script 'winpwnage.py' that is attempting to execute a command. The use of rundll32.exe to open a URL from a local temp directory is unusual and could be indicative of an attempt to execute malicious code or perform a stealthy action.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: suspicious 0.8 | failed parse: False | tok/s: 2.5122772719709925 | wall s: 170.7
The alert indicates that rundll32.exe is being used to execute a URL protocol with a potentially malicious file path (calc.exe). The execution is happening from a user's download directory, which is not typical for system processes. The high integrity level and the use of rundll32 for potentially malicious purposes suggest suspicious activity.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: suspicious 0.8 | failed parse: False | tok/s: 2.2162346665935733 | wall s: 177.8
The alert indicates that rundll32.exe is being used to execute calc.exe via the FileProtocolHandler of url.dll, which is unusual and potentially malicious. The execution is taking place from a user's download directory, which is a common tactic for malware to avoid detection.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: suspicious 0.8 | failed parse: False | tok/s: 2.352051110436234 | wall s: 185.3
The alert indicates suspicious Rundll32 activity with a known tactic for stealthy execution. The rundll32.exe is executing a script (calc.hta) from a potentially untrusted directory (programdata), which is a common tactic for malware to avoid detection.
============================================================
Rule: Windows Shell/Scripting Processes Spawning Suspicious Programs (level: high)
ATT&CK: T1059.005 Visual Basic (tactic: execution); T1059.001 PowerShell (tactic: execution); T1218 System Binary Proxy Execution (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\mshta.exe
RuleName: 
Description: Microsoft (R) HTML Application host
TerminalSessionId: 1
ParentCommandLine: rundll32.exe  url.dll,FileProtocolHandler file:///C:/programdata/calc.hta
Product: Internet Explorer
Company: Microsoft Corporation
ParentProcessId: 3856
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hash
--> verdict: suspicious 0.0 | failed parse: True | tok/s: 2.605544903237298 | wall s: 326.0
parse failure
(.venv) PS C:\Users\Estelle\Documents\GitHub\LLM-Assisted-Multi-Model-SOC-Alert-Triage-Pipeline-Using-Sigma-and-MITRE-ATTACK> python scripts/try_five.py local qwen3.5:9b
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: python  winpwnage.py -u execute -i 9 -p c:\Windows\system32\cmd.exe
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 1332
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC3046
--> verdict: likely_malicious 0.95 | failed parse: False | tok/s: 1.8162762059994983 | wall s: 295.5
The alert shows a Python script named 'winpwnage.py' executing from a suspicious directory ('WinPwnage-master') to launch cmd.exe via rundll32, which is a known technique for bypassing application whitelisting and executing arbitrary code. The command line explicitly invokes the rundll32 utility with an ieframe.dll URL handler, consistent with lateral movement or payload execution patterns.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: likely_malicious 0.95 | failed parse: False | tok/s: 2.2354225511259 | wall s: 189.1
The alert shows rundll32.exe being invoked to open a local calculator executable (calc.exe) via the url.dll interface, which is a classic technique for executing code or launching payloads. The process originates from a suspicious directory named 'WinPwnage-master' in the user's Downloads folder, indicating potential compromise or unauthorized execution.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: likely_malicious 0.95 | failed parse: False | tok/s: 2.0465855040848675 | wall s: 191.4
The alert shows rundll32.exe being invoked to execute 'calc.exe' via the FileProtocolHandler, a common technique used by malware to bypass execution restrictions or hide malicious payloads. The process is running from a suspicious directory named 'WinPwnage-master', which strongly suggests an attack vector involving downloaded tools.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: likely_malicious 0.95 | failed parse: False | tok/s: 1.8096899172941328 | wall s: 263.8
The alert shows rundll32.exe being invoked to open a file named 'calc.hta' located in the suspicious 'programdata' directory, which is a common indicator of an HTA-based calculator payload used for lateral movement or persistence. The process was launched from a user's Downloads folder containing 'WinPwnage-master', suggesting a compromised or malicious environment.
============================================================
Rule: Windows Shell/Scripting Processes Spawning Suspicious Programs (level: high)
ATT&CK: T1059.005 Visual Basic (tactic: execution); T1059.001 PowerShell (tactic: execution); T1218 System Binary Proxy Execution (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\mshta.exe
RuleName: 
Description: Microsoft (R) HTML Application host
TerminalSessionId: 1
ParentCommandLine: rundll32.exe  url.dll,FileProtocolHandler file:///C:/programdata/calc.hta
Product: Internet Explorer
Company: Microsoft Corporation
ParentProcessId: 3856
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hash
--> verdict: likely_malicious 0.95 | failed parse: False | tok/s: 2.1242273390306905 | wall s: 243.5
The alert shows mshta.exe executing calc.hta from the ProgramData directory, which is a classic indicator of the 'Calc' malware dropper. The parent process rundll32.exe was used to bypass User Account Control (UAC) by loading the malicious file via the file protocol, and the current directory suggests the payload was downloaded from an external source.
(.venv) PS C:\Users\Estelle\Documents\GitHub\LLM-Assisted-Multi-Model-SOC-Alert-Triage-Pipeline-Using-Sigma-and-MITRE-ATTACK> python scripts/try_five.py local gpt-oss:20b
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: python  winpwnage.py -u execute -i 9 -p c:\Windows\system32\cmd.exe
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 1332
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC3046
--> verdict: likely_malicious 0.8 | failed parse: False | tok/s: 1.5672044783205992 | wall s: 199.3
The process rundll32.exe is executing ieframe.dll with the OpenURL parameter, a known technique for malicious activity. It is launched by a Python script (winpwnage.py), indicating potential exploitation. The combination of rundll32 usage and a suspicious parent process suggests malicious intent.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: likely_malicious 0.8 | failed parse: False | tok/s: 2.1327967185766896 | wall s: 175.4
The process rundll32.exe is executing the url.dll,OpenURL function with a file:// URI pointing to calc.exe, a known technique for malicious execution via rundll32. The parent process is cmd.exe, indicating potential command-line abuse. This pattern matches ATT&CK T1218.011 and is considered suspicious.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: likely_malicious 0.8 | failed parse: False | tok/s: 2.249870862525834 | wall s: 140.9
The alert shows rundll32.exe being invoked with url.dll,FileProtocolHandler to launch calc.exe, a known technique for malicious execution. The parent process is cmd.exe, indicating potential command execution abuse. This pattern matches ATT&CK T1218.011 and is considered suspicious activity.
============================================================
Rule: Potentially Suspicious Rundll32 Activity (level: medium)
ATT&CK: T1218.011 Rundll32 (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\rundll32.exe
RuleName: 
Description: Windows host process (Rundll32)
TerminalSessionId: 1
ParentCommandLine: "C:\Windows\system32\cmd.exe" 
Product: Microsoft® Windows® Operating System
Company: Microsoft Corporation
ParentProcessId: 2936
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hashes: SHA1=892503B20247B341CFD20DDA5FDACFA41527A087,MD5=C648901695E275C8F2AD04B687A68CE2,SHA256=3FA4912EB43FC304652D7B01F118589259861E2D628FA7C86193E5
--> verdict: likely_malicious 0.8 | failed parse: False | tok/s: 2.2298137773599533 | wall s: 163.2
The alert shows rundll32.exe executing a URL protocol handler to launch an HTA file, a known technique for malicious execution. The command originates from cmd.exe and targets a user directory, indicating potential exploitation. This pattern aligns with ATT&CK T1218.011 and is considered high risk.
============================================================
Rule: Windows Shell/Scripting Processes Spawning Suspicious Programs (level: high)
ATT&CK: T1059.005 Visual Basic (tactic: execution); T1059.001 PowerShell (tactic: execution); T1218 System Binary Proxy Execution (tactic: stealth)
Asset criticality: medium
Image: C:\Windows\System32\mshta.exe
RuleName: 
Description: Microsoft (R) HTML Application host
TerminalSessionId: 1
ParentCommandLine: rundll32.exe  url.dll,FileProtocolHandler file:///C:/programdata/calc.hta
Product: Internet Explorer
Company: Microsoft Corporation
ParentProcessId: 3856
LogonGuid: 365ABB72-1596-5CD8-0000-0020103A0100
Hash
--> verdict: likely_malicious 0.85 | failed parse: False | tok/s: 1.88581247310436 | wall s: 211.6
The alert shows mshta.exe executing a .hta file located in a non‑standard directory (C:\programdata). This is a known technique for malicious execution (T1059.005). The parent process is rundll32.exe, a common proxy for stealthy execution. The presence of a custom .hta file in programdata strongly indicates malicious activity.
(.venv) PS C:\Users\Estelle\Documents\GitHub\LLM-Assisted-Multi-Model-SOC-Alert-Triage-Pipeline-Using-Sigma-and-MITRE-ATTACK>   