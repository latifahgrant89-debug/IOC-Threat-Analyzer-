# IOC-Threat-Analyzer-

ThreatTrace: Threat Intelligence IOC Analyzer

Project Overview
ThreatTrace is a Python project that compares sample indicators of compromise (IOCs) against a reference list to identify potential matches.Indicators of compromise are pieces of information that may help security professionals investigate suspicious activity. Examples include IP addresses, domain names, and file hashes. I developed this project to explore how threat intelligence can be used to support cybersecurity investigations and to strengthen my understanding of Python through a practical application.

Features
Reads indicators from a sample input file.
Compares the collected indicators against a reference threat list.
Identifies unique indicators to reduce duplicate entries.
Displays the total number of indicators analyzed.
Reports the number of unique indicators and matching entries.
Displays the indicators that match the reference list.

Technologies Used
Python 3 — Used to read, organize, and compare indicators.
Text files — Used to store sample indicators and the reference list.

Project Structure
threat-intelligence-ioc-analyzer/
├── main.py
├── sample_iocs.txt
└── threat_list.txt
main.py contains the code used to analyze and compare indicators.
sample_iocs.txt contains the indicators being analyzed.
threat_list.txt contains the reference indicators used for comparison.

How to Run the Project
Download or clone the repository.
Make sure Python 3 is installed.
Open the project folder in VS Code or another Python editor.
Confirm that both text files are in the same directory as main.py.
Run the following command in the terminal:
python3 main.py
The program will compare the indicators in sample_iocs.txt against those in threat_list.txt and display the results.

What I Learned
This project helped me practice file handling, list operations, duplicate removal, and comparing data in Python.
It also introduced me to the role of indicators of compromise in threat intelligence. I gained a better understanding of how security analysts can compare observed indicators with reference data to identify items that may require further investigation.

Limitations
The current version uses a manually created reference list containing illustrative indicators. It does not connect to a live threat intelligence service or independently verify whether an indicator is malicious. A match only means that an indicator appears in both files. It does not prove that the indicator is associated with an active threat.

Future Improvements
Categorize indicators by type, such as IP addresses, domains, and file hashes.
Add validation to help identify incorrectly formatted indicators.
Save matching indicators to a separate output file.
Connect the program to a reputable threat intelligence API.
Add error handling and automated tests.
Generate a more detailed report of the analysis.

