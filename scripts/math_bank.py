# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) Mathematics Question Bank Builder
Consolidates all Mathematics chapters into js/data/questionBankMath.js:
- Chapter 1: Real Numbers (1,102 MCQs)
- Chapter 2: Polynomials (141 MCQs)
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

math_all = []

# 1. Load Chapter 1
with open('js/data/questionBankMathCh01.js', 'r', encoding='utf-8') as f:
    text1 = f.read()
m1 = re.search(r'window\.BSEB_MATH_CH01_QUESTIONS\s*=\s*(\[.*?\]);', text1, re.DOTALL)
if m1:
    ch1_data = json.loads(m1.group(1))
    math_all.extend(ch1_data)
    print(f"Loaded Chapter 1: {len(ch1_data)} MCQs")

# 2. Load Chapter 2
with open('js/data/questionBankMathCh02.js', 'r', encoding='utf-8') as f:
    text2 = f.read()
m2 = re.search(r'window\.BSEB_MATH_CH02_QUESTIONS\s*=\s*(\[.*?\]);', text2, re.DOTALL)
if m2:
    ch2_data = json.loads(m2.group(1))
    math_all.extend(ch2_data)
    print(f"Loaded Chapter 2: {len(ch2_data)} MCQs")

print(f"Total Combined Mathematics MCQs: {len(math_all)}")

output_path = 'js/data/questionBankMath.js'
js_content = f"""/**
 * Class 10 Bihar Board (BSEB) - Mathematics Complete Question Bank
 * Chapters:
 * - Chapter 1: Real Numbers (वास्तविक संख्याएं)
 * - Chapter 2: Polynomials (बहुपद)
 * Total Verified Bilingual MCQs: {len(math_all)}
 */

window.BSEB_MATH_QUESTIONS = {json.dumps(math_all, ensure_ascii=False, indent=2)};
window.BSEB_MATH_CH01_QUESTIONS = window.BSEB_MATH_QUESTIONS.filter(function(q) {{ return q.chapter_id === 'math_ch_01'; }});
window.BSEB_MATH_CH02_QUESTIONS = window.BSEB_MATH_QUESTIONS.filter(function(q) {{ return q.chapter_id === 'math_ch_02'; }});
window.BSEB_MATH_CH01_TOPIC01_QUESTIONS = window.BSEB_MATH_CH01_QUESTIONS;
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully updated {output_path} with {len(math_all)} total MCQs.")
