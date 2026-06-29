import csv
import json

# Read CSV
with open("sample_data/candidate.csv", "r") as file:
    reader = csv.DictReader(file)
    candidate = list(reader)[0]

# Read Resume
with open("sample_data/resume.txt", "r") as file:
    resume = file.read()

# Create Final Candidate Profile
profile = {
    "education": "B.Tech in Computer Science",

"provenance": [
    {"field":"full_name","source":"candidate.csv"},
    {"field":"emails","source":"candidate.csv"},
    {"field":"phones","source":"candidate.csv"},
    {"field":"skills","source":"resume.txt"},
    {"field":"education","source":"resume.txt"}
],

"overall_confidence":0.95,
    "candidate_id": "C001",
    "full_name": candidate["name"],
    "emails": [candidate["email"]],
    "phones": ["+91" + candidate["phone"]],
    "headline": candidate["title"],
    "skills": ["Python", "Java", "SQL"],
    "location": "Hyderabad, India",
    "experience": candidate["current_company"],
    "education": "B.Tech in Computer Science"
}

print(json.dumps(profile, indent=4))
print("\n===== Custom Output =====")

with open("config.json", "r") as file:
    config = json.load(file)

custom_profile = {}

for field in config["fields"]:
    if field in profile:
        custom_profile[field] = profile[field]

print(json.dumps(custom_profile, indent=4))