# -*- coding: utf-8 -*-
"""
Build Complete Class 10 Bihar Board (BSEB) Academic Structure
Generates js/data/syllabus.js with complete hierarchy:
Board -> Class 10 -> Mediums -> Subject -> Book -> Section -> Chapter -> Topic
"""

import json
import os

SYLLABUS_DATA = {
    "board": "BSEB",
    "board_name_hi": "बिहार विद्यालय परीक्षा समिति",
    "board_name_en": "Bihar School Examination Board",
    "class": "10",
    "class_name_hi": "कक्षा 10",
    "class_name_en": "Class 10",
    "mediums": [
        {"id": "hi", "name_hi": "हिंदी", "name_en": "Hindi"},
        {"id": "en", "name_hi": "अंग्रेज़ी", "name_en": "English"}
    ],
    "subjects": []
}

# ==========================================
# 1. MATHEMATICS — गणित
# ==========================================
math_subject = {
    "id": "math",
    "code": "MATH",
    "name_hi": "गणित",
    "name_en": "Mathematics",
    "icon": "fa-calculator",
    "color": "from-blue-600 to-indigo-600",
    "accent": "#3b82f6",
    "books": [
        {
            "id": "math_book_01",
            "name_hi": "गणित (कक्षा 10)",
            "name_en": "Mathematics (Class 10)",
            "chapters": [
                {
                    "id": "math_ch_01",
                    "code": "CH01",
                    "chapter_number": 1,
                    "name_hi": "वास्तविक संख्याएं",
                    "name_en": "Real Numbers",
                    "topics": [
                        {"id": "math_ch_01_topic_01", "name_hi": "यूक्लिड विभाजन प्रमेय", "name_en": "Euclid's Division Lemma"},
                        {"id": "math_ch_01_topic_02", "name_hi": "यूक्लिड विभाजन एल्गोरिथ्म", "name_en": "Euclid's Division Algorithm"},
                        {"id": "math_ch_01_topic_03", "name_hi": "अंकगणित का मौलिक प्रमेय", "name_en": "Fundamental Theorem of Arithmetic"},
                        {"id": "math_ch_01_topic_04", "name_hi": "अभाज्य गुणनखंड", "name_en": "Prime Factorisation"},
                        {"id": "math_ch_01_topic_05", "name_hi": "महत्तम समापवर्तक", "name_en": "HCF"},
                        {"id": "math_ch_01_topic_06", "name_hi": "लघुत्तम समापवर्त्य", "name_en": "LCM"},
                        {"id": "math_ch_01_topic_07", "name_hi": "परिमेय संख्याएँ", "name_en": "Rational Numbers"},
                        {"id": "math_ch_01_topic_08", "name_hi": "अपरिमेय संख्याएँ", "name_en": "Irrational Numbers"},
                        {"id": "math_ch_01_topic_09", "name_hi": "परिमेय संख्याओं का दशमलव प्रसार", "name_en": "Decimal Expansion of Rational Numbers"},
                        {"id": "math_ch_01_topic_10", "name_hi": "HCF और LCM के अनुप्रयोग", "name_en": "Applications of HCF and LCM"}
                    ]
                },
                {
                    "id": "math_ch_02",
                    "code": "CH02",
                    "chapter_number": 2,
                    "name_hi": "बहुपद",
                    "name_en": "Polynomials",
                    "topics": [
                        {"id": "math_ch_02_topic_01", "name_hi": "बहुपद", "name_en": "Polynomials"},
                        {"id": "math_ch_02_topic_02", "name_hi": "बहुपद की घात", "name_en": "Degree of a Polynomial"},
                        {"id": "math_ch_02_topic_03", "name_hi": "बहुपद के शून्यक", "name_en": "Zeroes of a Polynomial"},
                        {"id": "math_ch_02_topic_04", "name_hi": "ग्राफ द्वारा शून्यक", "name_en": "Geometrical Meaning of Zeroes"},
                        {"id": "math_ch_02_topic_05", "name_hi": "शून्यकों और गुणांकों का संबंध", "name_en": "Relationship Between Zeroes and Coefficients"},
                        {"id": "math_ch_02_topic_06", "name_hi": "बहुपदों का विभाजन", "name_en": "Division of Polynomials"},
                        {"id": "math_ch_02_topic_07", "name_hi": "विभाजन एल्गोरिथ्म", "name_en": "Division Algorithm for Polynomials"}
                    ]
                },
                {
                    "id": "math_ch_03",
                    "code": "CH03",
                    "chapter_number": 3,
                    "name_hi": "दो चर वाले रैखिक समीकरण युग्म",
                    "name_en": "Pair of Linear Equations in Two Variables",
                    "topics": [
                        {"id": "math_ch_03_topic_01", "name_hi": "दो चर वाले रैखिक समीकरण", "name_en": "Linear Equations in Two Variables"},
                        {"id": "math_ch_03_topic_02", "name_hi": "रैखिक समीकरणों का युग्म", "name_en": "Pair of Linear Equations"},
                        {"id": "math_ch_03_topic_03", "name_hi": "ग्राफीय निरूपण", "name_en": "Graphical Representation"},
                        {"id": "math_ch_03_topic_04", "name_hi": "हल का अस्तित्व", "name_en": "Existence of Solutions"},
                        {"id": "math_ch_03_topic_05", "name_hi": "संगत समीकरण", "name_en": "Consistent Equations"},
                        {"id": "math_ch_03_topic_06", "name_hi": "असंगत समीकरण", "name_en": "Inconsistent Equations"},
                        {"id": "math_ch_03_topic_07", "name_hi": "प्रतिस्थापन विधि", "name_en": "Substitution Method"},
                        {"id": "math_ch_03_topic_08", "name_hi": "विलोपन विधि", "name_en": "Elimination Method"},
                        {"id": "math_ch_03_topic_09", "name_hi": "क्रॉस-गुणन विधि", "name_en": "Cross-Multiplication Method"},
                        {"id": "math_ch_03_topic_10", "name_hi": "रैखिक समीकरणों पर आधारित शब्द समस्याएँ", "name_en": "Word Problems"}
                    ]
                },
                {
                    "id": "math_ch_04",
                    "code": "CH04",
                    "chapter_number": 4,
                    "name_hi": "द्विघात समीकरण",
                    "name_en": "Quadratic Equations",
                    "topics": [
                        {"id": "math_ch_04_topic_01", "name_hi": "द्विघात समीकरण", "name_en": "Quadratic Equations"},
                        {"id": "math_ch_04_topic_02", "name_hi": "मानक रूप", "name_en": "Standard Form"},
                        {"id": "math_ch_04_topic_03", "name_hi": "गुणनखंड विधि", "name_en": "Factorisation Method"},
                        {"id": "math_ch_04_topic_04", "name_hi": "पूर्ण वर्ग बनाना", "name_en": "Completing the Square"},
                        {"id": "math_ch_04_topic_05", "name_hi": "द्विघात सूत्र", "name_en": "Quadratic Formula"},
                        {"id": "math_ch_04_topic_06", "name_hi": "मूल", "name_en": "Roots"},
                        {"id": "math_ch_04_topic_07", "name_hi": "मूलों की प्रकृति", "name_en": "Nature of Roots"},
                        {"id": "math_ch_04_topic_08", "name_hi": "विविक्तकर", "name_en": "Discriminant"},
                        {"id": "math_ch_04_topic_09", "name_hi": "मूलों और गुणांकों का संबंध", "name_en": "Relationship Between Roots and Coefficients"},
                        {"id": "math_ch_04_topic_10", "name_hi": "द्विघात समीकरणों की शब्द समस्याएँ", "name_en": "Word Problems"}
                    ]
                },
                {
                    "id": "math_ch_05",
                    "code": "CH05",
                    "chapter_number": 5,
                    "name_hi": "समांतर श्रेढ़ियाँ",
                    "name_en": "Arithmetic Progressions",
                    "topics": [
                        {"id": "math_ch_05_topic_01", "name_hi": "समांतर श्रेढ़ी", "name_en": "Arithmetic Progression"},
                        {"id": "math_ch_05_topic_02", "name_hi": "प्रथम पद", "name_en": "First Term"},
                        {"id": "math_ch_05_topic_03", "name_hi": "सार्व अंतर", "name_en": "Common Difference"},
                        {"id": "math_ch_05_topic_04", "name_hi": "पद", "name_en": "Terms"},
                        {"id": "math_ch_05_topic_05", "name_hi": "nवाँ पद", "name_en": "nth Term"},
                        {"id": "math_ch_05_topic_06", "name_hi": "प्रथम n पदों का योग", "name_en": "Sum of First n Terms"},
                        {"id": "math_ch_05_topic_07", "name_hi": "समांतर श्रेढ़ियों के अनुप्रयोग", "name_en": "Applications of Arithmetic Progressions"}
                    ]
                },
                {
                    "id": "math_ch_06",
                    "code": "CH06",
                    "chapter_number": 6,
                    "name_hi": "त्रिभुज",
                    "name_en": "Triangles",
                    "topics": [
                        {"id": "math_ch_06_topic_01", "name_hi": "समरूप आकृतियाँ", "name_en": "Similar Figures"},
                        {"id": "math_ch_06_topic_02", "name_hi": "त्रिभुजों की समरूपता", "name_en": "Similarity of Triangles"},
                        {"id": "math_ch_06_topic_03", "name_hi": "मूल समानुपातिकता प्रमेय", "name_en": "Basic Proportionality Theorem"},
                        {"id": "math_ch_06_topic_04", "name_hi": "समरूपता की कसौटियाँ", "name_en": "Criteria for Similarity"},
                        {"id": "math_ch_06_topic_05", "name_hi": "समरूप त्रिभुजों के क्षेत्रफल", "name_en": "Areas of Similar Triangles"},
                        {"id": "math_ch_06_topic_06", "name_hi": "पाइथागोरस प्रमेय", "name_en": "Pythagoras Theorem"},
                        {"id": "math_ch_06_topic_07", "name_hi": "पाइथागोरस प्रमेय का विलोम", "name_en": "Converse of Pythagoras Theorem"}
                    ]
                },
                {
                    "id": "math_ch_07",
                    "code": "CH07",
                    "chapter_number": 7,
                    "name_hi": "निर्देशांक ज्यामिति",
                    "name_en": "Coordinate Geometry",
                    "topics": [
                        {"id": "math_ch_07_topic_01", "name_hi": "निर्देशांक तल", "name_en": "Coordinate Plane"},
                        {"id": "math_ch_07_topic_02", "name_hi": "कार्तीय निर्देशांक", "name_en": "Cartesian Coordinates"},
                        {"id": "math_ch_07_topic_03", "name_hi": "दूरी सूत्र", "name_en": "Distance Formula"},
                        {"id": "math_ch_07_topic_04", "name_hi": "विभाजन सूत्र", "name_en": "Section Formula"},
                        {"id": "math_ch_07_topic_05", "name_hi": "मध्य-बिंदु", "name_en": "Midpoint"},
                        {"id": "math_ch_07_topic_06", "name_hi": "त्रिभुज का क्षेत्रफल", "name_en": "Area of Triangle"},
                        {"id": "math_ch_07_topic_07", "name_hi": "निर्देशांक ज्यामिति के अनुप्रयोग", "name_en": "Applications of Coordinate Geometry"}
                    ]
                },
                {
                    "id": "math_ch_08",
                    "code": "CH08",
                    "chapter_number": 8,
                    "name_hi": "त्रिकोणमिति का परिचय",
                    "name_en": "Introduction to Trigonometry",
                    "topics": [
                        {"id": "math_ch_08_topic_01", "name_hi": "त्रिकोणमितीय अनुपात", "name_en": "Trigonometric Ratios"},
                        {"id": "math_ch_08_topic_02", "name_hi": "ज्या", "name_en": "Sine"},
                        {"id": "math_ch_08_topic_03", "name_hi": "कोज्या", "name_en": "Cosine"},
                        {"id": "math_ch_08_topic_04", "name_hi": "स्पर्शज्या", "name_en": "Tangent"},
                        {"id": "math_ch_08_topic_05", "name_hi": "कोटिज्या", "name_en": "Cosecant"},
                        {"id": "math_ch_08_topic_06", "name_hi": "सेकेंट", "name_en": "Secant"},
                        {"id": "math_ch_08_topic_07", "name_hi": "कोटैन्जेंट", "name_en": "Cotangent"},
                        {"id": "math_ch_08_topic_08", "name_hi": "मानक कोणों के त्रिकोणमितीय अनुपात", "name_en": "Trigonometric Ratios of Standard Angles"},
                        {"id": "math_ch_08_topic_09", "name_hi": "त्रिकोणमितीय सर्वसमिकाएँ", "name_en": "Trigonometric Identities"},
                        {"id": "math_ch_08_topic_10", "name_hi": "सर्वसमिकाओं का उपयोग", "name_en": "Applications of Trigonometric Identities"}
                    ]
                },
                {
                    "id": "math_ch_09",
                    "code": "CH09",
                    "chapter_number": 9,
                    "name_hi": "त्रिकोणमिति के कुछ अनुप्रयोग",
                    "name_en": "Some Applications of Trigonometry",
                    "topics": [
                        {"id": "math_ch_09_topic_01", "name_hi": "ऊँचाई और दूरी", "name_en": "Heights and Distances"},
                        {"id": "math_ch_09_topic_02", "name_hi": "उन्नयन कोण", "name_en": "Angle of Elevation"},
                        {"id": "math_ch_09_topic_03", "name_hi": "अवनमन कोण", "name_en": "Angle of Depression"},
                        {"id": "math_ch_09_topic_04", "name_hi": "ऊँचाई ज्ञात करना", "name_en": "Finding Heights"},
                        {"id": "math_ch_09_topic_05", "name_hi": "दूरी ज्ञात करना", "name_en": "Finding Distances"},
                        {"id": "math_ch_09_topic_06", "name_hi": "त्रिकोणमिति के अनुप्रयोग", "name_en": "Applications of Trigonometry"}
                    ]
                },
                {
                    "id": "math_ch_10",
                    "code": "CH10",
                    "chapter_number": 10,
                    "name_hi": "वृत्त",
                    "name_en": "Circles",
                    "topics": [
                        {"id": "math_ch_10_topic_01", "name_hi": "स्पर्श रेखा", "name_en": "Tangent"},
                        {"id": "math_ch_10_topic_02", "name_hi": "वृत्त की स्पर्श रेखा", "name_en": "Tangent to a Circle"},
                        {"id": "math_ch_10_topic_03", "name_hi": "स्पर्श बिंदु", "name_en": "Point of Contact"},
                        {"id": "math_ch_10_topic_04", "name_hi": "किसी बिंदु से खींची गई स्पर्श रेखाएँ", "name_en": "Tangents from a Point"},
                        {"id": "math_ch_10_topic_05", "name_hi": "स्पर्श रेखाओं के गुण", "name_en": "Properties of Tangents"},
                        {"id": "math_ch_10_topic_06", "name_hi": "स्पर्श रेखा संबंधी प्रमेय", "name_en": "Theorems Related to Tangents"}
                    ]
                },
                {
                    "id": "math_ch_11",
                    "code": "CH11",
                    "chapter_number": 11,
                    "name_hi": "रचनाएँ",
                    "name_en": "Constructions",
                    "topics": [
                        {"id": "math_ch_11_topic_01", "name_hi": "रेखाखंड का विभाजन", "name_en": "Division of a Line Segment"},
                        {"id": "math_ch_11_topic_02", "name_hi": "समान त्रिभुजों की रचना", "name_en": "Construction of Similar Triangles"},
                        {"id": "math_ch_11_topic_03", "name_hi": "दिए गए अनुपात में रचना", "name_en": "Construction in a Given Ratio"},
                        {"id": "math_ch_11_topic_04", "name_hi": "वृत्त की स्पर्श रेखा की रचना", "name_en": "Construction of Tangent to a Circle"},
                        {"id": "math_ch_11_topic_05", "name_hi": "ज्यामितीय रचनाएँ", "name_en": "Geometrical Constructions"}
                    ]
                },
                {
                    "id": "math_ch_12",
                    "code": "CH12",
                    "chapter_number": 12,
                    "name_hi": "वृत्तों से संबंधित क्षेत्रफल",
                    "name_en": "Areas Related to Circles",
                    "topics": [
                        {"id": "math_ch_12_topic_01", "name_hi": "वृत्त की परिधि", "name_en": "Circumference"},
                        {"id": "math_ch_12_topic_02", "name_hi": "वृत्त का क्षेत्रफल", "name_en": "Area of Circle"},
                        {"id": "math_ch_12_topic_03", "name_hi": "त्रिज्यखंड", "name_en": "Sector"},
                        {"id": "math_ch_12_topic_04", "name_hi": "त्रिज्यखंड का क्षेत्रफल", "name_en": "Area of Sector"},
                        {"id": "math_ch_12_topic_05", "name_hi": "चाप की लंबाई", "name_en": "Length of Arc"},
                        {"id": "math_ch_12_topic_06", "name_hi": "वृत्तखंड", "name_en": "Segment"},
                        {"id": "math_ch_12_topic_07", "name_hi": "वृत्तखंड का क्षेत्रफल", "name_en": "Area of Segment"},
                        {"id": "math_ch_12_topic_08", "name_hi": "संयुक्त समतलीय आकृतियाँ", "name_en": "Areas of Combined Figures"}
                    ]
                },
                {
                    "id": "math_ch_13",
                    "code": "CH13",
                    "chapter_number": 13,
                    "name_hi": "पृष्ठीय क्षेत्रफल और आयतन",
                    "name_en": "Surface Areas and Volumes",
                    "topics": [
                        {"id": "math_ch_13_topic_01", "name_hi": "बेलन", "name_en": "Cylinder"},
                        {"id": "math_ch_13_topic_02", "name_hi": "शंकु", "name_en": "Cone"},
                        {"id": "math_ch_13_topic_03", "name_hi": "गोला", "name_en": "Sphere"},
                        {"id": "math_ch_13_topic_04", "name_hi": "अर्धगोला", "name_en": "Hemisphere"},
                        {"id": "math_ch_13_topic_05", "name_hi": "शंकु का छिन्नक", "name_en": "Frustum"},
                        {"id": "math_ch_13_topic_06", "name_hi": "पृष्ठीय क्षेत्रफल", "name_en": "Surface Area"},
                        {"id": "math_ch_13_topic_07", "name_hi": "आयतन", "name_en": "Volume"},
                        {"id": "math_ch_13_topic_08", "name_hi": "ठोसों का संयोजन", "name_en": "Combination of Solids"},
                        {"id": "math_ch_13_topic_09", "name_hi": "ठोसों का रूपांतरण", "name_en": "Conversion of Solids"},
                        {"id": "math_ch_13_topic_10", "name_hi": "पृष्ठीय क्षेत्रफल और आयतन के अनुप्रयोग", "name_en": "Applications"}
                    ]
                },
                {
                    "id": "math_ch_14",
                    "code": "CH14",
                    "chapter_number": 14,
                    "name_hi": "सांख्यिकी",
                    "name_en": "Statistics",
                    "topics": [
                        {"id": "math_ch_14_topic_01", "name_hi": "आँकड़ों का संग्रह", "name_en": "Collection of Data"},
                        {"id": "math_ch_14_topic_02", "name_hi": "वर्गीकृत आँकड़े", "name_en": "Grouped Data"},
                        {"id": "math_ch_14_topic_03", "name_hi": "माध्य", "name_en": "Mean"},
                        {"id": "math_ch_14_topic_04", "name_hi": "माध्यक", "name_en": "Median"},
                        {"id": "math_ch_14_topic_05", "name_hi": "बहुलक", "name_en": "Mode"},
                        {"id": "math_ch_14_topic_06", "name_hi": "संचयी बारंबारता", "name_en": "Cumulative Frequency"},
                        {"id": "math_ch_14_topic_07", "name_hi": "संचयी बारंबारता वक्र", "name_en": "Cumulative Frequency Curve"},
                        {"id": "math_ch_14_topic_08", "name_hi": "माध्य-माध्यक-बहुलक संबंध", "name_en": "Empirical Relationship"}
                    ]
                },
                {
                    "id": "math_ch_15",
                    "code": "CH15",
                    "chapter_number": 15,
                    "name_hi": "प्रायिकता",
                    "name_en": "Probability",
                    "topics": [
                        {"id": "math_ch_15_topic_01", "name_hi": "प्रायिकता", "name_en": "Probability"},
                        {"id": "math_ch_15_topic_02", "name_hi": "यादृच्छिक प्रयोग", "name_en": "Random Experiment"},
                        {"id": "math_ch_15_topic_03", "name_hi": "परिणाम", "name_en": "Outcomes"},
                        {"id": "math_ch_15_topic_04", "name_hi": "घटना", "name_en": "Event"},
                        {"id": "math_ch_15_topic_05", "name_hi": "किसी घटना की प्रायिकता", "name_en": "Probability of an Event"},
                        {"id": "math_ch_15_topic_06", "name_hi": "शास्त्रीय प्रायिकता", "name_en": "Classical Probability"},
                        {"id": "math_ch_15_topic_07", "name_hi": "प्रायिकता के अनुप्रयोग", "name_en": "Applications of Probability"}
                    ]
                }
            ]
        }
    ]
}
SYLLABUS_DATA["subjects"].append(math_subject)

# ==========================================
# 2. SCIENCE — विज्ञान (3 Sections)
# ==========================================
science_subject = {
    "id": "science",
    "code": "SCI",
    "name_hi": "विज्ञान",
    "name_en": "Science",
    "icon": "fa-flask",
    "color": "from-emerald-600 to-teal-600",
    "accent": "#10b981",
    "books": [
        {
            "id": "sci_book_01",
            "name_hi": "विज्ञान (कक्षा 10)",
            "name_en": "Science (Class 10)",
            "sections": [
                {
                    "id": "sci_sec_physics",
                    "name_hi": "भौतिक विज्ञान",
                    "name_en": "Physics",
                    "chapters": [
                        {
                            "id": "sci_phy_ch_10",
                            "code": "CH10",
                            "chapter_number": 10,
                            "name_hi": "प्रकाश – परावर्तन तथा अपवर्तन",
                            "name_en": "Light – Reflection and Refraction",
                            "topics": [
                                {"id": "sci_phy_ch_10_topic_01", "name_hi": "प्रकाश का परावर्तन", "name_en": "Reflection of Light"},
                                {"id": "sci_phy_ch_10_topic_02", "name_hi": "परावर्तन के नियम", "name_en": "Laws of Reflection"},
                                {"id": "sci_phy_ch_10_topic_03", "name_hi": "गोलीय दर्पण", "name_en": "Spherical Mirrors"},
                                {"id": "sci_phy_ch_10_topic_04", "name_hi": "अवतल दर्पण", "name_en": "Concave Mirror"},
                                {"id": "sci_phy_ch_10_topic_05", "name_hi": "उत्तल दर्पण", "name_en": "Convex Mirror"},
                                {"id": "sci_phy_ch_10_topic_06", "name_hi": "दर्पण सूत्र", "name_en": "Mirror Formula"},
                                {"id": "sci_phy_ch_10_topic_07", "name_hi": "आवर्धन", "name_en": "Magnification"},
                                {"id": "sci_phy_ch_10_topic_08", "name_hi": "प्रकाश का अपवर्तन", "name_en": "Refraction of Light"},
                                {"id": "sci_phy_ch_10_topic_09", "name_hi": "अपवर्तन के नियम", "name_en": "Laws of Refraction"},
                                {"id": "sci_phy_ch_10_topic_10", "name_hi": "अपवर्तनांक", "name_en": "Refractive Index"},
                                {"id": "sci_phy_ch_10_topic_11", "name_hi": "गोलीय लेंस", "name_en": "Spherical Lenses"},
                                {"id": "sci_phy_ch_10_topic_12", "name_hi": "उत्तल लेंस", "name_en": "Convex Lens"},
                                {"id": "sci_phy_ch_10_topic_13", "name_hi": "अवतल लेंस", "name_en": "Concave Lens"},
                                {"id": "sci_phy_ch_10_topic_14", "name_hi": "लेंस सूत्र", "name_en": "Lens Formula"},
                                {"id": "sci_phy_ch_10_topic_15", "name_hi": "लेंस का आवर्धन", "name_en": "Magnification of Lens"},
                                {"id": "sci_phy_ch_10_topic_16", "name_hi": "लेंस की शक्ति", "name_en": "Power of Lens"}
                            ]
                        },
                        {
                            "id": "sci_phy_ch_11",
                            "code": "CH11",
                            "chapter_number": 11,
                            "name_hi": "मानव नेत्र तथा रंगबिरंगा संसार",
                            "name_en": "The Human Eye and the Colourful World",
                            "topics": [
                                {"id": "sci_phy_ch_11_topic_01", "name_hi": "मानव नेत्र", "name_en": "Human Eye"},
                                {"id": "sci_phy_ch_11_topic_02", "name_hi": "मानव नेत्र की संरचना", "name_en": "Structure of Human Eye"},
                                {"id": "sci_phy_ch_11_topic_03", "name_hi": "समंजन", "name_en": "Accommodation"},
                                {"id": "sci_phy_ch_11_topic_04", "name_hi": "दृष्टि दोष", "name_en": "Defects of Vision"},
                                {"id": "sci_phy_ch_11_topic_05", "name_hi": "निकट-दृष्टिदोष", "name_en": "Myopia"},
                                {"id": "sci_phy_ch_11_topic_06", "name_hi": "दूर-दृष्टिदोष", "name_en": "Hypermetropia"},
                                {"id": "sci_phy_ch_11_topic_07", "name_hi": "जरा-दूरदृष्टिता", "name_en": "Presbyopia"},
                                {"id": "sci_phy_ch_11_topic_08", "name_hi": "दृष्टि दोषों का संशोधन", "name_en": "Correction of Vision"},
                                {"id": "sci_phy_ch_11_topic_09", "name_hi": "प्रिज्म द्वारा प्रकाश का अपवर्तन", "name_en": "Refraction Through a Prism"},
                                {"id": "sci_phy_ch_11_topic_10", "name_hi": "प्रकाश का विक्षेपण", "name_en": "Dispersion of Light"},
                                {"id": "sci_phy_ch_11_topic_11", "name_hi": "वायुमंडलीय अपवर्तन", "name_en": "Atmospheric Refraction"},
                                {"id": "sci_phy_ch_11_topic_12", "name_hi": "प्रकाश का प्रकीर्णन", "name_en": "Scattering of Light"}
                            ]
                        },
                        {
                            "id": "sci_phy_ch_12",
                            "code": "CH12",
                            "chapter_number": 12,
                            "name_hi": "विद्युत",
                            "name_en": "Electricity",
                            "topics": [
                                {"id": "sci_phy_ch_12_topic_01", "name_hi": "विद्युत धारा", "name_en": "Electric Current"},
                                {"id": "sci_phy_ch_12_topic_02", "name_hi": "विद्युत विभव", "name_en": "Electric Potential"},
                                {"id": "sci_phy_ch_12_topic_03", "name_hi": "विभवांतर", "name_en": "Potential Difference"},
                                {"id": "sci_phy_ch_12_topic_04", "name_hi": "विद्युत परिपथ", "name_en": "Electric Circuit"},
                                {"id": "sci_phy_ch_12_topic_05", "name_hi": "ओम का नियम", "name_en": "Ohm's Law"},
                                {"id": "sci_phy_ch_12_topic_06", "name_hi": "प्रतिरोध", "name_en": "Resistance"},
                                {"id": "sci_phy_ch_12_topic_07", "name_hi": "प्रतिरोध को प्रभावित करने वाले कारक", "name_en": "Factors Affecting Resistance"},
                                {"id": "sci_phy_ch_12_topic_08", "name_hi": "प्रतिरोधकता", "name_en": "Resistivity"},
                                {"id": "sci_phy_ch_12_topic_09", "name_hi": "श्रेणी संयोजन", "name_en": "Series Combination"},
                                {"id": "sci_phy_ch_12_topic_10", "name_hi": "समानांतर संयोजन", "name_en": "Parallel Combination"},
                                {"id": "sci_phy_ch_12_topic_11", "name_hi": "विद्युत धारा का तापीय प्रभाव", "name_en": "Heating Effect"},
                                {"id": "sci_phy_ch_12_topic_12", "name_hi": "विद्युत शक्ति", "name_en": "Electric Power"},
                                {"id": "sci_phy_ch_12_topic_13", "name_hi": "विद्युत ऊर्जा", "name_en": "Electrical Energy"}
                            ]
                        },
                        {
                            "id": "sci_phy_ch_13",
                            "code": "CH13",
                            "chapter_number": 13,
                            "name_hi": "विद्युत धारा के चुंबकीय प्रभाव",
                            "name_en": "Magnetic Effects of Electric Current",
                            "topics": [
                                {"id": "sci_phy_ch_13_topic_01", "name_hi": "चुंबकीय क्षेत्र", "name_en": "Magnetic Field"},
                                {"id": "sci_phy_ch_13_topic_02", "name_hi": "चुंबकीय क्षेत्र रेखाएँ", "name_en": "Magnetic Field Lines"},
                                {"id": "sci_phy_ch_13_topic_03", "name_hi": "विद्युत धारा के कारण चुंबकीय क्षेत्र", "name_en": "Magnetic Field Due to Current"},
                                {"id": "sci_phy_ch_13_topic_04", "name_hi": "सीधे चालक के कारण चुंबकीय क्षेत्र", "name_en": "Field Due to Straight Conductor"},
                                {"id": "sci_phy_ch_13_topic_05", "name_hi": "वृत्ताकार कुंडली", "name_en": "Circular Loop"},
                                {"id": "sci_phy_ch_13_topic_06", "name_hi": "परिनालिका", "name_en": "Solenoid"},
                                {"id": "sci_phy_ch_13_topic_07", "name_hi": "विद्युत चुंबक", "name_en": "Electromagnet"},
                                {"id": "sci_phy_ch_13_topic_08", "name_hi": "धारावाही चालक पर बल", "name_en": "Force on Current-Carrying Conductor"},
                                {"id": "sci_phy_ch_13_topic_09", "name_hi": "फ्लेमिंग का बायाँ हाथ नियम", "name_en": "Fleming's Left-Hand Rule"},
                                {"id": "sci_phy_ch_13_topic_10", "name_hi": "विद्युतचुंबकीय प्रेरण", "name_en": "Electromagnetic Induction"},
                                {"id": "sci_phy_ch_13_topic_11", "name_hi": "फ्लेमिंग का दायाँ हाथ नियम", "name_en": "Fleming's Right-Hand Rule"},
                                {"id": "sci_phy_ch_13_topic_12", "name_hi": "विद्युत मोटर", "name_en": "Electric Motor"},
                                {"id": "sci_phy_ch_13_topic_13", "name_hi": "विद्युत जनित्र", "name_en": "Electric Generator"},
                                {"id": "sci_phy_ch_13_topic_14", "name_hi": "घरेलू विद्युत परिपथ", "name_en": "Domestic Electric Circuits"}
                            ]
                        },
                        {
                            "id": "sci_phy_ch_14",
                            "code": "CH14",
                            "chapter_number": 14,
                            "name_hi": "ऊर्जा के स्रोत",
                            "name_en": "Sources of Energy",
                            "topics": [
                                {"id": "sci_phy_ch_14_topic_01", "name_hi": "ऊर्जा के स्रोत", "name_en": "Sources of Energy"},
                                {"id": "sci_phy_ch_14_topic_02", "name_hi": "परंपरागत ऊर्जा स्रोत", "name_en": "Conventional Sources"},
                                {"id": "sci_phy_ch_14_topic_03", "name_hi": "अपरंपरागत ऊर्जा स्रोत", "name_en": "Non-Conventional Sources"},
                                {"id": "sci_phy_ch_14_topic_04", "name_hi": "नवीकरणीय ऊर्जा", "name_en": "Renewable Energy"},
                                {"id": "sci_phy_ch_14_topic_05", "name_hi": "जीवाश्म ईंधन", "name_en": "Fossil Fuels"},
                                {"id": "sci_phy_ch_14_topic_06", "name_hi": "ताप विद्युत", "name_en": "Thermal Power"},
                                {"id": "sci_phy_ch_14_topic_07", "name_hi": "जल विद्युत", "name_en": "Hydroelectric Power"},
                                {"id": "sci_phy_ch_14_topic_08", "name_hi": "सौर ऊर्जा", "name_en": "Solar Energy"},
                                {"id": "sci_phy_ch_14_topic_09", "name_hi": "पवन ऊर्जा", "name_en": "Wind Energy"},
                                {"id": "sci_phy_ch_14_topic_10", "name_hi": "जैवमास", "name_en": "Biomass"},
                                {"id": "sci_phy_ch_14_topic_11", "name_hi": "भूतापीय ऊर्जा", "name_en": "Geothermal Energy"},
                                {"id": "sci_phy_ch_14_topic_12", "name_hi": "ज्वारीय ऊर्जा", "name_en": "Tidal Energy"},
                                {"id": "sci_phy_ch_14_topic_13", "name_hi": "नाभिकीय ऊर्जा", "name_en": "Nuclear Energy"},
                                {"id": "sci_phy_ch_14_topic_14", "name_hi": "ऊर्जा स्रोतों का पर्यावरणीय प्रभाव", "name_en": "Environmental Impact"},
                                {"id": "sci_phy_ch_14_topic_15", "name_hi": "सतत ऊर्जा", "name_en": "Sustainable Energy"}
                            ]
                        }
                    ]
                },
                {
                    "id": "sci_sec_chemistry",
                    "name_hi": "रसायन विज्ञान",
                    "name_en": "Chemistry",
                    "chapters": [
                        {
                            "id": "sci_chem_ch_01",
                            "code": "CH01",
                            "chapter_number": 1,
                            "name_hi": "रासायनिक अभिक्रियाएं एवं समीकरण",
                            "name_en": "Chemical Reactions and Equations",
                            "topics": [
                                {"id": "sci_chem_ch_01_topic_01", "name_hi": "रासायनिक अभिक्रियाएँ", "name_en": "Chemical Reactions"},
                                {"id": "sci_chem_ch_01_topic_02", "name_hi": "रासायनिक समीकरण", "name_en": "Chemical Equations"},
                                {"id": "sci_chem_ch_01_topic_03", "name_hi": "संतुलित रासायनिक समीकरण", "name_en": "Balanced Chemical Equations"},
                                {"id": "sci_chem_ch_01_topic_04", "name_hi": "संयोजन अभिक्रिया", "name_en": "Combination Reaction"},
                                {"id": "sci_chem_ch_01_topic_05", "name_hi": "वियोजन अभिक्रिया", "name_en": "Decomposition Reaction"},
                                {"id": "sci_chem_ch_01_topic_06", "name_hi": "विस्थापन अभिक्रिया", "name_en": "Displacement Reaction"},
                                {"id": "sci_chem_ch_01_topic_07", "name_hi": "द्विविस्थापन अभिक्रिया", "name_en": "Double Displacement Reaction"},
                                {"id": "sci_chem_ch_01_topic_08", "name_hi": "उपचयन", "name_en": "Oxidation"},
                                {"id": "sci_chem_ch_01_topic_09", "name_hi": "अपचयन", "name_en": "Reduction"},
                                {"id": "sci_chem_ch_01_topic_10", "name_hi": "रेडॉक्स अभिक्रिया", "name_en": "Redox Reaction"},
                                {"id": "sci_chem_ch_01_topic_11", "name_hi": "संक्षारण", "name_en": "Corrosion"},
                                {"id": "sci_chem_ch_01_topic_12", "name_hi": "विकृतगंधिता", "name_en": "Rancidity"}
                            ]
                        },
                        {
                            "id": "sci_chem_ch_02",
                            "code": "CH02",
                            "chapter_number": 2,
                            "name_hi": "अम्ल, क्षारक एवं लवण",
                            "name_en": "Acids, Bases and Salts",
                            "topics": [
                                {"id": "sci_chem_ch_02_topic_01", "name_hi": "अम्ल", "name_en": "Acids"},
                                {"id": "sci_chem_ch_02_topic_02", "name_hi": "क्षारक", "name_en": "Bases"},
                                {"id": "sci_chem_ch_02_topic_03", "name_hi": "सूचक", "name_en": "Indicators"},
                                {"id": "sci_chem_ch_02_topic_04", "name_hi": "अम्लों के गुण", "name_en": "Properties of Acids"},
                                {"id": "sci_chem_ch_02_topic_05", "name_hi": "क्षारकों के गुण", "name_en": "Properties of Bases"},
                                {"id": "sci_chem_ch_02_topic_06", "name_hi": "उदासीनीकरण", "name_en": "Neutralisation"},
                                {"id": "sci_chem_ch_02_topic_07", "name_hi": "pH पैमाना", "name_en": "pH Scale"},
                                {"id": "sci_chem_ch_02_topic_08", "name_hi": "लवण", "name_en": "Salts"},
                                {"id": "sci_chem_ch_02_topic_09", "name_hi": "सामान्य नमक", "name_en": "Common Salt"},
                                {"id": "sci_chem_ch_02_topic_10", "name_hi": "बेकिंग सोडा", "name_en": "Baking Soda"},
                                {"id": "sci_chem_ch_02_topic_11", "name_hi": "वाशिंग सोडा", "name_en": "Washing Soda"},
                                {"id": "sci_chem_ch_02_topic_12", "name_hi": "विरंजक चूर्ण", "name_en": "Bleaching Powder"},
                                {"id": "sci_chem_ch_02_topic_13", "name_hi": "प्लास्टर ऑफ पेरिस", "name_en": "Plaster of Paris"},
                                {"id": "sci_chem_ch_02_topic_14", "name_hi": "क्रिस्टलीकरण का जल", "name_en": "Water of Crystallisation"}
                            ]
                        },
                        {
                            "id": "sci_chem_ch_03",
                            "code": "CH03",
                            "chapter_number": 3,
                            "name_hi": "धातु एवं अधातु",
                            "name_en": "Metals and Non-metals",
                            "topics": [
                                {"id": "sci_chem_ch_03_topic_01", "name_hi": "धातुओं के भौतिक गुण", "name_en": "Physical Properties of Metals"},
                                {"id": "sci_chem_ch_03_topic_02", "name_hi": "अधातुओं के भौतिक गुण", "name_en": "Physical Properties of Non-Metals"},
                                {"id": "sci_chem_ch_03_topic_03", "name_hi": "धातुओं के रासायनिक गुण", "name_en": "Chemical Properties of Metals"},
                                {"id": "sci_chem_ch_03_topic_04", "name_hi": "अभिक्रियाशीलता श्रेणी", "name_en": "Reactivity Series"},
                                {"id": "sci_chem_ch_03_topic_05", "name_hi": "ऑक्सीजन के साथ अभिक्रिया", "name_en": "Reaction with Oxygen"},
                                {"id": "sci_chem_ch_03_topic_06", "name_hi": "जल के साथ अभिक्रिया", "name_en": "Reaction with Water"},
                                {"id": "sci_chem_ch_03_topic_07", "name_hi": "अम्लों के साथ अभिक्रिया", "name_en": "Reaction with Acids"},
                                {"id": "sci_chem_ch_03_topic_08", "name_hi": "लवण विलयनों के साथ अभिक्रिया", "name_en": "Reaction with Salt Solutions"},
                                {"id": "sci_chem_ch_03_topic_09", "name_hi": "आयनिक यौगिक", "name_en": "Ionic Compounds"},
                                {"id": "sci_chem_ch_03_topic_10", "name_hi": "धातुओं का निष्कर्षण", "name_en": "Extraction of Metals"},
                                {"id": "sci_chem_ch_03_topic_11", "name_hi": "धातुओं का परिष्करण", "name_en": "Refining of Metals"},
                                {"id": "sci_chem_ch_03_topic_12", "name_hi": "संक्षारण", "name_en": "Corrosion"},
                                {"id": "sci_chem_ch_03_topic_13", "name_hi": "मिश्रधातु", "name_en": "Alloys"}
                            ]
                        },
                        {
                            "id": "sci_chem_ch_04",
                            "code": "CH04",
                            "chapter_number": 4,
                            "name_hi": "कार्बन एवं उसके यौगिक",
                            "name_en": "Carbon and its Compounds",
                            "topics": [
                                {"id": "sci_chem_ch_04_topic_01", "name_hi": "कार्बन", "name_en": "Carbon"},
                                {"id": "sci_chem_ch_04_topic_02", "name_hi": "चतुसंयोजकता", "name_en": "Tetravalency"},
                                {"id": "sci_chem_ch_04_topic_03", "name_hi": "श्रृंखलन", "name_en": "Catenation"},
                                {"id": "sci_chem_ch_04_topic_04", "name_hi": "सहसंयोजक आबंध", "name_en": "Covalent Bond"},
                                {"id": "sci_chem_ch_04_topic_05", "name_hi": "हाइड्रोकार्बन", "name_en": "Hydrocarbons"},
                                {"id": "sci_chem_ch_04_topic_06", "name_hi": "संतृप्त हाइड्रोकार्बन", "name_en": "Saturated Hydrocarbons"},
                                {"id": "sci_chem_ch_04_topic_07", "name_hi": "असंतृप्त हाइड्रोकार्बन", "name_en": "Unsaturated Hydrocarbons"},
                                {"id": "sci_chem_ch_04_topic_08", "name_hi": "समजातीय श्रेणी", "name_en": "Homologous Series"},
                                {"id": "sci_chem_ch_04_topic_09", "name_hi": "नामकरण", "name_en": "Nomenclature"},
                                {"id": "sci_chem_ch_04_topic_10", "name_hi": "क्रियात्मक समूह", "name_en": "Functional Groups"},
                                {"id": "sci_chem_ch_04_topic_11", "name_hi": "कार्बन यौगिकों के रासायनिक गुण", "name_en": "Chemical Properties"},
                                {"id": "sci_chem_ch_04_topic_12", "name_hi": "एथेनॉल", "name_en": "Ethanol"},
                                {"id": "sci_chem_ch_04_topic_13", "name_hi": "एथेनोइक अम्ल", "name_en": "Ethanoic Acid"},
                                {"id": "sci_chem_ch_04_topic_14", "name_hi": "साबुन", "name_en": "Soaps"},
                                {"id": "sci_chem_ch_04_topic_15", "name_hi": "अपमार्जक", "name_en": "Detergents"}
                            ]
                        },
                        {
                            "id": "sci_chem_ch_05",
                            "code": "CH05",
                            "chapter_number": 5,
                            "name_hi": "तत्वों का आवर्त वर्गीकरण",
                            "name_en": "Periodic Classification of Elements",
                            "topics": [
                                {"id": "sci_chem_ch_05_topic_01", "name_hi": "तत्वों का वर्गीकरण", "name_en": "Classification of Elements"},
                                {"id": "sci_chem_ch_05_topic_02", "name_hi": "डोबेरेनर के त्रिक", "name_en": "Dobereiner's Triads"},
                                {"id": "sci_chem_ch_05_topic_03", "name_hi": "न्यूलैंड्स का अष्टक नियम", "name_en": "Newlands' Law of Octaves"},
                                {"id": "sci_chem_ch_05_topic_04", "name_hi": "मेंडलीफ की आवर्त सारणी", "name_en": "Mendeleev's Periodic Table"},
                                {"id": "sci_chem_ch_05_topic_05", "name_hi": "आधुनिक आवर्त सारणी", "name_en": "Modern Periodic Table"},
                                {"id": "sci_chem_ch_05_topic_06", "name_hi": "समूह", "name_en": "Groups"},
                                {"id": "sci_chem_ch_05_topic_07", "name_hi": "आवर्त", "name_en": "Periods"},
                                {"id": "sci_chem_ch_05_topic_08", "name_hi": "संयोजकता", "name_en": "Valency"},
                                {"id": "sci_chem_ch_05_topic_09", "name_hi": "परमाणु आकार", "name_en": "Atomic Size"},
                                {"id": "sci_chem_ch_05_topic_10", "name_hi": "धात्विक गुण", "name_en": "Metallic Character"},
                                {"id": "sci_chem_ch_05_topic_11", "name_hi": "अधात्विक गुण", "name_en": "Non-Metallic Character"},
                                {"id": "sci_chem_ch_05_topic_12", "name_hi": "आवर्तिता", "name_en": "Periodicity"}
                            ]
                        }
                    ]
                },
                {
                    "id": "sci_sec_biology",
                    "name_hi": "जीव विज्ञान एवं पर्यावरण",
                    "name_en": "Biology & Environment",
                    "chapters": [
                        {
                            "id": "sci_bio_ch_06",
                            "code": "CH06",
                            "chapter_number": 6,
                            "name_hi": "जैव प्रक्रम",
                            "name_en": "Life Processes",
                            "topics": [
                                {"id": "sci_bio_ch_06_topic_01", "name_hi": "जैव प्रक्रम", "name_en": "Life Processes"},
                                {"id": "sci_bio_ch_06_topic_02", "name_hi": "पोषण", "name_en": "Nutrition"},
                                {"id": "sci_bio_ch_06_topic_03", "name_hi": "स्वपोषी पोषण", "name_en": "Autotrophic Nutrition"},
                                {"id": "sci_bio_ch_06_topic_04", "name_hi": "परपोषी पोषण", "name_en": "Heterotrophic Nutrition"},
                                {"id": "sci_bio_ch_06_topic_05", "name_hi": "प्रकाश संश्लेषण", "name_en": "Photosynthesis"},
                                {"id": "sci_bio_ch_06_topic_06", "name_hi": "मानव पाचन", "name_en": "Human Digestion"},
                                {"id": "sci_bio_ch_06_topic_07", "name_hi": "श्वसन", "name_en": "Respiration"},
                                {"id": "sci_bio_ch_06_topic_08", "name_hi": "वायवीय श्वसन", "name_en": "Aerobic Respiration"},
                                {"id": "sci_bio_ch_06_topic_09", "name_hi": "अवायवीय श्वसन", "name_en": "Anaerobic Respiration"},
                                {"id": "sci_bio_ch_06_topic_10", "name_hi": "मानव श्वसन तंत्र", "name_en": "Human Respiratory System"},
                                {"id": "sci_bio_ch_06_topic_11", "name_hi": "परिवहन", "name_en": "Transportation"},
                                {"id": "sci_bio_ch_06_topic_12", "name_hi": "मानव परिसंचरण तंत्र", "name_en": "Human Circulatory System"},
                                {"id": "sci_bio_ch_06_topic_13", "name_hi": "रक्त", "name_en": "Blood"},
                                {"id": "sci_bio_ch_06_topic_14", "name_hi": "हृदय", "name_en": "Heart"},
                                {"id": "sci_bio_ch_06_topic_15", "name_hi": "उत्सर्जन", "name_en": "Excretion"},
                                {"id": "sci_bio_ch_06_topic_16", "name_hi": "मानव उत्सर्जन तंत्र", "name_en": "Human Excretory System"},
                                {"id": "sci_bio_ch_06_topic_17", "name_hi": "पौधों में परिवहन एवं उत्सर्जन", "name_en": "Transport and Excretion in Plants"}
                            ]
                        },
                        {
                            "id": "sci_bio_ch_07",
                            "code": "CH07",
                            "chapter_number": 7,
                            "name_hi": "नियंत्रण एवं समन्वय",
                            "name_en": "Control and Coordination",
                            "topics": [
                                {"id": "sci_bio_ch_07_topic_01", "name_hi": "नियंत्रण एवं समन्वय", "name_en": "Control and Coordination"},
                                {"id": "sci_bio_ch_07_topic_02", "name_hi": "तंत्रिका तंत्र", "name_en": "Nervous System"},
                                {"id": "sci_bio_ch_07_topic_03", "name_hi": "न्यूरॉन", "name_en": "Neuron"},
                                {"id": "sci_bio_ch_07_topic_04", "name_hi": "प्रतिवर्ती क्रिया", "name_en": "Reflex Action"},
                                {"id": "sci_bio_ch_07_topic_05", "name_hi": "मानव मस्तिष्क", "name_en": "Human Brain"},
                                {"id": "sci_bio_ch_07_topic_06", "name_hi": "पौधों में समन्वय", "name_en": "Coordination in Plants"},
                                {"id": "sci_bio_ch_07_topic_07", "name_hi": "पादप हार्मोन", "name_en": "Plant Hormones"},
                                {"id": "sci_bio_ch_07_topic_08", "name_hi": "जंतु हार्मोन", "name_en": "Animal Hormones"},
                                {"id": "sci_bio_ch_07_topic_09", "name_hi": "अंतःस्रावी तंत्र", "name_en": "Endocrine System"},
                                {"id": "sci_bio_ch_07_topic_10", "name_hi": "अनुवर्तन गतियाँ", "name_en": "Tropic Movements"}
                            ]
                        },
                        {
                            "id": "sci_bio_ch_08",
                            "code": "CH08",
                            "chapter_number": 8,
                            "name_hi": "जीव जनन कैसे करते हैं?",
                            "name_en": "How do Organisms Reproduce?",
                            "topics": [
                                {"id": "sci_bio_ch_08_topic_01", "name_hi": "जनन", "name_en": "Reproduction"},
                                {"id": "sci_bio_ch_08_topic_02", "name_hi": "अलैंगिक जनन", "name_en": "Asexual Reproduction"},
                                {"id": "sci_bio_ch_08_topic_03", "name_hi": "द्विखंडन", "name_en": "Binary Fission"},
                                {"id": "sci_bio_ch_08_topic_04", "name_hi": "बहुखंडन", "name_en": "Multiple Fission"},
                                {"id": "sci_bio_ch_08_topic_05", "name_hi": "मुकुलन", "name_en": "Budding"},
                                {"id": "sci_bio_ch_08_topic_06", "name_hi": "विखंडन", "name_en": "Fragmentation"},
                                {"id": "sci_bio_ch_08_topic_07", "name_hi": "पुनर्जनन", "name_en": "Regeneration"},
                                {"id": "sci_bio_ch_08_topic_08", "name_hi": "कायिक प्रवर्धन", "name_en": "Vegetative Propagation"},
                                {"id": "sci_bio_ch_08_topic_09", "name_hi": "लैंगिक जनन", "name_en": "Sexual Reproduction"},
                                {"id": "sci_bio_ch_08_topic_10", "name_hi": "पौधों में लैंगिक जनन", "name_en": "Sexual Reproduction in Plants"},
                                {"id": "sci_bio_ch_08_topic_11", "name_hi": "मानव जनन तंत्र", "name_en": "Human Reproductive System"},
                                {"id": "sci_bio_ch_08_topic_12", "name_hi": "मासिक धर्म चक्र", "name_en": "Menstrual Cycle"},
                                {"id": "sci_bio_ch_08_topic_13", "name_hi": "निषेचन", "name_en": "Fertilisation"},
                                {"id": "sci_bio_ch_08_topic_14", "name_hi": "गर्भावस्था", "name_en": "Pregnancy"},
                                {"id": "sci_bio_ch_08_topic_15", "name_hi": "प्रजनन स्वास्थ्य", "name_en": "Reproductive Health"},
                                {"id": "sci_bio_ch_08_topic_16", "name_hi": "गर्भनिरोध", "name_en": "Contraception"}
                            ]
                        },
                        {
                            "id": "sci_bio_ch_09",
                            "code": "CH09",
                            "chapter_number": 9,
                            "name_hi": "आनुवंशिकता एवं जैव विकास",
                            "name_en": "Heredity and Evolution",
                            "topics": [
                                {"id": "sci_bio_ch_09_topic_01", "name_hi": "आनुवंशिकता", "name_en": "Heredity"},
                                {"id": "sci_bio_ch_09_topic_02", "name_hi": "विभिन्नता", "name_en": "Variation"},
                                {"id": "sci_bio_ch_09_topic_03", "name_hi": "मेंडल के प्रयोग", "name_en": "Mendel's Experiments"},
                                {"id": "sci_bio_ch_09_topic_04", "name_hi": "प्रभावी लक्षण", "name_en": "Dominant Traits"},
                                {"id": "sci_bio_ch_09_topic_05", "name_hi": "अप्रभावी लक्षण", "name_en": "Recessive Traits"},
                                {"id": "sci_bio_ch_09_topic_06", "name_hi": "आनुवंशिकता के नियम", "name_en": "Laws of Heredity"},
                                {"id": "sci_bio_ch_09_topic_07", "name_hi": "लिंग निर्धारण", "name_en": "Sex Determination"},
                                {"id": "sci_bio_ch_09_topic_08", "name_hi": "जैव विकास", "name_en": "Evolution"},
                                {"id": "sci_bio_ch_09_topic_09", "name_hi": "प्राकृतिक चयन", "name_en": "Natural Selection"},
                                {"id": "sci_bio_ch_09_topic_10", "name_hi": "उपार्जित लक्षण", "name_en": "Acquired Traits"},
                                {"id": "sci_bio_ch_09_topic_11", "name_hi": "जीवाश्म", "name_en": "Fossils"},
                                {"id": "sci_bio_ch_09_topic_12", "name_hi": "विकासीय संबंध", "name_en": "Evolutionary Relationships"}
                            ]
                        },
                        {
                            "id": "sci_bio_ch_15",
                            "code": "CH15",
                            "chapter_number": 15,
                            "name_hi": "हमारा पर्यावरण",
                            "name_en": "Our Environment",
                            "topics": [
                                {"id": "sci_bio_ch_15_topic_01", "name_hi": "पारितंत्र", "name_en": "Ecosystem"},
                                {"id": "sci_bio_ch_15_topic_02", "name_hi": "पारितंत्र के घटक", "name_en": "Components of Ecosystem"},
                                {"id": "sci_bio_ch_15_topic_03", "name_hi": "खाद्य श्रृंखला", "name_en": "Food Chain"},
                                {"id": "sci_bio_ch_15_topic_04", "name_hi": "खाद्य जाल", "name_en": "Food Web"},
                                {"id": "sci_bio_ch_15_topic_05", "name_hi": "पोषी स्तर", "name_en": "Trophic Levels"},
                                {"id": "sci_bio_ch_15_topic_06", "name_hi": "ऊर्जा प्रवाह", "name_en": "Energy Flow"},
                                {"id": "sci_bio_ch_15_topic_07", "name_hi": "जैव आवर्धन", "name_en": "Biological Magnification"},
                                {"id": "sci_bio_ch_15_topic_08", "name_hi": "ओजोन परत", "name_en": "Ozone Layer"},
                                {"id": "sci_bio_ch_15_topic_09", "name_hi": "पर्यावरणीय समस्याएँ", "name_en": "Environmental Problems"},
                                {"id": "sci_bio_ch_15_topic_10", "name_hi": "अपशिष्ट प्रबंधन", "name_en": "Waste Management"}
                            ]
                        },
                        {
                            "id": "sci_bio_ch_16",
                            "code": "CH16",
                            "chapter_number": 16,
                            "name_hi": "प्राकृतिक संसाधनों का संपोषित प्रबंधन",
                            "name_en": "Sustainable Management of Natural Resources",
                            "topics": [
                                {"id": "sci_bio_ch_16_topic_01", "name_hi": "प्राकृतिक संसाधन", "name_en": "Natural Resources"},
                                {"id": "sci_bio_ch_16_topic_02", "name_hi": "संपोषित प्रबंधन", "name_en": "Sustainable Management"},
                                {"id": "sci_bio_ch_16_topic_03", "name_hi": "वन संसाधन", "name_en": "Forest Resources"},
                                {"id": "sci_bio_ch_16_topic_04", "name_hi": "वन संरक्षण", "name_en": "Forest Conservation"},
                                {"id": "sci_bio_ch_16_topic_05", "name_hi": "जल संसाधन", "name_en": "Water Resources"},
                                {"id": "sci_bio_ch_16_topic_06", "name_hi": "कोयला और पेट्रोलियम", "name_en": "Coal and Petroleum"},
                                {"id": "sci_bio_ch_16_topic_07", "name_hi": "वन्यजीव संरक्षण", "name_en": "Wildlife Conservation"},
                                {"id": "sci_bio_ch_16_topic_08", "name_hi": "हितधारक", "name_en": "Stakeholders"},
                                {"id": "sci_bio_ch_16_topic_09", "name_hi": "सतत विकास", "name_en": "Sustainable Development"}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
SYLLABUS_DATA["subjects"].append(science_subject)

# ==========================================
# 3. SOCIAL SCIENCE — सामाजिक विज्ञान (5 Books)
# ==========================================
social_subject = {
    "id": "social",
    "code": "SST",
    "name_hi": "सामाजिक विज्ञान",
    "name_en": "Social Science",
    "icon": "fa-globe-americas",
    "color": "from-amber-600 to-orange-600",
    "accent": "#f59e0b",
    "books": [
        # Book 1: History
        {
            "id": "sst_book_01",
            "name_hi": "इतिहास की दुनिया (भाग 2)",
            "name_en": "World of History (Part 2)",
            "chapters": [
                {
                    "id": "hist_ch_01",
                    "code": "CH01",
                    "chapter_number": 1,
                    "name_hi": "यूरोप में राष्ट्रवाद",
                    "name_en": "Nationalism in Europe",
                    "topics": [
                        {"id": "hist_ch_01_topic_01", "name_hi": "राष्ट्रवाद", "name_en": "Nationalism"},
                        {"id": "hist_ch_01_topic_02", "name_hi": "फ्रांसीसी क्रांति", "name_en": "French Revolution"},
                        {"id": "hist_ch_01_topic_03", "name_hi": "नेपोलियन", "name_en": "Napoleon"},
                        {"id": "hist_ch_01_topic_04", "name_hi": "उदारवाद", "name_en": "Liberalism"},
                        {"id": "hist_ch_01_topic_05", "name_hi": "रूढ़िवाद", "name_en": "Conservatism"},
                        {"id": "hist_ch_01_topic_06", "name_hi": "जर्मनी का एकीकरण", "name_en": "Unification of Germany"},
                        {"id": "hist_ch_01_topic_07", "name_hi": "इटली का एकीकरण", "name_en": "Unification of Italy"},
                        {"id": "hist_ch_01_topic_08", "name_hi": "ब्रिटेन", "name_en": "Britain"},
                        {"id": "hist_ch_01_topic_09", "name_hi": "बाल्कन क्षेत्र", "name_en": "Balkan Region"},
                        {"id": "hist_ch_01_topic_10", "name_hi": "राष्ट्रवाद और साम्राज्यवाद", "name_en": "Nationalism and Imperialism"}
                    ]
                },
                {
                    "id": "hist_ch_02",
                    "code": "CH02",
                    "chapter_number": 2,
                    "name_hi": "समाजवाद एवं साम्यवाद",
                    "name_en": "Socialism and Communism",
                    "topics": [
                        {"id": "hist_ch_02_topic_01", "name_hi": "समाजवाद", "name_en": "Socialism"},
                        {"id": "hist_ch_02_topic_02", "name_hi": "पूँजीवाद", "name_en": "Capitalism"},
                        {"id": "hist_ch_02_topic_03", "name_hi": "कार्ल मार्क्स", "name_en": "Karl Marx"},
                        {"id": "hist_ch_02_topic_04", "name_hi": "फ्रेडरिक एंगेल्स", "name_en": "Friedrich Engels"},
                        {"id": "hist_ch_02_topic_05", "name_hi": "रूसी क्रांति", "name_en": "Russian Revolution"},
                        {"id": "hist_ch_02_topic_06", "name_hi": "बोल्शेविक", "name_en": "Bolsheviks"},
                        {"id": "hist_ch_02_topic_07", "name_hi": "अक्टूबर क्रांति", "name_en": "October Revolution"},
                        {"id": "hist_ch_02_topic_08", "name_hi": "सोवियत संघ", "name_en": "Soviet Union"},
                        {"id": "hist_ch_02_topic_09", "name_hi": "साम्यवाद", "name_en": "Communism"}
                    ]
                },
                {
                    "id": "hist_ch_03",
                    "code": "CH03",
                    "chapter_number": 3,
                    "name_hi": "हिंद-चीन में राष्ट्रवादी आंदोलन",
                    "name_en": "Nationalist Movement in Indo-China",
                    "topics": [
                        {"id": "hist_ch_03_topic_01", "name_hi": "हिंद-चीन", "name_en": "Indo-China"},
                        {"id": "hist_ch_03_topic_02", "name_hi": "फ्रांसीसी उपनिवेशवाद", "name_en": "French Colonialism"},
                        {"id": "hist_ch_03_topic_03", "name_hi": "वियतनामी राष्ट्रवाद", "name_en": "Vietnamese Nationalism"},
                        {"id": "hist_ch_03_topic_04", "name_hi": "फान बोई चाऊ", "name_en": "Phan Boi Chau"},
                        {"id": "hist_ch_03_topic_05", "name_hi": "फान चु त्रिन्ह", "name_en": "Phan Chu Trinh"},
                        {"id": "hist_ch_03_topic_06", "name_hi": "हो ची मिन्ह", "name_en": "Ho Chi Minh"},
                        {"id": "hist_ch_03_topic_07", "name_hi": "वियतनामी आंदोलन", "name_en": "Vietnamese Movement"},
                        {"id": "hist_ch_03_topic_08", "name_hi": "औपनिवेशिक शिक्षा", "name_en": "Colonial Education"}
                    ]
                },
                {
                    "id": "hist_ch_04",
                    "code": "CH04",
                    "chapter_number": 4,
                    "name_hi": "भारत में राष्ट्रवाद",
                    "name_en": "Nationalism in India",
                    "topics": [
                        {"id": "hist_ch_04_topic_01", "name_hi": "प्रथम विश्व युद्ध", "name_en": "First World War"},
                        {"id": "hist_ch_04_topic_02", "name_hi": "सत्याग्रह", "name_en": "Satyagraha"},
                        {"id": "hist_ch_04_topic_03", "name_hi": "रॉलेट एक्ट", "name_en": "Rowlatt Act"},
                        {"id": "hist_ch_04_topic_04", "name_hi": "जलियाँवाला बाग", "name_en": "Jallianwala Bagh"},
                        {"id": "hist_ch_04_topic_05", "name_hi": "असहयोग आंदोलन", "name_en": "Non-Cooperation Movement"},
                        {"id": "hist_ch_04_topic_06", "name_hi": "सविनय अवज्ञा आंदोलन", "name_en": "Civil Disobedience Movement"},
                        {"id": "hist_ch_04_topic_07", "name_hi": "नमक मार्च", "name_en": "Salt March"},
                        {"id": "hist_ch_04_topic_08", "name_hi": "साइमन कमीशन", "name_en": "Simon Commission"},
                        {"id": "hist_ch_04_topic_09", "name_hi": "भारत छोड़ो आंदोलन", "name_en": "Quit India Movement"},
                        {"id": "hist_ch_04_topic_10", "name_hi": "राष्ट्रवादी प्रतीक", "name_en": "Nationalist Symbols"}
                    ]
                },
                {
                    "id": "hist_ch_05",
                    "code": "CH05",
                    "chapter_number": 5,
                    "name_hi": "अर्थव्यवस्था और आजीविका",
                    "name_en": "Economy and Livelihood",
                    "topics": [
                        {"id": "hist_ch_05_topic_01", "name_hi": "औद्योगीकरण", "name_en": "Industrialisation"},
                        {"id": "hist_ch_05_topic_02", "name_hi": "श्रमिक", "name_en": "Workers"},
                        {"id": "hist_ch_05_topic_03", "name_hi": "श्रम", "name_en": "Labour"},
                        {"id": "hist_ch_05_topic_04", "name_hi": "उद्योग", "name_en": "Industries"},
                        {"id": "hist_ch_05_topic_05", "name_hi": "रोजगार", "name_en": "Employment"},
                        {"id": "hist_ch_05_topic_06", "name_hi": "अर्थव्यवस्था", "name_en": "Economy"},
                        {"id": "hist_ch_05_topic_07", "name_hi": "आजीविका", "name_en": "Livelihood"},
                        {"id": "hist_ch_05_topic_08", "name_hi": "औद्योगिक विकास", "name_en": "Industrial Development"}
                    ]
                },
                {
                    "id": "hist_ch_06",
                    "code": "CH06",
                    "chapter_number": 6,
                    "name_hi": "शहरीकरण एवं शहरी जीवन",
                    "name_en": "Urbanization and Urban Life",
                    "topics": [
                        {"id": "hist_ch_06_topic_01", "name_hi": "शहरीकरण", "name_en": "Urbanisation"},
                        {"id": "hist_ch_06_topic_02", "name_hi": "शहर", "name_en": "Cities"},
                        {"id": "hist_ch_06_topic_03", "name_hi": "औद्योगिक शहर", "name_en": "Industrial Cities"},
                        {"id": "hist_ch_06_topic_04", "name_hi": "शहरी जीवन", "name_en": "Urban Life"},
                        {"id": "hist_ch_06_topic_05", "name_hi": "प्रवास", "name_en": "Migration"},
                        {"id": "hist_ch_06_topic_06", "name_hi": "श्रमिक जीवन", "name_en": "Workers' Life"},
                        {"id": "hist_ch_06_topic_07", "name_hi": "आवास", "name_en": "Housing"},
                        {"id": "hist_ch_06_topic_08", "name_hi": "परिवहन", "name_en": "Transport"},
                        {"id": "hist_ch_06_topic_09", "name_hi": "सामाजिक परिवर्तन", "name_en": "Social Change"}
                    ]
                },
                {
                    "id": "hist_ch_07",
                    "code": "CH07",
                    "chapter_number": 7,
                    "name_hi": "व्यापार और भूमंडलीकरण",
                    "name_en": "Trade and Globalization",
                    "topics": [
                        {"id": "hist_ch_07_topic_01", "name_hi": "व्यापार", "name_en": "Trade"},
                        {"id": "hist_ch_07_topic_02", "name_hi": "भूमंडलीकरण", "name_en": "Globalisation"},
                        {"id": "hist_ch_07_topic_03", "name_hi": "औद्योगीकरण", "name_en": "Industrialisation"},
                        {"id": "hist_ch_07_topic_04", "name_hi": "अंतरराष्ट्रीय व्यापार", "name_en": "International Trade"},
                        {"id": "hist_ch_07_topic_05", "name_hi": "औपनिवेशिक व्यापार", "name_en": "Colonial Trade"},
                        {"id": "hist_ch_07_topic_06", "name_hi": "बाजार", "name_en": "Markets"},
                        {"id": "hist_ch_07_topic_07", "name_hi": "वैश्विक अर्थव्यवस्था", "name_en": "Global Economy"},
                        {"id": "hist_ch_07_topic_08", "name_hi": "आर्थिक एकीकरण", "name_en": "Economic Integration"}
                    ]
                },
                {
                    "id": "hist_ch_08",
                    "code": "CH08",
                    "chapter_number": 8,
                    "name_hi": "प्रेस-संस्कृति और राष्ट्रवाद",
                    "name_en": "Press Culture and Nationalism",
                    "topics": [
                        {"id": "hist_ch_08_topic_01", "name_hi": "मुद्रण प्रेस", "name_en": "Printing Press"},
                        {"id": "hist_ch_08_topic_02", "name_hi": "मुद्रण संस्कृति", "name_en": "Print Culture"},
                        {"id": "hist_ch_08_topic_03", "name_hi": "समाचार पत्र", "name_en": "Newspapers"},
                        {"id": "hist_ch_08_topic_04", "name_hi": "पुस्तकें", "name_en": "Books"},
                        {"id": "hist_ch_08_topic_05", "name_hi": "जनमत", "name_en": "Public Opinion"},
                        {"id": "hist_ch_08_topic_06", "name_hi": "सामाजिक सुधार", "name_en": "Social Reform"},
                        {"id": "hist_ch_08_topic_07", "name_hi": "राष्ट्रवाद", "name_en": "Nationalism"},
                        {"id": "hist_ch_08_topic_08", "name_hi": "सेंसरशिप", "name_en": "Censorship"},
                        {"id": "hist_ch_08_topic_09", "name_hi": "प्रेस और भारतीय राष्ट्रवाद", "name_en": "Print and Indian Nationalism"}
                    ]
                }
            ]
        },

        # Book 2: Geography
        {
            "id": "sst_book_02",
            "name_hi": "भारत: संसाधन एवं उपयोग",
            "name_en": "India: Resources and Utilization",
            "chapters": [
                {
                    "id": "geo_ch_01",
                    "code": "CH01",
                    "chapter_number": 1,
                    "name_hi": "भारत: संसाधन एवं उपयोग",
                    "name_en": "India: Resources and Utilization",
                    "topics": [
                        {"id": "geo_ch_01_topic_01", "name_hi": "प्राकृतिक संसाधन", "name_en": "Natural Resources"},
                        {"id": "geo_ch_01_topic_02", "name_hi": "जल संसाधन", "name_en": "Water Resources"},
                        {"id": "geo_ch_01_topic_03", "name_hi": "वन एवं वन्य जीव संसाधन", "name_en": "Forest and Wildlife Resources"},
                        {"id": "geo_ch_01_topic_04", "name_hi": "खनिज संसाधन", "name_en": "Mineral Resources"},
                        {"id": "geo_ch_01_topic_05", "name_hi": "शक्ति/ऊर्जा संसाधन", "name_en": "Power and Energy Resources"}
                    ]
                },
                {
                    "id": "geo_ch_02",
                    "code": "CH02",
                    "chapter_number": 2,
                    "name_hi": "कृषि",
                    "name_en": "Agriculture",
                    "topics": [
                        {"id": "geo_ch_02_topic_01", "name_hi": "कृषि के प्रकार", "name_en": "Types of Farming"},
                        {"id": "geo_ch_02_topic_02", "name_hi": "फसलें", "name_en": "Crops"},
                        {"id": "geo_ch_02_topic_03", "name_hi": "प्रमुख फसलें", "name_en": "Major Crops"},
                        {"id": "geo_ch_02_topic_04", "name_hi": "धान", "name_en": "Rice"},
                        {"id": "geo_ch_02_topic_05", "name_hi": "गेहूँ", "name_en": "Wheat"},
                        {"id": "geo_ch_02_topic_06", "name_hi": "मोटे अनाज", "name_en": "Millets"},
                        {"id": "geo_ch_02_topic_07", "name_hi": "दलहन", "name_en": "Pulses"},
                        {"id": "geo_ch_02_topic_08", "name_hi": "गन्ना", "name_en": "Sugarcane"},
                        {"id": "geo_ch_02_topic_09", "name_hi": "चाय", "name_en": "Tea"},
                        {"id": "geo_ch_02_topic_10", "name_hi": "कॉफी", "name_en": "Coffee"},
                        {"id": "geo_ch_02_topic_11", "name_hi": "कपास", "name_en": "Cotton"},
                        {"id": "geo_ch_02_topic_12", "name_hi": "जूट", "name_en": "Jute"},
                        {"id": "geo_ch_02_topic_13", "name_hi": "कृषि विकास", "name_en": "Agricultural Development"},
                        {"id": "geo_ch_02_topic_14", "name_hi": "कृषि समस्याएँ", "name_en": "Agricultural Problems"}
                    ]
                },
                {
                    "id": "geo_ch_03",
                    "code": "CH03",
                    "chapter_number": 3,
                    "name_hi": "निर्माण उद्योग",
                    "name_en": "Manufacturing Industries",
                    "topics": [
                        {"id": "geo_ch_03_topic_01", "name_hi": "विनिर्माण", "name_en": "Manufacturing"},
                        {"id": "geo_ch_03_topic_02", "name_hi": "विनिर्माण का महत्व", "name_en": "Importance of Manufacturing"},
                        {"id": "geo_ch_03_topic_03", "name_hi": "औद्योगिक अवस्थिति", "name_en": "Industrial Location"},
                        {"id": "geo_ch_03_topic_04", "name_hi": "कृषि-आधारित उद्योग", "name_en": "Agro-Based Industries"},
                        {"id": "geo_ch_03_topic_05", "name_hi": "खनिज-आधारित उद्योग", "name_en": "Mineral-Based Industries"},
                        {"id": "geo_ch_03_topic_06", "name_hi": "वस्त्र उद्योग", "name_en": "Textile Industry"},
                        {"id": "geo_ch_03_topic_07", "name_hi": "लौह-इस्पात उद्योग", "name_en": "Iron and Steel Industry"},
                        {"id": "geo_ch_03_topic_08", "name_hi": "रासायनिक उद्योग", "name_en": "Chemical Industries"},
                        {"id": "geo_ch_03_topic_09", "name_hi": "औद्योगिक प्रदूषण", "name_en": "Industrial Pollution"},
                        {"id": "geo_ch_03_topic_10", "name_hi": "पर्यावरण प्रबंधन", "name_en": "Environmental Management"}
                    ]
                },
                {
                    "id": "geo_ch_04",
                    "code": "CH04",
                    "chapter_number": 4,
                    "name_hi": "परिवहन, संचार एवं व्यापार",
                    "name_en": "Transport, Communication and Trade",
                    "topics": [
                        {"id": "geo_ch_04_topic_01", "name_hi": "सड़क परिवहन", "name_en": "Roadways"},
                        {"id": "geo_ch_04_topic_02", "name_hi": "रेल परिवहन", "name_en": "Railways"},
                        {"id": "geo_ch_04_topic_03", "name_hi": "पाइपलाइन", "name_en": "Pipelines"},
                        {"id": "geo_ch_04_topic_04", "name_hi": "जल परिवहन", "name_en": "Waterways"},
                        {"id": "geo_ch_04_topic_05", "name_hi": "वायु परिवहन", "name_en": "Airways"},
                        {"id": "geo_ch_04_topic_06", "name_hi": "संचार", "name_en": "Communication"},
                        {"id": "geo_ch_04_topic_07", "name_hi": "अंतरराष्ट्रीय व्यापार", "name_en": "International Trade"},
                        {"id": "geo_ch_04_topic_08", "name_hi": "बंदरगाह", "name_en": "Ports"},
                        {"id": "geo_ch_04_topic_09", "name_hi": "पर्यटन", "name_en": "Tourism"}
                    ]
                },
                {
                    "id": "geo_ch_05",
                    "code": "CH05",
                    "chapter_number": 5,
                    "name_hi": "बिहार: कृषि एवं वन संसाधन",
                    "name_en": "Bihar: Agriculture and Forest Resources",
                    "topics": [
                        {"id": "geo_ch_05_topic_01", "name_hi": "बिहार की कृषि", "name_en": "Agriculture in Bihar"},
                        {"id": "geo_ch_05_topic_02", "name_hi": "बिहार की प्रमुख फसलें", "name_en": "Major Crops of Bihar"},
                        {"id": "geo_ch_05_topic_03", "name_hi": "सिंचाई", "name_en": "Irrigation"},
                        {"id": "geo_ch_05_topic_04", "name_hi": "कृषि समस्याएँ", "name_en": "Agricultural Problems"},
                        {"id": "geo_ch_05_topic_05", "name_hi": "बिहार के वन संसाधन", "name_en": "Forest Resources of Bihar"},
                        {"id": "geo_ch_05_topic_06", "name_hi": "वन संरक्षण", "name_en": "Forest Conservation"},
                        {"id": "geo_ch_05_topic_07", "name_hi": "कृषि विकास", "name_en": "Agricultural Development"}
                    ]
                },
                {
                    "id": "geo_ch_06",
                    "code": "CH06",
                    "chapter_number": 6,
                    "name_hi": "मानचित्र अध्ययन - उच्चावच प्रदर्शन",
                    "name_en": "Map Reading and Relief Representation",
                    "topics": [
                        {"id": "geo_ch_06_topic_01", "name_hi": "मानचित्र अध्ययन", "name_en": "Map Reading"},
                        {"id": "geo_ch_06_topic_02", "name_hi": "मानचित्र संकेत", "name_en": "Map Symbols"},
                        {"id": "geo_ch_06_topic_03", "name_hi": "मापनी", "name_en": "Scale"},
                        {"id": "geo_ch_06_topic_04", "name_hi": "उच्चावच", "name_en": "Relief"},
                        {"id": "geo_ch_06_topic_05", "name_hi": "समोच्च रेखाएँ", "name_en": "Contour Lines"},
                        {"id": "geo_ch_06_topic_06", "name_hi": "उच्चावच प्रदर्शन", "name_en": "Relief Representation"},
                        {"id": "geo_ch_06_topic_07", "name_hi": "स्थलाकृतिक जानकारी", "name_en": "Topographical Information"}
                    ]
                }
            ]
        },

        # Book 3: Disaster Management
        {
            "id": "sst_book_03",
            "name_hi": "आपदा प्रबंधन",
            "name_en": "Disaster Management",
            "chapters": [
                {
                    "id": "dm_ch_01",
                    "code": "CH01",
                    "chapter_number": 1,
                    "name_hi": "प्राकृतिक आपदा: एक परिचय",
                    "name_en": "Natural Disasters: An Introduction",
                    "topics": [
                        {"id": "dm_ch_01_topic_01", "name_hi": "प्राकृतिक आपदा", "name_en": "Natural Disaster"},
                        {"id": "dm_ch_01_topic_02", "name_hi": "आपदाओं के प्रकार", "name_en": "Types of Disasters"},
                        {"id": "dm_ch_01_topic_03", "name_hi": "आपदा के कारण", "name_en": "Causes"},
                        {"id": "dm_ch_01_topic_04", "name_hi": "आपदा के प्रभाव", "name_en": "Effects"},
                        {"id": "dm_ch_01_topic_05", "name_hi": "आपदा प्रबंधन", "name_en": "Disaster Management"},
                        {"id": "dm_ch_01_topic_06", "name_hi": "जोखिम", "name_en": "Risk"},
                        {"id": "dm_ch_01_topic_07", "name_hi": "संवेदनशीलता", "name_en": "Vulnerability"},
                        {"id": "dm_ch_01_topic_08", "name_hi": "तैयारी", "name_en": "Preparedness"}
                    ]
                },
                {
                    "id": "dm_ch_02",
                    "code": "CH02",
                    "chapter_number": 2,
                    "name_hi": "प्राकृतिक आपदा एवं प्रबंधन: बाढ़ और सुखाड़",
                    "name_en": "Flood and Drought",
                    "topics": [
                        {"id": "dm_ch_02_topic_01", "name_hi": "बाढ़", "name_en": "Flood"},
                        {"id": "dm_ch_02_topic_02", "name_hi": "बाढ़ के कारण", "name_en": "Causes of Flood"},
                        {"id": "dm_ch_02_topic_03", "name_hi": "बाढ़ के प्रभाव", "name_en": "Effects of Flood"},
                        {"id": "dm_ch_02_topic_04", "name_hi": "बाढ़ प्रबंधन", "name_en": "Flood Management"},
                        {"id": "dm_ch_02_topic_05", "name_hi": "सुखाड़", "name_en": "Drought"},
                        {"id": "dm_ch_02_topic_06", "name_hi": "सुखाड़ के कारण", "name_en": "Causes of Drought"},
                        {"id": "dm_ch_02_topic_07", "name_hi": "सुखाड़ के प्रभाव", "name_en": "Effects of Drought"},
                        {"id": "dm_ch_02_topic_08", "name_hi": "सुखाड़ प्रबंधन", "name_en": "Drought Management"}
                    ]
                },
                {
                    "id": "dm_ch_03",
                    "code": "CH03",
                    "chapter_number": 3,
                    "name_hi": "प्राकृतिक आपदा एवं प्रबंधन: भूकंप एवं सुनामी",
                    "name_en": "Earthquake and Tsunami",
                    "topics": [
                        {"id": "dm_ch_03_topic_01", "name_hi": "भूकंप", "name_en": "Earthquake"},
                        {"id": "dm_ch_03_topic_02", "name_hi": "भूकंप के कारण", "name_en": "Causes of Earthquake"},
                        {"id": "dm_ch_03_topic_03", "name_hi": "भूकंपीय तरंगें", "name_en": "Seismic Waves"},
                        {"id": "dm_ch_03_topic_04", "name_hi": "भूकंप सुरक्षा", "name_en": "Earthquake Safety"},
                        {"id": "dm_ch_03_topic_05", "name_hi": "सुनामी", "name_en": "Tsunami"},
                        {"id": "dm_ch_03_topic_06", "name_hi": "सुनामी के कारण", "name_en": "Causes of Tsunami"},
                        {"id": "dm_ch_03_topic_07", "name_hi": "सुनामी के प्रभाव", "name_en": "Effects of Tsunami"},
                        {"id": "dm_ch_03_topic_08", "name_hi": "सुनामी से तैयारी", "name_en": "Tsunami Preparedness"}
                    ]
                },
                {
                    "id": "dm_ch_04",
                    "code": "CH04",
                    "chapter_number": 4,
                    "name_hi": "जीवन रक्षक आकस्मिक प्रबंधन",
                    "name_en": "Life-Saving Emergency Management",
                    "topics": [
                        {"id": "dm_ch_04_topic_01", "name_hi": "आकस्मिक प्रबंधन", "name_en": "Emergency Management"},
                        {"id": "dm_ch_04_topic_02", "name_hi": "प्राथमिक उपचार", "name_en": "First Aid"},
                        {"id": "dm_ch_04_topic_03", "name_hi": "बचाव", "name_en": "Rescue"},
                        {"id": "dm_ch_04_topic_04", "name_hi": "निकासी", "name_en": "Evacuation"},
                        {"id": "dm_ch_04_topic_05", "name_hi": "आपातकालीन प्रतिक्रिया", "name_en": "Emergency Response"},
                        {"id": "dm_ch_04_topic_06", "name_hi": "जीवन रक्षक उपाय", "name_en": "Life-Saving Measures"}
                    ]
                },
                {
                    "id": "dm_ch_05",
                    "code": "CH05",
                    "chapter_number": 5,
                    "name_hi": "आपदा काल में वैकल्पिक संचार व्यवस्था",
                    "name_en": "Alternative Communication Systems During Disasters",
                    "topics": [
                        {"id": "dm_ch_05_topic_01", "name_hi": "आपदा के समय संचार", "name_en": "Communication During Disasters"},
                        {"id": "dm_ch_05_topic_02", "name_hi": "वैकल्पिक संचार", "name_en": "Alternative Communication"},
                        {"id": "dm_ch_05_topic_03", "name_hi": "आपातकालीन संचार", "name_en": "Emergency Communication"},
                        {"id": "dm_ch_05_topic_04", "name_hi": "संचार प्रणालियाँ", "name_en": "Communication Systems"},
                        {"id": "dm_ch_05_topic_05", "name_hi": "आपदा सूचना", "name_en": "Disaster Information"}
                    ]
                },
                {
                    "id": "dm_ch_06",
                    "code": "CH06",
                    "chapter_number": 6,
                    "name_hi": "आपदा और सह-अस्तित्व",
                    "name_en": "Disaster and Co-existence",
                    "topics": [
                        {"id": "dm_ch_06_topic_01", "name_hi": "आपदा और समाज", "name_en": "Disaster and Society"},
                        {"id": "dm_ch_06_topic_02", "name_hi": "सह-अस्तित्व", "name_en": "Co-existence"},
                        {"id": "dm_ch_06_topic_03", "name_hi": "सामुदायिक भागीदारी", "name_en": "Community Participation"},
                        {"id": "dm_ch_06_topic_04", "name_hi": "आपदा तैयारी", "name_en": "Disaster Preparedness"},
                        {"id": "dm_ch_06_topic_05", "name_hi": "सतत जीवन", "name_en": "Sustainable Living"},
                        {"id": "dm_ch_06_topic_06", "name_hi": "आपदा जोखिम न्यूनीकरण", "name_en": "Disaster Risk Reduction"}
                    ]
                }
            ]
        },

        # Book 4: Political Science
        {
            "id": "sst_book_04",
            "name_hi": "लोकतांत्रिक राजनीति (भाग 2)",
            "name_en": "Democratic Politics (Part 2)",
            "chapters": [
                {
                    "id": "pol_ch_01",
                    "code": "CH01",
                    "chapter_number": 1,
                    "name_hi": "लोकतंत्र में सत्ता की साझेदारी",
                    "name_en": "Power Sharing in Democracy",
                    "topics": [
                        {"id": "pol_ch_01_topic_01", "name_hi": "सत्ता की साझेदारी", "name_en": "Power Sharing"},
                        {"id": "pol_ch_01_topic_02", "name_hi": "बेल्जियम", "name_en": "Belgium"},
                        {"id": "pol_ch_01_topic_03", "name_hi": "श्रीलंका", "name_en": "Sri Lanka"},
                        {"id": "pol_ch_01_topic_04", "name_hi": "बहुसंख्यकवाद", "name_en": "Majoritarianism"},
                        {"id": "pol_ch_01_topic_05", "name_hi": "सामुदायिक सरकार", "name_en": "Community Government"},
                        {"id": "pol_ch_01_topic_06", "name_hi": "सत्ता साझेदारी के रूप", "name_en": "Forms of Power Sharing"}
                    ]
                },
                {
                    "id": "pol_ch_02",
                    "code": "CH02",
                    "chapter_number": 2,
                    "name_hi": "सत्ता में साझेदारी की कार्यप्रणाली",
                    "name_en": "Working of Power Sharing",
                    "topics": [
                        {"id": "pol_ch_02_topic_01", "name_hi": "सत्ता साझेदारी", "name_en": "Power Sharing"},
                        {"id": "pol_ch_02_topic_02", "name_hi": "विधायिका", "name_en": "Legislature"},
                        {"id": "pol_ch_02_topic_03", "name_hi": "कार्यपालिका", "name_en": "Executive"},
                        {"id": "pol_ch_02_topic_04", "name_hi": "न्यायपालिका", "name_en": "Judiciary"},
                        {"id": "pol_ch_02_topic_05", "name_hi": "संघवाद", "name_en": "Federalism"},
                        {"id": "pol_ch_02_topic_06", "name_hi": "क्षैतिज सत्ता साझेदारी", "name_en": "Horizontal Power Sharing"},
                        {"id": "pol_ch_02_topic_07", "name_hi": "ऊर्ध्वाधर सत्ता साझेदारी", "name_en": "Vertical Power Sharing"}
                    ]
                },
                {
                    "id": "pol_ch_03",
                    "code": "CH03",
                    "chapter_number": 3,
                    "name_hi": "लोकतंत्र में प्रतिस्पर्धा एवं संघर्ष",
                    "name_en": "Competition and Conflict in Democracy",
                    "topics": [
                        {"id": "pol_ch_03_topic_01", "name_hi": "राजनीतिक प्रतिस्पर्धा", "name_en": "Political Competition"},
                        {"id": "pol_ch_03_topic_02", "name_hi": "राजनीतिक दल", "name_en": "Political Parties"},
                        {"id": "pol_ch_03_topic_03", "name_hi": "दबाव समूह", "name_en": "Pressure Groups"},
                        {"id": "pol_ch_03_topic_04", "name_hi": "आंदोलन", "name_en": "Movements"},
                        {"id": "pol_ch_03_topic_05", "name_hi": "लोकतांत्रिक भागीदारी", "name_en": "Democratic Participation"},
                        {"id": "pol_ch_03_topic_06", "name_hi": "संघर्ष और लोकतंत्र", "name_en": "Conflict and Democracy"}
                    ]
                },
                {
                    "id": "pol_ch_04",
                    "code": "CH04",
                    "chapter_number": 4,
                    "name_hi": "लोकतंत्र की उपलब्धियाँ",
                    "name_en": "Outcomes of Democracy",
                    "topics": [
                        {"id": "pol_ch_04_topic_01", "name_hi": "जवाबदेह सरकार", "name_en": "Accountable Government"},
                        {"id": "pol_ch_04_topic_02", "name_hi": "उत्तरदायी सरकार", "name_en": "Responsive Government"},
                        {"id": "pol_ch_04_topic_03", "name_hi": "वैध सरकार", "name_en": "Legitimate Government"},
                        {"id": "pol_ch_04_topic_04", "name_hi": "आर्थिक विकास", "name_en": "Economic Growth"},
                        {"id": "pol_ch_04_topic_05", "name_hi": "असमानता", "name_en": "Inequality"},
                        {"id": "pol_ch_04_topic_06", "name_hi": "सामाजिक विविधता", "name_en": "Social Diversity"},
                        {"id": "pol_ch_04_topic_07", "name_hi": "गरिमा और स्वतंत्रता", "name_en": "Dignity and Freedom"}
                    ]
                },
                {
                    "id": "pol_ch_05",
                    "code": "CH05",
                    "chapter_number": 5,
                    "name_hi": "लोकतंत्र की चुनौतियाँ",
                    "name_en": "Challenges to Democracy",
                    "topics": [
                        {"id": "pol_ch_05_topic_01", "name_hi": "लोकतंत्र की चुनौतियाँ", "name_en": "Challenges to Democracy"},
                        {"id": "pol_ch_05_topic_02", "name_hi": "बुनियादी चुनौती", "name_en": "Foundational Challenge"},
                        {"id": "pol_ch_05_topic_03", "name_hi": "विस्तार की चुनौती", "name_en": "Expansion Challenge"},
                        {"id": "pol_ch_05_topic_04", "name_hi": "लोकतंत्र को गहरा करने की चुनौती", "name_en": "Deepening of Democracy"},
                        {"id": "pol_ch_05_topic_05", "name_hi": "लोकतांत्रिक सुधार", "name_en": "Democratic Reforms"},
                        {"id": "pol_ch_05_topic_06", "name_hi": "राजनीतिक भागीदारी", "name_en": "Political Participation"}
                    ]
                }
            ]
        },

        # Book 5: Economics
        {
            "id": "sst_book_05",
            "name_hi": "हमारी अर्थव्यवस्था (भाग 2)",
            "name_en": "Our Economy (Part 2)",
            "chapters": [
                {
                    "id": "eco_ch_01",
                    "code": "CH01",
                    "chapter_number": 1,
                    "name_hi": "अर्थव्यवस्था एवं इसके विकास का इतिहास",
                    "name_en": "Economy and History of its Development",
                    "topics": [
                        {"id": "eco_ch_01_topic_01", "name_hi": "अर्थव्यवस्था", "name_en": "Economy"},
                        {"id": "eco_ch_01_topic_02", "name_hi": "आर्थिक विकास", "name_en": "Economic Development"},
                        {"id": "eco_ch_01_topic_03", "name_hi": "आर्थिक गतिविधियाँ", "name_en": "Economic Activities"},
                        {"id": "eco_ch_01_topic_04", "name_hi": "विकास", "name_en": "Development"},
                        {"id": "eco_ch_01_topic_05", "name_hi": "विकास के संकेतक", "name_en": "Development Indicators"},
                        {"id": "eco_ch_01_topic_06", "name_hi": "प्रति व्यक्ति आय", "name_en": "Per Capita Income"},
                        {"id": "eco_ch_01_topic_07", "name_hi": "मानव विकास", "name_en": "Human Development"}
                    ]
                },
                {
                    "id": "eco_ch_02",
                    "code": "CH02",
                    "chapter_number": 2,
                    "name_hi": "राज्य एवं राष्ट्र की आय",
                    "name_en": "State and National Income",
                    "topics": [
                        {"id": "eco_ch_02_topic_01", "name_hi": "राज्य आय", "name_en": "State Income"},
                        {"id": "eco_ch_02_topic_02", "name_hi": "राष्ट्रीय आय", "name_en": "National Income"},
                        {"id": "eco_ch_02_topic_03", "name_hi": "प्रति व्यक्ति आय", "name_en": "Per Capita Income"},
                        {"id": "eco_ch_02_topic_04", "name_hi": "सकल घरेलू उत्पाद", "name_en": "Gross Domestic Product"},
                        {"id": "eco_ch_02_topic_05", "name_hi": "आर्थिक वृद्धि", "name_en": "Economic Growth"},
                        {"id": "eco_ch_02_topic_06", "name_hi": "आय वितरण", "name_en": "Income Distribution"}
                    ]
                },
                {
                    "id": "eco_ch_03",
                    "code": "CH03",
                    "chapter_number": 3,
                    "name_hi": "मुद्रा, बचत एवं साख",
                    "name_en": "Money, Savings and Credit",
                    "topics": [
                        {"id": "eco_ch_03_topic_01", "name_hi": "मुद्रा", "name_en": "Money"},
                        {"id": "eco_ch_03_topic_02", "name_hi": "मुद्रा के कार्य", "name_en": "Functions of Money"},
                        {"id": "eco_ch_03_topic_03", "name_hi": "बचत", "name_en": "Savings"},
                        {"id": "eco_ch_03_topic_04", "name_hi": "साख", "name_en": "Credit"},
                        {"id": "eco_ch_03_topic_05", "name_hi": "औपचारिक साख", "name_en": "Formal Credit"},
                        {"id": "eco_ch_03_topic_06", "name_hi": "अनौपचारिक साख", "name_en": "Informal Credit"},
                        {"id": "eco_ch_03_topic_07", "name_hi": "बैंक", "name_en": "Banks"},
                        {"id": "eco_ch_03_topic_08", "name_hi": "स्वयं सहायता समूह", "name_en": "Self-Help Groups"}
                    ]
                },
                {
                    "id": "eco_ch_04",
                    "code": "CH04",
                    "chapter_number": 4,
                    "name_hi": "हमारी वित्तीय संस्थाएँ",
                    "name_en": "Our Financial Institutions",
                    "topics": [
                        {"id": "eco_ch_04_topic_01", "name_hi": "वित्तीय संस्थाएँ", "name_en": "Financial Institutions"},
                        {"id": "eco_ch_04_topic_02", "name_hi": "बैंक", "name_en": "Banks"},
                        {"id": "eco_ch_04_topic_03", "name_hi": "केंद्रीय बैंक", "name_en": "Central Bank"},
                        {"id": "eco_ch_04_topic_04", "name_hi": "वाणिज्यिक बैंक", "name_en": "Commercial Banks"},
                        {"id": "eco_ch_04_topic_05", "name_hi": "साख संस्थाएँ", "name_en": "Credit Institutions"},
                        {"id": "eco_ch_04_topic_06", "name_hi": "वित्तीय सेवाएँ", "name_en": "Financial Services"}
                    ]
                },
                {
                    "id": "eco_ch_05",
                    "code": "CH05",
                    "chapter_number": 5,
                    "name_hi": "रोजगार एवं सेवाएँ",
                    "name_en": "Employment and Services",
                    "topics": [
                        {"id": "eco_ch_05_topic_01", "name_hi": "रोजगार", "name_en": "Employment"},
                        {"id": "eco_ch_05_topic_02", "name_hi": "बेरोजगारी", "name_en": "Unemployment"},
                        {"id": "eco_ch_05_topic_03", "name_hi": "संगठित क्षेत्र", "name_en": "Organised Sector"},
                        {"id": "eco_ch_05_topic_04", "name_hi": "असंगठित क्षेत्र", "name_en": "Unorganised Sector"},
                        {"id": "eco_ch_05_topic_05", "name_hi": "सेवा क्षेत्र", "name_en": "Service Sector"},
                        {"id": "eco_ch_05_topic_06", "name_hi": "सार्वजनिक क्षेत्र", "name_en": "Public Sector"},
                        {"id": "eco_ch_05_topic_07", "name_hi": "निजी क्षेत्र", "name_en": "Private Sector"}
                    ]
                },
                {
                    "id": "eco_ch_06",
                    "code": "CH06",
                    "chapter_number": 6,
                    "name_hi": "वैश्वीकरण",
                    "name_en": "Globalization",
                    "topics": [
                        {"id": "eco_ch_06_topic_01", "name_hi": "वैश्वीकरण", "name_en": "Globalisation"},
                        {"id": "eco_ch_06_topic_02", "name_hi": "बहुराष्ट्रीय कंपनियाँ", "name_en": "Multinational Companies"},
                        {"id": "eco_ch_06_topic_03", "name_hi": "विदेशी निवेश", "name_en": "Foreign Investment"},
                        {"id": "eco_ch_06_topic_04", "name_hi": "उदारीकरण", "name_en": "Liberalisation"},
                        {"id": "eco_ch_06_topic_05", "name_hi": "अंतरराष्ट्रीय व्यापार", "name_en": "International Trade"},
                        {"id": "eco_ch_06_topic_06", "name_hi": "WTO", "name_en": "World Trade Organization"},
                        {"id": "eco_ch_06_topic_07", "name_hi": "वैश्विक बाजार", "name_en": "Global Market"}
                    ]
                },
                {
                    "id": "eco_ch_07",
                    "code": "CH07",
                    "chapter_number": 7,
                    "name_hi": "उपभोक्ता जागरण एवं संरक्षण",
                    "name_en": "Consumer Awareness and Protection",
                    "topics": [
                        {"id": "eco_ch_07_topic_01", "name_hi": "उपभोक्ता", "name_en": "Consumer"},
                        {"id": "eco_ch_07_topic_02", "name_hi": "उपभोक्ता अधिकार", "name_en": "Consumer Rights"},
                        {"id": "eco_ch_07_topic_03", "name_hi": "उपभोक्ता संरक्षण", "name_en": "Consumer Protection"},
                        {"id": "eco_ch_07_topic_04", "name_hi": "उपभोक्ता जागरूकता", "name_en": "Consumer Awareness"},
                        {"id": "eco_ch_07_topic_05", "name_hi": "उपभोक्ता न्यायालय", "name_en": "Consumer Courts"},
                        {"id": "eco_ch_07_topic_06", "name_hi": "मानकीकरण चिह्न", "name_en": "Standardisation Marks"},
                        {"id": "eco_ch_07_topic_07", "name_hi": "उपभोक्ता की जिम्मेदारियाँ", "name_en": "Consumer Responsibilities"}
                    ]
                }
            ]
        }
    ]
}
SYLLABUS_DATA["subjects"].append(social_subject)

# ==========================================
# 4. HINDI — हिंदी (2 Books, Sections in Book A)
# ==========================================
hindi_subject = {
    "id": "hindi",
    "code": "HIN",
    "name_hi": "हिंदी",
    "name_en": "Hindi",
    "icon": "fa-book-open",
    "color": "from-rose-600 to-pink-600",
    "accent": "#e11d48",
    "books": [
        # Book A: Godhuli Part 2 (Prose & Poetry Sections)
        {
            "id": "hin_book_01",
            "name_hi": "गोधूलि (भाग 2)",
            "name_en": "Godhuli (Part 2)",
            "sections": [
                {
                    "id": "hin_sec_prose",
                    "name_hi": "गद्य खंड",
                    "name_en": "Prose Section",
                    "chapters": [
                        {
                            "id": "hin_ch_01", "code": "CH01", "chapter_number": 1,
                            "name_hi": "श्रम विभाजन और जाति प्रथा", "name_en": "Division of Labour and Caste System",
                            "topics": [
                                {"id": "hin_ch_01_topic_01", "name_hi": "लेखक परिचय — डॉ. भीमराव आंबेडकर", "name_en": "Author Introduction — Dr. B.R. Ambedkar"},
                                {"id": "hin_ch_01_topic_02", "name_hi": "पाठ का मुख्य विचार एवं उद्देश्य", "name_en": "Main Idea and Objective"},
                                {"id": "hin_ch_01_topic_03", "name_hi": "जाति प्रथा के दोष एवं आर्थिक पहलू", "name_en": "Flaws of Caste System & Economic Aspect"},
                                {"id": "hin_ch_01_topic_04", "name_hi": "सच्चे लोकतंत्र की अवधारणा और भाईचारा", "name_en": "Concept of True Democracy & Brotherhood"},
                                {"id": "hin_ch_01_topic_05", "name_hi": "भाषा-शैली एवं पाठ-आधारित समझ", "name_en": "Language Style & Text Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_02", "code": "CH02", "chapter_number": 2,
                            "name_hi": "विष के दाँत", "name_en": "The Teeth of Poison",
                            "topics": [
                                {"id": "hin_ch_02_topic_01", "name_hi": "लेखक परिचय — नलिन विलोचन शर्मा", "name_en": "Author Introduction — Nalin Vilochan Sharma"},
                                {"id": "hin_ch_02_topic_02", "name_hi": "कहानी का कथानक एवं मुख्य घटनाएँ", "name_en": "Plot & Key Events"},
                                {"id": "hin_ch_02_topic_03", "name_hi": "पात्र-चित्रण (कासू, मदन, सेन साहब, गिरधर)", "name_en": "Character Analysis (Kasu, Madan, Sen Sahab, Girdhar)"},
                                {"id": "hin_ch_02_topic_04", "name_hi": "मध्यमवर्गीय अंतर्विरोध एवं वर्ग-संघर्ष", "name_en": "Middle-Class Dilemma & Class Conflict"},
                                {"id": "hin_ch_02_topic_05", "name_hi": "संदेश एवं पाठ-आधारित समझ", "name_en": "Message & Text Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_03", "code": "CH03", "chapter_number": 3,
                            "name_hi": "भारत से हम क्या सीखें", "name_en": "What Can We Learn from India",
                            "topics": [
                                {"id": "hin_ch_03_topic_01", "name_hi": "लेखक परिचय — मैक्समूलर", "name_en": "Author Introduction — Max Muller"},
                                {"id": "hin_ch_03_topic_02", "name_hi": "भाषण का संदर्भ एवं पृष्ठभूमि", "name_en": "Speech Context & Background"},
                                {"id": "hin_ch_03_topic_03", "name_hi": "भारतीय संस्कृति और ज्ञान की महत्ता", "name_en": "Significance of Indian Culture & Knowledge"},
                                {"id": "hin_ch_03_topic_04", "name_hi": "संस्कृत भाषा और विश्व साहित्य", "name_en": "Sanskrit Language & World Literature"},
                                {"id": "hin_ch_03_topic_05", "name_hi": "सार एवं पाठ-आधारित समझ", "name_en": "Essence & Text Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_04", "code": "CH04", "chapter_number": 4,
                            "name_hi": "नाखून क्यों बढ़ते हैं", "name_en": "Why Do Nails Grow",
                            "topics": [
                                {"id": "hin_ch_04_topic_01", "name_hi": "लेखक परिचय — आचार्य हजारीप्रसाद द्विवेदी", "name_en": "Author Introduction — Hazari Prasad Dwivedi"},
                                {"id": "hin_ch_04_topic_02", "name_hi": "निबंध का केंद्रीय भाव एवं दार्शनिक विचार", "name_en": "Central Theme & Philosophical Thoughts"},
                                {"id": "hin_ch_04_topic_03", "name_hi": "पशुता बनाम मनुष्यता का द्वंद्व", "name_en": "Animality vs Humanity Conflict"},
                                {"id": "hin_ch_04_topic_04", "name_hi": "अस्त्र-शस्त्र की होड़ और आत्मसंयम", "name_en": "Arms Race & Self-Restraint"},
                                {"id": "hin_ch_04_topic_05", "name_hi": "ललित निबंध की भाषा-शैली व संदेश", "name_en": "Essay Style & Message"}
                            ]
                        },
                        {
                            "id": "hin_ch_05", "code": "CH05", "chapter_number": 5,
                            "name_hi": "नागरी लिपि", "name_en": "Nagari Script",
                            "topics": [
                                {"id": "hin_ch_05_topic_01", "name_hi": "लेखक परिचय — गुणाकर मुले", "name_en": "Author Introduction — Gunakar Mule"},
                                {"id": "hin_ch_05_topic_02", "name_hi": "नागरी लिपि की उत्पत्ति एवं ऐतिहासिक विकास", "name_en": "Origin & Historical Evolution of Nagari Script"},
                                {"id": "hin_ch_05_topic_03", "name_hi": "देवनागरी और भारत की विभिन्न लिपियाँ", "name_en": "Devnagari & Various Indian Scripts"},
                                {"id": "hin_ch_05_topic_04", "name_hi": "शिलालेख, सिक्के और प्राचीन प्रमाण", "name_en": "Inscriptions, Coins & Ancient Records"},
                                {"id": "hin_ch_05_topic_05", "name_hi": "महत्वपूर्ण तथ्य एवं पाठ-बोध", "name_en": "Key Facts & Text Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_06", "code": "CH06", "chapter_number": 6,
                            "name_hi": "बहादुर", "name_en": "Bahadur",
                            "topics": [
                                {"id": "hin_ch_06_topic_01", "name_hi": "लेखक परिचय — अमरकांत", "name_en": "Author Introduction — Amarkant"},
                                {"id": "hin_ch_06_topic_02", "name_hi": "कहानी का कथानक एवं बहादुर का आगमन", "name_en": "Plot & Bahadur's Arrival"},
                                {"id": "hin_ch_06_topic_03", "name_hi": "पात्र-चित्रण (बहादुर, निर्मला, किशोर, लेखक)", "name_en": "Character Analysis (Bahadur, Nirmala, Kishor, Author)"},
                                {"id": "hin_ch_06_topic_04", "name_hi": "चोरी का झूठा आरोप और बहादुर का प्रस्थान", "name_en": "False Accusation & Departure"},
                                {"id": "hin_ch_06_topic_05", "name_hi": "मध्यमवर्गीय मानसिकता, पछतावा व संदेश", "name_en": "Middle-Class Mentality, Regret & Message"}
                            ]
                        },
                        {
                            "id": "hin_ch_07", "code": "CH07", "chapter_number": 7,
                            "name_hi": "परंपरा का मूल्यांकन", "name_en": "Evaluation of Tradition",
                            "topics": [
                                {"id": "hin_ch_07_topic_01", "name_hi": "लेखक परिचय — डॉ. रामविलास शर्मा", "name_en": "Author Introduction — Dr. Ramvilas Sharma"},
                                {"id": "hin_ch_07_topic_02", "name_hi": "साहित्यिक परंपरा की समझ और मूल्यांकन", "name_en": "Understanding & Evaluation of Literary Tradition"},
                                {"id": "hin_ch_07_topic_03", "name_hi": "जातीय अस्मिता और साहित्य का महत्व", "name_en": "Cultural Identity & Role of Literature"},
                                {"id": "hin_ch_07_topic_04", "name_hi": "द्वंद्वात्मक भौतिकवाद और प्रगतिशील विचार", "name_en": "Dialectical Materialism & Progressive Ideas"},
                                {"id": "hin_ch_07_topic_05", "name_hi": "निबंध का सार एवं पाठ-बोध", "name_en": "Essay Summary & Text Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_08", "code": "CH08", "chapter_number": 8,
                            "name_hi": "जित-जित मैं निरखत हूँ", "name_en": "Jit-Jit Main Nirakhat Hoon",
                            "topics": [
                                {"id": "hin_ch_08_topic_01", "name_hi": "साक्षात्कार एवं पंडित बिरजू महाराज परिचय", "name_en": "Interview & Pandit Birju Maharaj Biography"},
                                {"id": "hin_ch_08_topic_02", "name_hi": "कथक नृत्य परंपरा एवं गुरु-शिष्य संबंध", "name_en": "Kathak Tradition & Guru-Shishya Bond"},
                                {"id": "hin_ch_08_topic_03", "name_hi": "बचपन का संघर्ष और कला साधना", "name_en": "Childhood Struggles & Artistic Dedication"},
                                {"id": "hin_ch_08_topic_04", "name_hi": "संगीत-कला की बारीकियां व संस्मरण", "name_en": "Nuances of Music-Art & Recollections"},
                                {"id": "hin_ch_08_topic_05", "name_hi": "पाठ का संदेश एवं मुख्य तथ्य", "name_en": "Lesson Message & Key Facts"}
                            ]
                        },
                        {
                            "id": "hin_ch_09", "code": "CH09", "chapter_number": 9,
                            "name_hi": "आविन्यों", "name_en": "Avignon",
                            "topics": [
                                {"id": "hin_ch_09_topic_01", "name_hi": "लेखक परिचय — अशोक वाजपेयी", "name_en": "Author Introduction — Ashok Vajpeyi"},
                                {"id": "hin_ch_09_topic_02", "name_hi": "यात्रा-वृत्तांत: आविन्यों की भौगोलिक व सांस्कृतिक पृष्ठभूमि", "name_en": "Travelogue: Geography & Culture of Avignon"},
                                {"id": "hin_ch_09_topic_03", "name_hi": "ला शित्रूज एवं पिकासो की कला साधना", "name_en": "La Chartreuse & Picasso's Artistic Creations"},
                                {"id": "hin_ch_09_topic_04", "name_hi": "रोन नदी और रचनात्मक एकांत", "name_en": "Rhone River & Creative Solitude"},
                                {"id": "hin_ch_09_topic_05", "name_hi": "रचनात्मक अनुभव एवं पाठ-बोध", "name_en": "Creative Insights & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_10", "code": "CH10", "chapter_number": 10,
                            "name_hi": "मछली", "name_en": "Fish",
                            "topics": [
                                {"id": "hin_ch_10_topic_01", "name_hi": "लेखक परिचय — विनोद कुमार शुक्ल", "name_en": "Author Introduction — Vinod Kumar Shukla"},
                                {"id": "hin_ch_10_topic_02", "name_hi": "कहानी का कथानक एवं बाल-मनोविज्ञान", "name_en": "Plot & Child Psychology"},
                                {"id": "hin_ch_10_topic_03", "name_hi": "पात्र-चित्रण (संतू, नरेन, भग्गू, पिता)", "name_en": "Character Analysis (Santu, Naren, Bhaggue, Father)"},
                                {"id": "hin_ch_10_topic_04", "name_hi": "मछली और परिवार की संवेदनशील स्थिति", "name_en": "Fish & Domestic Emotional Milieu"},
                                {"id": "hin_ch_10_topic_05", "name_hi": "प्रतीकात्मक अर्थ, संदेश एवं पाठ-बोध", "name_en": "Symbolism, Message & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_11", "code": "CH11", "chapter_number": 11,
                            "name_hi": "नौबतखाने में इबादत", "name_en": "Worship in the Naubatkhana",
                            "topics": [
                                {"id": "hin_ch_11_topic_01", "name_hi": "लेखक परिचय — यतीन्द्र मिश्र", "name_en": "Author Introduction — Yatindra Mishra"},
                                {"id": "hin_ch_11_topic_02", "name_hi": "उस्ताद बिस्मिल्ला खाँ का जीवन व व्यक्तित्व", "name_en": "Ustad Bismillah Khan's Life & Persona"},
                                {"id": "hin_ch_11_topic_03", "name_hi": "शहनाई वादन और काशी की संगीत परंपरा", "name_en": "Shehnai Playing & Kashi's Music Heritage"},
                                {"id": "hin_ch_11_topic_04", "name_hi": "धार्मिक सद्भाव और सुर-साधना", "name_en": "Religious Harmony & Musical Devotion"},
                                {"id": "hin_ch_11_topic_05", "name_hi": "संस्मरण का सार व पाठ-बोध", "name_en": "Memoir Summary & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_12", "code": "CH12", "chapter_number": 12,
                            "name_hi": "शिक्षा और संस्कृति", "name_en": "Education and Culture",
                            "topics": [
                                {"id": "hin_ch_12_topic_01", "name_hi": "लेखक परिचय — महात्मा गांधी", "name_en": "Author Introduction — Mahatma Gandhi"},
                                {"id": "hin_ch_12_topic_02", "name_hi": "गांधीजी के शैक्षणिक विचार एवं बेसिक शिक्षा", "name_en": "Gandhi's Educational Philosophy & Basic Education"},
                                {"id": "hin_ch_12_topic_03", "name_hi": "चरित्र निर्माण और हस्तकला आधारित शिक्षा", "name_en": "Character Building & Vocational Learning"},
                                {"id": "hin_ch_12_topic_04", "name_hi": "सच्ची संस्कृति एवं समन्वयकारी दृष्टिकोण", "name_en": "True Culture & Harmonious Vision"},
                                {"id": "hin_ch_12_topic_05", "name_hi": "संदेश, भाषा-शैली व पाठ-बोध", "name_en": "Message, Style & Text Comprehension"}
                            ]
                        }
                    ]
                },
                {
                    "id": "hin_sec_poetry",
                    "name_hi": "काव्य खंड",
                    "name_en": "Poetry Section",
                    "chapters": [
                        {
                            "id": "hin_ch_13", "code": "CH13", "chapter_number": 1,
                            "name_hi": "राम बिनु बिरथे जगि जनमा / जो नर दुख में दुख नहिं मानै", "name_en": "Ram Binu Birthe Jagi Janma / Jo Nar Dukh Mein Dukh Nahin Manai",
                            "topics": [
                                {"id": "hin_ch_13_topic_01", "name_hi": "कवि परिचय — गुरु नानक", "name_en": "Poet Introduction — Guru Nanak"},
                                {"id": "hin_ch_13_topic_02", "name_hi": "पद 1: नाम-स्मरण की महत्ता एवं बाह्याडंबर का विरोध", "name_en": "Verse 1: Significance of Divine Name & Anti-Ritualism"},
                                {"id": "hin_ch_13_topic_03", "name_hi": "पद 2: सुख-दुख में समभाव एवं अंतःशुद्धि", "name_en": "Verse 2: Equanimity in Joy-Sorrow & Inner Purity"},
                                {"id": "hin_ch_13_topic_04", "name_hi": "काव्य-सौंदर्य, ब्रजभाषा व छंद", "name_en": "Poetic Aesthetics, Language & Meter"},
                                {"id": "hin_ch_13_topic_05", "name_hi": "भावार्थ एवं पाठ-बोध", "name_en": "Meaning & Poem Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_14", "code": "CH14", "chapter_number": 2,
                            "name_hi": "प्रेम अयनि श्री राधिका / करील के कुंजन ऊपर वारौं", "name_en": "Prem Ayani Shri Radhika / Karil Ke Kunjan Upar Varaun",
                            "topics": [
                                {"id": "hin_ch_14_topic_01", "name_hi": "कवि परिचय — रसखान", "name_en": "Poet Introduction — Raskhan"},
                                {"id": "hin_ch_14_topic_02", "name_hi": "राधा-कृष्ण के युगल प्रेम का वर्णन", "name_en": "Description of Radha-Krishna's Divine Love"},
                                {"id": "hin_ch_14_topic_03", "name_hi": "ब्रजभूमि के प्रति अनन्य समर्पण व सवैया भाव", "name_en": "Devotion to Braj & Savaiya Stanza Sense"},
                                {"id": "hin_ch_14_topic_04", "name_hi": "माधुर्य गुण, रस व अलंकार", "name_en": "Lyrical Quality, Rasa & Figures of Speech"},
                                {"id": "hin_ch_14_topic_05", "name_hi": "भावार्थ एवं महत्वपूर्ण पंक्तियाँ", "name_en": "Meaning & Key Lines"}
                            ]
                        },
                        {
                            "id": "hin_ch_15", "code": "CH15", "chapter_number": 3,
                            "name_hi": "अति सूधो सनेह को मारग है / मो अंसुवानिहिं लै बरसौ", "name_en": "Ati Sudho Saneh Ko Marag Hai / Mo Ansuvanihin Lai Barsau",
                            "topics": [
                                {"id": "hin_ch_15_topic_01", "name_hi": "कवि परिचय — घनानंद", "name_en": "Poet Introduction — Ghananand"},
                                {"id": "hin_ch_15_topic_02", "name_hi": "प्रेम मार्ग की सरलता एवं निश्छलता", "name_en": "Simplicity & Sincerity of Path of Love"},
                                {"id": "hin_ch_15_topic_03", "name_hi": "विरह-वेदना एवं मेघ-प्रार्थना", "name_en": "Pangs of Separation & Cloud Supplication"},
                                {"id": "hin_ch_15_topic_04", "name_hi": "रीतिमुक्त काव्य-सौंदर्य व लाक्षणिक भाषा", "name_en": "Reetimukt Poetic Style & Figurative Language"},
                                {"id": "hin_ch_15_topic_05", "name_hi": "भावार्थ एवं पाठ-बोध", "name_en": "Meaning & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_16", "code": "CH16", "chapter_number": 4,
                            "name_hi": "स्वदेशी", "name_en": "Swadeshi",
                            "topics": [
                                {"id": "hin_ch_16_topic_01", "name_hi": "कवि परिचय — बदरीनारायण चौधरी 'प्रेमघन'", "name_en": "Poet Introduction — Badri Narayan Chaudhary 'Premghan'"},
                                {"id": "hin_ch_16_topic_02", "name_hi": "पराधीनता और विदेशी दासता पर व्यंग्य", "name_en": "Satire on Servitude & Western Emulation"},
                                {"id": "hin_ch_16_topic_03", "name_hi": "स्वदेशी चेतना और भारतीय संस्कृति का जागरण", "name_en": "Swadeshi Consciousness & Cultural Awakening"},
                                {"id": "hin_ch_16_topic_04", "name_hi": "दोहा छंद, भाषा व काव्य-शिल्प", "name_en": "Doha Meter, Language & Craft"},
                                {"id": "hin_ch_16_topic_05", "name_hi": "राष्ट्रीय संदेश एवं पाठ-बोध", "name_en": "Patriotic Message & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_17", "code": "CH17", "chapter_number": 5,
                            "name_hi": "भारतमाता", "name_en": "Bharatmata",
                            "topics": [
                                {"id": "hin_ch_17_topic_01", "name_hi": "कवि परिचय — सुमित्रानंदन पंत", "name_en": "Poet Introduction — Sumitranandan Pant"},
                                {"id": "hin_ch_17_topic_02", "name_hi": "ग्रामवासिनी भारतमाता का यथार्थवादी चित्रण", "name_en": "Realistic Depiction of Rural Mother India"},
                                {"id": "hin_ch_17_topic_03", "name_hi": "गुलामी की पीड़ा, दरिद्रता और अश्रु", "name_en": "Pain of Bondage, Poverty & Tears"},
                                {"id": "hin_ch_17_topic_04", "name_hi": "छायावादी बिंब, प्रकृति-चित्रण व मानवीयता", "name_en": "Chhayavadi Imagery, Nature & Humanity"},
                                {"id": "hin_ch_17_topic_05", "name_hi": "भावार्थ, संदेश एवं पाठ-बोध", "name_en": "Meaning, Message & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_18", "code": "CH18", "chapter_number": 6,
                            "name_hi": "जनतंत्र का जन्म", "name_en": "Birth of Democracy",
                            "topics": [
                                {"id": "hin_ch_18_topic_01", "name_hi": "कवि परिचय — रामधारी सिंह 'दिनकर'", "name_en": "Poet Introduction — Ramdhari Singh 'Dinkar'"},
                                {"id": "hin_ch_18_topic_02", "name_hi": "जनता की शक्ति और लोकतंत्र का आह्वान", "name_en": "Power of the Masses & Call for Democracy"},
                                {"id": "hin_ch_18_topic_03", "name_hi": "सिंहासन खाली करने का ऐतिहासिक उद्घोष", "name_en": "Historic Proclamation to Vacate the Throne"},
                                {"id": "hin_ch_18_topic_04", "name_hi": "ओज गुण, राष्ट्रप्रेम एवं क्रांति-भाव", "name_en": "Heroic Tone, Patriotism & Revolutionary Zeal"},
                                {"id": "hin_ch_18_topic_05", "name_hi": "भावार्थ एवं महत्वपूर्ण पंक्तियाँ", "name_en": "Meaning & Key Verses"}
                            ]
                        },
                        {
                            "id": "hin_ch_19", "code": "CH19", "chapter_number": 7,
                            "name_hi": "हिरोशिमा", "name_en": "Hiroshima",
                            "topics": [
                                {"id": "hin_ch_19_topic_01", "name_hi": "कवि परिचय — सच्चिदानंद हीरानंद वात्स्यायन 'अज्ञेय'", "name_en": "Poet Introduction — S.H. Vatsyayan 'Agyeya'"},
                                {"id": "hin_ch_19_topic_02", "name_hi": "परमाणु त्रासदी और मानव-रचित विभीषिका", "name_en": "Nuclear Tragedy & Man-Made Catastrophe"},
                                {"id": "hin_ch_19_topic_03", "name_hi": "सूरज का प्रतीकात्मक बिंब और मानवीय साखी", "name_en": "Symbolic Sun Metaphor & Human Witness"},
                                {"id": "hin_ch_19_topic_04", "name_hi": "वैज्ञानिक विध्वंस पर चेतावनी एवं मानवीय वेदना", "name_en": "Warning on Scientific Destruction & Pathos"},
                                {"id": "hin_ch_19_topic_05", "name_hi": "काव्य-सौंदर्य व पाठ-बोध", "name_en": "Poetic Craft & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_20", "code": "CH20", "chapter_number": 8,
                            "name_hi": "एक वृक्ष की हत्या", "name_en": "Murder of a Tree",
                            "topics": [
                                {"id": "hin_ch_20_topic_01", "name_hi": "कवि परिचय — कुँवर नारायण", "name_en": "Poet Introduction — Kunwar Narayan"},
                                {"id": "hin_ch_20_topic_02", "name_hi": "पुराने वृक्ष का चौकीदार रूपी बिंब", "name_en": "Imagery of Old Tree as a Sentinel"},
                                {"id": "hin_ch_20_topic_03", "name_hi": "पर्यावरण संकट, वृक्ष कटाई एवं मानवीय संवेदनहीनता", "name_en": "Environmental Crisis, Deforestation & Callousness"},
                                {"id": "hin_ch_20_topic_04", "name_hi": "सभ्यता को बचाने का संदेश एवं शहर-सुरक्षा", "name_en": "Message to Save Civilization & Cities"},
                                {"id": "hin_ch_20_topic_05", "name_hi": "भावार्थ एवं पाठ-बोध", "name_en": "Meaning & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_21", "code": "CH21", "chapter_number": 9,
                            "name_hi": "हमारी नींद", "name_en": "During Our Sleep",
                            "topics": [
                                {"id": "hin_ch_21_topic_01", "name_hi": "कवि परिचय — वीरेन डंगवाल", "name_en": "Poet Introduction — Viren Dangwal"},
                                {"id": "hin_ch_21_topic_02", "name_hi": "नींद और सतत जीवन-संघर्ष का प्रतीक", "name_en": "Sleep & Symbol of Ongoing Life Struggle"},
                                {"id": "hin_ch_21_topic_03", "name_hi": "मक्खी का जीवन-क्रम और सामाजिक शोषण", "name_en": "Life Cycle of a Fly & Social Exploitation"},
                                {"id": "hin_ch_21_topic_04", "name_hi": "आधुनिक सुविधाभोग और प्रतिरोध की चेतना", "name_en": "Modern Complacency & Spirit of Resistance"},
                                {"id": "hin_ch_21_topic_05", "name_hi": "भावार्थ एवं पाठ-बोध", "name_en": "Meaning & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_22", "code": "CH22", "chapter_number": 10,
                            "name_hi": "अक्षर-ज्ञान", "name_en": "Knowledge of the Alphabets",
                            "topics": [
                                {"id": "hin_ch_22_topic_01", "name_hi": "कवि परिचय — अनामिका", "name_en": "Poet Introduction — Anamika"},
                                {"id": "hin_ch_22_topic_02", "name_hi": "बालक की अक्षर सीखने की आरंभिक विवशता (क, ख, ग, घ)", "name_en": "Child's Initial Struggles in Alphabet Learning"},
                                {"id": "hin_ch_22_topic_03", "name_hi": "'ङ' में माँ और गोदी में बैठे बेटे का ममत्व", "name_en": "Motherhood & Child Bond Symbolized in 'Nga'"},
                                {"id": "hin_ch_22_topic_04", "name_hi": "विफलता के आंसू और पहली सृष्टि की खोज", "name_en": "Tears of Failure & Discovery of Creation"},
                                {"id": "hin_ch_22_topic_05", "name_hi": "बाल-मनोविज्ञान, भावार्थ व पाठ-बोध", "name_en": "Child Psychology, Meaning & Comprehension"}
                            ]
                        },
                        {
                            "id": "hin_ch_23", "code": "CH23", "chapter_number": 11,
                            "name_hi": "लौटकर आऊँगा फिर", "name_en": "I Will Return Again",
                            "topics": [
                                {"id": "hin_ch_23_topic_01", "name_hi": "कवि परिचय — जीवनानंद दास (अनुवादक: प्रयाग शुक्ल)", "name_en": "Poet Introduction — Jibanananda Das"},
                                {"id": "hin_ch_23_topic_02", "name_hi": "बंगाल की हरी-भरी प्रकृति एवं मातृभूमि से प्रेम", "name_en": "Lush Nature of Bengal & Love for Homeland"},
                                {"id": "hin_ch_23_topic_03", "name_hi": "पक्षी/जीव रूप में पुनर्जन्म की तीव्र अभिलाषा", "name_en": "Deep Desire for Rebirth as Bird/Creature in Bengal"},
                                {"id": "hin_ch_23_topic_04", "name_hi": "दृश्य बिंब, नदी-खेत व लोक-संस्कृति", "name_en": "Visual Imagery, Rivers-Fields & Folk Heritage"},
                                {"id": "hin_ch_23_topic_05", "name_hi": "भावार्थ एवं काव्य-सौंदर्य", "name_en": "Meaning & Poetic Aesthetics"}
                            ]
                        },
                        {
                            "id": "hin_ch_24", "code": "CH24", "chapter_number": 12,
                            "name_hi": "मेरे बिना तुम प्रभु", "name_en": "Lord, What Will You Do Without Me",
                            "topics": [
                                {"id": "hin_ch_24_topic_01", "name_hi": "कवि परिचय — रेनर मारिया रिल्के (अनुवादक: धर्मवीर भारती)", "name_en": "Poet Introduction — Rainer Maria Rilke"},
                                {"id": "hin_ch_24_topic_02", "name_hi": "भक्त और भगवान की अन्योन्याश्रित निर्भरता", "name_en": "Interdependence of Devotee and God"},
                                {"id": "hin_ch_24_topic_03", "name_hi": "भक्त के अस्तित्व से ही भगवान की महत्ता", "name_en": "God's Glory Embodied in the Devotee"},
                                {"id": "hin_ch_24_topic_04", "name_hi": "दार्शनिक रहस्यवाद और अगाध आस्था", "name_en": "Philosophical Mysticism & Unshakable Faith"},
                                {"id": "hin_ch_24_topic_05", "name_hi": "भावार्थ एवं महत्वपूर्ण पंक्तियाँ", "name_en": "Meaning & Key Lines"}
                            ]
                        }
                    ]
                }
            ]
        },

        # Book B: Varnika Part 2 (Supplementary)
        {
            "id": "hin_book_02",
            "name_hi": "वर्णिका (भाग 2)",
            "name_en": "Varnika (Part 2)",
            "chapters": [
                {
                    "id": "var_ch_01", "code": "CH01", "chapter_number": 1,
                    "name_hi": "दही वाली मंगम्मा", "name_en": "Dahi Wali Mangamma",
                    "topics": [
                        {"id": "var_ch_01_topic_01", "name_hi": "लेखक परिचय — श्रीनिवास (कन्नड़ कहानी)", "name_en": "Author Introduction — Srinivas (Kannada Story)"},
                        {"id": "var_ch_01_topic_02", "name_hi": "कथानक एवं मंगम्मा का दही बेचने का दैनिक जीवन", "name_en": "Plot & Mangamma's Daily Routine of Selling Curd"},
                        {"id": "var_ch_01_topic_03", "name_hi": "सास-बहू (मंगम्मा और नजम्मा) का पारिवारिक विवाद", "name_en": "Mother-in-Law & Daughter-in-Law Domestic Conflict"},
                        {"id": "var_ch_01_topic_04", "name_hi": "रंगप्पा का लालच और परिवार का पुनर्मिलन", "name_en": "Rangappa's Greed & Family Reconciliation"},
                        {"id": "var_ch_01_topic_05", "name_hi": "ग्रामीण परिवेश, चरित्र-चित्रण व संदेश", "name_en": "Rural Setting, Character Study & Message"}
                    ]
                },
                {
                    "id": "var_ch_02", "code": "CH02", "chapter_number": 2,
                    "name_hi": "ढहते विश्वास", "name_en": "Dhalte Vishwas",
                    "topics": [
                        {"id": "var_ch_02_topic_01", "name_hi": "लेखक परिचय — सातकोड़ी होता (उड़िया कहानी)", "name_en": "Author Introduction — Satkodi Hota (Odia Story)"},
                        {"id": "var_ch_02_topic_02", "name_hi": "कथानक: महानदी-दलेई बांध पर मंडराती बाढ़", "name_en": "Plot: Flood Threat on Mahanadi-Dalei Dam"},
                        {"id": "var_ch_02_topic_03", "name_hi": "लक्ष्मी का संघर्ष और ग्रामीण समाज की एकजुटता", "name_en": "Laxmi's Struggle & Village Community Solidarity"},
                        {"id": "var_ch_02_topic_04", "name_hi": "बाढ़ की विनाशलीला एवं विश्वास का डगमगाना", "name_en": "Flood Havoc & Crushed Faith in Providence"},
                        {"id": "var_ch_02_topic_05", "name_hi": "प्राकृतिक आपदा की त्रासदी एवं संदेश", "name_en": "Tragedy of Natural Disaster & Message"}
                    ]
                },
                {
                    "id": "var_ch_03", "code": "CH03", "chapter_number": 3,
                    "name_hi": "माँ", "name_en": "Maa",
                    "topics": [
                        {"id": "var_ch_03_topic_01", "name_hi": "लेखक परिचय — ईश्वर पेटलीकर (गुजराती कहानी)", "name_en": "Author Introduction — Ishwar Petlikar (Gujarati Story)"},
                        {"id": "var_ch_03_topic_02", "name_hi": "मंगु की मानसिक स्थिति और मां का अगाध वात्सल्य", "name_en": "Mangu's Mental Disability & Mother's Unconditional Love"},
                        {"id": "var_ch_03_topic_03", "name_hi": "समाज की संवेदनहीनता एवं अस्पताल भेजने का द्वंद्व", "name_en": "Social Indifference & Hospital Admission Dilemma"},
                        {"id": "var_ch_03_topic_04", "name_hi": "कुसुम का स्वस्थ होना और मां का अंतिम निर्णय", "name_en": "Kusum's Recovery & Mother's Final Decision"},
                        {"id": "var_ch_03_topic_05", "name_hi": "मातृत्व की पराकाष्ठा, मार्मिक अंत व पाठ-बोध", "name_en": "Peak of Motherhood, Touching Climax & Comprehension"}
                    ]
                },
                {
                    "id": "var_ch_04", "code": "CH04", "chapter_number": 4,
                    "name_hi": "नगर", "name_en": "Nagar",
                    "topics": [
                        {"id": "var_ch_04_topic_01", "name_hi": "लेखक परिचय — सुजाता (तमिल कहानी)", "name_en": "Author Introduction — Sujata (Tamil Story)"},
                        {"id": "var_ch_04_topic_02", "name_hi": "वल्ली अम्मल और उसकी बीमार बेटी पाप्पाति का मदुरै आगमन", "name_en": "Valli Ammal & Pappati's Arrival in Madurai for Treatment"},
                        {"id": "var_ch_04_topic_03", "name_hi": "सरकारी अस्पताल की अव्यवस्था, नौकरशाही व उपेक्षा", "name_en": "Government Hospital Apathy, Red Tape & Neglect"},
                        {"id": "var_ch_04_topic_04", "name_hi": "अनपढ़ मां की लाचारी, भटकन और अंधविश्वास", "name_en": "Helplessness of Illiterate Mother & Superstition"},
                        {"id": "var_ch_04_topic_05", "name_hi": "शहरी व्यवस्था पर करारा व्यंग्य व संदेश", "name_en": "Satire on Urban Healthcare System & Message"}
                    ]
                },
                {
                    "id": "var_ch_05", "code": "CH05", "chapter_number": 5,
                    "name_hi": "धरती कब तक घूमेगी", "name_en": "Dharti Kab Tak Ghoomegi",
                    "topics": [
                        {"id": "var_ch_05_topic_01", "name_hi": "लेखक परिचय — साँवर दइया (राजस्थानी कहानी)", "name_en": "Author Introduction — Sanwar Daiya (Rajasthani Story)"},
                        {"id": "var_ch_05_topic_02", "name_hi": "सीता का पारिवारिक संताप और बेटों का बंटवारा", "name_en": "Sita's Family Pain & Sons' Monthly Turn Arrangement"},
                        {"id": "var_ch_05_topic_03", "name_hi": "रोटी और पचास रुपये मासिक भत्ते का अपमान", "name_en": "Humiliation of Food Rations & 50-Rupee Monthly Allowance"},
                        {"id": "var_ch_05_topic_04", "name_hi": "सीता का स्वाभिमान और घर छोड़कर प्रस्थान", "name_en": "Sita's Self-Respect & Decision to Leave Home"},
                        {"id": "var_ch_05_topic_05", "name_hi": "बुजुर्गों की उपेक्षा, मार्मिक यथार्थ व संदेश", "name_en": "Neglect of Elderly, Harsh Reality & Message"}
                    ]
                }
            ]
        }
    ]
}
SYLLABUS_DATA["subjects"].append(hindi_subject)

# ==========================================
# 5. ENGLISH (2 Books, Sections in Book A)
# ==========================================
english_subject = {
    "id": "english",
    "code": "ENG",
    "name_hi": "अंग्रेज़ी",
    "name_en": "English",
    "icon": "fa-language",
    "color": "from-purple-600 to-indigo-600",
    "accent": "#8b5cf6",
    "books": [
        # Book A: Panorama Part 2
        {
            "id": "eng_book_01",
            "name_hi": "पैनोरामा (भाग 2)",
            "name_en": "Panorama (Part 2)",
            "sections": [
                {
                    "id": "eng_sec_prose",
                    "name_hi": "गद्य खंड (Prose)",
                    "name_en": "Prose Section",
                    "chapters": [
                        {
                            "id": "eng_prose_ch_01", "code": "CH01", "chapter_number": 1,
                            "name_hi": "The Pace for Living", "name_en": "The Pace for Living",
                            "topics": [
                                {"id": "eng_prose_ch_01_topic_01", "name_hi": "Author Introduction — R.C. Hutchinson", "name_en": "Author Introduction — R.C. Hutchinson"},
                                {"id": "eng_prose_ch_01_topic_02", "name_hi": "The Dublin Play & Elderly Corn Merchant", "name_en": "The Dublin Play & Elderly Corn Merchant"},
                                {"id": "eng_prose_ch_01_topic_03", "name_hi": "Fast Pace of Modern Life & Technology", "name_en": "Fast Pace of Modern Life & Technology"},
                                {"id": "eng_prose_ch_01_topic_04", "name_hi": "Slow Thinkers vs Fast Thinkers", "name_en": "Slow Thinkers vs Fast Thinkers"},
                                {"id": "eng_prose_ch_01_topic_05", "name_hi": "Vocabulary, Themes & Comprehension", "name_en": "Vocabulary, Themes & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_prose_ch_02", "code": "CH02", "chapter_number": 2,
                            "name_hi": "Me and the Ecology Bit", "name_en": "Me and the Ecology Bit",
                            "topics": [
                                {"id": "eng_prose_ch_02_topic_01", "name_hi": "Author Introduction — Joan Lexau", "name_en": "Author Introduction — Joan Lexau"},
                                {"id": "eng_prose_ch_02_topic_02", "name_hi": "Jim's Route & Environmental Awareness", "name_en": "Jim's Route & Environmental Awareness"},
                                {"id": "eng_prose_ch_02_topic_03", "name_hi": "Interactions with Mr. Williams & Ms. Greene", "name_en": "Interactions with Mr. Williams & Ms. Greene"},
                                {"id": "eng_prose_ch_02_topic_04", "name_hi": "Composting, Recycling & Energy Conservation", "name_en": "Composting, Recycling & Energy Conservation"},
                                {"id": "eng_prose_ch_02_topic_05", "name_hi": "Human Hypocrisy towards Ecology & Message", "name_en": "Human Hypocrisy towards Ecology & Message"}
                            ]
                        },
                        {
                            "id": "eng_prose_ch_03", "code": "CH03", "chapter_number": 3,
                            "name_hi": "Gillu", "name_en": "Gillu",
                            "topics": [
                                {"id": "eng_prose_ch_03_topic_01", "name_hi": "Author Introduction — Mahadevi Verma", "name_en": "Author Introduction — Mahadevi Verma"},
                                {"id": "eng_prose_ch_03_topic_02", "name_hi": "Rescue and Care of the Baby Squirrel", "name_en": "Rescue and Care of the Baby Squirrel"},
                                {"id": "eng_prose_ch_03_topic_03", "name_hi": "Gillu's Playful Habits & Affection", "name_en": "Gillu's Playful Habits & Affection"},
                                {"id": "eng_prose_ch_03_topic_04", "name_hi": "Gillu's Illness, Death & Sonjuhi Plant", "name_en": "Gillu's Illness, Death & Sonjuhi Plant"},
                                {"id": "eng_prose_ch_03_topic_05", "name_hi": "Bond Between Humans and Animals & Vocabulary", "name_en": "Bond Between Humans and Animals & Vocabulary"}
                            ]
                        },
                        {
                            "id": "eng_prose_ch_04", "code": "CH04", "chapter_number": 4,
                            "name_hi": "What is Wrong with Indian Films", "name_en": "What is Wrong with Indian Films",
                            "topics": [
                                {"id": "eng_prose_ch_04_topic_01", "name_hi": "Author Introduction — Satyajit Ray", "name_en": "Author Introduction — Satyajit Ray"},
                                {"id": "eng_prose_ch_04_topic_02", "name_hi": "Quantity vs Quality in Indian Cinema", "name_en": "Quantity vs Quality in Indian Cinema"},
                                {"id": "eng_prose_ch_04_topic_03", "name_hi": "Blind Imitation of Hollywood & Lack of Realism", "name_en": "Blind Imitation of Hollywood & Lack of Realism"},
                                {"id": "eng_prose_ch_04_topic_04", "name_hi": "Need for Authentic Storytelling & Visual Grammar", "name_en": "Need for Authentic Storytelling & Visual Grammar"},
                                {"id": "eng_prose_ch_04_topic_05", "name_hi": "Critical Insights, Vocabulary & Comprehension", "name_en": "Critical Insights, Vocabulary & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_prose_ch_05", "code": "CH05", "chapter_number": 5,
                            "name_hi": "Acceptance Speech", "name_en": "Acceptance Speech",
                            "topics": [
                                {"id": "eng_prose_ch_05_topic_01", "name_hi": "Speaker Context — Alexander Aris for Aung San Suu Kyi", "name_en": "Speaker Context — Alexander Aris for Aung San Suu Kyi"},
                                {"id": "eng_prose_ch_05_topic_02", "name_hi": "Nobel Peace Prize Award Acceptance", "name_en": "Nobel Peace Prize Award Acceptance"},
                                {"id": "eng_prose_ch_05_topic_03", "name_hi": "Struggle for Democracy & Human Rights in Burma", "name_en": "Struggle for Democracy & Human Rights in Burma"},
                                {"id": "eng_prose_ch_05_topic_04", "name_hi": "Non-Violence, Freedom and Global Solidarity", "name_en": "Non-Violence, Freedom and Global Solidarity"},
                                {"id": "eng_prose_ch_05_topic_05", "name_hi": "Key Quotes, Vocabulary & Comprehension", "name_en": "Key Quotes, Vocabulary & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_prose_ch_06", "code": "CH06", "chapter_number": 6,
                            "name_hi": "Once Upon a Time", "name_en": "Once Upon a Time",
                            "topics": [
                                {"id": "eng_prose_ch_06_topic_01", "name_hi": "Author Introduction — Toni Morrison", "name_en": "Author Introduction — Toni Morrison"},
                                {"id": "eng_prose_ch_06_topic_02", "name_hi": "Parable of the Old Wise Woman and the Bird", "name_en": "Parable of the Old Wise Woman and the Bird"},
                                {"id": "eng_prose_ch_06_topic_03", "name_hi": "Responsibility of Language: Living vs Dead Language", "name_en": "Responsibility of Language: Living vs Dead Language"},
                                {"id": "eng_prose_ch_06_topic_04", "name_hi": "Power of Words, Oppression and Empowerment", "name_en": "Power of Words, Oppression and Empowerment"},
                                {"id": "eng_prose_ch_06_topic_05", "name_hi": "Allegory, Themes & Comprehension", "name_en": "Allegory, Themes & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_prose_ch_07", "code": "CH07", "chapter_number": 7,
                            "name_hi": "The Unity of Indian Culture", "name_en": "The Unity of Indian Culture",
                            "topics": [
                                {"id": "eng_prose_ch_07_topic_01", "name_hi": "Author Introduction — Humayun Kabir", "name_en": "Author Introduction — Humayun Kabir"},
                                {"id": "eng_prose_ch_07_topic_02", "name_hi": "Continuity and Vitality of Indian Civilization", "name_en": "Continuity and Vitality of Indian Civilization"},
                                {"id": "eng_prose_ch_07_topic_03", "name_hi": "Unity in Diversity & Tolerant Synthesis", "name_en": "Unity in Diversity & Tolerant Synthesis"},
                                {"id": "eng_prose_ch_07_topic_04", "name_hi": "Culture vs Civilization Distinction", "name_en": "Culture vs Civilization Distinction"},
                                {"id": "eng_prose_ch_07_topic_05", "name_hi": "Key Historical Arguments & Comprehension", "name_en": "Key Historical Arguments & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_prose_ch_08", "code": "CH08", "chapter_number": 8,
                            "name_hi": "Little Girls Wiser Than Men", "name_en": "Little Girls Wiser Than Men",
                            "topics": [
                                {"id": "eng_prose_ch_08_topic_01", "name_hi": "Author Introduction — Leo Tolstoy", "name_en": "Author Introduction — Leo Tolstoy"},
                                {"id": "eng_prose_ch_08_topic_02", "name_hi": "Easter Setting, Akoulya and Malasha", "name_en": "Easter Setting, Akoulya and Malasha"},
                                {"id": "eng_prose_ch_08_topic_03", "name_hi": "Puddle Incident & Quarrel Among Adults", "name_en": "Puddle Incident & Quarrel Among Adults"},
                                {"id": "eng_prose_ch_08_topic_04", "name_hi": "Children's Forgiveness and Reconciliation", "name_en": "Children's Forgiveness and Reconciliation"},
                                {"id": "eng_prose_ch_08_topic_05", "name_hi": "Moral Message, Vocabulary & Comprehension", "name_en": "Moral Message, Vocabulary & Comprehension"}
                            ]
                        }
                    ]
                },
                {
                    "id": "eng_sec_poetry",
                    "name_hi": "काव्य खंड (Poetry)",
                    "name_en": "Poetry Section",
                    "chapters": [
                        {
                            "id": "eng_poetry_ch_01", "code": "PO01", "chapter_number": 1,
                            "name_hi": "God Made the Country", "name_en": "God Made the Country",
                            "topics": [
                                {"id": "eng_poetry_ch_01_topic_01", "name_hi": "Poet Introduction — William Cowper", "name_en": "Poet Introduction — William Cowper"},
                                {"id": "eng_poetry_ch_01_topic_02", "name_hi": "Rural Simplicity vs Urban Artificiality", "name_en": "Rural Simplicity vs Urban Artificiality"},
                                {"id": "eng_poetry_ch_01_topic_03", "name_hi": "Natural Virtues, Health and Quiet Peace", "name_en": "Natural Virtues, Health and Quiet Peace"},
                                {"id": "eng_poetry_ch_01_topic_04", "name_hi": "Literary Devices, Tone and Imagery", "name_en": "Literary Devices, Tone and Imagery"},
                                {"id": "eng_poetry_ch_01_topic_05", "name_hi": "Stanza-wise Meaning & Comprehension", "name_en": "Stanza-wise Meaning & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_poetry_ch_02", "code": "PO02", "chapter_number": 2,
                            "name_hi": "Ode on Solitude", "name_en": "Ode on Solitude",
                            "topics": [
                                {"id": "eng_poetry_ch_02_topic_01", "name_hi": "Poet Introduction — Alexander Pope", "name_en": "Poet Introduction — Alexander Pope"},
                                {"id": "eng_poetry_ch_02_topic_02", "name_hi": "The Truly Happy and Contented Man", "name_en": "The Truly Happy and Contented Man"},
                                {"id": "eng_poetry_ch_02_topic_03", "name_hi": "Self-Sufficiency, Health and Peace of Mind", "name_en": "Self-Sufficiency, Health and Peace of Mind"},
                                {"id": "eng_poetry_ch_02_topic_04", "name_hi": "Desire to Live and Die Unseen / Unlamented", "name_en": "Desire to Live and Die Unseen / Unlamented"},
                                {"id": "eng_poetry_ch_02_topic_05", "name_hi": "Poetic Structure, Rhyme Scheme & Comprehension", "name_en": "Poetic Structure, Rhyme Scheme & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_poetry_ch_03", "code": "PO03", "chapter_number": 3,
                            "name_hi": "Polythene Bag", "name_en": "Polythene Bag",
                            "topics": [
                                {"id": "eng_poetry_ch_03_topic_01", "name_hi": "Poet Introduction — Durga Prasad Panda", "name_en": "Poet Introduction — Durga Prasad Panda"},
                                {"id": "eng_poetry_ch_03_topic_02", "name_hi": "Non-Biodegradable Nature of Polythene", "name_en": "Non-Biodegradable Nature of Polythene"},
                                {"id": "eng_poetry_ch_03_topic_03", "name_hi": "Polythene Bag as a Metaphor for Grief and Hurt", "name_en": "Polythene Bag as a Metaphor for Grief and Hurt"},
                                {"id": "eng_poetry_ch_03_topic_04", "name_hi": "Environmental Hazard and Emotional Wounds", "name_en": "Environmental Hazard and Emotional Wounds"},
                                {"id": "eng_poetry_ch_03_topic_05", "name_hi": "Imagery, Meaning & Comprehension", "name_en": "Imagery, Meaning & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_poetry_ch_04", "code": "PO04", "chapter_number": 4,
                            "name_hi": "Thinner Than a Crescent", "name_en": "Thinner Than a Crescent",
                            "topics": [
                                {"id": "eng_poetry_ch_04_topic_01", "name_hi": "Poet Introduction — Vidyapati", "name_en": "Poet Introduction — Vidyapati"},
                                {"id": "eng_poetry_ch_04_topic_02", "name_hi": "Radha's Intense Grief in Separation from Lord Krishna", "name_en": "Radha's Intense Grief in Separation from Lord Krishna"},
                                {"id": "eng_poetry_ch_04_topic_03", "name_hi": "Physical Emaciation & Crescent Moon Simile", "name_en": "Physical Emaciation & Crescent Moon Simile"},
                                {"id": "eng_poetry_ch_04_topic_04", "name_hi": "Friend's Plea and Devotional Lyricism", "name_en": "Friend's Plea and Devotional Lyricism"},
                                {"id": "eng_poetry_ch_04_topic_05", "name_hi": "Key Lines, Meaning & Comprehension", "name_en": "Key Lines, Meaning & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_poetry_ch_05", "code": "PO05", "chapter_number": 5,
                            "name_hi": "The Empty Heart", "name_en": "The Empty Heart",
                            "topics": [
                                {"id": "eng_poetry_ch_05_topic_01", "name_hi": "Poet Introduction — Periasamy Thooran", "name_en": "Poet Introduction — Periasamy Thooran"},
                                {"id": "eng_poetry_ch_05_topic_02", "name_hi": "The Rich Man's Prayer to the Kalpataru Tree", "name_en": "The Rich Man's Prayer to the Kalpataru Tree"},
                                {"id": "eng_poetry_ch_05_topic_03", "name_hi": "Seven Full Pitchers & the Curse of the Half-Filled Eighth", "name_en": "Seven Full Pitchers & the Curse of the Half-Filled Eighth"},
                                {"id": "eng_poetry_ch_05_topic_04", "name_hi": "Insatiable Greed Leading to Physical and Moral Ruin", "name_en": "Insatiable Greed Leading to Physical and Moral Ruin"},
                                {"id": "eng_poetry_ch_05_topic_05", "name_hi": "Moral Lesson, Symbolism & Comprehension", "name_en": "Moral Lesson, Symbolism & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_poetry_ch_06", "code": "PO06", "chapter_number": 6,
                            "name_hi": "Koel", "name_en": "Koel",
                            "topics": [
                                {"id": "eng_poetry_ch_06_topic_01", "name_hi": "Poet Introduction — Puran Singh", "name_en": "Poet Introduction — Puran Singh"},
                                {"id": "eng_poetry_ch_06_topic_02", "name_hi": "The Song of the Black Cuckoo & Mango Leaves", "name_en": "The Song of the Black Cuckoo & Mango Leaves"},
                                {"id": "eng_poetry_ch_06_topic_03", "name_hi": "Fire of Love and Separation in the Koel's Melodic Cry", "name_en": "Fire of Love and Separation in the Koel's Melodic Cry"},
                                {"id": "eng_poetry_ch_06_topic_04", "name_hi": "Romantic Longing and Nature's Restlessness", "name_en": "Romantic Longing and Nature's Restlessness"},
                                {"id": "eng_poetry_ch_06_topic_05", "name_hi": "Poetic Dialogue, Tone & Comprehension", "name_en": "Poetic Dialogue, Tone & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_poetry_ch_07", "code": "PO07", "chapter_number": 7,
                            "name_hi": "The Sleeping Porter", "name_en": "The Sleeping Porter",
                            "topics": [
                                {"id": "eng_poetry_ch_07_topic_01", "name_hi": "Poet Introduction — Laxmi Prasad Devkota", "name_en": "Poet Introduction — Laxmi Prasad Devkota"},
                                {"id": "eng_poetry_ch_07_topic_02", "name_hi": "Himalayan Porter's Heavy 54-Seer Load & Steep Ascent", "name_en": "Himalayan Porter's Heavy 54-Seer Load & Steep Ascent"},
                                {"id": "eng_poetry_ch_07_topic_03", "name_hi": "Extreme Poverty, Hardship and Physical Exhaustion", "name_en": "Extreme Poverty, Hardship and Physical Exhaustion"},
                                {"id": "eng_poetry_ch_07_topic_04", "name_hi": "Peaceful Sleep atop the Cliff as Nature's Sovereign", "name_en": "Peaceful Sleep atop the Cliff as Nature's Sovereign"},
                                {"id": "eng_poetry_ch_07_topic_05", "name_hi": "Social Realism, Contrast & Comprehension", "name_en": "Social Realism, Contrast & Comprehension"}
                            ]
                        },
                        {
                            "id": "eng_poetry_ch_08", "code": "PO08", "chapter_number": 8,
                            "name_hi": "Martha", "name_en": "Martha",
                            "topics": [
                                {"id": "eng_poetry_ch_08_topic_01", "name_hi": "Poet Introduction — Walter de la Mare", "name_en": "Poet Introduction — Walter de la Mare"},
                                {"id": "eng_poetry_ch_08_topic_02", "name_hi": "Martha's Enchanting Clear Grey Eyes & Hazel Glen", "name_en": "Martha's Enchanting Clear Grey Eyes & Hazel Glen"},
                                {"id": "eng_poetry_ch_08_topic_03", "name_hi": "Storytelling Magic: Fairies, Gnomes and Ages Past", "name_en": "Storytelling Magic: Fairies, Gnomes and Ages Past"},
                                {"id": "eng_poetry_ch_08_topic_04", "name_hi": "Childhood Nostalgia, Dreamlike Atmosphere & Wonder", "name_en": "Childhood Nostalgia, Dreamlike Atmosphere & Wonder"},
                                {"id": "eng_poetry_ch_08_topic_05", "name_hi": "Rhyme Scheme, Lyrical Beauty & Comprehension", "name_en": "Rhyme Scheme, Lyrical Beauty & Comprehension"}
                            ]
                        }
                    ]
                }
            ]
        },

        # Book B: Supplementary English Reader
        {
            "id": "eng_book_02",
            "name_hi": "पैनोरामा इंग्लिश रीडर (भाग 2 पूरक)",
            "name_en": "Panorama English Reader (Part 2 Supplementary)",
            "chapters": [
                {
                    "id": "eng_supp_ch_01", "code": "CH01", "chapter_number": 1,
                    "name_hi": "January Night", "name_en": "January Night",
                    "topics": [
                        {"id": "eng_supp_ch_01_topic_01", "name_hi": "Author Introduction — Premchand", "name_en": "Author Introduction — Premchand"},
                        {"id": "eng_supp_ch_01_topic_02", "name_hi": "Halku, Munni and the Debt to Sahna", "name_en": "Halku, Munni and the Debt to Sahna"},
                        {"id": "eng_supp_ch_01_topic_03", "name_hi": "The Biting Winter Cold & Dog Jabra in the Field", "name_en": "The Biting Winter Cold & Dog Jabra in the Field"},
                        {"id": "eng_supp_ch_01_topic_04", "name_hi": "The Wild Animals Ruining the Crop & Leaf Fire Warmth", "name_en": "The Wild Animals Ruining the Crop & Leaf Fire Warmth"},
                        {"id": "eng_supp_ch_01_topic_05", "name_hi": "Rural Indebtedness, Themes & Comprehension", "name_en": "Rural Indebtedness, Themes & Comprehension"}
                    ]
                },
                {
                    "id": "eng_supp_ch_02", "code": "CH02", "chapter_number": 2,
                    "name_hi": "Allergy", "name_en": "Allergy",
                    "topics": [
                        {"id": "eng_supp_ch_02_topic_01", "name_hi": "Author Introduction — Dr. Rana S.P. Singh", "name_en": "Author Introduction — Dr. Rana S.P. Singh"},
                        {"id": "eng_supp_ch_02_topic_02", "name_hi": "Understanding Allergy: Antigens and Allergens", "name_en": "Understanding Allergy: Antigens and Allergens"},
                        {"id": "eng_supp_ch_02_topic_03", "name_hi": "Common Symptoms: Sneezing, Wheezing and Rash", "name_en": "Common Symptoms: Sneezing, Wheezing and Rash"},
                        {"id": "eng_supp_ch_02_topic_04", "name_hi": "Preventive Measures, Diagnosis and Medical Management", "name_en": "Preventive Measures, Diagnosis and Medical Management"},
                        {"id": "eng_supp_ch_02_topic_05", "name_hi": "Scientific Insights, Vocabulary & Comprehension", "name_en": "Scientific Insights, Vocabulary & Comprehension"}
                    ]
                },
                {
                    "id": "eng_supp_ch_03", "code": "CH03", "chapter_number": 3,
                    "name_hi": "The Bet", "name_en": "The Bet",
                    "topics": [
                        {"id": "eng_supp_ch_03_topic_01", "name_hi": "Author Introduction — Anton Chekhov", "name_en": "Author Introduction — Anton Chekhov"},
                        {"id": "eng_supp_ch_03_topic_02", "name_hi": "The Party Debate: Capital Punishment vs Life Imprisonment", "name_en": "The Party Debate: Capital Punishment vs Life Imprisonment"},
                        {"id": "eng_supp_ch_03_topic_03", "name_hi": "The 15-Year Solitary Confinement Agreement", "name_en": "The 15-Year Solitary Confinement Agreement"},
                        {"id": "eng_supp_ch_03_topic_04", "name_hi": "The Lawyer's Spiritual Transformation & Letter of Renunciation", "name_en": "The Lawyer's Spiritual Transformation & Letter of Renunciation"},
                        {"id": "eng_supp_ch_03_topic_05", "name_hi": "Materialism vs Wisdom, Climax & Comprehension", "name_en": "Materialism vs Wisdom, Climax & Comprehension"}
                    ]
                },
                {
                    "id": "eng_supp_ch_04", "code": "CH04", "chapter_number": 4,
                    "name_hi": "Quality", "name_en": "Quality",
                    "topics": [
                        {"id": "eng_supp_ch_04_topic_01", "name_hi": "Author Introduction — John Galsworthy", "name_en": "Author Introduction — John Galsworthy"},
                        {"id": "eng_supp_ch_04_topic_02", "name_hi": "Mr. Gessler Brothers & the London Boot Shop", "name_en": "Mr. Gessler Brothers & the London Boot Shop"},
                        {"id": "eng_supp_ch_04_topic_03", "name_hi": "Art of Handmade Bootmaking & Unmatched Quality", "name_en": "Art of Handmade Bootmaking & Unmatched Quality"},
                        {"id": "eng_supp_ch_04_topic_04", "name_hi": "Loss to Big Commercial Advertisers & Starvation", "name_en": "Loss to Big Commercial Advertisers & Starvation"},
                        {"id": "eng_supp_ch_04_topic_05", "name_hi": "Tribute to Honest Craftsmanship & Comprehension", "name_en": "Tribute to Honest Craftsmanship & Comprehension"}
                    ]
                },
                {
                    "id": "eng_supp_ch_05", "code": "CH05", "chapter_number": 5,
                    "name_hi": "Sun and Moon", "name_en": "Sun and Moon",
                    "topics": [
                        {"id": "eng_supp_ch_05_topic_01", "name_hi": "Author Introduction — Katherine Mansfield", "name_en": "Author Introduction — Katherine Mansfield"},
                        {"id": "eng_supp_ch_05_topic_02", "name_hi": "Children's Perspective on Grand Adult Party Preparations", "name_en": "Children's Perspective on Grand Adult Party Preparations"},
                        {"id": "eng_supp_ch_05_topic_03", "name_hi": "The Beautiful Ice Pudding Little House", "name_en": "The Beautiful Ice Pudding Little House"},
                        {"id": "eng_supp_ch_05_topic_04", "name_hi": "Morning-After Mess, Sun's Tears & Emotional Sensitivity", "name_en": "Morning-After Mess, Sun's Tears & Emotional Sensitivity"},
                        {"id": "eng_supp_ch_05_topic_05", "name_hi": "Child Psychology, Innocence & Comprehension", "name_en": "Child Psychology, Innocence & Comprehension"}
                    ]
                },
                {
                    "id": "eng_supp_ch_06", "code": "CH06", "chapter_number": 6,
                    "name_hi": "Two Horizons", "name_en": "Two Horizons",
                    "topics": [
                        {"id": "eng_supp_ch_06_topic_01", "name_hi": "Author Introduction — Binapani Mohanty", "name_en": "Author Introduction — Binapani Mohanty"},
                        {"id": "eng_supp_ch_06_topic_02", "name_hi": "Epistolary Exchange: Letters Between Mother and Daughter", "name_en": "Epistolary Exchange: Letters Between Mother and Daughter"},
                        {"id": "eng_supp_ch_06_topic_03", "name_hi": "Daughter's Modern Urban Loneliness & Yearning", "name_en": "Daughter's Modern Urban Loneliness & Yearning"},
                        {"id": "eng_supp_ch_06_topic_04", "name_hi": "Mother's Wisdom, Traditional Warmth and Solace", "name_en": "Mother's Wisdom, Traditional Warmth and Solace"},
                        {"id": "eng_supp_ch_06_topic_05", "name_hi": "Generational Bond, Emotional Realism & Comprehension", "name_en": "Generational Bond, Emotional Realism & Comprehension"}
                    ]
                },
                {
                    "id": "eng_supp_ch_07", "code": "CH07", "chapter_number": 7,
                    "name_hi": "Love Defiled", "name_en": "Love Defiled",
                    "topics": [
                        {"id": "eng_supp_ch_07_topic_01", "name_hi": "Author Introduction — Giridhar Jha", "name_en": "Author Introduction — Giridhar Jha"},
                        {"id": "eng_supp_ch_07_topic_02", "name_hi": "Eight-Year Youthful Relationship & Aspirations", "name_en": "Eight-Year Youthful Relationship & Aspirations"},
                        {"id": "eng_supp_ch_07_topic_03", "name_hi": "Social Status, Caste Pressures and Parental Expectations", "name_en": "Social Status, Caste Pressures and Parental Expectations"},
                        {"id": "eng_supp_ch_07_topic_04", "name_hi": "Girlfriend's Marriage Elsewhere and Lifelong Memory", "name_en": "Girlfriend's Marriage Elsewhere and Lifelong Memory"},
                        {"id": "eng_supp_ch_07_topic_05", "name_hi": "Bitter-Sweet Realities of Love & Comprehension", "name_en": "Bitter-Sweet Realities of Love & Comprehension"}
                    ]
                }
            ]
        }
    ]
}
SYLLABUS_DATA["subjects"].append(english_subject)

# ==========================================
# 6. SANSKRIT — संस्कृत (1 Book)
# ==========================================
sanskrit_subject = {
    "id": "sanskrit",
    "code": "SAN",
    "name_hi": "संस्कृत",
    "name_en": "Sanskrit",
    "icon": "fa-scroll",
    "color": "from-cyan-600 to-blue-600",
    "accent": "#06b6d4",
    "books": [
        {
            "id": "san_book_01",
            "name_hi": "पीयूषम् (भाग 2)",
            "name_en": "Piyusham (Part 2)",
            "chapters": [
                {
                    "id": "san_ch_01", "code": "CH01", "chapter_number": 1,
                    "name_hi": "मङ्गलम्", "name_en": "Mangalam",
                    "topics": [
                        {"id": "san_ch_01_topic_01", "name_hi": "उपनिषद् परिचय एवं मंगलाचरण", "name_en": "Upanishad Introduction & Invocation"},
                        {"id": "san_ch_01_topic_02", "name_hi": "सत्य का स्वरूप एवं 'सत्यमेव जयते'", "name_en": "Nature of Truth & 'Satyameva Jayate'"},
                        {"id": "san_ch_01_topic_03", "name_hi": "आत्मा का सूक्ष्म रूप एवं ईश्वर-साक्षात्कार", "name_en": "Subtle Soul & Divine Realization"},
                        {"id": "san_ch_01_topic_04", "name_hi": "नदियों का समुद्र में विलीन होना (नाम-रूप त्याग)", "name_en": "Merging of Rivers into Ocean (Ego Transcendence)"},
                        {"id": "san_ch_01_topic_05", "name_hi": "श्लोकार्थ, व्याकरण एवं पाठ-बोध", "name_en": "Verse Meaning, Grammar & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_02", "code": "CH02", "chapter_number": 2,
                    "name_hi": "पाटलिपुत्रवैभवम्", "name_en": "Glory of Patliputra",
                    "topics": [
                        {"id": "san_ch_02_topic_01", "name_hi": "पाटलिपुत्र (पटना) का ऐतिहासिक परिचय", "name_en": "Historical Overview of Patliputra"},
                        {"id": "san_ch_02_topic_02", "name_hi": "भगवान बुद्ध की भविष्यवाणी एवं पाटलिग्राम", "name_en": "Lord Buddha's Prophecy & Patligram"},
                        {"id": "san_ch_02_topic_03", "name_hi": "मौर्य-गुप्त काल, चन्द्रगुप्त व अशोक शासन", "name_en": "Maurya & Gupta Era, Chandragupta & Ashoka"},
                        {"id": "san_ch_02_topic_04", "name_hi": "विदेशी यात्री विवरण, सिख गुरु गोविंद सिंह व दर्शनीय स्थल", "name_en": "Foreign Accounts, Guru Gobind Singh & Landmarks"},
                        {"id": "san_ch_02_topic_05", "name_hi": "पाठ-आधारित तथ्य, शब्दार्थ एवं अभ्यास", "name_en": "Key Facts, Word Meanings & Exercises"}
                    ]
                },
                {
                    "id": "san_ch_03", "code": "CH03", "chapter_number": 3,
                    "name_hi": "अलसकथा", "name_en": "The Story of Lazy Men",
                    "topics": [
                        {"id": "san_ch_03_topic_01", "name_hi": "रचनाकार परिचय — विद्यापति ('पुरुषपरीक्षा')", "name_en": "Author Introduction — Vidyapati ('Purusha Pariksha')"},
                        {"id": "san_ch_03_topic_02", "name_hi": "मंत्री बीरेश्वर का दानशील स्वभाव", "name_en": "Minister Bireswar's Benevolence"},
                        {"id": "san_ch_03_topic_03", "name_hi": "अलसशाला में आग लगाना और आलसियों की परीक्षा", "name_en": "Alas-shala Fire & Test of Real Lazy Men"},
                        {"id": "san_ch_03_topic_04", "name_hi": "चार सच्चे आलसियों की रोचक बातचीत व बचाव", "name_en": "Conversation of Four True Lazy Men & Rescue"},
                        {"id": "san_ch_03_topic_05", "name_hi": "आलस्य का मानव जीवन पर दुष्प्रभाव व संदेश", "name_en": "Ill Effects of Laziness & Moral Message"}
                    ]
                },
                {
                    "id": "san_ch_04", "code": "CH04", "chapter_number": 4,
                    "name_hi": "संस्कृतसाहित्ये लेखिकाः", "name_en": "Women Writers in Sanskrit Literature",
                    "topics": [
                        {"id": "san_ch_04_topic_01", "name_hi": "वैदिक काल की विदुषियाँ (गार्गी, मैत्रेयी, अपाला, यमी)", "name_en": "Vedic Era Female Scholars (Gargi, Maitreyi, Apala)"},
                        {"id": "san_ch_04_topic_02", "name_hi": "लौकिक संस्कृत साहित्य: विजयाङ्का (श्यामवर्णा सरस्वती)", "name_en": "Classical Sanskrit: Vijayanka (Dark Saraswati)"},
                        {"id": "san_ch_04_topic_03", "name_hi": "विजयनगर साम्राज्य की कवयित्रियाँ (गंगादेवी, तिरुमलाम्बा)", "name_en": "Vijayanagara Poetesses (Gangadevi, Tirumalamba)"},
                        {"id": "san_ch_04_topic_04", "name_hi": "आधुनिक काल की प्रमुख लेखिका पंडिता क्षमाराव", "name_en": "Modern Era Scholar Pandita Kshamarao"},
                        {"id": "san_ch_04_topic_05", "name_hi": "पाठ का महत्व, शब्दार्थ एवं पाठ-बोध", "name_en": "Significance, Word Meanings & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_05", "code": "CH05", "chapter_number": 5,
                    "name_hi": "भारतमहिमा", "name_en": "The Glory of India",
                    "topics": [
                        {"id": "san_ch_05_topic_01", "name_hi": "पौराणिक श्लोक: विष्णुपुराण एवं भागवतपुराण", "name_en": "Puranic Verses: Vishnu Purana & Bhagavata Purana"},
                        {"id": "san_ch_05_topic_02", "name_hi": "देवताओं द्वारा भारतभूमि की प्रशंसा", "name_en": "Gods Praising the Sacred Soil of India"},
                        {"id": "san_ch_05_topic_03", "name_hi": "आधुनिक श्लोक: भारत की विशालता व प्राकृतिक सौंदर्य", "name_en": "Modern Verses: Majesty & Natural Beauty of India"},
                        {"id": "san_ch_05_topic_04", "name_hi": "विविधता में एकता एवं देशभक्ति का भाव", "name_en": "Unity in Diversity & Spirit of Patriotism"},
                        {"id": "san_ch_05_topic_05", "name_hi": "श्लोकार्थ, अन्वय एवं पाठ-बोध", "name_en": "Verse Translation, Anvaya & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_06", "code": "CH06", "chapter_number": 6,
                    "name_hi": "भारतीयसंस्काराः", "name_en": "Indian Sacraments / Rituals",
                    "topics": [
                        {"id": "san_ch_06_topic_01", "name_hi": "संस्कारों का अर्थ एवं भारतीय संस्कृति में महत्व", "name_en": "Meaning & Significance of Sanskaras in India"},
                        {"id": "san_ch_06_topic_02", "name_hi": "जन्मपूर्व के 3 संस्कार (गर्भाधान, पुंसवन, सीमन्तोन्नयन)", "name_en": "3 Prenatal Sacraments (Garbhadhana, Pumsavana, Simantonnayana)"},
                        {"id": "san_ch_06_topic_03", "name_hi": "शैशवावस्था के 6 एवं शैक्षणिक 5 संस्कार (उपनयन, वेदारम्भ)", "name_en": "6 Infancy & 5 Educational Sacraments (Upanayana, Vedarambha)"},
                        {"id": "san_ch_06_topic_04", "name_hi": "विवाह संस्कार (सप्तपदी, सिन्दूरदान) एवं अंत्येष्टि संस्कार", "name_en": "Marriage Sacrament (Saptapadi) & Funeral Rites"},
                        {"id": "san_ch_06_topic_05", "name_hi": "16 मुख्य संस्कार, शब्दार्थ एवं पाठ-बोध", "name_en": "16 Main Sacraments, Glossary & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_07", "code": "CH07", "chapter_number": 7,
                    "name_hi": "नीतिश्लोकाः", "name_en": "Moral Verses",
                    "topics": [
                        {"id": "san_ch_07_topic_01", "name_hi": "ग्रंथ परिचय — 'महाभारत' उद्योगपर्व (विदुर नीति)", "name_en": "Text Introduction — 'Mahabharata' Udyoga Parva (Vidura Niti)"},
                        {"id": "san_ch_07_topic_02", "name_hi": "पंडित के लक्षण एवं मूर्ख (मूढ़चेता) के लक्षण", "name_en": "Traits of Wise Persons (Pandits) vs Fools"},
                        {"id": "san_ch_07_topic_03", "name_hi": "त्रिविधं नरकस्येदं द्वारं (काम, क्रोध, लोभ)", "name_en": "Three Gates to Ruin (Lust, Anger, Greed)"},
                        {"id": "san_ch_07_topic_04", "name_hi": "षड् दोषाः (निद्रा, तन्द्रा, भय, क्रोध, आलस्य, दीर्घसूत्रता)", "name_en": "Six Flaws to Avoid for Success"},
                        {"id": "san_ch_07_topic_05", "name_hi": "सत्य, शील, कुल-रक्षा श्लोकार्थ एवं अभ्यास", "name_en": "Truth, Conduct, Heritage Verses & Practice"}
                    ]
                },
                {
                    "id": "san_ch_08", "code": "CH08", "chapter_number": 8,
                    "name_hi": "कर्मवीर कथा", "name_en": "The Story of a Karmaveer",
                    "topics": [
                        {"id": "san_ch_08_topic_01", "name_hi": "भीखनटोला गांव एवं रामप्रवेश राम का परिचय", "name_en": "Bhikhan Tola Village & Intro to Rampravesh Ram"},
                        {"id": "san_ch_08_topic_02", "name_hi": "शिक्षक का आगमन एवं विद्याभ्यास की लगन", "name_en": "Teacher's Arrival & Passion for Education"},
                        {"id": "san_ch_08_topic_03", "name_hi": "प्राथमिक, माध्यमिक एवं कॉलेज में प्रथम स्थान", "name_en": "Top Academic Ranks in School and College"},
                        {"id": "san_ch_08_topic_04", "name_hi": "केंद्रीय लोक सेवा (UPSC) परीक्षा में उत्कृष्ट सफलता", "name_en": "Brilliant Success in UPSC Civil Services Exam"},
                        {"id": "san_ch_08_topic_05", "name_hi": "कठिन परिश्रम, कर्मठता का संदेश एवं पाठ-बोध", "name_en": "Diligence Message, Vocabulary & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_09", "code": "CH09", "chapter_number": 9,
                    "name_hi": "स्वामी दयानन्दः", "name_en": "Swami Dayanand",
                    "topics": [
                        {"id": "san_ch_09_topic_01", "name_hi": "स्वामी दयानन्द का बाल्यकाल (टंकारा गांव, मूलशंकर)", "name_en": "Childhood in Tankara (Moolshankar)"},
                        {"id": "san_ch_09_topic_02", "name_hi": "शिवरात्रि की घटना एवं मूर्तिपूजा से अनास्था", "name_en": "Shivratri Incident & Disillusionment with Idol Worship"},
                        {"id": "san_ch_09_topic_03", "name_hi": "मथुरा में स्वामी विरजानन्द से वैदिक ज्ञान प्राप्ति", "name_en": "Vedic Learning under Swami Virjanand at Mathura"},
                        {"id": "san_ch_09_topic_04", "name_hi": "'सत्यार्थ प्रकाश' रचना एवं आर्य समाज (1875) स्थापना", "name_en": "'Satyarth Prakash' & Arya Samaj (1875) Foundation"},
                        {"id": "san_ch_09_topic_05", "name_hi": "स्त्री-शिक्षा, बाल-विवाह निवारण व डी.ए.वी. विद्यालय", "name_en": "Women Education, Anti-Child Marriage & DAV Schools"}
                    ]
                },
                {
                    "id": "san_ch_10", "code": "CH10", "chapter_number": 10,
                    "name_hi": "मन्दाकिनीवर्णनम्", "name_en": "Description of Mandakini River",
                    "topics": [
                        {"id": "san_ch_10_topic_01", "name_hi": "ग्रंथ संदर्भ — वाल्मीकि रामायण (अयोध्याकाण्ड)", "name_en": "Text Context — Valmiki Ramayana (Ayodhya Kanda)"},
                        {"id": "san_ch_10_topic_02", "name_hi": "चित्रकूट पर्वत के निकट मन्दाकिनी नदी का सौंदर्य", "name_en": "Scenic Beauty of Mandakini River near Chitrakoot"},
                        {"id": "san_ch_10_topic_03", "name_hi": "ऋषि-मुनियों की सूर्य-उपासना एवं स्नान वर्णन", "name_en": "Sages Worshipping Sun God & River Bathing"},
                        {"id": "san_ch_10_topic_04", "name_hi": "हंस-सारस पक्षी, पुष्प और निर्मल जल का प्राकृतिक चित्रण", "name_en": "Swans, Cranes, Flowers & Crystal Water Imagery"},
                        {"id": "san_ch_10_topic_05", "name_hi": "अनुष्टुप् छंद, श्लोकार्थ एवं पाठ-बोध", "name_en": "Anushtubh Meter, Meaning & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_11", "code": "CH11", "chapter_number": 11,
                    "name_hi": "व्याघ्रपथिककथा", "name_en": "The Story of the Tiger and the Traveler",
                    "topics": [
                        {"id": "san_ch_11_topic_01", "name_hi": "ग्रंथ परिचय — नारायण पंडित कृत 'हितोपदेश' (मित्रलाभ)", "name_en": "Text Introduction — Narayana Pandit's 'Hitopadesha'"},
                        {"id": "san_ch_11_topic_02", "name_hi": "बूढ़े बाघ का सोने का कंगन दिखाकर पथिक को लुभाना", "name_en": "Old Tiger Tempting Traveler with Golden Bangle"},
                        {"id": "san_ch_11_topic_03", "name_hi": "पथिक का लोभ और धार्मिक उपदेशों पर अंधविश्वास", "name_en": "Traveler's Greed & Gullibility to Tiger's Virtuous Talk"},
                        {"id": "san_ch_11_topic_04", "name_hi": "दलदल (कीचड़) में फंसना और बाघ द्वारा भक्षण", "name_en": "Getting Trapped in Quagmire & Killed by Tiger"},
                        {"id": "san_ch_11_topic_05", "name_hi": "लोभ के दुष्परिणाम का नीतिपरक संदेश एवं अभ्यास", "name_en": "Fatal Consequences of Greed & Exercises"}
                    ]
                },
                {
                    "id": "san_ch_12", "code": "CH12", "chapter_number": 12,
                    "name_hi": "कर्णस्य दानवीरता", "name_en": "The Generosity of Karna",
                    "topics": [
                        {"id": "san_ch_12_topic_01", "name_hi": "नाटककार परिचय — महाकवि भास ('कर्णभारम्')", "name_en": "Playwright Introduction — Bhasa ('Karnabharam')"},
                        {"id": "san_ch_12_topic_02", "name_hi": "इन्द्र का ब्राह्मण (शक्र) वेश में दान मांगना", "name_en": "Indra Disguised as Brahmin (Shakra) Begging Alms"},
                        {"id": "san_ch_12_topic_03", "name_hi": "कर्ण द्वारा गाय, घोड़े, हाथी, सोना आदि का प्रस्ताव", "name_en": "Karna's Offers: Cows, Horses, Elephants, Gold"},
                        {"id": "san_ch_12_topic_04", "name_hi": "शैल्य के रोकने पर भी कवच और कुण्डल का अभूतपूर्व दान", "name_en": "Supreme Donation of Armor & Earrings despite Shalya's Warning"},
                        {"id": "san_ch_12_topic_05", "name_hi": "दानवीरता, यश की अमरता एवं पाठ-बोध", "name_en": "Supreme Charity, Immortality of Fame & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_13", "code": "CH13", "chapter_number": 13,
                    "name_hi": "विश्वशान्तिः", "name_en": "World Peace",
                    "topics": [
                        {"id": "san_ch_13_topic_01", "name_hi": "वर्तमान विश्व में अशांति का वातावरण", "name_en": "Contemporary Atmosphere of Global Discord"},
                        {"id": "san_ch_13_topic_02", "name_hi": "अशांति के दो मुख्य कारण: द्वेष और असहिष्णुता", "name_en": "Two Primary Causes of Discord: Enmity & Intolerance"},
                        {"id": "san_ch_13_topic_03", "name_hi": "स्वार्थ, शस्त्र-प्रतिस्पर्धा एवं विनाश का भय", "name_en": "Selfishness, Arms Race & Threat of Destruction"},
                        {"id": "san_ch_13_topic_04", "name_hi": "शांति के उपाय: परोपकार, सहिष्णुता व 'वसुधैव कुटुम्बकम्'", "name_en": "Pathways to Peace: Benevolence, Harmony & Universal Family"},
                        {"id": "san_ch_13_topic_05", "name_hi": "नीति-वाक्य, संयुक्त राष्ट्र संघ की भूमिका व पाठ-बोध", "name_en": "Moral Sayings, UN Role & Comprehension"}
                    ]
                },
                {
                    "id": "san_ch_14", "code": "CH14", "chapter_number": 14,
                    "name_hi": "शास्त्रकाराः", "name_en": "The Authors of Scriptures",
                    "topics": [
                        {"id": "san_ch_14_topic_01", "name_hi": "शास्त्र का अर्थ, स्वरूप एवं महत्व", "name_en": "Meaning, Nature & Importance of Shastras"},
                        {"id": "san_ch_14_topic_02", "name_hi": "6 वेदांग एवं प्रवर्तक (शिक्षा, कल्प, व्याकरण, निरुक्त, छंद, ज्योतिष)", "name_en": "6 Vedangas & Authors (Panini, Yaska, Pingala, Lagadha)"},
                        {"id": "san_ch_14_topic_03", "name_hi": "6 दर्शन एवं प्रणेता (सांख्य-कपिल, योग-पतंजलि, न्याय-गौतम, वैशेषिक-कणाद)", "name_en": "6 Darshanas & Sages (Sankhya, Yoga, Nyaya, Vaisheshika)"},
                        {"id": "san_ch_14_topic_04", "name_hi": "मीमांसा (जैमिनी), वेदान्त (बादरायण) एवं प्राचीन विज्ञान (आयुर्वेद, खगोल, गणित)", "name_en": "Mimamsa, Vedanta & Ancient Science (Charaka, Sushruta, Aryabhata, Varahamihira)"},
                        {"id": "san_ch_14_topic_05", "name_hi": "भारतीय ज्ञान-परंपरा, मुख्य तथ्य एवं अभ्यास", "name_en": "Indian Knowledge Tradition, Key Facts & Exercises"}
                    ]
                }
            ]
        }
    ]
}
SYLLABUS_DATA["subjects"].append(sanskrit_subject)

def standardize_and_validate(data):
    """
    Ensure every entity has both:
    1. Direct name_hi / name_en
    2. title/name bilingual object: { hi: ..., en: ... } for backward compatibility with UI components
    3. Proper chapter flattening in books where sections are used
    """
    all_subject_ids = set()
    all_book_ids = set()
    all_chapter_ids = set()
    all_topic_ids = set()

    for sub in data["subjects"]:
        if sub["id"] in all_subject_ids:
            raise ValueError(f"Duplicate subject ID: {sub['id']}")
        all_subject_ids.add(sub["id"])
        sub["name"] = {"hi": sub["name_hi"], "en": sub["name_en"]}

        for book in sub["books"]:
            if book["id"] in all_book_ids:
                raise ValueError(f"Duplicate book ID: {book['id']}")
            all_book_ids.add(book["id"])
            book["name"] = {"hi": book["name_hi"], "en": book["name_en"]}

            # If sections are present, also flatten chapters array on the book for UI components
            flat_chapters = []
            if "sections" in book:
                for sec in book["sections"]:
                    sec["name"] = {"hi": sec["name_hi"], "en": sec["name_en"]}
                    for ch in sec["chapters"]:
                        ch["section_id"] = sec["id"]
                        ch["section"] = sec["name"]
                        flat_chapters.append(ch)
            elif "chapters" in book:
                flat_chapters = book["chapters"]

            book["chapters"] = flat_chapters

            for ch in flat_chapters:
                if ch["id"] in all_chapter_ids:
                    raise ValueError(f"Duplicate chapter ID: {ch['id']}")
                all_chapter_ids.add(ch["id"])
                ch["title"] = {"hi": ch["name_hi"], "en": ch["name_en"]}
                ch["name"] = {"hi": ch["name_hi"], "en": ch["name_en"]}

                if "topics" not in ch:
                    ch["topics"] = []

                for tp in ch["topics"]:
                    if tp["id"] in all_topic_ids:
                        raise ValueError(f"Duplicate topic ID: {tp['id']}")
                    all_topic_ids.add(tp["id"])
                    tp["title"] = {"hi": tp["name_hi"], "en": tp["name_en"]}
                    tp["name"] = {"hi": tp["name_hi"], "en": tp["name_en"]}

    print("=" * 60)
    print("ACADEMIC HIERARCHY VALIDATION SUCCESSFUL!")
    print(f"Total Subjects: {len(all_subject_ids)}")
    print(f"Total Books:    {len(all_book_ids)}")
    print(f"Total Chapters: {len(all_chapter_ids)}")
    print(f"Total Topics:   {len(all_topic_ids)}")
    print("=" * 60)

standardize_and_validate(SYLLABUS_DATA)

# Write to js/data/syllabus.js
js_content = f"""/**
 * Bihar Board (BSEB) Class 10 Academic Hierarchy & Syllabus Data
 * Strictly Bihar Board Class 10 Syllabus (Bilingual: Hindi + English)
 * 
 * Hierarchy:
 * Board -> Class 10 -> Medium -> Subject -> Book -> Section -> Chapter -> Topic
 */

window.BSEB_SYLLABUS = {json.dumps(SYLLABUS_DATA, ensure_ascii=False, indent=2)};
"""

output_path = os.path.join(os.path.dirname(__file__), "..", "js", "data", "syllabus.js")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Wrote complete academic hierarchy to: {os.path.abspath(output_path)}")
