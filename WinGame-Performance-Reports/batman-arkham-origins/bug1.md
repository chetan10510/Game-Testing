Bug Report: Batman Arkham Origins – Interrogation Glitch

Game: Batman: Arkham Origins  
Settings: Very High  
Duration: ~5 minutes into session  
Platform: Windows 10 ARM, Ryzen 7 5800HS, GTX 1650, 16GB RAM  
Logging Tool: PresentMon  
Overlay: MSI Afterburner (RTSS)  
Evidence: Gameplay recording, CSV log

Description:  
While attempting to interrogate an enemy during early gameplay, pressing the designated interrogation key results in no action. The character remains idle, and the game does not proceed, effectively halting progress. The prompt is visible, but the interaction fails every time.

Reproducibility:  
Yes – restarting the checkpoint and retrying the interaction leads to the same issue.

Artifacts:  
- CSV Log: batman_test_veryhigh.csv  
- Video/Screenshot: bug_interrogation_glitch.mp4

Severity:  
High – Game-breaking bug; player is unable to proceed beyond the affected sequence.

Notes:  
Potentially a script-trigger failure or interaction handler issue. May be triggered due to timing or enemy position mismatch.

