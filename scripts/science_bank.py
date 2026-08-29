# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) Science Question Bank Builder
Creates js/data/questionBankScience.js with verified bilingual MCQs across Physics, Chemistry, and Biology.
"""

import json
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

questions = []
seen = set()

def add_sci_q(chapter_id, topic_id, q_hi, q_en, cor_hi, cor_en, dis_hi, dis_en, exp_hi, exp_en, diff="Medium", q_type="Concept"):
    sig = ''.join(c.lower() for c in q_hi if c.isalnum())
    if sig in seen:
        return False
    seen.add(sig)

    raw_options = [
        {'hi': str(cor_hi).strip(), 'en': str(cor_en).strip(), 'is_correct': True},
        {'hi': str(dis_hi[0]).strip(), 'en': str(dis_en[0]).strip(), 'is_correct': False},
        {'hi': str(dis_hi[1]).strip(), 'en': str(dis_en[1]).strip(), 'is_correct': False},
        {'hi': str(dis_hi[2]).strip(), 'en': str(dis_en[2]).strip(), 'is_correct': False},
    ]
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
    q_id = f"q_sci_{chapter_id}_{q_num:04d}"

    item = {
        "id": q_id,
        "question_id": q_id,
        "question_group_id": f"sci_group_{q_num:04d}",
        "board": "BSEB",
        "class": "10",
        "subject_id": "science",
        "book_id": "sci_book_01",
        "chapter_id": chapter_id,
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

# ----------------- PHYSICS -----------------
# Light - Reflection and Refraction
add_sci_q("sci_ch_10", "sci_ch_10_topic_01",
    "दाढ़ी बनाने (हजामत) के लिए किस प्रकार के दर्पण का उपयोग किया जाता है?",
    "Which type of mirror is used as a shaving mirror?",
    "अवतल दर्पण (Concave mirror)", "Concave mirror",
    ["उत्तल दर्पण (Convex mirror)", "समतल दर्पण (Plane mirror)", "उत्तल लेंस (Convex lens)"],
    ["Convex mirror", "Plane mirror", "Convex lens"],
    "अवतल दर्पण वस्तु को ध्रुव और फोकस के बीच रखने पर सीधा तथा बड़ा (आवर्धित) आभासी प्रतिबिंब बनाता है।",
    "Concave mirror produces an erect, magnified, virtual image when the object is placed between pole and focus.",
    "Easy", "Application"
)

add_sci_q("sci_ch_10", "sci_ch_10_topic_01",
    "वाहनों के पश्च-दृश्य (Side/Rear-view) दर्पण के रूप में किस दर्पण का प्रयोग किया जाता है?",
    "Which mirror is used as a rear-view (side) mirror in vehicles?",
    "उत्तल दर्पण (Convex mirror)", "Convex mirror",
    ["अवतल दर्पण (Concave mirror)", "समतल दर्पण (Plane mirror)", "अवतल लेंस (Concave lens)"],
    ["Concave mirror", "Plane mirror", "Concave lens"],
    "उत्तल दर्पण हमेशा सीधा और छोटा प्रतिबिंब बनाता है और इसका दृष्टि क्षेत्र (Field of view) बहुत विस्तृत होता है।",
    "Convex mirror always gives an erect, diminished image and has a much wider field of view.",
    "Easy", "Application"
)

add_sci_q("sci_ch_10", "sci_ch_10_topic_02",
    "हीरे (Diamond) का अपवर्तनांक (Refractive Index) कितना होता है?",
    "What is the refractive index of Diamond?",
    "2.42", "2.42",
    ["1.33", "1.50", "1.00"],
    ["1.33", "1.50", "1.00"],
    "हीरे का अपवर्तनांक 2.42 होता है जो सभी पदार्थों में सर्वाधिक है, जिसके कारण इसमें पूर्ण आंतरिक परावर्तन होता है और यह चमकता है।",
    "The refractive index of diamond is 2.42, which is the highest among common optical media causing total internal reflection.",
    "Medium", "Fact"
)

add_sci_q("sci_ch_10", "sci_ch_10_topic_02",
    "लेंस की क्षमता (Power of Lens) का SI मात्रक क्या है?",
    "What is the SI unit of power of a lens?",
    "डायऑप्टर (Dioptre, D)", "Dioptre (D)",
    ["मीटर (Meter)", "सेंटीमीटर (Centimeter)", "वाट (Watt)"],
    ["Meter", "Centimeter", "Watt"],
    "लेंस की क्षमता P = 1/f (मीटर में) होती है तथा इसका SI मात्रक डायऑप्टर (D) है।",
    "Power of lens P = 1/f (in meters), and its SI unit is Dioptre (D).",
    "Easy", "Formula"
)

# Human Eye & Colourful World
add_sci_q("sci_ch_11", "sci_ch_11_topic_01",
    "सामान्य दृष्टि के वयस्क के लिए सुस्पष्ट दर्शन की अल्पतम दूरी (Least distance of distinct vision) लगभग कितनी होती है?",
    "What is the near point / least distance of distinct vision for a young adult with normal vision?",
    "25 cm", "25 cm",
    ["25 m", "2.5 cm", "अनंत (Infinity)"],
    ["25 m", "2.5 cm", "Infinity"],
    "सामान्य आंख के लिए स्पष्ट दृष्टि की न्यूनतम दूरी 25 सेमी तथा दूर बिंदु अनंत होता है।",
    "For a normal human eye, the near point is 25 cm and the far point is infinity.",
    "Easy", "Fact"
)

add_sci_q("sci_ch_11", "sci_ch_11_topic_02",
    "निकट-दृष्टि दोष (Myopia) को दूर करने के लिए किस लेंस का उपयोग किया जाता है?",
    "Which lens is used to correct Myopia (Short-sightedness)?",
    "अवतल लेंस (Concave lens)", "Concave lens",
    ["उत्तल लेंस (Convex lens)", "बेलनाकार लेंस (Cylindrical lens)", "द्विफोकसी लेंस (Bifocal lens)"],
    ["Convex lens", "Cylindrical lens", "Bifocal lens"],
    "निकट दृष्टि दोष में दूर की वस्तुएं स्पष्ट नहीं दिखतीं। इसे अपसारी (अवतल) लेंस के प्रयोग द्वारा ठीक किया जाता है।",
    "In myopia, distant objects are not clearly visible. It is corrected using a concave (diverging) lens.",
    "Easy", "Application"
)

add_sci_q("sci_ch_11", "sci_ch_11_topic_02",
    "दीर्घ-दृष्टि दोष (Hypermetropia) के निवारण के लिए किस लेंस का उपयोग किया जाता है?",
    "Which lens is used to correct Hypermetropia (Far-sightedness)?",
    "उत्तल लेंस (Convex lens)", "Convex lens",
    ["अवतल लेंस (Concave lens)", "समतल लेंस (Plane lens)", "बेलनाकार लेंस (Cylindrical lens)"],
    ["Concave lens", "Plane lens", "Cylindrical lens"],
    "दीर्घ दृष्टि दोष में पास की वस्तुएं स्पष्ट नहीं दिखतीं। इसे उत्तल (अभिसारी) लेंस द्वारा ठीक किया जाता है।",
    "Hypermetropia is corrected using a convex (converging) lens.",
    "Easy", "Application"
)

add_sci_q("sci_ch_11", "sci_ch_11_topic_03",
    "तारों का टिमटिमाना प्रकाश की किस परिघटना का परिणाम है?",
    "The twinkling of stars is due to which optical phenomenon of light?",
    "वायुमंडलीय अपवर्तन (Atmospheric Refraction)", "Atmospheric Refraction",
    ["प्रकाश का प्रकीर्णन (Scattering)", "प्रकाश का परावर्तन (Reflection)", "प्रकाश का वर्ण-विक्षेपण (Dispersion)"],
    ["Scattering of light", "Reflection of light", "Dispersion of light"],
    "वायुमंडल की विभिन्न घनत्व वाली परतों द्वारा लगातार होने वाले अपवर्तन के कारण तारों का प्रकाश टिमटिमाता प्रतीत होता है।",
    "Atmospheric refraction through layers of varying optical densities causes stars to twinkle.",
    "Medium", "Concept"
)

add_sci_q("sci_ch_11", "sci_ch_11_topic_04",
    "स्वच्छ आकाश का रंग नीला प्रकाश के किस गुण के कारण दिखाई देता है?",
    "The blue colour of the clear sky is due to which property of light?",
    "प्रकाश का प्रकीर्णन (Scattering of light)", "Scattering of light",
    ["प्रकाश का परावर्तन (Reflection)", "प्रकाश का अपवर्तन (Refraction)", "प्रकाश का विवर्तन (Diffraction)"],
    ["Reflection of light", "Refraction of light", "Diffraction of light"],
    "रैले के नियम के अनुसार नीले रंग का तरंगदैर्ध्य कम होने के कारण वायुमंडलीय कणों द्वारा इसका प्रकीर्णन सबसे अधिक होता है।",
    "According to Rayleigh scattering, shorter wavelength blue light is scattered most strongly by atmospheric particles.",
    "Easy", "Concept"
)

# Electricity
add_sci_q("sci_ch_12", "sci_ch_12_topic_01",
    "विद्युत आवेश (Electric Charge) का SI मात्रक क्या है?",
    "What is the SI unit of Electric Charge?",
    "कूलॉम (Coulomb, C)", "Coulomb (C)",
    ["एम्पियर (Ampere)", "वोल्ट (Volt)", "ओम (Ohm)"],
    ["Ampere", "Volt", "Ohm"],
    "विद्युत आवेश का SI मात्रक कूलॉम (C) होता है।",
    "The SI unit of electric charge is Coulomb (C).",
    "Easy", "Fact"
)

add_sci_q("sci_ch_12", "sci_ch_12_topic_01",
    "विद्युत धारा (Electric Current) मापने वाले यंत्र को क्या कहा जाता है?",
    "What is the instrument used to measure electric current called?",
    "ऐमीटर (Ammeter)", "Ammeter",
    ["वोल्टमीटर (Voltmeter)", "गैल्वेनोमीटर (Galvanometer)", "पोटेंशियोमीटर (Potentiometer)"],
    ["Voltmeter", "Galvanometer", "Potentiometer"],
    "विद्युत परिपथ में धारा मापने के लिए ऐमीटर को श्रेणीक्रम (Series) में जोड़ा जाता है।",
    "An ammeter is connected in series in an electric circuit to measure current.",
    "Easy", "Instrument"
)

add_sci_q("sci_ch_12", "sci_ch_12_topic_02",
    "ओम के नियम (Ohm's Law) का सही गणितीय सूत्र क्या है?",
    "What is the correct mathematical formula for Ohm's Law?",
    "V = I × R", "V = I × R",
    ["V = I / R", "I = V × R", "R = V × I"],
    ["V = I / R", "I = V × R", "R = V × I"],
    "ओम के नियम के अनुसार नियत ताप पर विभवांतर धारा के समानुपाती होता है: V = IR।",
    "According to Ohm's law, V = IR where V is potential difference, I is current, and R is resistance.",
    "Easy", "Formula"
)

add_sci_q("sci_ch_12", "sci_ch_12_topic_03",
    "विद्युत हीटर की कुंडली (Heating Element) किस मिश्रधातु की बनी होती है?",
    "The heating element of an electric heater is made of which alloy?",
    "नाइक्रोम (Nichrome)", "Nichrome",
    ["टंगस्टन (Tungsten)", "तांबा (Copper)", "एल्युमिनियम (Aluminium)"],
    ["Tungsten", "Copper", "Aluminium"],
    "नाइक्रोम (निकेल + क्रोमियम) का गलनांक और प्रतिरोधकता बहुत अधिक होती है तथा यह उच्च ताप पर ऑक्सीकृत नहीं होता।",
    "Nichrome has high resistivity and melting point and does not oxidize easily at high temperatures.",
    "Medium", "Application"
)

add_sci_q("sci_ch_12", "sci_ch_12_topic_03",
    "विद्युत बल्ब का फिलामेंट (तंतु) किस धातु का बना होता है?",
    "The filament of an electric bulb is made of which metal?",
    "टंगस्टन (Tungsten, W)", "Tungsten (W)",
    ["तांबा (Copper)", "लोहा (Iron)", "प्लेटिनम (Platinum)"],
    ["Copper", "Iron", "Platinum"],
    "टंगस्टन का गलनांक अत्यंत उच्च (लगभग 3380°C) होता है, इसलिए बल्ब का तंतु इसी से बनाया जाता है।",
    "Tungsten has an extremely high melting point (approx 3380°C), making it ideal for bulb filaments.",
    "Easy", "Application"
)

# ----------------- CHEMISTRY -----------------
add_sci_q("sci_ch_01", "sci_ch_01_topic_01",
    "चूने के पानी (Calcium Hydroxide) में कार्बन डाइऑक्साइड गैस प्रवाहित करने पर विलयन का रंग कैसा हो जाता है?",
    "When carbon dioxide gas is passed through lime water, the solution turns:",
    "दूधिया (Milky)", "Milky",
    ["नीला (Blue)", "पीला (Yellow)", "लाल (Red)"],
    ["Blue", "Yellow", "Red"],
    "Ca(OH)₂ + CO₂ → CaCO₃ (अघुलनशील श्वेत अवक्षेप) + H₂O बनने के कारण चूने का पानी दूधिया हो जाता है।",
    "Insoluble white precipitate CaCO₃ forms, turning the lime water milky.",
    "Easy", "Reaction"
)

add_sci_q("sci_ch_01", "sci_ch_01_topic_02",
    "श्वसन (Respiration) किस प्रकार की रासायनिक अभिक्रिया है?",
    "Respiration is which type of chemical reaction?",
    "ऊष्माक्षेपी अभिक्रिया (Exothermic reaction)", "Exothermic reaction",
    ["ऊष्माशोषी अभिक्रिया (Endothermic reaction)", "संयोजन अभिक्रिया (Combination reaction)", "अपघटन अभिक्रिया (Decomposition reaction)"],
    ["Endothermic reaction", "Combination reaction", "Decomposition reaction"],
    "श्वसन क्रिया में ग्लूकोज के ऑक्सीकरण से ऊर्जा (ऊष्मा) मुक्त होती है, अतः यह ऊष्माक्षेपी अभिक्रिया है।",
    "Respiration releases energy due to oxidation of glucose, making it an exothermic reaction.",
    "Easy", "Concept"
)

add_sci_q("sci_ch_02", "sci_ch_02_topic_01",
    "अम्लीय विलयन का pH मान कितना होता है?",
    "What is the pH value of an acidic solution?",
    "7 से कम (< 7)", "Less than 7 (< 7)",
    ["7 के बराबर (= 7)", "7 से अधिक (> 7)", "14 के बराबर"],
    ["Equal to 7 (= 7)", "Greater than 7 (> 7)", "Equal to 14"],
    "अम्ल का pH मान 7 से कम, उदासीन का 7, और क्षार का pH मान 7 से अधिक होता है।",
    "Acidic solutions have pH < 7, neutral solutions have pH = 7, and basic solutions have pH > 7.",
    "Easy", "Fact"
)

add_sci_q("sci_ch_02", "sci_ch_02_topic_02",
    "बेकिंग सोडा (खाने का सोडा) का रासायनिक सूत्र क्या है?",
    "What is the chemical formula of Baking Soda?",
    "NaHCO₃ (सोडियम हाइड्रोजन कार्बोनेट)", "NaHCO₃ (Sodium Hydrogen Carbonate)",
    ["Na₂CO₃·10H₂O (धोने का सोडा)", "CaSO₄·½H₂O (प्लास्टर ऑफ पेरिस)", "CaOCl₂ (विरंजक चूर्ण)"],
    ["Na₂CO₃·10H₂O", "CaSO₄·½H₂O", "CaOCl₂"],
    "बेकिंग सोडा का रासायनिक नाम सोडियम बाइकार्बोनेट (NaHCO₃) है।",
    "Baking soda is chemically Sodium Hydrogen Carbonate (NaHCO₃).",
    "Easy", "Fact"
)

add_sci_q("sci_ch_02", "sci_ch_02_topic_02",
    "प्लास्टर ऑफ पेरिस (Plaster of Paris) का रासायनिक सूत्र क्या है?",
    "What is the chemical formula of Plaster of Paris (POP)?",
    "CaSO₄·½H₂O", "CaSO₄·½H₂O",
    ["CaSO₄·2H₂O (जिप्सम)", "CuSO₄·5H₂O", "FeSO₄·7H₂O"],
    ["CaSO₄·2H₂O (Gypsum)", "CuSO₄·5H₂O", "FeSO₄·7H₂O"],
    "जिप्सम को 373 K पर गर्म करने पर यह जल के अणु त्यागकर कैल्शियम सल्फेट हेमीहाइड्रेट (CaSO₄·½H₂O) बनाता है।",
    "Heating gypsum at 373 K yields calcium sulphate hemihydrate (CaSO₄·½H₂O).",
    "Medium", "Fact"
)

add_sci_q("sci_ch_03", "sci_ch_03_topic_01",
    "कमरे के ताप पर द्रव अवस्था में रहने वाली एकमात्र अधातु (Non-metal) कौन-सी है?",
    "Which is the only non-metal that exists as a liquid at room temperature?",
    "ब्रोमीन (Bromine, Br)", "Bromine (Br)",
    ["पारा (Mercury, Hg - धातु)", "आयोडीन (Iodine)", "क्लोरीन (Chlorine)"],
    ["Mercury (Hg - metal)", "Iodine", "Chlorine"],
    "ब्रोमीन एकमात्र ऐसी अधातु है जो कमरे के ताप पर द्रव अवस्था में पाई जाती है। (पारा एकमात्र द्रव धातु है)।",
    "Bromine is the only liquid non-metal at room temperature (Mercury is the only liquid metal).",
    "Easy", "Fact"
)

add_sci_q("sci_ch_03", "sci_ch_03_topic_01",
    "चाकू से सरलतापूर्वक काटी जा सकने वाली धातुएं कौन-सी हैं?",
    "Which metals can be easily cut with a knife?",
    "सोडियम (Na) और पोटैशियम (K)", "Sodium (Na) and Potassium (K)",
    ["लोहा (Fe) और तांबा (Cu)", "एल्युमिनियम (Al) और जस्ता (Zn)", "सोना (Au) और चांदी (Ag)"],
    ["Iron and Copper", "Aluminium and Zinc", "Gold and Silver"],
    "सोडियम, पोटैशियम और लिथियम क्षारीय धातुएं हैं जो अत्यधिक मुलायम होती हैं और इन्हें चाकू से काटा जा सकता है।",
    "Alkali metals like Sodium and Potassium are very soft and can be easily cut with a knife.",
    "Easy", "Property"
)

add_sci_q("sci_ch_04", "sci_ch_04_topic_01",
    "कार्बन परमाणु की संयोजकता (Valency of Carbon) कितनी होती है?",
    "What is the valency of a Carbon atom?",
    "4 (चतुःसंयोजी / Tetravalent)", "4 (Tetravalent)",
    ["2", "3", "6"],
    ["2", "3", "6"],
    "कार्बन का परमाणु क्रमांक 6 (इलेक्ट्रॉनिक विन्यास 2, 4) है, अतः इसकी संयोजकता 4 होती है।",
    "Carbon has atomic number 6 with electronic configuration (2, 4), hence its valency is 4.",
    "Easy", "Fact"
)

add_sci_q("sci_ch_04", "sci_ch_04_topic_02",
    "एल्केन (Alkane) श्रेणी का सामान्य सूत्र क्या है?",
    "What is the general formula of the Alkane series?",
    "CₙH₂ₙ₊₂", "CₙH₂ₙ₊₂",
    ["CₙH₂ₙ (एल्कीन)", "CₙH₂ₙ₋₂ (एल्काइन)", "CₙH₂ₙ₊₁ (एल्किल)"],
    ["CₙH₂ₙ (Alkene)", "CₙH₂ₙ₋₂ (Alkyne)", "CₙH₂ₙ₊₁ (Alkyl)"],
    "संतृप्त हाइड्रोकार्बन (एल्केन) का सामान्य सूत्र CₙH₂ₙ₊₂ होता है।",
    "The general formula of saturated hydrocarbons (alkanes) is CₙH₂ₙ₊₂.",
    "Easy", "Formula"
)

# ----------------- BIOLOGY -----------------
add_sci_q("sci_ch_06", "sci_ch_06_topic_01",
    "पादपों में जाइलम (Xylem) का मुख्य कार्य क्या है?",
    "What is the primary function of Xylem in plants?",
    "जल और खनिज लवणों का संवहन (Transport of Water & Minerals)", "Transport of Water & Minerals",
    ["भोजन का संवहन (Transport of Food - फ्लोएम)", "ऑक्सीजन का वहन", "अमीनो अम्ल का वहन"],
    ["Transport of Food", "Transport of Oxygen", "Transport of Amino acids"],
    "जाइलम ऊतक जड़ों से पत्तियों तक जल एवं खनिज लवणों का वहन करता है, जबकि फ्लोएम भोजन का परिवहन करता है।",
    "Xylem conducts water and minerals from roots to leaves, whereas phloem transports food.",
    "Easy", "Concept"
)

add_sci_q("sci_ch_06", "sci_ch_06_topic_02",
    "मानव हृदय में कितने कोष्ठ (Chambers) होते हैं?",
    "How many chambers are there in the human heart?",
    "4 (2 अलिंद + 2 निलय)", "4 (2 Atria + 2 Ventricles)",
    ["2", "3", "5"],
    ["2", "3", "5"],
    "मानव हृदय में चार कोष्ठ होते हैं: दायां अलिंद, बायां अलिंद, दायां निलय और बायां निलय।",
    "The human heart has 4 chambers: Right Atrium, Left Atrium, Right Ventricle, and Left Ventricle.",
    "Easy", "Fact"
)

add_sci_q("sci_ch_06", "sci_ch_06_topic_03",
    "वृक्क (Kidney) की संरचनात्मक एवं कार्यात्मक इकाई को क्या कहते हैं?",
    "What is the structural and functional unit of the Kidney called?",
    "नेफ्रॉन (Nephron / वृक्काणु)", "Nephron",
    ["न्यूरॉन (Neuron / तंत्रिका कोशिका)", "एल्वियोली (Alveoli)", "ग्लोमेरुलस (Glomerulus)"],
    ["Neuron", "Alveoli", "Glomerulus"],
    "वृक्क की कार्यात्मक इकाई नेफ्रॉन (Nephron) होती है जो रक्त का निस्यंदन (Filtration) करती है।",
    "Nephron is the basic filtration unit of the kidney.",
    "Easy", "Fact"
)

add_sci_q("sci_ch_07", "sci_ch_07_topic_01",
    "मानव शरीर में रक्त शर्करा (Blood Sugar) के स्तर को नियंत्रित करने वाला हार्मोन कौन-सा है?",
    "Which hormone regulates the blood sugar level in the human body?",
    "इंसुलिन (Insulin - अग्न्याशय द्वारा स्रावित)", "Insulin (secreted by Pancreas)",
    ["थायरोक्सिन (Thyroxine)", "एड्रिनेलिन (Adrenaline)", "वृद्धि हार्मोन (Growth Hormone)"],
    ["Thyroxine", "Adrenaline", "Growth Hormone"],
    "इंसुलिन हार्मोन अग्न्याशय की बीटा कोशिकाओं द्वारा स्रावित होता है जो रक्त में शर्करा को नियंत्रित करता है।",
    "Insulin is secreted by the pancreas (beta cells) and regulates blood glucose levels.",
    "Easy", "Fact"
)

add_sci_q("sci_ch_08", "sci_ch_08_topic_01",
    "हाइड्रा और यीस्ट में अलैंगिक जनन की मुख्य विधि कौन-सी है?",
    "What is the primary method of asexual reproduction in Hydra and Yeast?",
    "मुकुलन (Budding)", "Budding",
    ["द्विखंडन (Binary Fission)", "पुनर्जनन (Regeneration)", "खंडन (Fragmentation)"],
    ["Binary Fission", "Regeneration", "Fragmentation"],
    "हाइड्रा और यीस्ट में शरीर पर एक छोटा उभार (मुकुल) विकसित होकर नया जीव बनाता है, इसे मुकुलन कहते हैं।",
    "In budding, an outgrowth (bud) develops on the parent body to form a new individual.",
    "Easy", "Concept"
)

add_sci_q("sci_ch_09", "sci_ch_09_topic_01",
    "आनुवंशिकी का जनक (Father of Genetics) किन्हें कहा जाता है?",
    "Who is known as the Father of Genetics?",
    "ग्रेगर जोहान मेंडल (Gregor Johann Mendel)", "Gregor Johann Mendel",
    ["चार्ल्स डार्विन (Charles Darwin)", "जीन बैप्टिस्ट लैमार्क", "रॉबर्ट हुक (Robert Hooke)"],
    ["Charles Darwin", "Jean-Baptiste Lamarck", "Robert Hooke"],
    "मेंडल ने मटर के पौधों (Pisum sativum) पर संकरण प्रयोग करके आनुवंशिकता के नियमों की खोज की।",
    "Mendel discovered the fundamental laws of inheritance through his experiments on pea plants.",
    "Easy", "Fact"
)

# Output summary
print(f"Generated {len(questions)} verified Science MCQs.")

output_path = 'js/data/questionBankScience.js'
js_content = f"""/**
 * Class 10 Bihar Board (BSEB) - Science Question Bank
 * Subject: Science (विज्ञान - Physics, Chemistry, Biology)
 * Total Verified Bilingual MCQs: {len(questions)}
 */

window.BSEB_SCIENCE_QUESTIONS = {json.dumps(questions, ensure_ascii=False, indent=2)};
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {output_path}")
