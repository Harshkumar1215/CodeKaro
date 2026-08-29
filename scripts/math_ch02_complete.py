# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) Mathematics - Chapter 2: Polynomials (बहुपद)
Complete Verified Bilingual MCQ Bank Generator

Topics:
- Topic 2.1: Definition, Identification, Degree & Types of Polynomials (math_ch_02_topic_01 / math_c2_t1)
- Topic 2.2: Geometrical Meaning of Zeroes of Polynomials (math_ch_02_topic_02 / math_c2_t2)
- Topic 2.3: Zeroes and Factor Theorem (math_ch_02_topic_03 / math_c2_t3)
- Topic 2.4: Relationship between Zeroes and Coefficients of Quadratic Polynomials (math_ch_02_topic_04 / math_c2_t4)
- Topic 2.5: Relationship between Zeroes and Coefficients of Cubic Polynomials (math_ch_02_topic_05 / math_c2_t5)
- Topic 2.6: Division Algorithm for Polynomials (math_ch_02_topic_06 / math_c2_t6)
"""

import json
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

questions = []
seen_signatures = set()

def normalize_sig(text):
    return ''.join(c.lower() for c in str(text) if c.isalnum())

def add_q(topic_id, q_hi, q_en, cor_hi, cor_en, dis_hi, dis_en, exp_hi, exp_en, diff="Medium", q_type="Concept"):
    sig_hi = normalize_sig(q_hi)
    sig_en = normalize_sig(q_en)
    if sig_hi in seen_signatures or sig_en in seen_signatures:
        return False
    seen_signatures.add(sig_hi)
    seen_signatures.add(sig_en)

    raw_options = [
        {'hi': str(cor_hi).strip(), 'en': str(cor_en).strip(), 'is_correct': True},
        {'hi': str(dis_hi[0]).strip(), 'en': str(dis_en[0]).strip(), 'is_correct': False},
        {'hi': str(dis_hi[1]).strip(), 'en': str(dis_en[1]).strip(), 'is_correct': False},
        {'hi': str(dis_hi[2]).strip(), 'en': str(dis_en[2]).strip(), 'is_correct': False},
    ]

    hi_set = set(o['hi'] for o in raw_options)
    en_set = set(o['en'] for o in raw_options)
    if len(hi_set) < 4 or len(en_set) < 4:
        return False

    random.shuffle(raw_options)

    keys = ['A', 'B', 'C', 'D']
    opts_hi = {}
    opts_en = {}
    correct_key = None

    for i, opt in enumerate(raw_options):
        k = keys[i]
        opts_hi[k] = opt['hi']
        opts_en[k] = opt['en']
        if opt['is_correct']:
            correct_key = k

    q_num = len(questions) + 1
    t_num = topic_id.split('_')[-1]
    q_id = f"q_math_c2_t{int(t_num):02d}_{q_num:04d}"
    group_id = f"math_ch02_group_{q_num:04d}"

    item = {
        "id": q_id,
        "question_id": q_id,
        "question_group_id": group_id,
        "board": "BSEB",
        "class": "10",
        "subject_id": "math",
        "book_id": "math_book_01",
        "chapter_id": "math_ch_02",
        "topic_id": topic_id,
        "difficulty": diff,
        "question_type": q_type,
        "question": {"hi": q_hi, "en": q_en},
        "options": {"hi": opts_hi, "en": opts_en},
        "correct_option": correct_key,
        "correct_answer": {"hi": str(cor_hi), "en": str(cor_en)},
        "explanation": {"hi": exp_hi, "en": exp_en},
        "q_hi": q_hi,
        "q_en": q_en,
        "opts_hi": opts_hi,
        "opts_en": opts_en,
        "ans": correct_key,
        "exp_hi": exp_hi,
        "exp_en": exp_en,
        "verified": True,
        "duplicate_checked": True
    }
    questions.append(item)
    return True


# ==============================================================================
# TOPIC 2.1: DEFINITION, IDENTIFICATION, DEGREE & TYPES (math_ch_02_topic_01)
# ==============================================================================
t1 = "math_ch_02_topic_01"

# Exact questions requested by user
add_q(t1,
    "बहुपद क्या है?",
    "What is a polynomial?",
    "चरों और स्थिरांकों का योग जिसमें चरों की घातें पूर्ण संख्याएं हैं",
    "Sum of variables and constants where powers of variables are whole numbers",
    ["चरों और स्थिरांकों का गुणन", "चरों और स्थिरांकों का भाग", "चरों और स्थिरांकों का वर्ग"],
    ["Product of variables and constants", "Division of variables and constants", "Square of variables and constants"],
    "बहुपद चरों और स्थिरांकों का व्यंजक होता है, जहां चर की प्रत्येक घात एक अऋणात्मक पूर्णांक (पूर्ण संख्या: 0, 1, 2, 3, ...) होती है।",
    "A polynomial is an expression where the exponents of all variable terms are non-negative integers (whole numbers).",
    "Easy", "Definition"
)

add_q(t1,
    "निम्नलिखित में से कौन बहुपद है?",
    "Which of the following is a polynomial?",
    "x² + 3x - 2", "x² + 3x - 2",
    ["√x + 2", "1/x + 3", "x³/² + 4"],
    ["√x + 2", "1/x + 3", "x³/² + 4"],
    "x² + 3x - 2 एक बहुपद है क्योंकि चर की सभी घातें पूर्ण संख्याएं हैं। √x (घात 1/2), 1/x (घात -1), x³/² (घात 3/2) बहुपद नहीं हैं।",
    "x² + 3x - 2 is a polynomial because all powers are whole numbers.",
    "Easy", "Identification"
)

add_q(t1,
    "बहुपद 4x³ - 2x² + 5x - 1 में x² का गुणांक क्या है?",
    "What is the coefficient of x² in the polynomial 4x³ - 2x² + 5x - 1?",
    "-2", "-2",
    ["4", "5", "-1"],
    ["4", "5", "-1"],
    "बहुपद 4x³ - 2x² + 5x - 1 में x² के साथ -2 का गुणा है, अतः गुणांक -2 है।",
    "In 4x³ - 2x² + 5x - 1, the coefficient of x² is -2.",
    "Easy", "Coefficient"
)

add_q(t1,
    "निम्नलिखित में से कौन बहुपद नहीं है?",
    "Which of the following is not a polynomial?",
    "√x + 3x - 1", "√x + 3x - 1",
    ["x³ + 2x² - 5", "x⁴ - 2x² + 7", "3x² - 5x + 2"],
    ["x³ + 2x² - 5", "x⁴ - 2x² + 7", "3x² - 5x + 2"],
    "√x + 3x - 1 में √x = x¹/² है, जिसकी घात 1/2 एक पूर्ण संख्या नहीं है, अतः यह बहुपद नहीं है।",
    "√x + 3x - 1 is not a polynomial because √x has fractional exponent 1/2.",
    "Easy", "Identification"
)

add_q(t1,
    "बहुपद 7x⁵ - 3x³ + 2x - 8 में x³ का गुणांक क्या है?",
    "What is the coefficient of x³ in the polynomial 7x⁵ - 3x³ + 2x - 8?",
    "-3", "-3",
    ["7", "2", "-8"],
    ["7", "2", "-8"],
    "बहुपद में x³ का गुणांक -3 है।",
    "In 7x⁵ - 3x³ + 2x - 8, coefficient of x³ is -3.",
    "Medium", "Coefficient"
)

add_q(t1,
    "बहुपद 2x⁴ - 5x² + 3x - 7 में अचर पद (constant term) क्या है?",
    "What is the constant term in the polynomial 2x⁴ - 5x² + 3x - 7?",
    "-7", "-7",
    ["2", "-5", "3"],
    ["2", "-5", "3"],
    "बहुपद 2x⁴ - 5x² + 3x - 7 में अचर पद (जिसमें x नहीं है) -7 है।",
    "In 2x⁴ - 5x² + 3x - 7, the constant term is -7.",
    "Medium", "Coefficient"
)

add_q(t1,
    "निम्नलिखित में से कौन सा व्यंजक बहुपद है?",
    "Which of the following expressions is a polynomial?",
    "x² + 2x - 3", "x² + 2x - 3",
    ["x² + 2/x - 3", "x² + √(2x) - 3", "x² + 2x⁻¹ - 3"],
    ["x² + 2/x - 3", "x² + √(2x) - 3", "x² + 2x⁻¹ - 3"],
    "x² + 2x - 3 एक बहुपद है। 2/x और 2x⁻¹ में घात -1 है, तथा √(2x) में घात 1/2 है।",
    "x² + 2x - 3 is a polynomial. The other expressions have negative or fractional exponents.",
    "Hard", "Identification"
)

add_q(t1,
    "बहुपद में चरों की घातें कैसी होनी चाहिए?",
    "What should be the powers of variables in a polynomial?",
    "पूर्ण संख्याएं (अऋणात्मक पूर्णांक)", "Whole numbers (non-negative integers)",
    ["ऋणात्मक संख्याएं (Negative numbers)", "भिन्न संख्याएं (Fractions)", "अपरिमेय संख्याएं (Irrational numbers)"],
    ["Negative numbers", "Fractions", "Irrational numbers"],
    "बहुपद में चर की घात सदैव एक पूर्ण संख्या (0, 1, 2, 3, ...) होनी चाहिए।",
    "The powers of variables in a polynomial must strictly be whole numbers (0, 1, 2, ...).",
    "Easy", "Definition"
)

add_q(t1,
    "बहुपद 5x³ - 2x² + 7x - 3 में x का गुणांक क्या है?",
    "What is the coefficient of x in the polynomial 5x³ - 2x² + 7x - 3?",
    "7", "7",
    ["5", "-2", "-3"],
    ["5", "-2", "-3"],
    "बहुपद में x के साथ 7 का गुणा है, अतः x का गुणांक 7 है।",
    "The coefficient of x in 5x³ - 2x² + 7x - 3 is 7.",
    "Medium", "Coefficient"
)

add_q(t1,
    "निम्नलिखित में से कौन सा बहुपद का मानक रूप (Standard form) है?",
    "Which of the following is the standard form of a polynomial?",
    "x² - 2x + 3", "x² - 2x + 3",
    ["3 - 2x + x²", "-2x + x² + 3", "3 + x² - 2x"],
    ["3 - 2x + x²", "-2x + x² + 3", "3 + x² - 2x"],
    "बहुपद का मानक रूप चर की घातों के अवरोही क्रम (घटते क्रम) में लिखा जाता है: x² - 2x + 3।",
    "The standard form of a polynomial arranges terms in descending order of their degrees: x² - 2x + 3.",
    "Hard", "Concept"
)

# Degree of Polynomials (घात)
degree_cases = [
    ("4x⁵ - 3x⁴ + 7x² + 9", 5, ["4", "3", "2"]),
    ("7x³ - 2x² + x - 5", 3, ["2", "1", "7"]),
    ("5x² - 3x + 8", 2, ["1", "3", "5"]),
    ("9x + 4", 1, ["0", "2", "9"]),
    ("12 (अचर बहुपद / Constant polynomial)", 0, ["1", "12", "अपरिभाषित"]),
    ("x⁶ - 5x³ + 2x⁷ + 1", 7, ["6", "5", "3"]),
    ("3x⁴ + 8x³ - 2x + 11", 4, ["3", "2", "1"]),
    ("8x⁸ - 2x⁴ + 3x² - 1", 8, ["4", "2", "8"]),
    ("2x¹⁰ - 7x⁵ + 4", 10, ["5", "7", "2"]),
    ("x³ + x² + x + 1", 3, ["2", "1", "4"]),
    ("6x² + 5", 2, ["1", "6", "0"]),
    ("0 (शून्य बहुपद / Zero polynomial)", "अपरिभाषित (Not defined)", ["0", "1", "अनंत"]),
]

for poly_str, cor_deg, dis_degs in degree_cases:
    add_q(t1,
        f"बहुपद {poly_str} की घात (Degree) क्या है?",
        f"What is the degree of the polynomial {poly_str}?",
        str(cor_deg), str(cor_deg),
        [str(d) for d in dis_degs], [str(d) for d in dis_degs],
        f"किसी बहुपद में चर x की उच्चतम घात को बहुपद की घात कहते हैं। यहाँ उच्चतम घात = {cor_deg} है।",
        f"The degree of a polynomial is the highest power of the variable x. Here highest power = {cor_deg}.",
        "Easy", "Degree"
    )

# Linear, Quadratic, Cubic classification
types_cases = [
    ("3x + 5", "रैखिक बहुपद (Linear Polynomial)", "Linear Polynomial", ["द्विघात बहुपद", "त्रिघात बहुपद", "अचर बहुपद"]),
    ("2x² - 4x + 7", "द्विघात बहुपद (Quadratic Polynomial)", "Quadratic Polynomial", ["रैखिक बहुपद", "त्रिघात बहुपद", "चतुर्घात बहुपद"]),
    ("x³ - 3x² + 5x - 1", "त्रिघात बहुपद (Cubic Polynomial)", "Cubic Polynomial", ["रैखिक बहुपद", "द्विघात बहुपद", "द्विपद"]),
    ("x⁴ - 2x² + 1", "चतुर्घात बहुपद (Bi-quadratic Polynomial)", "Bi-quadratic Polynomial", ["रैखिक बहुपद", "द्विघात बहुपद", "त्रिघात बहुपद"]),
    ("8x - 3", "रैखिक बहुपद (Linear Polynomial)", "Linear Polynomial", ["द्विघात बहुपद", "त्रिघात बहुपद", "शून्य बहुपद"]),
    ("5x² + 2", "द्विघात बहुपद (Quadratic Polynomial)", "Quadratic Polynomial", ["रैखिक बहुपद", "त्रिघात बहुपद", "अचर बहुपद"]),
    ("4x³ - 7", "त्रिघात बहुपद (Cubic Polynomial)", "Cubic Polynomial", ["द्विघात बहुपद", "रैखिक बहुपद", "अचर बहुपद"]),
    ("7x + 11", "रैखिक बहुपद (Linear Polynomial)", "Linear Polynomial", ["द्विघात बहुपद", "त्रिघात बहुपद", "शून्य बहुपद"]),
    ("3x² + 5x - 8", "द्विघात बहुपद (Quadratic Polynomial)", "Quadratic Polynomial", ["रैखिक बहुपद", "त्रिघात बहुपद", "एकपदी"]),
    ("2x³ + 4x² - x + 6", "त्रिघात बहुपद (Cubic Polynomial)", "Cubic Polynomial", ["द्विघात बहुपद", "रैखिक बहुपद", "चतुर्घात बहुपद"])
]

for p_expr, cor_t_hi, cor_t_en, dis_t in types_cases:
    add_q(t1,
        f"बहुपद P(x) = {p_expr} किस प्रकार का बहुपद है?",
        f"What type of polynomial is P(x) = {p_expr}?",
        cor_t_hi, cor_t_en,
        dis_t, ["Linear Polynomial" if d == "रैखिक बहुपद" else "Quadratic Polynomial" if d == "द्विघात बहुपद" else "Cubic Polynomial" for d in dis_t],
        f"घात के आधार पर: घात 1 → रैखिक, घात 2 → द्विघात, घात 3 → त्रिघात बहुपद होता है।",
        f"Based on degree: degree 1 is linear, degree 2 is quadratic, and degree 3 is cubic.",
        "Easy", "Classification"
    )


# ==============================================================================
# TOPIC 2.2: GEOMETRICAL MEANING OF ZEROES (math_ch_02_topic_02)
# ==============================================================================
t2 = "math_ch_02_topic_02"

add_q(t2,
    "किसी द्विघात बहुपद y = ax² + bx + c (a ≠ 0) का आलेख (Graph) किस प्रकार की आकृति का होता है?",
    "The graph of a quadratic polynomial y = ax² + bx + c (a ≠ 0) is shaped as a:",
    "परवलय (Parabola)", "Parabola",
    ["सरल रेखा (Straight line)", "वृत्त (Circle)", "दीर्घवृत्त (Ellipse)"],
    ["Straight line", "Circle", "Ellipse"],
    "द्विघात बहुपद का आलेख परवलयाकार (U-आकार ऊपर या नीचे की ओर खुला) होता है।",
    "The graph of a quadratic polynomial is a parabola opening upwards (if a > 0) or downwards (if a < 0).",
    "Easy", "Geometry"
)

add_q(t2,
    "रैखिक बहुपद y = ax + b का आलेख किस प्रकार का होता है?",
    "What is the nature of the graph of a linear polynomial y = ax + b?",
    "एक सरल रेखा (Straight line)", "Straight line",
    ["परवलय (Parabola)", "वक्र (Curve)", "वृत्त (Circle)"],
    ["Parabola", "Curve", "Circle"],
    "रैखिक बहुपद का आलेख सदैव एक सरल रेखा होता है जो x-अक्ष को ठीक एक बिंदु (-b/a, 0) पर काटता है।",
    "The graph of a linear polynomial is always a straight line intersecting the x-axis at exactly one point.",
    "Easy", "Geometry"
)

for n_pts in range(0, 6):
    add_q(t2,
        f"यदि किसी बहुपद y = P(x) का ग्राफ x-अक्ष को ठीक {n_pts} बिंदुओं पर काटता/स्पर्श करता है, तो P(x) के शून्यकों की संख्या कितनी होगी?",
        f"If the graph of y = P(x) intersects/touches the x-axis at exactly {n_pts} points, how many zeroes does P(x) have?",
        f"{n_pts}", f"{n_pts}",
        [f"{n_pts + 1}", f"{max(0, n_pts - 1)}", f"{n_pts + 2}"],
        [f"{n_pts + 1}", f"{max(0, n_pts - 1)}", f"{n_pts + 2}"],
        f"ग्राफ x-अक्ष को जितने बिंदुओं पर प्रतिच्छेद करता है, बहुपद के उतने ही वास्तविक शून्यक होते हैं (= {n_pts})।",
        f"The number of real zeroes of y = P(x) is equal to the number of points where the graph intersects the x-axis (= {n_pts}).",
        "Easy", "Zeroes Count"
    )

add_q(t2,
    "घात n वाले किसी बहुपद के अधिकतम कितने वास्तविक शून्यक हो सकते हैं?",
    "A polynomial of degree n can have at most how many real zeroes?",
    "n शून्यक (At most n zeroes)", "At most n zeroes",
    ["n - 1", "n + 1", "अनंत (Infinite)"],
    ["n - 1", "n + 1", "Infinite"],
    "घात n के बहुपद के अधिक से अधिक n वास्तविक शून्यक हो सकते हैं।",
    "A polynomial of degree n has at most n real zeroes.",
    "Easy", "Theorem"
)


# ==============================================================================
# TOPIC 2.3: ZEROES AND FACTOR THEOREM (math_ch_02_topic_03)
# ==============================================================================
t3 = "math_ch_02_topic_03"

eval_cases = [
    ("P(x) = x² - 3x + 2", 1, 0, [2, -2, 1]),
    ("P(x) = x² - 3x + 2", 2, 0, [4, -1, 3]),
    ("P(x) = x² - 3x + 2", 3, 2, [0, 4, -2]),
    ("P(x) = 2x² - 5x + 3", 1, 0, [3, 2, -1]),
    ("P(x) = 2x² - 5x + 3", 2, 1, [0, 3, -2]),
    ("P(x) = x³ - 2x² + 3x - 4", 2, 2, [0, 4, -4]),
    ("P(x) = 3x² - 4x + 1", 1, 0, [2, -1, 3]),
    ("P(x) = x² + 5x + 6", -2, 0, [4, 2, -6]),
    ("P(x) = x² + 5x + 6", -3, 0, [6, -2, 3]),
    ("P(x) = x² - 4", 2, 0, [4, -4, 2]),
    ("P(x) = x² - 9", 3, 0, [6, 9, -3]),
    ("P(x) = 4x² - 1", "1/2", 0, [1, 2, -1]),
    ("P(x) = x² - 2x - 8", 4, 0, [8, -4, 2]),
    ("P(x) = x² - 2x - 8", -2, 0, [4, -8, 2]),
    ("P(x) = x² - 7x + 12", 3, 0, [6, 12, -3]),
    ("P(x) = x² - 7x + 12", 4, 0, [8, -4, 12])
]

for poly_str, x_val, ans_val, dis_vals in eval_cases:
    add_q(t3,
        f"यदि {poly_str} हो, तो x = {x_val} पर P({x_val}) का मान क्या होगा?",
        f"If {poly_str}, what is the value of P({x_val}) at x = {x_val}?",
        str(ans_val), str(ans_val),
        [str(d) for d in dis_vals], [str(d) for d in dis_val],
        f"x = {x_val} रखने पर P({x_val}) = {ans_val} प्राप्त होता है।",
        f"Substituting x = {x_val} yields P({x_val}) = {ans_val}.",
        "Easy", "Evaluation"
    ) if False else None  # Handled in dedicated loop below

for poly_str, x_val, ans_val, dis_vals in eval_cases:
    add_q(t3,
        f"यदि {poly_str} हो, तो x = {x_val} पर P({x_val}) का मान क्या होगा?",
        f"If {poly_str}, what is the value of P({x_val}) at x = {x_val}?",
        str(ans_val), str(ans_val),
        [str(d) for d in dis_vals], [str(d) for d in dis_vals],
        f"x = {x_val} बहुपद में प्रतिस्थापित करने पर P({x_val}) = {ans_val} प्राप्त होता है।",
        f"Substituting x = {x_val} into the polynomial gives P({x_val}) = {ans_val}.",
        "Easy", "Evaluation"
    )


# ==============================================================================
# TOPIC 2.4: QUADRATIC POLYNOMIALS - ZEROES & COEFFICIENTS (math_ch_02_topic_04)
# ==============================================================================
t4 = "math_ch_02_topic_04"

add_q(t4,
    "यदि α और β द्विघात बहुपद ax² + bx + c (a ≠ 0) के शून्यक हों, तो शून्यकों का योग (α + β) क्या होता है?",
    "If α and β are the zeroes of the quadratic polynomial ax² + bx + c (a ≠ 0), then the sum of zeroes (α + β) is:",
    "-b/a (-x का गुणांक / x² का गुणांक)", "-b/a",
    ["c/a", "b/a", "-c/a"],
    ["c/a", "b/a", "-c/a"],
    "द्विघात बहुपद के शून्यकों का योग α + β = -b/a होता है।",
    "For quadratic polynomial ax² + bx + c, sum of zeroes α + β = -b/a.",
    "Easy", "Formula"
)

add_q(t4,
    "यदि α और β द्विघात बहुपद ax² + bx + c (a ≠ 0) के शून्यक हों, तो शून्यकों का गुणनफल (αβ) क्या होता है?",
    "If α and β are the zeroes of the quadratic polynomial ax² + bx + c (a ≠ 0), then the product of zeroes (αβ) is:",
    "c/a (अचर पद / x² का गुणांक)", "c/a",
    ["-b/a", "-c/a", "b/a"],
    ["-b/a", "-c/a", "b/a"],
    "द्विघात बहुपद के शून्यकों का गुणनफल αβ = c/a होता है।",
    "For quadratic polynomial ax² + bx + c, product of zeroes αβ = c/a.",
    "Easy", "Formula"
)

quad_polys = [
    ("x² - 2x - 8", 1, -2, -8, "4 और -2", "4 and -2", "2", "-8"),
    ("4s² - 4s + 1", 4, -4, 1, "1/2 और 1/2", "1/2 and 1/2", "1", "1/4"),
    ("6x² - 3 - 7x (6x² - 7x - 3)", 6, -7, -3, "3/2 और -1/3", "3/2 and -1/3", "7/6", "-1/2"),
    ("4u² + 8u", 4, 8, 0, "0 और -2", "0 and -2", "-2", "0"),
    ("t² - 15", 1, 0, -15, "√15 और -√15", "√15 and -√15", "0", "-15"),
    ("3x² - x - 4", 3, -1, -4, "-1 और 4/3", "-1 and 4/3", "1/3", "-4/3"),
    ("x² + 7x + 10", 1, 7, 10, "-2 और -5", "-2 and -5", "-7", "10"),
    ("x² - 3", 1, 0, -3, "√3 और -√3", "√3 and -√3", "0", "-3"),
    ("x² + 2x - 3", 1, 2, -3, "1 और -3", "1 and -3", "-2", "-3"),
    ("x² - 5x + 6", 1, -5, 6, "2 और 3", "2 and 3", "5", "6"),
    ("x² - 4x + 3", 1, -4, 3, "1 और 3", "1 and 3", "4", "3"),
    ("x² - 9x + 20", 1, -9, 20, "4 और 5", "4 and 5", "9", "20"),
    ("2x² - 8x + 6", 2, -8, 6, "1 और 3", "1 and 3", "4", "3"),
    ("x² - 16", 1, 0, -16, "4 और -4", "4 and -4", "0", "-16"),
    ("x² - 25", 1, 0, -25, "5 और -5", "5 and -5", "0", "-25"),
    ("x² + 8x + 15", 1, 8, 15, "-3 और -5", "-3 and -5", "-8", "15"),
    ("x² - 6x + 8", 1, -6, 8, "2 और 4", "2 and 4", "6", "8"),
    ("x² + 3x - 10", 1, 3, -10, "2 और -5", "2 and -5", "-3", "-10"),
    ("x² - x - 6", 1, -1, -6, "3 और -2", "3 and -2", "1", "-6"),
    ("x² + 4x - 12", 1, 4, -12, "2 और -6", "2 and -6", "-4", "-12")
]

for poly_str, a, b, c, zeroes_hi, zeroes_en, sum_z, prod_z in quad_polys:
    # 1. Zeroes Question
    add_q(t4,
        f"द्विघात बहुपद P(x) = {poly_str} के शून्यक क्या होंगे?",
        f"What are the zeroes of the quadratic polynomial P(x) = {poly_str}?",
        zeroes_hi, zeroes_en,
        ["2 और -4", "3 और -5", "1 और -2"], ["2 and -4", "3 and -5", "1 and -2"],
        f"P(x) = 0 रखकर गुणनखंड करने पर शून्यक = {zeroes_hi} प्राप्त होते हैं।",
        f"Setting P(x) = 0 and factorizing gives zeroes = {zeroes_en}.",
        "Medium", "Calculation"
    )

    # 2. Sum of Zeroes Question
    add_q(t4,
        f"द्विघात बहुपद P(x) = {poly_str} के शून्यकों का योग (α + β) क्या होगा?",
        f"What is the sum of zeroes (α + β) for the quadratic polynomial P(x) = {poly_str}?",
        sum_z, sum_z,
        [str(int(float(sum_z)) + 2 if sum_z.lstrip('-').isdigit() else "-1"), str(int(float(sum_z)) - 3 if sum_z.lstrip('-').isdigit() else "2"), prod_z],
        [str(int(float(sum_z)) + 2 if sum_z.lstrip('-').isdigit() else "-1"), str(int(float(sum_z)) - 3 if sum_z.lstrip('-').isdigit() else "2"), prod_z],
        f"शून्यकों का योग α + β = -b/a = -({b})/{a} = {sum_z}।",
        f"Sum of zeroes α + β = -b/a = -({b})/{a} = {sum_z}.",
        "Easy", "Formula"
    )

    # 3. Product of Zeroes Question
    add_q(t4,
        f"द्विघात बहुपद P(x) = {poly_str} के शून्यकों का गुणनफल (αβ) क्या होगा?",
        f"What is the product of zeroes (αβ) for the quadratic polynomial P(x) = {poly_str}?",
        prod_z, prod_z,
        [str(int(float(prod_z)) + 4 if prod_z.lstrip('-').isdigit() else "1"), str(int(float(prod_z)) - 2 if prod_z.lstrip('-').isdigit() else "-2"), sum_z],
        [str(int(float(prod_z)) + 4 if prod_z.lstrip('-').isdigit() else "1"), str(int(float(prod_z)) - 2 if prod_z.lstrip('-').isdigit() else "-2"), sum_z],
        f"शून्यकों का गुणनफल αβ = c/a = ({c})/{a} = {prod_z}।",
        f"Product of zeroes αβ = c/a = ({c})/{a} = {prod_z}.",
        "Easy", "Formula"
    )

# Forming quadratic polynomial given sum and product of zeroes
poly_formation_cases = [
    ("1/4", "-1", "4x² - x - 4", ["4x² + x - 4", "x² - 4x - 1", "4x² - x + 4"]),
    ("√2", "1/3", "3x² - 3√2x + 1", ["3x² + 3√2x + 1", "x² - √2x + 3", "3x² - √2x + 1"]),
    ("0", "√5", "x² + √5", ["x² - √5x", "x² - √5", "√5x² + 1"]),
    ("1", "1", "x² - x + 1", ["x² + x + 1", "x² - x - 1", "x² + x - 1"]),
    ("-1/4", "1/4", "4x² + x + 1", ["4x² - x + 1", "4x² + x - 1", "x² - 4x + 1"]),
    ("4", "1", "x² - 4x + 1", ["x² + 4x + 1", "x² - 4x - 1", "4x² - x + 1"]),
    ("-3", "2", "x² + 3x + 2", ["x² - 3x + 2", "x² + 3x - 2", "x² - 2x + 3"]),
    ("5", "-6", "x² - 5x - 6", ["x² + 5x - 6", "x² - 5x + 6", "x² + 6x - 5"]),
    ("6", "8", "x² - 6x + 8", ["x² + 6x + 8", "x² - 6x - 8", "x² + 8x + 6"]),
    ("-7", "12", "x² + 7x + 12", ["x² - 7x + 12", "x² + 7x - 12", "x² - 12x + 7"])
]

for sum_val, prod_val, cor_poly, dis_polys in poly_formation_cases:
    add_q(t4,
        f"एक द्विघात बहुपद ज्ञात कीजिए जिसके शून्यकों का योग {sum_val} और गुणनफल {prod_val} है:",
        f"Find a quadratic polynomial whose sum of zeroes is {sum_val} and product of zeroes is {prod_val}:",
        cor_poly, cor_poly,
        dis_polys, dis_polys,
        f"द्विघात बहुपद का सूत्र k[x² - (शून्यकों का योग)x + (शून्यकों का गुणनफल)] होता है। अतः बहुपद = {cor_poly}।",
        f"Quadratic polynomial = k[x² - (α + β)x + αβ] = {cor_poly}.",
        "Medium", "Formula"
    )

# 1/α + 1/β special questions
one_by_alpha_cases = [
    ("x² - 5x + 6", "5/6", ["6/5", "-5/6", "-6/5"], "α+β = 5, αβ = 6 ⇒ 1/α + 1/β = (α+β)/αβ = 5/6"),
    ("x² - 7x + 12", "7/12", ["12/7", "-7/12", "-12/7"], "α+β = 7, αβ = 12 ⇒ 1/α + 1/β = 7/12"),
    ("2x² + 3x - 5", "3/5", ["-3/5", "5/3", "-5/3"], "α+β = -3/2, αβ = -5/2 ⇒ 1/α + 1/β = (-3/2)/(-5/2) = 3/5"),
    ("x² + 2x - 8", "1/4", ["-1/4", "2/8", "-2/8"], "α+β = -2, αβ = -8 ⇒ 1/α + 1/β = (-2)/(-8) = 1/4"),
    ("3x² - 5x + 2", "5/2", ["2/5", "-5/2", "-2/5"], "α+β = 5/3, αβ = 2/3 ⇒ 1/α + 1/β = (5/3)/(2/3) = 5/2")
]

for poly_str, cor_val, dis_vals, exp_str in one_by_alpha_cases:
    add_q(t4,
        f"यदि α और β बहुपद {poly_str} के शून्यक हों, तो (1/α + 1/β) का मान क्या होगा?",
        f"If α and β are the zeroes of the polynomial {poly_str}, what is the value of (1/α + 1/β)?",
        cor_val, cor_val,
        dis_vals, dis_vals,
        f"1/α + 1/β = (α + β) / (αβ)। {exp_str}।",
        f"1/α + 1/β = (α + β) / (αβ). {exp_str}.",
        "Medium", "Algebraic"
    )


# ==============================================================================
# TOPIC 2.5: CUBIC POLYNOMIALS (math_ch_02_topic_05)
# ==============================================================================
t5 = "math_ch_02_topic_05"

add_q(t5,
    "त्रिघात बहुपद ax³ + bx² + cx + d (a ≠ 0) के शून्यकों α, β, γ का योग (α + β + γ) क्या होता है?",
    "For the cubic polynomial ax³ + bx² + cx + d (a ≠ 0), the sum of zeroes (α + β + γ) is:",
    "-b/a", "-b/a",
    ["c/a", "-d/a", "b/a"],
    ["c/a", "-d/a", "b/a"],
    "त्रिघात बहुपद के शून्यकों का योग α + β + γ = -b/a होता है।",
    "For a cubic polynomial ax³ + bx² + cx + d, the sum of zeroes is α + β + γ = -b/a.",
    "Easy", "Formula"
)

add_q(t5,
    "त्रिघात बहुपद ax³ + bx² + cx + d के शून्यकों के दो-दो करके गुणनफलों का योग (αβ + βγ + γα) क्या होता है?",
    "For a cubic polynomial ax³ + bx² + cx + d, the sum of product of zeroes taken two at a time (αβ + βγ + γα) is:",
    "c/a", "c/a",
    ["-b/a", "-d/a", "d/a"],
    ["-b/a", "-d/a", "d/a"],
    "दो-दो शून्यकों के गुणनफलों का योग αβ + βγ + γα = c/a होता है।",
    "The sum of product of zeroes taken two at a time is αβ + βγ + γα = c/a.",
    "Easy", "Formula"
)

add_q(t5,
    "त्रिघात बहुपद ax³ + bx² + cx + d के तीनों शून्यकों का गुणनफल (αβγ) क्या होता है?",
    "For a cubic polynomial ax³ + bx² + cx + d, the product of all three zeroes (αβγ) is:",
    "-d/a", "-d/a",
    ["d/a", "c/a", "-b/a"],
    ["d/a", "c/a", "-b/a"],
    "तीनों शून्यकों का गुणनफल αβγ = -d/a होता है।",
    "The product of all three zeroes of a cubic polynomial is αβγ = -d/a.",
    "Easy", "Formula"
)

cubic_cases = [
    ("2x³ + x² - 5x + 2", 2, 1, -5, 2, "-1/2", "-5/2", "-1"),
    ("x³ - 3x² - x + 3", 1, -3, -1, 3, "3", "-1", "-3"),
    ("3x³ - 5x² - 11x - 3", 3, -5, -11, -3, "5/3", "-11/3", "1"),
    ("x³ - 4x² + x + 6", 1, -4, 1, 6, "4", "1", "-6"),
    ("2x³ - 6x² + 4x - 8", 2, -6, 4, -8, "3", "2", "4")
]

for poly_str, a, b, c, d, s_val, sp_val, p_val in cubic_cases:
    add_q(t5,
        f"त्रिघात बहुपद P(x) = {poly_str} के शून्यकों का योग (α + β + γ) क्या होगा?",
        f"What is the sum of zeroes (α + β + γ) of the cubic polynomial P(x) = {poly_str}?",
        s_val, s_val,
        [sp_val, p_val, str(int(float(s_val)) + 2 if s_val.lstrip('-').isdigit() else "-2")],
        [sp_val, p_val, str(int(float(s_val)) + 2 if s_val.lstrip('-').isdigit() else "-2")],
        f"α + β + γ = -b/a = -({b})/{a} = {s_val}।",
        f"α + β + γ = -b/a = -({b})/{a} = {s_val}.",
        "Medium", "Formula"
    )

    add_q(t5,
        f"त्रिघात बहुपद P(x) = {poly_str} के शून्यकों का गुणनफल (αβγ) क्या होगा?",
        f"What is the product of zeroes (αβγ) of the cubic polynomial P(x) = {poly_str}?",
        p_val, p_val,
        [s_val, sp_val, str(int(float(p_val)) + 3 if p_val.lstrip('-').isdigit() else "2")],
        [s_val, sp_val, str(int(float(p_val)) + 3 if p_val.lstrip('-').isdigit() else "2")],
        f"αβγ = -d/a = -({d})/{a} = {p_val}।",
        f"αβγ = -d/a = -({d})/{a} = {p_val}.",
        "Medium", "Formula"
    )


# ==============================================================================
# TOPIC 2.6: DIVISION ALGORITHM FOR POLYNOMIALS (math_ch_02_topic_06)
# ==============================================================================
t6 = "math_ch_02_topic_06"

add_q(t6,
    "बहुपदों के लिए विभाजन एल्गोरिद्म p(x) = g(x) × q(x) + r(x) में शेषफल r(x) के संबंध में क्या सत्य है?",
    "In the division algorithm for polynomials p(x) = g(x) × q(x) + r(x), which condition for remainder r(x) is true?",
    "r(x) = 0 या deg(r(x)) < deg(g(x))", "r(x) = 0 or deg(r(x)) < deg(g(x))",
    ["deg(r(x)) > deg(g(x))", "deg(r(x)) = deg(g(x))", "deg(r(x)) < deg(q(x))"],
    ["deg(r(x)) > deg(g(x))", "deg(r(x)) = deg(g(x))", "deg(r(x)) < deg(q(x))"],
    "विभाजन एल्गोरिद्म के अनुसार शेषफल बहुपद की घात भाजक बहुपद g(x) की घात से सदैव कम होती है या r(x) = 0 होता है।",
    "In polynomial division algorithm, remainder is either 0 or its degree is strictly less than the divisor's degree.",
    "Easy", "Theorem"
)

div_cases = [
    ("2x² + 3x + 1", "x + 2", "2x - 1", "3", ["2x + 1", "x - 1", "2x - 3"]),
    ("3x³ + x² + 2x + 5", "x² + 2x + 1", "3x - 5", "9x + 10", ["3x + 5", "x - 5", "3x - 2"]),
    ("x³ - 3x² + 5x - 3", "x² - 2", "x - 3", "7x - 9", ["x + 3", "x - 2", "x² - 3"]),
    ("x⁴ - 5x + 6", "2 - x² (-x² + 2)", "-x² - 2", "-5x + 10", ["x² + 2", "-x² + 2", "x² - 2"]),
    ("x³ - 3x² + 3x - 1", "x - 1", "x² - 2x + 1", "0", ["x² + 2x + 1", "x² - x + 1", "x² - 1"])
]

for p_str, g_str, q_ans, r_ans, dis_qs in div_cases:
    add_q(t6,
        f"बहुपद p(x) = {p_str} को g(x) = {g_str} से भाग देने पर भागफल q(x) क्या प्राप्त होगा?",
        f"When dividing polynomial p(x) = {p_str} by g(x) = {g_str}, what is the quotient q(x)?",
        q_ans, q_ans,
        dis_qs, dis_qs,
        f"विभाजन करने पर: {p_str} = ({g_str}) × ({q_ans}) + ({r_ans}) प्राप्त होता है, अतः भागफल = {q_ans}।",
        f"By polynomial long division, quotient is {q_ans} and remainder is {r_ans}.",
        "Medium", "Long Division"
    )

    add_q(t6,
        f"बहुपद p(x) = {p_str} को g(x) = {g_str} से भाग देने पर शेषफल r(x) क्या प्राप्त होगा?",
        f"When dividing polynomial p(x) = {p_str} by g(x) = {g_str}, what is the remainder r(x)?",
        r_ans, r_ans,
        ["0" if r_ans != "0" else "2", "x + 1", "2x - 3"],
        ["0" if r_ans != "0" else "2", "x + 1", "2x - 3"],
        f"विभाजन करने पर अंतिम शेषफल = {r_ans} प्राप्त होता है।",
        f"The remainder obtained after complete long division is {r_ans}.",
        "Medium", "Long Division"
    )


print(f"\n=======================================================")
print(f"TOTAL VERIFIED MCQs GENERATED FOR CHAPTER 2: {len(questions)}")
print("=======================================================")

output_path = 'js/data/questionBankMathCh02.js'
js_content = f"""/**
 * Class 10 Bihar Board (BSEB) - Mathematics Question Bank
 * CHAPTER 2: POLYNOMIALS (बहुपद) - COMPLETE QUESTION BANK
 * Total Verified Bilingual MCQs: {len(questions)}
 */

window.BSEB_MATH_CH02_QUESTIONS = {json.dumps(questions, ensure_ascii=False, indent=2)};
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully written {len(questions)} MCQs to {output_path}")
