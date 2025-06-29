WinGame Performance Reports
===========================

This repository contains compatibility and performance reports for Windows PC games tested on x86 hardware, simulating scenarios relevant for Windows-on-ARM platforms. Testing is conducted using a structured methodology involving system monitoring, crash logging, and automated FPS analysis using Python.

Project Objective
-----------------

To showcase expertise in professional game QA, system diagnostics, and performance benchmarking with an emphasis on tooling, reproducibility, and documentation. This suite is built as a portfolio project targeting roles such as:

- Game QA Engineer
- Performance Analyst
- System Software Tester
- GPU/Driver Debugging Intern
- Game Platform Validation Engineer

Test System
-----------

- CPU: AMD Ryzen 7 5800HS  
- GPU: NVIDIA GTX 1650 (Laptop)  
- RAM: 16 GB DDR4  
- OS: Windows 10 x64  
- Tools Used:
  - PresentMon v2.3.1
  - MSI Afterburner + RTSS
  - Python (pandas, matplotlib, numpy)

Methodology
-----------

1. Record gameplay sessions at two quality presets (Medium and High) for each game.
2. Capture .csv logs using PresentMon for each session.
3. Use Python scripts to analyze FPS, 1% Low, and 0.1% Low performance.
4. Generate plots for each session and save as PNG.
5. Log bugs or crashes with structured markdown reports.
6. Document performance summary in a dedicated markdown file per game.

Tested Games
------------

| Game                               | Settings Tested     | Status      | Report Path                               |
|------------------------------------|----------------------|-------------|-------------------------------------------|
| ARK: Survival Evolved              | Medium / High        | Completed   | ark-survival-evolved/performance.md       |
| Serious Sam Fusion 2017           | To be tested         | Pending     | —                                         |
| Serious Sam: The Random Encounter | To be tested         | Pending     | —                                         |
| Attack on Titan: Wings of Freedom | To be tested         | Pending     | —                                         |
| Sniper Ghost Warrior Contracts 2  | To be tested         | Pending     | —                                         |

Directory Structure
-------------------

WinGame-Performance-Reports/
│
├── ark-survival-evolved/
│ ├── ark_test_medium.csv
│ ├── ark_test_high.csv
│ ├── ark_test_crash.csv
│ ├── medium_settings_fps_plot.png
│ ├── high_settings_fps_plot.png
│ ├── crash_session_fps_plot.png
│ ├── bug1.md
│ └── performance.md
│
├── serious-sam-fusion/
├── serious-sam-random-encounter/
├── attack-on-titan/
└── sniper-ghost-warrior/


Performance Reports
-------------------

Each performance report includes:

- Average FPS, 1% Low, 0.1% Low
- Duration and total frame count
- Line graph (FPS over time)
- Analysis notes and crash observations (if any)

Example (ARK: Survival Evolved):

| Configuration   | Avg FPS | 1% Low | 0.1% Low |
| --------------- | ------- | ------ | -------- |
| Medium Settings | 124.74  | 27.35  | 6.62     |
| High Settings   | 70.90   | 18.41  | 7.03     |
| Crash Session   | 178.00  | 12.20  | 4.83     |



Bug Reports
-----------

All critical crashes or anomalies are documented in `bugN.md` files within the respective game folder.  
Each includes:

- Stack trace or error message
- Trigger conditions
- PresentMon log correlation
- Screenshot (if available)
- Reproducibility rating

Example: `ark-survival-evolved/bug1.md` documents a UE4 TaskGraph crash when joining the same server repeatedly.

Future Goals
------------

- Add support for GPU/CPU temperature extraction from MSI logs
- Automate Markdown report generation from analysis script
- Expand to 10+ AAA and indie games
- Add compatibility testing on ARM hardware or virtualized environments

License
-------

This project is open for review and use in educational or professional QA portfolios. No proprietary data or reverse engineering of game binaries is involved.


