Bug Report: Crash in ARK - High Settings

Game: ARK: Survival Evolved  
Settings: High  
Duration: Approximately 15 minutes  
Platform: Windows 10 ARM, Ryzen 7 5800HS, GTX 1650, 16GB RAM  
Logging Tool: PresentMon  
Overlay: MSI Afterburner (RTSS)  
Crash Detection: Event Viewer

Crash Details:  
Type: APPCRASH  
Fault Module: KERNELBASE.dll  
Engine: Unreal Engine 4 (UE4-ShooterGame)  
Signature:  
Assertion failed: CurrentThreadIfKnown == ENamedThreads::GetThreadIndex(GetCurrentThread())  
File: TaskGraph.cpp  
Line: 1751

Source: Event Viewer  
Log Path: Application Logs → Event ID 1001 → Source: Windows Error Reporting  
Report Folder: C:\ProgramData\Microsoft\Windows\WER\ReportQueue\AppCrash_UE4-ShooterGame_...

Reproducibility:  
Not reproducible on repeated attempts. Occurred once after an extended session on high settings.

Artifacts:  
Log File: ark_test_high.csv  
FPS Graph: high_settings_fps_plot.png  
Screenshot (if available): screenshots/crash2.png

Severity:  
Medium - one-time crash during extended gameplay. Player progress interrupted.

Notes:  
Crash originated in Unreal Engine thread handling. Possibly related to system thread mismatch or long runtime stability. Recommend reviewing engine-level multithreading assertions and validating KERNELBASE stability on target platform.

log:
Log Name:      Application
Source:        Windows Error Reporting
Date:          30-06-2025 01:28:54
Event ID:      1001
Task Category: None
Level:         Information
Keywords:      
User:          NANI\koriv
Computer:      NANI
Description:
Fault bucket , type 0
Event Name: APPCRASH
Response: Not available
Cab Id: 0

Problem signature:
P1: UE4-ShooterGame
P2: 4.5.1.0
P3: 685609db
P4: KERNELBASE.dll
P5: 10.0.26100.4484
P6: 00000000
P7: 00000001
P8: 00000000000C7F9A
P9: ! -CULTURE=en!AssertLog="Assertion failed: CurrentThreadIfKnown == ENamedThreads::GetThreadIndex(GetCurrentThread()) [File:F:\build\LostIsland\Engine\Source\Runtime\Core\Private\Async\TaskGraph.cpp] [Line: 1751] ##"
P10: UE4!D:/SteamLibrary/steamapps/common/ARK/ShooterGame/Binaries/Win64/!Game!0

Attached files:

These files may be available here:
\\?\C:\ProgramData\Microsoft\Windows\WER\ReportQueue\AppCrash_UE4-ShooterGame_d26a77b44c6c442f30ebb9a147ba8d5d2bbc2_00000000_c3cbb449-61ed-4c17-b11f-12b7c5028d60

Analysis symbol: 
Rechecking for solution: 0
Report Id: c3cbb449-61ed-4c17-b11f-12b7c5028d60
Report Status: 4
Hashed bucket: 
Cab Guid: 0
Event Xml:
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Windows Error Reporting" Guid="{0ead09bd-2157-539a-8d6d-c87f95b64d70}" />
    <EventID>1001</EventID>
    <Version>0</Version>
    <Level>4</Level>
    <Task>0</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8000000000000000</Keywords>
    <TimeCreated SystemTime="2025-06-29T19:58:54.1101016Z" />
    <EventRecordID>20885</EventRecordID>
    <Correlation />
    <Execution ProcessID="16928" ThreadID="1936" />
    <Channel>Application</Channel>
    <Computer>NANI</Computer>
    <Security UserID="S-1-5-21-3854236759-473524843-963813587-1016" />
  </System>
  <EventData>
    <Data Name="Bucket">
    </Data>
    <Data Name="BucketType">0</Data>
    <Data Name="EventName">APPCRASH</Data>
    <Data Name="Response">Not available</Data>
    <Data Name="CabId">0</Data>
    <Data Name="P1">UE4-ShooterGame</Data>
    <Data Name="P2">4.5.1.0</Data>
    <Data Name="P3">685609db</Data>
    <Data Name="P4">KERNELBASE.dll</Data>
    <Data Name="P5">10.0.26100.4484</Data>
    <Data Name="P6">00000000</Data>
    <Data Name="P7">00000001</Data>
    <Data Name="P8">00000000000C7F9A</Data>
    <Data Name="P9">! -CULTURE=en!AssertLog="Assertion failed: CurrentThreadIfKnown == ENamedThreads::GetThreadIndex(GetCurrentThread()) [File:F:\build\LostIsland\Engine\Source\Runtime\Core\Private\Async\TaskGraph.cpp] [Line: 1751] ##"</Data>
    <Data Name="P10">UE4!D:/SteamLibrary/steamapps/common/ARK/ShooterGame/Binaries/Win64/!Game!0</Data>
    <Data Name="AttachedFiles">
    </Data>
    <Data Name="StorePath">\\?\C:\ProgramData\Microsoft\Windows\WER\ReportQueue\AppCrash_UE4-ShooterGame_d26a77b44c6c442f30ebb9a147ba8d5d2bbc2_00000000_c3cbb449-61ed-4c17-b11f-12b7c5028d60</Data>
    <Data Name="AnalysisSymbol">
    </Data>
    <Data Name="Rechecking">0</Data>
    <Data Name="ReportId">c3cbb449-61ed-4c17-b11f-12b7c5028d60</Data>
    <Data Name="ReportStatus">4</Data>
    <Data Name="HashedBucket">
    </Data>
    <Data Name="CabGuid">0</Data>
  </EventData>
</Event>