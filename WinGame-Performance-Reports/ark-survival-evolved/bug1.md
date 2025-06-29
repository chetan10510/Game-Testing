# Bug Report: UE4 Crash — TaskGraph Assertion Failure

**Game:** ARK: Survival Evolved  
**Platform:** Steam  
**Settings Tested:** Medium / Very High  
**Test System:** Ryzen 7 5800HS, GTX 1650, 16GB RAM  
**Tools Used:** PresentMon v2.3.1, MSI Afterburner  
**Crash Screenshot:** `screenshots/crash1.png`  
**Date:** 2025-06-29

---

##  Crash Summary

- **Crash Type:** Unreal Engine 4 Fatal Error  
- **File:** TaskGraph.cpp  
- **Line:** 1751  
- **Message:**  
Assertion failed: CurrentThreadIfKnown == ENamedThreads::GetThreadIndex(GetCurrentThread())

- **Context:** Occurred while joining the same non-dedicated server (3rd attempt). Host remained online, only game client crashed.

---

##  PresentMon Logs

- `ark_test_medium.csv`
- `ark_test_veryhigh.csv`
- `ark_test_crash.csv`

---

##  Reproduction Steps

1. Launch ARK  
2. Join a non-dedicated multiplayer session  
3. Exit to main menu  
4. Rejoin the same server twice  
5. Crash occurs on 3rd attempt

---

**Severity:**  Critical  
**Reproducibility:**  Yes  
**Suspected Cause:** Engine-side threading issue during multiplayer join handshake
