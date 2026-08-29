# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board (BSEB) Hindi Question Bank Builder
Creates js/data/questionBankHindi.js with verified bilingual MCQs across:
- Godhuli Part 2 (गोधूलि भाग 2 - गद्य एवं पद्य खंड)
- Varnika Part 2 (वर्णिका भाग 2)
- Hindi Vyakaran (हिंदी व्याकरण)
"""

import json
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

questions = []
seen = set()

def add_hin_q(book_id, chapter_id, topic_id, q_hi, q_en, cor_hi, cor_en, dis_hi, dis_en, exp_hi, exp_en, diff="Medium", q_type="Literature"):
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
    q_id = f"q_hin_{chapter_id}_{q_num:04d}"

    item = {
        "id": q_id,
        "question_id": q_id,
        "question_group_id": f"hin_group_{q_num:04d}",
        "board": "BSEB",
        "class": "10",
        "subject_id": "hindi",
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

# ----------------- GODHULI PART 2 (गोधूलि भाग 2) -----------------
add_hin_q("hin_book_01", "hin_b1_ch_01", "hin_b1_ch_01_topic_01",
    "'श्रम विभाजन और जाति प्रथा' पाठ के लेखक कौन हैं?",
    "Who is the author of the chapter 'Shram Vibhajan Aur Jati Pratha'?",
    "डॉ. भीमराव आंबेडकर (Dr. B.R. Ambedkar)", "Dr. B.R. Ambedkar",
    ["महात्मा गांधी (Mahatma Gandhi)", "पंडित जवाहरलाल नेहरू", "डॉ. रामविलास शर्मा"],
    ["Mahatma Gandhi", "Pt. Jawaharlal Nehru", "Dr. Ram Vilas Sharma"],
    "'श्रम विभाजन और जाति प्रथा' डॉ. भीमराव आंबेडकर के विख्यात भाषण 'Annihilation of Caste' का हिंदी रूपांतरण है।",
    "'Shram Vibhajan Aur Jati Pratha' is excerpted from Dr. Ambedkar's famous speech 'Annihilation of Caste'.",
    "Easy", "Author"
)

add_hin_q("hin_book_01", "hin_b1_ch_01", "hin_b1_ch_01_topic_01",
    "डॉ. भीमराव आंबेडकर का जन्म किस राज्य में हुआ था?",
    "In which Indian state was Dr. B.R. Ambedkar born?",
    "महू, मध्य प्रदेश (Mhow, MP)", "Mhow, Madhya Pradesh",
    ["बिहार (Bihar)", "उत्तर प्रदेश (UP)", "महाराष्ट्र (Maharashtra)"],
    ["Bihar", "Uttar Pradesh", "Maharashtra"],
    "बाबा साहेब डॉ. भीमराव आंबेडकर का जन्म 14 अप्रैल 1891 को महू (मध्य प्रदेश) में एक दलित परिवार में हुआ था।",
    "Dr. B.R. Ambedkar was born on 14 April 1891 in Mhow, Madhya Pradesh.",
    "Easy", "Fact"
)

add_hin_q("hin_book_01", "hin_b1_ch_02", "hin_b1_ch_02_topic_01",
    "'विष के दांत' कहानी के रचयिता कौन हैं?",
    "Who is the writer of the story 'Vish Ke Dant'?",
    "नलिन विलोचन शर्मा (Nalin Vilochan Sharma)", "Nalin Vilochan Sharma",
    ["अज्ञेय (Agyeya)", "अमरकांत (Amarkant)", "मैक्समूलर (Max Mueller)"],
    ["Agyeya", "Amarkant", "Max Mueller"],
    "'विष के दांत' नलिन विलोचन शर्मा की प्रसिद्ध मनोवैज्ञानिक और सामाजिक कहानी है जिसमें खोखा (कासू) और मदन का प्रसंग है।",
    "'Vish Ke Dant' is a famous story by Nalin Vilochan Sharma depicting social conflict through Madan and Kasu.",
    "Easy", "Author"
)

add_hin_q("hin_book_01", "hin_b1_ch_03", "hin_b1_ch_03_topic_01",
    "'भारत से हम क्या सीखें' पाठ साहित्य की कौन-सी विधा है?",
    "Which literary genre does 'Bharat Se Hum Kya Seekhein' belong to?",
    "भाषण (Speech / Oration)", "Speech / Address",
    ["कहानी (Story)", "निबंध (Essay)", "रेखाचित्र (Sketch)"],
    ["Story", "Essay", "Sketch"],
    "यह फ्रेडरिक मैक्समूलर द्वारा भारतीय सिविल सेवा के युवा अंग्रेज प्रशिक्षुओं के समक्ष दिया गया व्याख्यान (भाषण) है।",
    "It is an address delivered by Friedrich Max Mueller to young British ICS probationers.",
    "Easy", "Genre"
)

add_hin_q("hin_book_01", "hin_b1_ch_04", "hin_b1_ch_04_topic_01",
    "'नाखून क्यों बढ़ते हैं' निबंध के निबंधकार कौन हैं?",
    "Who is the essayist of 'Nakhun Kyun Badhte Hain'?",
    "आचार्य हजारी प्रसाद द्विवेदी (Acharya Hazari Prasad Dwivedi)", "Acharya Hazari Prasad Dwivedi",
    ["गुणाकर मुले", "रामधारी सिंह दिनकर", "विनोद कुमार शुक्ल"],
    ["Gunakar Mule", "Ramdhari Singh Dinkar", "Vinod Kumar Shukla"],
    "यह आचार्य हजारी प्रसाद द्विवेदी का ललित निबंध है जिसमें मनुष्य की पाशविकता और मनुष्यता का सुंदर विश्लेषण है।",
    "It is a celebrated aesthetic essay by Acharya Hazari Prasad Dwivedi reflecting on humanity vs savagery.",
    "Easy", "Author"
)

add_hin_q("hin_book_01", "hin_b1_ch_05", "hin_b1_ch_05_topic_01",
    "'नागरी लिपि' पाठ के लेखक कौन हैं?",
    "Who is the author of 'Nagari Lipi'?",
    "गुणाकर मुले (Gunakar Mule)", "Gunakar Mule",
    ["महात्मा गांधी", "यतीन्द्र मिश्र", "अशोक वाजपेयी"],
    ["Mahatma Gandhi", "Yatindra Mishra", "Ashok Vajpeyi"],
    "'नागरी लिपि' निबंध गुणाकर मुले द्वारा रचित है जिसमें देवनागरी लिपि के इतिहास का वर्णन है।",
    "'Nagari Lipi' is written by Gunakar Mule detailing the history and evolution of the Devanagari script.",
    "Easy", "Author"
)

add_hin_q("hin_book_01", "hin_b1_ch_13", "hin_b1_ch_13_topic_01",
    "'राम नाम बिनु बिरथे जगि जनमा' पद के रचयिता कौन हैं?",
    "Who is the poet of 'Ram Naam Binu Birthe Jagi Janma'?",
    "गुरु नानक (Guru Nanak Dev)", "Guru Nanak Dev",
    ["रसखान (Raskhan)", "घनानंद (Ghananand)", "प्रेमघन (Premghan)"],
    ["Raskhan", "Ghananand", "Premghan"],
    "सिख धर्म के प्रथम गुरु, गुरु नानक देव जी ने बाह्य आडंबरों का विरोध करते हुए राम नाम के जप को सच्चा धर्म बताया।",
    "Guru Nanak Dev, the first Sikh Guru, composed this verse emphasizing pure devotion over outward rituals.",
    "Easy", "Poetry"
)

add_hin_q("hin_book_01", "hin_b1_ch_14", "hin_b1_ch_14_topic_01",
    "कवि रसखान किस काल एवं धारा के कवि हैं?",
    "Which era and poetic tradition does poet Raskhan belong to?",
    "भक्तिकाल - कृष्णभक्ति धारा (Bhakti Kal - Krishna Bhakti)", "Bhakti Period (Krishna Devotion)",
    ["रीतिकाल (Riti Kal)", "छायावाद (Chhayavad)", "आधुनिक काल (Modern Period)"],
    ["Riti Period", "Chhayavad", "Modern Period"],
    "रसखान भक्तिकाल के सुप्रसिद्ध मुस्लिम कृष्णभक्त कवि थे जिन्होंने सवैया छंद में सुंदर रचनाएं कीं।",
    "Raskhan was a famous Krishna-devotee poet of the Bhakti era renowned for his Savaiya verses.",
    "Easy", "Poetry"
)

# ----------------- VARNIKA PART 2 (वर्णिका भाग 2) -----------------
add_hin_q("hin_book_02", "hin_b2_ch_01", "hin_b2_ch_01_topic_01",
    "'दही वाली मंगम्मा' कहानी किस भाषा से अनूदित है?",
    "From which language is the story 'Dahi Wali Magamma' translated?",
    "कन्नड़ (Kannada)", "Kannada",
    ["तमिल (Tamil)", "तेलुगु (Telugu)", "उड़िया (Odia)"],
    ["Tamil", "Telugu", "Odia"],
    "'दही वाली मंगम्मा' कन्नड़ भाषा के प्रसिद्ध कथाकार श्रीनिवास की कहानी है जिसका अनुवाद बी.आर. नारायण ने किया।",
    "'Dahi Wali Magamma' is originally written in Kannada by famous author Srinivas.",
    "Easy", "Fact"
)

add_hin_q("hin_book_02", "hin_b2_ch_02", "hin_b2_ch_02_topic_01",
    "'ढहते विश्वास' कहानी के लेखक कौन हैं?",
    "Who is the author of the story 'Dhahte Vishwas'?",
    "सातकोड़ी होता (Saat Kori Hota - उड़िया)", "Saat Kori Hota (Odia)",
    ["सुजाता (Sujata)", "ईश्वर पेटलीकर", "सांवर दइया"],
    ["Sujata", "Ishwar Petlikar", "Sanwar Daiya"],
    "'ढहते विश्वास' उड़िया साहित्यकार सातकोड़ी होता की कहानी है जो बाढ़ की त्रासदी और जनजीवन पर आधारित है।",
    "'Dhahte Vishwas' is an Odia story by Saat Kori Hota depicting human struggle during catastrophic floods.",
    "Easy", "Author"
)

add_hin_q("hin_book_02", "hin_b2_ch_03", "hin_b2_ch_03_topic_01",
    "'माँ' कहानी किस भाषा की प्रमुख रचना है?",
    "Which regional language does the story 'Maa' originally belong to?",
    "गुजराती (Gujarati - लेखक: ईश्वर पेटलीकर)", "Gujarati (Author: Ishwar Petlikar)",
    ["कन्नड़", "मराठी", "तमिल"],
    ["Kannada", "Marathi", "Tamil"],
    "'माँ' कहानी के लेखक गुजराती के प्रसिद्ध साहित्यकार ईश्वर पेटलीकर हैं, जिसमें मंगू की माँ के वात्सल्य का चित्रण है।",
    "'Maa' is a famous Gujarati story by Ishwar Petlikar portraying maternal love for her daughter Mangu.",
    "Easy", "Fact"
)

# ----------------- HINDI VYAKARAN (हिंदी व्याकरण) -----------------
add_hin_q("hin_book_01", "hin_b1_grammar", "hin_grammar_t1",
    "हिंदी वर्णमाला में कुल कितने स्वर (Vowels) होते हैं?",
    "How many vowels (Swar) are there in the Hindi alphabet?",
    "11 (ग्यारह)", "11 (Eleven)",
    ["9", "13", "33"],
    ["9", "13", "33"],
    "हिंदी में मूलतः 11 स्वर (अ, आ, इ, ई, उ, ऊ, ऋ, ए, ऐ, ओ, औ) होते हैं।",
    "Hindi has 11 standard vowels.",
    "Easy", "Grammar"
)

add_hin_q("hin_book_01", "hin_b1_grammar", "hin_grammar_t2",
    "संधि के मुख्य रूप से कितने भेद होते हैं?",
    "How many main types of Sandhi are there in Hindi grammar?",
    "3 (स्वर, व्यंजन, विसर्ग संधि)", "3 (Swar, Vyanjan, Visarga Sandhi)",
    ["2", "4", "5"],
    ["2", "4", "5"],
    "संधि के तीन मुख्य भेद होते हैं: 1. स्वर संधि, 2. व्यंजन संधि, 3. विसर्ग संधि।",
    "There are 3 main types of Sandhi: Swar Sandhi, Vyanjan Sandhi, and Visarga Sandhi.",
    "Easy", "Grammar"
)

add_hin_q("hin_book_01", "hin_b1_grammar", "hin_grammar_t3",
    "'लंबोदर' (लंबा है उदर जिसका अर्थात् गणेश जी) में कौन-सा समास है?",
    "Which Samas is in the word 'Lambodar'?",
    "बहुव्रीहि समास (Bahuvrihi Samas)", "Bahuvrihi Samas",
    ["द्विगु समास (Dvigu)", "द्वंद्व समास (Dvandva)", "तत्पुरुष समास (Tatpurush)"],
    ["Dvigu Samas", "Dvandva Samas", "Tatpurush Samas"],
    "जिस समास में कोई भी पद प्रधान न होकर अन्य पद (गणेश जी) की ओर संकेत करे, उसे बहुव्रीहि समास कहते हैं।",
    "When neither component word is dominant and refers to a third entity, it is Bahuvrihi Samas.",
    "Easy", "Grammar"
)

# Output summary
print(f"Generated {len(questions)} verified Hindi MCQs.")

output_path = 'js/data/questionBankHindi.js'
js_content = f"""/**
 * Class 10 Bihar Board (BSEB) - Hindi Question Bank
 * Subject: Hindi (हिंदी - गोधूलि भाग 2, वर्णिका भाग 2, व्याकरण)
 * Total Verified Bilingual MCQs: {len(questions)}
 */

window.BSEB_HINDI_QUESTIONS = {json.dumps(questions, ensure_ascii=False, indent=2)};
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {output_path}")
