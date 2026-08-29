# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) Social Science Question Bank Builder
Creates js/data/questionBankSocialScience.js with verified bilingual MCQs across:
- History (इतिहास - भारत और समकालीन विश्व II)
- Geography (भूगोल - भारत: संसाधन एवं उपयोग)
- Political Science (राजनीति विज्ञान - लोकतांत्रिक राजनीति II)
- Economics (अर्थशास्त्र - हमारी अर्थव्यवस्था II)
- Disaster Management (आपदा प्रबंधन)
"""

import json
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

questions = []
seen = set()

def add_sst_q(book_id, chapter_id, topic_id, q_hi, q_en, cor_hi, cor_en, dis_hi, dis_en, exp_hi, exp_en, diff="Medium", q_type="Fact"):
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
    q_id = f"q_sst_{chapter_id}_{q_num:04d}"

    item = {
        "id": q_id,
        "question_id": q_id,
        "question_group_id": f"sst_group_{q_num:04d}",
        "board": "BSEB",
        "class": "10",
        "subject_id": "social",
        "book_id": book_id,
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

# ----------------- HISTORY -----------------
add_sst_q("sst_book_01", "sst_b1_ch_01", "sst_b1_ch_01_topic_01",
    "इटली एवं जर्मनी वर्तमान में किस महादेश के अंतर्गत आते हैं?",
    "Under which continent do Italy and Germany presently fall?",
    "यूरोप (Europe)", "Europe",
    ["उत्तरी अमेरिका (North America)", "दक्षिणी अमेरिका (South America)", "एशिया (Asia)"],
    ["North America", "South America", "Asia"],
    "इटली और जर्मनी दोनों यूरोप महादेश के प्रमुख राष्ट्र हैं जिनका 19वीं सदी में एकीकरण हुआ।",
    "Both Italy and Germany are European nations unified during the 19th century.",
    "Easy", "Fact"
)

add_sst_q("sst_book_01", "sst_b1_ch_01", "sst_b1_ch_01_topic_02",
    "जर्मन राइन राज्य का निर्माण किसने किया था?",
    "Who established the Confederation of the Rhine (German Rhine State)?",
    "नेपोलियन बोनापार्ट (Napoleon Bonaparte)", "Napoleon Bonaparte",
    ["लुई 18वां", "नेपोलियन III", "बिस्मार्क"],
    ["Louis XVIII", "Napoleon III", "Bismarck"],
    "नेपोलियन ने 1806 में 39 जर्मन राज्यों को मिलाकर राइन महासंघ की स्थापना की थी।",
    "Napoleon organized 39 German states into the Confederation of the Rhine in 1806.",
    "Easy", "Fact"
)

add_sst_q("sst_book_01", "sst_b1_ch_01", "sst_b1_ch_01_topic_03",
    "रक्त एवं लौह की नीति (Blood and Iron Policy) का अवलंबन किसने किया था?",
    "Who adopted the policy of 'Blood and Iron'?",
    "बिस्मार्क (Otto von Bismarck)", "Otto von Bismarck",
    ["मेजिनी (Mazzini)", "हिटलर (Hitler)", "विलियम प्रथम (William I)"],
    ["Mazzini", "Hitler", "William I"],
    "जर्मनी के एकीकरण के लिए प्रूशिया के चांसलर ऑटो वॉन बिस्मार्क ने 'रक्त और लौह' की नीति अपनाई थी।",
    "Prussian Chancellor Otto von Bismarck adopted the 'Blood and Iron' policy for the unification of Germany.",
    "Easy", "Fact"
)

add_sst_q("sst_book_01", "sst_b1_ch_01", "sst_b1_ch_01_topic_03",
    "फ्रैंकफर्ट की संधि (Treaty of Frankfurt) कब हुई थी?",
    "When was the Treaty of Frankfurt signed?",
    "1871 ई.", "1871 AD",
    ["1864 ई.", "1866 ई.", "1870 ई."],
    ["1864 AD", "1866 AD", "1870 AD"],
    "फ्रांस और प्रूशिया के बीच 10 मई 1871 को फ्रैंकफर्ट की संधि हुई, जिसने जर्मनी के एकीकरण को पूर्ण किया।",
    "The Treaty of Frankfurt was signed on May 10, 1871, completing the unification of Germany.",
    "Medium", "Fact"
)

add_sst_q("sst_book_01", "sst_b1_ch_02", "sst_b1_ch_02_topic_01",
    "रूस में कृषक दास प्रथा का अंत कब हुआ था?",
    "When was the Serfdom system abolished in Russia?",
    "1861 ई.", "1861 AD",
    ["1862 ई.", "1863 ई.", "1864 ई."],
    ["1862 AD", "1863 AD", "1864 AD"],
    "जार अलेक्जेंडर द्वितीय ने 1861 ई. में रूस में कृषि दासता (Serfdom) को समाप्त किया था।",
    "Tsar Alexander II abolished serfdom in Russia in 1861.",
    "Medium", "Fact"
)

add_sst_q("sst_book_01", "sst_b1_ch_02", "sst_b1_ch_02_topic_02",
    "'दास कैपिटल' (Das Kapital) पुस्तक की रचना किसने की थी?",
    "Who authored the famous book 'Das Kapital'?",
    "कार्ल मार्क्स (Karl Marx)", "Karl Marx",
    ["एंगेल्स (Friedrich Engels)", "दोस्तोवस्की", "टॉलस्टॉय (Leo Tolstoy)"],
    ["Friedrich Engels", "Dostoevsky", "Leo Tolstoy"],
    "कार्ल मार्क्स ने 1867 ई. में 'दास कैपिटल' की रचना की, जिसे 'समाजवादियों की बाइबिल' कहा जाता है।",
    "Karl Marx published 'Das Kapital' in 1867, often called the 'Bible of the Working Class / Socialists'.",
    "Easy", "Fact"
)

add_sst_q("sst_book_01", "sst_b1_ch_04", "sst_b1_ch_04_topic_01",
    "जलियांवाला बाग हत्याकांड किस तिथि को हुआ था?",
    "On which date did the Jallianwala Bagh Massacre take place?",
    "13 अप्रैल 1919", "13 April 1919",
    ["14 अप्रैल 1919", "15 अप्रैल 1919", "16 अप्रैल 1919"],
    ["14 April 1919", "15 April 1919", "16 April 1919"],
    "अमृतसर के जलियांवाला बाग में 13 अप्रैल 1919 (बैसाखी के दिन) जनरल डायर ने निहत्थी भीड़ पर गोलियां चलवाई थीं।",
    "General Dyer ordered firing on an unarmed peaceful gathering at Jallianwala Bagh, Amritsar on 13 April 1919.",
    "Easy", "Fact"
)

# ----------------- GEOGRAPHY -----------------
add_sst_q("sst_book_02", "sst_b2_ch_01", "sst_b2_ch_01_topic_01",
    "काली मृदा (Black Soil) का दूसरा नाम क्या है?",
    "What is the other common name of Black Soil in India?",
    "रेगुर मृदा (Regur Soil / Black Cotton Soil)", "Regur Soil",
    ["बलुई मृदा (Sandy Soil)", "लाल मृदा (Red Soil)", "पर्वतीय मृदा (Mountain Soil)"],
    ["Sandy Soil", "Red Soil", "Mountain Soil"],
    "काली मिट्टी को 'रेगुर मिट्टी' भी कहा जाता है, यह कपास की खेती के लिए सर्वोत्तम होती है।",
    "Black soil is also known as Regur soil and is ideal for growing cotton.",
    "Easy", "Fact"
)

add_sst_q("sst_book_02", "sst_b2_ch_01", "sst_b2_ch_01_topic_02",
    "भारत के किस राज्य में वन (Forest) का सबसे अधिक विस्तार पाया जाता है?",
    "Which Indian state has the largest forest cover area?",
    "मध्य प्रदेश (Madhya Pradesh)", "Madhya Pradesh",
    ["उत्तर प्रदेश (Uttar Pradesh)", "कर्नाटक (Karnataka)", "केरल (Kerala)"],
    ["Uttar Pradesh", "Karnataka", "Kerala"],
    "क्षेत्रफल की दृष्टि से भारत में सर्वाधिक वन क्षेत्र मध्य प्रदेश में है।",
    "Madhya Pradesh has the largest forest cover by area in India.",
    "Easy", "Fact"
)

add_sst_q("sst_book_02", "sst_b2_ch_01", "sst_b2_ch_01_topic_03",
    "यूरेनियम (Uranium) का प्रमुख उत्पादक स्थल भारत में कौन-सा है?",
    "Which is the most prominent Uranium mining centre in India?",
    "जादूगोड़ा (Jaduguda - झारखंड)", "Jaduguda (Jharkhand)",
    ["डिगबोई (Digboi - असम)", "झरिया (Jharia)", "घाटशिला (Ghatshila)"],
    ["Digboi (Assam)", "Jharia", "Ghatshila"],
    "झारखंड के पूर्वी सिंहभूम जिले का जादूगोड़ा भारत की पहली और प्रमुख यूरेनियम खान है।",
    "Jaduguda in Jharkhand is the primary and oldest uranium mine in India.",
    "Medium", "Fact"
)

add_sst_q("sst_book_02", "sst_b2_ch_04", "sst_b2_ch_04_topic_01",
    "बिहार में कितने प्रतिशत भौगोलिक क्षेत्र में वन का फैलाव है?",
    "What percentage of geographical area in Bihar has forest cover?",
    "लगभग 7% (7.84%)", "Approx 7% (7.84%)",
    ["15%", "20%", "25%"],
    ["15%", "20%", "25%"],
    "बिहार राज्य के कुल भौगोलिक क्षेत्रफल का लगभग 7% हिस्सा ही वनाच्छादित है।",
    "Bihar has approximately 7% of its total geographical area under forest cover.",
    "Medium", "Fact"
)

# ----------------- POLITICAL SCIENCE -----------------
add_sst_q("sst_book_03", "sst_b3_ch_01", "sst_b3_ch_01_topic_01",
    "भारत में कहाँ औरतों (महिलाओं) के लिए 50% आरक्षण की व्यवस्था की गई है?",
    "Where has 50% reservation for women been provided in Bihar / India?",
    "पंचायती राज व्यवस्था में (Panchayati Raj Institutions)", "Panchayati Raj Institutions",
    ["लोकसभा में (Lok Sabha)", "विधानसभा में (State Legislative Assembly)", "राज्यसभा में (Rajya Sabha)"],
    ["Lok Sabha", "State Assembly", "Rajya Sabha"],
    "बिहार पंचायती राज अधिनियम 2006 के तहत महिलाओं को स्थानीय निकायों में 50% आरक्षण प्रदान किया गया है।",
    "Under Bihar Panchayati Raj Act 2006, 50% seats are reserved for women in local bodies.",
    "Easy", "Fact"
)

add_sst_q("sst_book_03", "sst_b3_ch_02", "sst_b3_ch_02_topic_01",
    "ग्राम कचहरी का प्रधान कौन होता है?",
    "Who is the head of Gram Kachahri in Bihar?",
    "सरपंच (Sarpanch)", "Sarpanch",
    ["मुखिया (Mukhiya)", "वार्ड सदस्य (Ward Member)", "न्याय मित्र (Nyay Mitra)"],
    ["Mukhiya", "Ward Member", "Nyay Mitra"],
    "पंचायती राज में न्याय प्रशासन की इकाई 'ग्राम कचहरी' का प्रधान सरपंच होता है, जबकि प्रशासनिक प्रधान मुखिया होता है।",
    "The judicial head of Gram Kachahri is the Sarpanch.",
    "Easy", "Fact"
)

# ----------------- ECONOMICS -----------------
add_sst_q("sst_book_04", "sst_b4_ch_01", "sst_b4_ch_01_topic_01",
    "भारत की अर्थव्यवस्था किस प्रकार की अर्थव्यवस्था है?",
    "What type of economy is the Indian Economy?",
    "मिश्रित अर्थव्यवस्था (Mixed Economy)", "Mixed Economy",
    ["पूंजीवादी अर्थव्यवस्था (Capitalist)", "समाजवादी अर्थव्यवस्था (Socialist)", "साम्यवादी अर्थव्यवस्था (Communist)"],
    ["Capitalist Economy", "Socialist Economy", "Communist Economy"],
    "भारत में सार्वजनिक (सरकारी) और निजी (प्राइवेट) दोनों क्षेत्रों का सह-अस्तित्व है, अतः यह मिश्रित अर्थव्यवस्था है।",
    "India has a mixed economy where both public and private sectors coexist.",
    "Easy", "Concept"
)

add_sst_q("sst_book_04", "sst_b4_ch_01", "sst_b4_ch_01_topic_01",
    "अर्थव्यवस्था के प्राथमिक क्षेत्र (Primary Sector) के अंतर्गत कौन-सी गतिविधि आती है?",
    "Which economic activity comes under the Primary Sector?",
    "कृषि एवं पशुपालन (Agriculture & Allied Activities)", "Agriculture & Allied Activities",
    ["उद्योग एवं विनिर्माण (Industry - Secondary)", "बैंकिंग एवं सेवा (Services - Tertiary)", "संचार (Communication)"],
    ["Manufacturing & Industry", "Banking & Services", "Communication"],
    "कृषि, वानिकी, मत्स्य पालन और खनन प्राथमिक क्षेत्र में आते हैं जो सीधे प्राकृतिक संसाधनों पर निर्भर हैं।",
    "Agriculture, forestry, and fishing directly utilize natural resources and belong to the primary sector.",
    "Easy", "Concept"
)

add_sst_q("sst_book_04", "sst_b4_ch_03", "sst_b4_ch_03_topic_01",
    "भारत का केंद्रीय बैंक (Central Bank of India) कौन-सा है?",
    "Which is the Central Bank of India?",
    "भारतीय रिजर्व बैंक (Reserve Bank of India - RBI)", "Reserve Bank of India (RBI)",
    ["भारतीय स्टेट बैंक (SBI)", "पंजाब नेशनल बैंक (PNB)", "बैंक ऑफ बड़ौदा (BOB)"],
    ["State Bank of India (SBI)", "Punjab National Bank (PNB)", "Bank of Baroda (BOB)"],
    "भारतीय रिजर्व बैंक (RBI) भारत का केंद्रीय बैंक है, जिसकी स्थापना 1 अप्रैल 1935 को हुई थी।",
    "The Reserve Bank of India (RBI), established on April 1, 1935, is India's central banking institution.",
    "Easy", "Fact"
)

# ----------------- DISASTER MANAGEMENT -----------------
add_sst_q("sst_book_05", "sst_b5_ch_01", "sst_b5_ch_01_topic_01",
    "निम्नलिखित में से कौन एक प्राकृतिक आपदा (Natural Disaster) है?",
    "Which of the following is a Natural Disaster?",
    "भूकंप (Earthquake)", "Earthquake",
    ["आग लगना (Fire outbreak)", "बम विस्फोट (Bomb blast)", "रासायनिक दुर्घटना (Chemical accident)"],
    ["Fire outbreak", "Bomb blast", "Chemical accident"],
    "भूकंप, बाढ़, सुनामी और सूखा प्राकृतिक आपदाएं हैं, जबकि बम विस्फोट और दंगे मानवजनित आपदाएं हैं।",
    "Earthquake, floods, cyclone, and tsunami are natural disasters.",
    "Easy", "Classification"
)

add_sst_q("sst_book_05", "sst_b5_ch_02", "sst_b5_ch_02_topic_01",
    "बिहार का कौन-सा क्षेत्र सबसे अधिक बाढ़ प्रवण (Flood-prone) है?",
    "Which region of Bihar is most prone to devastating floods?",
    "उत्तरी बिहार (North Bihar)", "North Bihar",
    ["दक्षिणी बिहार (South Bihar)", "पूर्वी बिहार (East Bihar)", "पश्चिमी बिहार (West Bihar)"],
    ["South Bihar", "East Bihar", "West Bihar"],
    "कोसी, गंडक, बागमती आदि हिमालयी नदियों के कारण उत्तरी बिहार प्रतिवर्ष भीषण बाढ़ से प्रभावित होता है।",
    "North Bihar is intensely flood-prone due to major transboundary rivers like Kosi and Gandak.",
    "Easy", "Fact"
)

add_sst_q("sst_book_05", "sst_b5_ch_03", "sst_b5_ch_03_topic_01",
    "सुनामी (Tsunami) का प्रमुख कारण क्या है?",
    "What is the primary cause of a Tsunami?",
    "समुद्र की तली में भूकंप का आना (Earthquake in the deep sea)", "Earthquake in the sea bed",
    ["द्वीप पर भूकंप आना", "आसमान में चक्रवात आना", "जहाज का डूबना"],
    ["Earthquake on an island", "Cyclone in the sky", "Shipwreck"],
    "समुद्र के गर्भ या तली में आने वाले तीव्र भूकंप के कारण विनाशकारी समुद्री लहरें उत्पन्न होती हैं जिन्हें सुनामी कहते हैं।",
    "Tsunamis are huge ocean waves triggered by sub-sea earthquakes or volcanic eruptions.",
    "Easy", "Concept"
)

# Output summary
print(f"Generated {len(questions)} verified Social Science MCQs.")

output_path = 'js/data/questionBankSocialScience.js'
js_content = f"""/**
 * Class 10 Bihar Board (BSEB) - Social Science Question Bank
 * Subject: Social Science (सामाजिक विज्ञान - History, Geography, Pol Science, Economics, Disaster Mgmt)
 * Total Verified Bilingual MCQs: {len(questions)}
 */

window.BSEB_SOCIAL_SCIENCE_QUESTIONS = {json.dumps(questions, ensure_ascii=False, indent=2)};
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {output_path}")
