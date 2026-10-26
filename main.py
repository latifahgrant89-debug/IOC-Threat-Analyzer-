# ThreatTrace - IOC Threat Analyzer

sample_file = "sample_iocs.txt"
threat_file = "threat_list.txt"

# Create empty lists
sample_iocs = []
threat_list = []
unique_iocs = []
matches = []

# Read the sample indicators
file = open(sample_file, "r")

for line in file:
    indicator = line.strip()

    if indicator != "":
        sample_iocs.append(indicator)

file.close()

# Read the reference threat list
file = open(threat_file, "r")

for line in file:
    indicator = line.strip()

    if indicator != "":
        threat_list.append(indicator)

file.close()

# Find unique indicators and matches
for indicator in sample_iocs:

    if indicator not in unique_iocs:
        unique_iocs.append(indicator)

    if indicator in threat_list:
        if indicator not in matches:
            matches.append(indicator)

# shows the report
print("THREATTRACE")
print("------------------------------")
print("Total indicators analyzed:", len(sample_iocs))
print("Unique indicators:", len(unique_iocs))
print("Unique reference-list matches:", len(matches))

print("\nMatching indicators:")

if len(matches) > 0:
    for indicator in matches:
        print(indicator)
else:
    print("No matching indicators found.")

print("\nAnalysis complete.")
