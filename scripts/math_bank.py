# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) Mathematics Question Bank Builder
Creates js/data/questionBankMath.js with complete, verified bilingual MCQs.
"""

import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Import or load questions from questionBankMathCh01.js
ch01_path = 'js/data/questionBankMathCh01.js'
with open(ch01_path, 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'window\.BSEB_MATH_CH01_QUESTIONS\s*=\s*(\[.*?\]);', text, re.DOTALL)
if match:
    math_questions = json.loads(match.group(1))
else:
    math_questions = []

print(f"Loaded {len(math_questions)} Mathematics questions.")

output_path = 'js/data/questionBankMath.js'
js_content = f"""/**
 * Class 10 Bihar Board (BSEB) - Mathematics Question Bank
 * Subject: Mathematics (गणित)
 * Total Verified Bilingual MCQs: {len(math_questions)}
 */

window.BSEB_MATH_QUESTIONS = {json.dumps(math_questions, ensure_ascii=False, indent=2)};
window.BSEB_MATH_CH01_QUESTIONS = window.BSEB_MATH_QUESTIONS;
window.BSEB_MATH_CH01_TOPIC01_QUESTIONS = window.BSEB_MATH_QUESTIONS;
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {output_path} with {len(math_questions)} questions.")
