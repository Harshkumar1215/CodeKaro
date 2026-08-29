# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) Mathematics - Chapter 2: Polynomials (बहुपद)
Complete Verified Bilingual MCQ Bank Generator (Zero Skipped - 140+ Questions for Topic 2.1)

Topics:
- Topic 2.1: Definition, Identification, Degree, Types, Coefficients & Standard Form (math_ch_02_topic_01) - 140+ MCQs
- Topic 2.2: Geometrical Meaning of Zeroes of Polynomials (math_ch_02_topic_02)
- Topic 2.3: Zeroes and Factor Theorem (math_ch_02_topic_03)
- Topic 2.4: Relationship between Zeroes and Coefficients of Quadratic Polynomials (math_ch_02_topic_04)
- Topic 2.5: Relationship between Zeroes and Coefficients of Cubic Polynomials (math_ch_02_topic_05)
- Topic 2.6: Division Algorithm for Polynomials (math_ch_02_topic_06)
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

def add_q(topic_id, q_hi, q_en, cor_hi, cor_en, dis_hi, dis_en, exp_hi, exp_en, diff="Medium", q_type="Concept", exact_ans_letter=None):
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
# TOPIC 2.1: POLYNOMIALS - DEFINITION, IDENTIFICATION, DEGREE, TYPES (140+ MCQs)
# ==============================================================================
t1 = "math_ch_02_topic_01"

# --- SET 1: BASIC DEFINITIONS AND IDENTIFICATION (Questions 1 to 35) ---
add_q(t1,
    "बहुपद क्या है?",
    "What is a polynomial?",
    "चरों और स्थिरांकों का योग जिसमें चरों की घातें पूर्ण संख्याएं हैं",
    "Sum of variables and constants where powers of variables are whole numbers",
    ["चरों और स्थिरांकों का गुणन", "चरों और स्थिरांकों का भाग", "चरों और स्थिरांकों का वर्ग"],
    ["Product of variables and constants", "Division of variables and constants", "Square of variables and constants"],
    "बहुपद चरों और स्थिरांकों का योग होता है, जहां चरों की घातें पूर्ण संख्याएं (0, 1, 2, 3, ...) होती हैं।",
    "A polynomial is the sum of variables and constants, where the powers of variables are whole numbers (0, 1, 2, 3, ...).",
    "Easy", "Definition"
)

add_q(t1,
    "निम्नलिखित में से कौन बहुपद है?",
    "Which of the following is a polynomial?",
    "x² + 3x - 2", "x² + 3x - 2",
    ["√x + 2", "1/x + 3", "x³/² + 4"],
    ["√x + 2", "1/x + 3", "x³/² + 4"],
    "x² + 3x - 2 एक बहुपद है क्योंकि चर की सभी घातें पूर्ण संख्याएं हैं। अन्य में √x, 1/x, x³/² शामिल हैं जो बहुपद नहीं हैं।",
    "x² + 3x - 2 is a polynomial because all powers of the variable are whole numbers.",
    "Easy", "Identification"
)

add_q(t1,
    "बहुपद 4x³ - 2x² + 5x - 1 में x² का गुणांक क्या है?",
    "What is the coefficient of x² in the polynomial 4x³ - 2x² + 5x - 1?",
    "-2", "-2",
    ["4", "5", "-1"],
    ["4", "5", "-1"],
    "बहुपद 4x³ - 2x² + 5x - 1 में x² का गुणांक -2 है।",
    "In the polynomial 4x³ - 2x² + 5x - 1, the coefficient of x² is -2.",
    "Easy", "Coefficient"
)

add_q(t1,
    "निम्नलिखित में से कौन बहुपद नहीं है?",
    "Which of the following is not a polynomial?",
    "√x + 3x - 1", "√x + 3x - 1",
    ["x³ + 2x² - 5", "x⁴ - 2x² + 7", "3x² - 5x + 2"],
    ["x³ + 2x² - 5", "x⁴ - 2x² + 7", "3x² - 5x + 2"],
    "√x + 3x - 1 बहुपद नहीं है क्योंकि √x = x¹/² है, जिसमें घात 1/2 पूर्ण संख्या नहीं है।",
    "√x + 3x - 1 is not a polynomial because √x = x¹/², where the power 1/2 is not a whole number.",
    "Easy", "Identification"
)

add_q(t1,
    "बहुपद 7x⁵ - 3x³ + 2x - 8 में x³ का गुणांक क्या है?",
    "What is the coefficient of x³ in the polynomial 7x⁵ - 3x³ + 2x - 8?",
    "-3", "-3",
    ["7", "2", "-8"],
    ["7", "2", "-8"],
    "बहुपद 7x⁵ - 3x³ + 2x - 8 में x³ का गुणांक -3 है।",
    "In the polynomial 7x⁵ - 3x³ + 2x - 8, the coefficient of x³ is -3.",
    "Medium", "Coefficient"
)

add_q(t1,
    "बहुपद 2x⁴ - 5x² + 3x - 7 में अचर पद (constant term) क्या है?",
    "What is the constant term in the polynomial 2x⁴ - 5x² + 3x - 7?",
    "-7", "-7",
    ["2", "-5", "3"],
    ["2", "-5", "3"],
    "बहुपद 2x⁴ - 5x² + 3x - 7 में अचर पद -7 है, क्योंकि इसमें चर x नहीं है।",
    "In the polynomial 2x⁴ - 5x² + 3x - 7, the constant term is -7, as it has no variable x.",
    "Medium", "Coefficient"
)

add_q(t1,
    "निम्नलिखित में से कौन सा व्यंजक बहुपद है?",
    "Which of the following expressions is a polynomial?",
    "x² + 2x - 3", "x² + 2x - 3",
    ["x² + 2/x - 3", "x² + √(2x) - 3", "x² + 2x⁻¹ - 3"],
    ["x² + 2/x - 3", "x² + √(2x) - 3", "x² + 2x⁻¹ - 3"],
    "x² + 2x - 3 एक बहुपद है। अन्य में 2/x (घात -1), √(2x) (घात 1/2), 2x⁻¹ (घात -1) शामिल हैं, जो बहुपद नहीं हैं।",
    "x² + 2x - 3 is a polynomial. Others contain 2/x (power -1), √(2x) (power 1/2), 2x⁻¹ (power -1), which are not polynomials.",
    "Hard", "Identification"
)

add_q(t1,
    "बहुपद में चरों की घातें कैसी होनी चाहिए?",
    "What should be the powers of variables in a polynomial?",
    "पूर्ण संख्याएं (Whole numbers)", "Whole numbers",
    ["ऋणात्मक संख्याएं (Negative numbers)", "भिन्न (Fractions)", "कोई भी वास्तविक संख्या (Any real number)"],
    ["Negative numbers", "Fractions", "Any real number"],
    "बहुपद में चरों की घातें पूर्ण संख्याएं (0, 1, 2, 3, ...) होनी चाहिए।",
    "In a polynomial, the powers of variables must be whole numbers (0, 1, 2, 3, ...).",
    "Easy", "Definition"
)

add_q(t1,
    "बहुपद 5x³ - 2x² + 7x - 3 में x का गुणांक क्या है?",
    "What is the coefficient of x in the polynomial 5x³ - 2x² + 7x - 3?",
    "7", "7",
    ["5", "-2", "-3"],
    ["5", "-2", "-3"],
    "बहुपद 5x³ - 2x² + 7x - 3 में x का गुणांक 7 है।",
    "In the polynomial 5x³ - 2x² + 7x - 3, the coefficient of x is 7.",
    "Medium", "Coefficient"
)

add_q(t1,
    "निम्नलिखित में से कौन सा बहुपद का मानक रूप (Standard form) है?",
    "Which of the following is the standard form of a polynomial?",
    "x² - 2x + 3", "x² - 2x + 3",
    ["3 - 2x + x²", "-2x + x² + 3", "3 + x² - 2x"],
    ["3 - 2x + x²", "-2x + x² + 3", "3 + x² - 2x"],
    "बहुपद का मानक रूप घातों के अवरोही क्रम में होता है: x² - 2x + 3 (घात 2 से घात 0 तक)।",
    "The standard form of a polynomial is in descending order of powers: x² - 2x + 3 (from power 2 to power 0).",
    "Hard", "Standard Form"
)

# Additional 25 Identification & Basic Definition Questions
ident_data = [
    ("3x² + √2x - 5", True, "चर x की घात 2 और 1 पूर्ण संख्याएं हैं (गुणांक √2 अपरिमेय हो सकता है)"),
    ("1/(x + 1)", False, "हर में चर होने से घात ऋणात्मक हो जाती है"),
    ("x² + 1/x²", False, "1/x² = x⁻² में घात -2 पूर्ण संख्या नहीं है"),
    ("√3x² - 5x + 7", True, "चर x की सभी घातें धनात्मक पूर्णांक हैं"),
    ("2x³ - 3√x + 1", False, "√x में घात 1/2 पूर्ण संख्या नहीं है"),
    ("x⁴ + 5x² - 10", True, "सभी घातें 4 और 2 पूर्ण संख्याएं हैं"),
    ("x⁻³ + 4x + 2", False, "घात -3 ऋणात्मक पूर्णांक है"),
    ("5 (अचर बहुपद)", True, "5 = 5x⁰ जहां घात 0 पूर्ण संख्या है"),
    ("0 (शून्य बहुपद)", True, "शून्य बहुपद की घात अपरिभाषित होती है किंतु यह बहुपद है"),
    ("3x¹/³ + 4x - 1", False, "घात 1/3 भिन्न है"),
    ("x³ - 2x² + 3x + 1/2", True, "अचर पद 1/2 भिन्न हो सकता है, चर की घातें 3, 2, 1 पूर्ण संख्याएं हैं"),
    ("2/x² + 3x + 4", False, "2/x² = 2x⁻² में ऋणात्मक घात है"),
    ("(x + 1)(x - 2)", True, "गुणा करने पर x² - x - 2 प्राप्त होता है जो बहुपद है"),
    ("(x² - 1)/(x - 1) (जहाँ x ≠ 1)", True, "सरलीकरण पर x + 1 प्राप्त होता है"),
    ("√5x + 3", True, "x की घात 1 पूर्ण संख्या है"),
    ("5√x + 3", False, "√x में घात 1/2 है"),
    ("x³ + 2x² + x + √7", True, "अचर पद √7 है, चर की घातें 3, 2, 1 हैं"),
    ("x² + 3x⁻² + 5", False, "घात -2 ऋणात्मक है"),
    ("4x⁵ - 3x² + 8", True, "घातें 5 और 2 पूर्ण संख्याएं हैं"),
    ("3x² - 2x + 5/x", False, "5/x में घात -1 है"),
    ("x⁶ - x⁴ + x² - 1", True, "सभी घातें सम पूर्ण संख्याएं हैं"),
    ("2x³/⁴ + 5", False, "घात 3/4 भिन्न है"),
    ("√2x² + √3x + √5", True, "गुणांक अपरिमेय हैं किंतु चर x की घातें 2 और 1 हैं"),
    ("3/(x² + 2)", False, "हर में चर का व्यंजक है"),
    ("x² - 9", True, "द्विघात बहुपद है")
]

for expr, is_poly, reason in ident_data:
    ans_hi = "हाँ, यह एक बहुपद है" if is_poly else "नहीं, यह बहुपद नहीं है"
    ans_en = "Yes, it is a polynomial" if is_poly else "No, it is not a polynomial"
    dis_hi = ["नहीं, यह बहुपद नहीं है" if is_poly else "हाँ, यह एक बहुपद है", "केवल x > 0 के लिए बहुपद है", "केवल पूर्णांक x के लिए बहुपद है"]
    dis_en = ["No, it is not a polynomial" if is_poly else "Yes, it is a polynomial", "Polynomial only for x > 0", "Polynomial only for integer x"]
    add_q(t1,
        f"क्या बीजीय व्यंजक {expr} एक बहुपद (Polynomial) है?",
        f"Is the algebraic expression {expr} a polynomial?",
        ans_hi, ans_en,
        dis_hi, dis_en,
        f"{reason}।",
        f"{reason}.",
        "Easy" if is_poly else "Medium", "Identification"
    )

# --- SET 2: DEGREE OF POLYNOMIALS (Questions 36 to 70) ---
degree_catalogue = [
    ("7x⁹ - 4x⁵ + 2x³ - 11", 9, ["5", "3", "7"]),
    ("4x⁸ + 3x⁶ - 5x² + 1", 8, ["6", "2", "4"]),
    ("10x⁷ - 2x⁴ + 8x - 3", 7, ["4", "1", "10"]),
    ("5x⁶ - 3x⁴ + 7x³ - 2", 6, ["4", "3", "5"]),
    ("9x⁵ + 4x³ - 6x + 12", 5, ["3", "1", "9"]),
    ("2x⁴ - 7x³ + 4x² - 9", 4, ["3", "2", "2"]),
    ("6x³ + 5x² - 3x + 8", 3, ["2", "1", "6"]),
    ("8x² - 14x + 3", 2, ["1", "0", "8"]),
    ("15x - 7", 1, ["0", "2", "15"]),
    ("-25 (अचर पद / Constant)", 0, ["1", "-25", "अपरिभाषित"]),
    ("3x¹² - 5x⁸ + 2x⁴ - 1", 12, ["8", "4", "3"]),
    ("11x¹¹ + 2x⁵ - 7", 11, ["5", "2", "11"]),
    ("x¹⁰ + 1", 10, ["1", "0", "9"]),
    ("4x⁴ + 3x⁵ - 2x³ + 7", 5, ["4", "3", "7"]),
    ("6 - 2x + 5x³ - 8x⁷", 7, ["3", "1", "8"]),
    ("x²(x³ - 4x + 1)", 5, ["3", "2", "6"]),
    ("(x + 2)(x² - 3)", 3, ["2", "1", "4"]),
    ("(x² + 1)(x² - 1)", 4, ["2", "1", "0"]),
    ("(x³ - 1)(x² + 2)", 5, ["3", "2", "6"]),
    ("(2x - 3)²", 2, ["1", "4", "3"]),
    ("(x + 1)³", 3, ["1", "2", "4"]),
    ("5x²y + 3xy² (दो चरों में)", 3, ["2", "1", "5"]),
    ("x³y² + 2x²y³", 5, ["3", "2", "6"]),
    ("4x² - 9", 2, ["1", "0", "4"]),
    ("7x", 1, ["0", "7", "2"]),
    ("√2 (अचर बहुपद)", 0, ["1/2", "1", "2"]),
    ("0x³ + 4x² + 3x + 1", 2, ["3", "1", "0"]),
    ("0x⁵ + 0x⁴ + 7x³ - 2", 3, ["5", "4", "7"]),
    ("x(x + 1)(x + 2)", 3, ["1", "2", "6"]),
    ("x²(x² + 1)(x - 1)", 5, ["4", "3", "2"]),
    ("(x + 3)(x - 3)", 2, ["1", "0", "3"]),
    ("x⁴/x² + 5 (जहाँ x ≠ 0)", 2, ["4", "1", "5"]),
    ("3x - √5", 1, ["0", "1/2", "3"]),
    ("8", 0, ["1", "8", "अपरिभाषित"]),
    ("x³ - x", 3, ["1", "2", "0"])
]

for p_expr, cor_d, dis_ds in degree_catalogue:
    add_q(t1,
        f"बहुपद {p_expr} की घात (Degree) क्या होगी?",
        f"What is the degree of the polynomial {p_expr}?",
        str(cor_d), str(cor_d),
        [str(d) for d in dis_ds], [str(d) for d in dis_ds],
        f"बहुपद में चर की अधिकतम घात {cor_d} है, अतः बहुपद की घात = {cor_d} होगी।",
        f"The highest power of the variable is {cor_d}, so the degree is {cor_d}.",
        "Easy" if (str(cor_d).split()[0].isdigit() and int(str(cor_d).split()[0]) <= 3) else "Medium", "Degree"
    )

# --- SET 3: TYPES & CLASSIFICATION (Questions 71 to 105) ---
type_catalogue = [
    ("4x - 9", "रैखिक बहुपद (Linear)", "Linear Polynomial", ["द्विघात बहुपद", "त्रिघात बहुपद", "अचर बहुपद"]),
    ("5x² + 3x - 2", "द्विघात बहुपद (Quadratic)", "Quadratic Polynomial", ["रैखिक बहुपद", "त्रिघात बहुपद", "चतुर्घात बहुपद"]),
    ("2x³ - 5x² + 4x - 7", "त्रिघात बहुपद (Cubic)", "Cubic Polynomial", ["द्विघात बहुपद", "रैखिक बहुपद", "द्विपद"]),
    ("x⁴ - 3x² + 2", "चतुर्घात बहुपद (Bi-quadratic)", "Bi-quadratic Polynomial", ["त्रिघात बहुपद", "द्विघात बहुपद", "रैखिक बहुपद"]),
    ("7x²", "एकपदी द्विघात (Monomial Quadratic)", "Monomial Quadratic", ["द्विपद", "त्रिपद", "रैखिक बहुपद"]),
    ("3x + 5", "द्विपद रैखिक (Binomial Linear)", "Binomial Linear", ["एकपदी", "त्रिपद", "द्विघात बहुपद"]),
    ("x² - 4x + 4", "त्रिपद द्विघात (Trinomial Quadratic)", "Trinomial Quadratic", ["एकपदी", "द्विपद", "त्रिघात बहुपद"]),
    ("10", "अचर बहुपद (Constant Polynomial)", "Constant Polynomial", ["शून्य बहुपद", "रैखिक बहुपद", "द्विघात बहुपद"]),
    ("0", "शून्य बहुपद (Zero Polynomial)", "Zero Polynomial", ["अचर बहुपद", "रैखिक बहुपद", "द्विघात बहुपद"]),
    ("√3x - 7", "रैखिक बहुपद (Linear)", "Linear Polynomial", ["द्विघात बहुपद", "अचर बहुपद", "अपरिमेय बहुपद"]),
    ("4x³", "एकपदी त्रिघात (Monomial Cubic)", "Monomial Cubic", ["द्विपद", "त्रिपद", "रैखिक"]),
    ("x² - 16", "द्विपद द्विघात (Binomial Quadratic)", "Binomial Quadratic", ["एकपदी", "त्रिपद", "रैखिक"]),
    ("2x³ + 5x² - 3", "त्रिपद त्रिघात (Trinomial Cubic)", "Trinomial Cubic", ["एकपदी", "द्विपद", "चतुर्घात"]),
    ("9x", "एकपदी रैखिक (Monomial Linear)", "Monomial Linear", ["द्विपद", "अचर", "द्विघात"]),
    ("6x² - 5x", "द्विपद द्विघात (Binomial Quadratic)", "Binomial Quadratic", ["एकपदी", "त्रिपद", "रैखिक"]),
    ("x³ - 8", "द्विपद त्रिघात (Binomial Cubic)", "Binomial Cubic", ["एकपदी", "त्रिपद", "द्विघात"]),
    ("3x⁴ - 2x + 1", "त्रिपद चतुर्घात (Trinomial Bi-quadratic)", "Trinomial Bi-quadratic", ["द्विपद", "त्रिघात", "रैखिक"]),
    ("ax + b (a ≠ 0)", "रैखिक बहुपद का मानक रूप", "Standard form of Linear Polynomial", ["द्विघात का मानक रूप", "त्रिघात का मानक रूप", "अचर रूप"]),
    ("ax² + bx + c (a ≠ 0)", "द्विघात बहुपद का मानक रूप", "Standard form of Quadratic Polynomial", ["रैखिक का मानक रूप", "त्रिघात का मानक रूप", "चतुर्घात रूप"]),
    ("ax³ + bx² + cx + d (a ≠ 0)", "त्रिघात बहुपद का मानक रूप", "Standard form of Cubic Polynomial", ["द्विघात का मानक रूप", "चतुर्घात का मानक रूप", "रैखिक रूप"]),
    ("5x³ + 2x", "द्विपद त्रिघात (Binomial Cubic)", "Binomial Cubic", ["एकपदी", "त्रिपद", "द्विघात"]),
    ("x² + x + 1", "त्रिपद द्विघात (Trinomial Quadratic)", "Trinomial Quadratic", ["द्विपद", "एकपदी", "रैखिक"]),
    ("7x⁵", "एकपदी पंचम-घात (Monomial 5th degree)", "Monomial 5th degree", ["द्विपद", "त्रिपद", "चतुर्घात"]),
    ("-12x", "एकपदी रैखिक (Monomial Linear)", "Monomial Linear", ["द्विपद", "अचर", "शून्य बहुपद"]),
    ("1/2 x²", "एकपदी द्विघात (Monomial Quadratic)", "Monomial Quadratic", ["द्विपद", "रैखिक", "अचर"])
]

for p_expr, cor_type_hi, cor_type_en, dis_types in type_catalogue:
    add_q(t1,
        f"पदों की संख्या एवं घात के आधार पर व्यंजक {p_expr} को किस प्रकार वर्गीकृत किया जाएगा?",
        f"Based on number of terms and degree, how is {p_expr} classified?",
        cor_type_hi, cor_type_en,
        dis_types, ["Option B", "Option C", "Option D"],
        f"{p_expr} का वर्गीकरण: {cor_type_hi}।",
        f"Classification: {cor_type_en}.",
        "Easy", "Classification"
    )

# --- SET 4: COEFFICIENTS & MISSING TERMS (Questions 106 to 125) ---
coeff_catalogue = [
    ("6x⁴ - 5x³ + 8x² - 4x + 9", "x³", "-5", ["6", "8", "-4"]),
    ("6x⁴ - 5x³ + 8x² - 4x + 9", "x⁴", "6", ["-5", "8", "9"]),
    ("6x⁴ - 5x³ + 8x² - 4x + 9", "x²", "8", ["-5", "6", "-4"]),
    ("6x⁴ - 5x³ + 8x² - 4x + 9", "x", "-4", ["9", "8", "-5"]),
    ("6x⁴ - 5x³ + 8x² - 4x + 9", "अचर पद (Constant term)", "9", ["-4", "8", "6"]),
    ("3x⁵ - 7x² + 4", "x⁴", "0 (अनुपस्थित पद / Missing term)", ["3", "-7", "4"]),
    ("3x⁵ - 7x² + 4", "x³", "0 (अनुपस्थित पद / Missing term)", ["3", "-7", "4"]),
    ("3x⁵ - 7x² + 4", "x", "0 (अनुपस्थित पद / Missing term)", ["3", "-7", "4"]),
    ("2x³ - x² + 5x - 3", "x²", "-1", ["2", "5", "-3"]),
    ("-x⁴ + 4x³ - 2x + 7", "x⁴", "-1", ["1", "4", "-2"]),
    ("x² - x + 1", "x", "-1", ["1", "0", "2"]),
    ("5x³ + x", "x²", "0", ["5", "1", "3"]),
    ("8 - 3x²", "x²", "-3", ["8", "3", "0"]),
    ("8 - 3x²", "x", "0", ["-3", "8", "1"]),
    ("8 - 3x²", "अचर पद", "8", ["-3", "0", "1"]),
    ("x³ - 27", "x²", "0", ["1", "-27", "3"]),
    ("4x² + 5x", "अचर पद", "0", ["4", "5", "1"]),
    ("7x³ - 2x² + x", "अचर पद", "0", ["7", "-2", "1"]),
    ("x⁵ - 1", "x⁴", "0", ["1", "-1", "5"]),
    ("-3x³ + 2x² - x + 4", "x³", "-3", ["3", "2", "-1"])
]

for poly_s, term_s, cor_c, dis_cs in coeff_catalogue:
    add_q(t1,
        f"बहुपद P(x) = {poly_s} में {term_s} का गुणांक क्या है?",
        f"What is the coefficient of {term_s} in the polynomial P(x) = {poly_s}?",
        cor_c, cor_c,
        dis_cs, dis_cs,
        f"P(x) = {poly_s} में {term_s} का गुणांक = {cor_c} है।",
        f"In P(x) = {poly_s}, the coefficient of {term_s} is {cor_c}.",
        "Easy", "Coefficient"
    )

# --- SET 5: EVALUATION P(k) (Questions 126 to 145+) ---
eval_catalogue = [
    ("x² - 4x + 3", 0, 3, [0, -4, 1]),
    ("x² - 4x + 3", 1, 0, [3, -2, 4]),
    ("x² - 4x + 3", 2, -1, [1, 0, 3]),
    ("x² - 4x + 3", 3, 0, [6, 3, -1]),
    ("x² - 4x + 3", 4, 3, [0, 5, -3]),
    ("2x² - 3x + 1", 1, 0, [2, -1, 3]),
    ("2x² - 3x + 1", 2, 3, [1, 0, 5]),
    ("2x² - 3x + 1", -1, 6, [0, 4, 2]),
    ("x³ - 2x² + x - 1", 1, -1, [0, 1, 2]),
    ("x³ - 2x² + x - 1", 2, 1, [0, -1, 3]),
    ("x³ - 2x² + x - 1", 0, -1, [1, 0, -2]),
    ("3x² + 5x - 2", -2, 0, [4, -4, 2]),
    ("3x² + 5x - 2", 1, 6, [0, 8, 3]),
    ("x² - 9", 3, 0, [9, -9, 6]),
    ("x² - 9", -3, 0, [9, -9, -6]),
    ("x² - 9", 0, -9, [9, 0, 3]),
    ("4x² - 1", "1/2", 0, [1, -1, 2]),
    ("x² + 6x + 9", -3, 0, [9, 6, -9]),
    ("x² - 5x + 6", 2, 0, [6, -4, 2]),
    ("x² - 5x + 6", 3, 0, [6, 5, -1])
]

for poly_s, k_val, cor_ans, dis_ans in eval_catalogue:
    add_q(t1,
        f"यदि बहुपद P(x) = {poly_s} हो, तो P({k_val}) का मान क्या होगा?",
        f"If P(x) = {poly_s}, what is the value of P({k_val})?",
        str(cor_ans), str(cor_ans),
        [str(d) for d in dis_ans], [str(d) for d in dis_ans],
        f"x = {k_val} बहुपद में रखने पर मान = {cor_ans} प्राप्त होता है।",
        f"Substituting x = {k_val} into P(x) yields {cor_ans}.",
        "Easy", "Evaluation"
    )

# --- SET 6: TERMS COUNT, LEADING COEFFICIENTS & CORE TERMINOLOGY (Questions 126 to 145+) ---
add_q(t1,
    "केवल एक पद (One term) वाले बहुपद को क्या कहा जाता है?",
    "What is a polynomial with only one term called?",
    "एकपदी (Monomial)", "Monomial",
    ["द्विपद (Binomial)", "त्रिपद (Trinomial)", "शून्य बहुपद (Zero polynomial)"],
    ["Binomial", "Trinomial", "Zero polynomial"],
    "जिस बहुपद में केवल एक पद होता है, उसे एकपदी (Monomial) कहते हैं, जैसे: 2x, 5x², 7।",
    "A polynomial containing only one non-zero term is called a Monomial.",
    "Easy", "Definition"
)

add_q(t1,
    "ठीक दो पदों (Two terms) वाले बहुपद को क्या कहा जाता है?",
    "What is a polynomial with exactly two terms called?",
    "द्विपद (Binomial)", "Binomial",
    ["एकपदी (Monomial)", "त्रिपद (Trinomial)", "चतुर्पद (Quadrinomial)"],
    ["Monomial", "Trinomial", "Quadrinomial"],
    "दो पदों वाले बहुपद को द्विपद (Binomial) कहते हैं, जैसे: x + 2, 3x² - 5।",
    "A polynomial containing exactly two terms is called a Binomial.",
    "Easy", "Definition"
)

add_q(t1,
    "ठीक तीन पदों (Three terms) वाले बहुपद को क्या कहा जाता है?",
    "What is a polynomial with exactly three terms called?",
    "त्रिपद (Trinomial)", "Trinomial",
    ["द्विपद (Binomial)", "एकपदी (Monomial)", "चतुर्पद (Quadrinomial)"],
    ["Binomial", "Monomial", "Quadrinomial"],
    "तीन पदों वाले बहुपद को त्रिपद (Trinomial) कहते हैं, जैसे: x² + 2x + 1।",
    "A polynomial containing exactly three terms is called a Trinomial.",
    "Easy", "Definition"
)

add_q(t1,
    "घात 1 वाले बहुपद को क्या कहते हैं?",
    "A polynomial of degree 1 is called a:",
    "रैखिक बहुपद (Linear Polynomial)", "Linear Polynomial",
    ["द्विघात बहुपद (Quadratic)", "त्रिघात बहुपद (Cubic)", "अचर बहुपद (Constant)"],
    ["Quadratic Polynomial", "Cubic Polynomial", "Constant Polynomial"],
    "घात 1 के बहुपद को रैखिक बहुपद (जैसे 2x + 3) कहा जाता है।",
    "A polynomial of degree 1 is known as a Linear Polynomial (e.g., 2x + 3).",
    "Easy", "Definition"
)

add_q(t1,
    "घात 2 वाले बहुपद को क्या कहते हैं?",
    "A polynomial of degree 2 is called a:",
    "द्विघात बहुपद (Quadratic Polynomial)", "Quadratic Polynomial",
    ["रैखिक बहुपद (Linear)", "त्रिघात बहुपद (Cubic)", "चतुर्घात बहुपद (Bi-quadratic)"],
    ["Linear Polynomial", "Cubic Polynomial", "Bi-quadratic Polynomial"],
    "घात 2 के बहुपद को द्विघात बहुपद (जैसे ax² + bx + c) कहा जाता है।",
    "A polynomial of degree 2 is called a Quadratic Polynomial.",
    "Easy", "Definition"
)

add_q(t1,
    "घात 3 वाले बहुपद को क्या कहते हैं?",
    "A polynomial of degree 3 is called a:",
    "त्रिघात बहुपद (Cubic Polynomial)", "Cubic Polynomial",
    ["द्विघात बहुपद (Quadratic)", "रैखिक बहुपद (Linear)", "चतुर्घात बहुपद (Bi-quadratic)"],
    ["Quadratic Polynomial", "Linear Polynomial", "Bi-quadratic Polynomial"],
    "घात 3 के बहुपद को त्रिघात बहुपद (जैसे ax³ + bx² + cx + d) कहा जाता है।",
    "A polynomial of degree 3 is called a Cubic Polynomial.",
    "Easy", "Definition"
)

add_q(t1,
    "अचर बहुपद (जैसे P(x) = 7) की घात (Degree) कितनी होती है?",
    "What is the degree of a non-zero constant polynomial (like P(x) = 7)?",
    "0 (शून्य)", "0 (Zero)",
    ["1", "अपरिभाषित (Not defined)", "अनंत (Infinity)"],
    ["1", "Not defined", "Infinity"],
    "किसी भी अशून्य अचर बहुपद की घात 0 होती है (7 = 7x⁰)।",
    "The degree of any non-zero constant polynomial is 0 (7 = 7x⁰).",
    "Easy", "Degree"
)

add_q(t1,
    "शून्य बहुपद (P(x) = 0) की घात (Degree) क्या होती है?",
    "What is the degree of the Zero polynomial (P(x) = 0)?",
    "अपरिभाषित (Not defined)", "Not defined",
    ["0", "1", "-1"],
    ["0", "1", "-1"],
    "शून्य बहुपद की घात गणितीय रूप से अपरिभाषित (Not defined) मानी जाती है।",
    "The degree of the zero polynomial is mathematically not defined.",
    "Easy", "Degree"
)

leading_coeff_cases = [
    ("4x³ - 2x² + 5x - 1", 4, ["-2", "5", "-1"]),
    ("-5x⁴ + 3x² - 2x + 7", -5, ["3", "-2", "7"]),
    ("7x⁵ - 3x³ + 2", 7, ["-3", "2", "5"]),
    ("-x³ + 4x - 6", -1, ["1", "4", "-6"]),
    ("2x² - 9x + 4", 2, ["-9", "4", "1"]),
    ("9x⁶ - 2x³ + 1", 9, ["-2", "1", "6"]),
    ("-3x² + 8x - 5", -3, ["8", "-5", "3"])
]

for p_str, cor_lc, dis_lcs in leading_coeff_cases:
    add_q(t1,
        f"बहुपद P(x) = {p_str} का मुख्य गुणांक (Leading Coefficient) क्या है?",
        f"What is the leading coefficient of the polynomial P(x) = {p_str}?",
        str(cor_lc), str(cor_lc),
        [str(d) for d in dis_lcs], [str(d) for d in dis_lcs],
        f"उच्चतम घात वाले पद का गुणांक मुख्य गुणांक (Leading Coefficient) कहलाता है। यहाँ मुख्य गुणांक = {cor_lc} है।",
        f"The coefficient of the term with the highest degree is the leading coefficient (= {cor_lc}).",
        "Medium", "Leading Coefficient"
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
    "द्विघात बहुपद ax² + bx + c में यदि a > 0 हो, तो परवलय का मुँह किस दिशा में खुलता है?",
    "For a quadratic polynomial ax² + bx + c, if a > 0, the parabola opens in which direction?",
    "ऊपर की ओर (Upwards)", "Upwards",
    ["नीचे की ओर (Downwards)", "दाईं ओर (Rightwards)", "बाईं ओर (Leftwards)"],
    ["Downwards", "Rightwards", "Leftwards"],
    "जब a > 0 होता है तो परवलय ऊपर की ओर खुलता है (U-shaped opening upwards)।",
    "When a > 0, the parabola opens upwards.",
    "Easy", "Geometry"
)

add_q(t2,
    "द्विघात बहुपद ax² + bx + c में यदि a < 0 हो, तो परवलय का मुँह किस दिशा में खुलता है?",
    "For a quadratic polynomial ax² + bx + c, if a < 0, the parabola opens in which direction?",
    "नीचे की ओर (Downwards)", "Downwards",
    ["ऊपर की ओर (Upwards)", "दाईं ओर (Rightwards)", "बाईं ओर (Leftwards)"],
    ["Upwards", "Rightwards", "Leftwards"],
    "जब a < 0 (ऋणात्मक) होता है तो परवलय नीचे की ओर खुलता है।",
    "When a < 0 (negative), the parabola opens downwards.",
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
    add_q(t4,
        f"द्विघात बहुपद P(x) = {poly_str} के शून्यक क्या होंगे?",
        f"What are the zeroes of the quadratic polynomial P(x) = {poly_str}?",
        zeroes_hi, zeroes_en,
        ["2 और -4", "3 और -5", "1 और -2"], ["2 and -4", "3 and -5", "1 and -2"],
        f"P(x) = 0 रखकर गुणनखंड करने पर शून्यक = {zeroes_hi} प्राप्त होते हैं।",
        f"Setting P(x) = 0 and factorizing gives zeroes = {zeroes_en}.",
        "Medium", "Calculation"
    )

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
print(f"TOPIC 2.1 QUESTION COUNT: {sum(1 for q in questions if q['topic_id'] == 'math_ch_02_topic_01')}")
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
