# file-integrity-monitor
A python tool that detects file modifications using SHA-256 hashes.
File Integrity Monitoring System
Overview
This Python project detects changes to a selected file by comparing its current SHA-256 hash with a reference hash calculated when monitoring begins.
Features
- Lets the user enter a file path.
- Checks that the file exists using os.path.isfile().
- Calculates a SHA-256 hash using Python's hashlib library.
- Recalculates the hash when the user checks integrity.
- Reports whether the file is unchanged, modified, or missing.
- Reads files in binary chunks, so it can handle files larger than memory-friendly text reads.
Requirements
- Python 3.8 or later
- No third-party packages are required.
How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:
   python file_integrity_monitor.py
4. Enter the path to a file, such as sample.txt (or an absolute path).
5. Choose 1 to check its integrity or 2 to exit.
6. To test change detection, edit the monitored file in another editor and then choose 1 again.
How it works
1. os.path.isfile() verifies that the entered path points to an existing file.
2. calculate_sha256() reads the file in binary mode and updates a SHA-256 digest in chunks.
3. The first digest is saved in reference_hash for the current program session.
4. Each integrity check calculates a fresh digest.
5. If the hashes match, the program reports that no content changes were detected. If they differ, it reports a modification.
Example output
Enter the path of the file to monitor: sample.txt

Reference SHA-256 hash saved for this session:
[64-character SHA-256 hash]

--- File Integrity Monitor ---
1. Check file integrity
2. Exit
Choose an option (1 or 2): 1
Current SHA-256 hash: [64-character SHA-256 hash]
STATUS: File integrity verified. No content changes detected.
After changing the file, the next check should report:
STATUS: WARNING! File contents have been modified.
Important limitation
The reference hash is stored in memory only and is lost when the program exits. This is suitable for a basic demonstration. For persistent monitoring, the reference hash could be stored securely in a separate file or database. If an attacker can change both the monitored file and the reference hash, detection may be bypassed. This program detects content changes; it does not identify who changed the file.
Project files
- file_integrity_monitor.py — complete source code
- README.md — project documentation
- project_report.docx — step-by-step project report with example output screenshots
