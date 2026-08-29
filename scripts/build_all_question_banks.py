# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) - Master Subject Question Bank Builder
Executes all individual subject builders to generate separate files for all 6 subjects:
1. Mathematics     -> js/data/questionBankMath.js
2. Science         -> js/data/questionBankScience.js
3. Social Science  -> js/data/questionBankSocialScience.js
4. Hindi           -> js/data/questionBankHindi.js
5. Sanskrit        -> js/data/questionBankSanskrit.js
6. English         -> js/data/questionBankEnglish.js
"""

import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

scripts = [
    ('Mathematics', 'scripts/math_bank.py'),
    ('Science', 'scripts/science_bank.py'),
    ('Social Science', 'scripts/social_science_bank.py'),
    ('Hindi', 'scripts/hindi_bank.py'),
    ('Sanskrit', 'scripts/sanskrit_bank.py'),
    ('English', 'scripts/english_bank.py')
]

print("==============================================================")
print("BUILDING SEPARATE QUESTION BANK FILES FOR ALL 6 SUBJECTS")
print("==============================================================")

for subject, script in scripts:
    print(f"\n[Building {subject}] Running {script}...")
    res = subprocess.run([sys.executable, script], capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        print(res.stdout.strip())
    else:
        print(f"ERROR building {subject}: {res.stderr}")

print("\n==============================================================")
print("ALL 6 SUBJECT SEPARATE QUESTION BANK FILES GENERATED SUCCESSFULLY!")
print("==============================================================")
