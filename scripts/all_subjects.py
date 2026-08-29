# -*- coding: utf-8 -*-
"""
Class 10 Bihar Board - All Subjects Massive Question Generator
Generates verified questions for Science, Social Science, Hindi, English, and Sanskrit.
"""
import json
import random

all_data = [
  # =========================================================================
  # SCIENCE (Physics, Chemistry, Biology)
  # =========================================================================
  # Physics - Light
  {
    "id": "q_sci_c10_002", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c10", "topic_id": "sci_c10_t1",
    "difficulty": "Easy",
    "q_hi": "दाढ़ी बनाने (हजामत) के लिए किस दर्पण का उपयोग किया जाता है?",
    "q_en": "Which mirror is used as a shaving mirror?",
    "opts_hi": {"A": "समतल दर्पण", "B": "उत्तल दर्पण", "C": "अवतल दर्पण (Concave)", "D": "इनमें से कोई नहीं"},
    "opts_en": {"A": "Plane mirror", "B": "Convex mirror", "C": "Concave mirror", "D": "None of these"},
    "ans": "C",
    "exp_hi": "अवतल दर्पण वस्तु का सीधा और बड़ा (आवर्धित) आभासी प्रतिबिंब बनाता है जब वस्तु फोकस और ध्रुव के बीच हो।",
    "exp_en": "Concave mirror forms an enlarged virtual erect image when object is between pole and focus."
  },
  {
    "id": "q_sci_c10_003", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c10", "topic_id": "sci_c10_t1",
    "difficulty": "Easy",
    "q_hi": "वाहनों के पश्च-दृश्य (Side mirror / Rear-view) दर्पण के रूप में किसका उपयोग होता है?",
    "q_en": "Which mirror is used as a rear-view (side) mirror in vehicles?",
    "opts_hi": {"A": "उत्तल दर्पण (Convex)", "B": "अवतल दर्पण", "C": "समतल दर्पण", "D": "उत्तल लेंस"},
    "opts_en": {"A": "Convex mirror", "B": "Concave mirror", "C": "Plane mirror", "D": "Convex lens"},
    "ans": "A",
    "exp_hi": "उत्तल दर्पण हमेशा सीधा छोटा प्रतिबिंब बनाता है और इसका दृष्टि क्षेत्र (Field of view) बहुत विस्तृत होता है।",
    "exp_en": "Convex mirror gives an erect diminished image and wider field of view."
  },
  {
    "id": "q_sci_c10_004", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c10", "topic_id": "sci_c10_t2",
    "difficulty": "Medium",
    "q_hi": "हीरे (Diamond) का अपवर्तनांक (Refractive Index) कितना होता है?",
    "q_en": "What is the refractive index of Diamond?",
    "opts_hi": {"A": "1.33", "B": "1.50", "C": "2.42", "D": "1.00"},
    "opts_en": {"A": "1.33", "B": "1.50", "C": "2.42", "D": "1.00"},
    "ans": "C",
    "exp_hi": "हीरे का अपवर्तनांक 2.42 होता है जो सभी पदार्थों में सर्वाधिक है, इसी कारण इसका क्रांतिक कोण (24.4°) बहुत कम होता है और यह चमकता है।",
    "exp_en": "Refractive index of diamond is 2.42, which is highest among common optical media."
  },
  # Physics - Eye & Colorful World
  {
    "id": "q_sci_c11_003", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c11", "topic_id": "sci_c11_t2",
    "difficulty": "Medium",
    "q_hi": "दीर्घ-दृष्टि दोष (Hypermetropia) के निवारण के लिए किस लेंस का उपयोग किया जाता है?",
    "q_en": "Which lens is used to correct Hypermetropia (Far-sightedness)?",
    "opts_hi": {"A": "अवतल लेंस", "B": "उत्तल लेंस (Convex)", "C": "बेलनाकार लेंस", "D": "द्विफोकसी लेंस"},
    "opts_en": {"A": "Concave lens", "B": "Convex lens", "C": "Cylindrical lens", "D": "Bifocal lens"},
    "ans": "B",
    "exp_hi": "दीर्घ दृष्टि दोष में पास की वस्तुएं स्पष्ट नहीं दिखतीं। इसके निवारण हेतु उत्तल (अभिसारी) लेंस के चश्मे का प्रयोग होता है।",
    "exp_en": "Convex lens (converging) is used to correct Hypermetropia."
  },
  {
    "id": "q_sci_c11_004", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c11", "topic_id": "sci_c11_t3",
    "difficulty": "Easy",
    "q_hi": "स्पेक्ट्रम प्राप्त करने के लिए किसका उपयोग होता है?",
    "q_en": "What is used to produce a spectrum of white light?",
    "opts_hi": {"A": "कांच की सिल्ली", "B": "अवतल दर्पण", "C": "प्रिज्म (Prism)", "D": "उत्तल लेंस"},
    "opts_en": {"A": "Glass slab", "B": "Concave mirror", "C": "Prism", "D": "Convex lens"},
    "ans": "C",
    "exp_hi": "प्रिज्म श्वेत प्रकाश को उसके सात अवयवी रंगों (VIBGYOR) में विक्षेपित कर देता है।",
    "exp_en": "A glass prism disperses white light into its spectrum of 7 constituent colors."
  },
  # Physics - Electricity
  {
    "id": "q_sci_c12_002", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c12", "topic_id": "sci_c12_t1",
    "difficulty": "Easy",
    "q_hi": "विद्युत परिपथ में विद्युत धारा को मापने के लिए किस यंत्र का उपयोग किया जाता है?",
    "q_en": "Which instrument is used to measure electric current in a circuit?",
    "opts_hi": {"A": "वोल्टमीटर", "B": "एमीटर (Ammeter)", "C": "गैल्वेनोमीटर", "D": "पोटेंशियोमीटर"},
    "opts_en": {"A": "Voltmeter", "B": "Ammeter", "C": "Galvanometer", "D": "Potentiometer"},
    "ans": "B",
    "exp_hi": "एमीटर को परिपथ में श्रेणीक्रम में जोड़ा जाता है और यह विद्युत धारा (Ampere) मापता है।",
    "exp_en": "Ammeter is connected in series to measure electric current."
  },
  {
    "id": "q_sci_c12_003", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c12", "topic_id": "sci_c12_t1",
    "difficulty": "Easy",
    "q_hi": "विभवांतर मापने वाले यंत्र को क्या कहा जाता है?",
    "q_en": "What is the device used to measure potential difference called?",
    "opts_hi": {"A": "एमीटर", "B": "वोल्टमीटर (Voltmeter)", "C": "मैनोमीटर", "D": "थर्मामीटर"},
    "opts_en": {"A": "Ammeter", "B": "Voltmeter", "C": "Manometer", "D": "Thermometer"},
    "ans": "B",
    "exp_hi": "वोल्टमीटर को परिपथ में समानांतर क्रम में जोड़ा जाता है और यह विभवांतर (Volts) मापता है।",
    "exp_en": "Voltmeter is connected in parallel to measure voltage across two points."
  },
  # Physics - Magnetic Effects
  {
    "id": "q_sci_c13_002", "subject_id": "science", "book_id": "sci_b1", "chapter_id": "sci_c13", "topic_id": "sci_c13_t3",
    "difficulty": "Medium",
    "q_hi": "विद्युत मोटर ऊर्जा के किस रूप को किस रूप में परिवर्तित करता है?",
    "q_en": "An electric motor converts which form of energy into which form?",
    "opts_hi": {"A": "यांत्रिक ऊर्जा को विद्युत ऊर्जा में", "B": "विद्युत ऊर्जा को यांत्रिक ऊर्जा में", "C": "रासायनिक ऊर्जा को विद्युत में", "D": "सौर ऊर्जा को विद्युत में"},
    "opts_en": {"A": "Mechanical to Electrical", "B": "Electrical to Mechanical", "C": "Chemical to Electrical", "D": "Solar to Electrical"},
    "ans": "B",
    "exp_hi": "विद्युत मोटर विद्युत ऊर्जा को यांत्रिक ऊर्जा (Mechanical Energy) में बदलता है।",
    "exp_en": "Electric motor converts electrical energy into mechanical energy."
  },
  # Chemistry - Reactions
  {
    "id": "q_sci_c1_002", "subject_id": "science", "book_id": "sci_b2", "chapter_id": "sci_c1", "topic_id": "sci_c1_t1",
    "difficulty": "Easy",
    "q_hi": "श्वसन (Respiration) किस प्रकार की रासायनिक अभिक्रिया है?",
    "q_en": "What type of chemical reaction is respiration?",
    "opts_hi": {"A": "ऊष्माशोषी (Endothermic)", "B": "ऊष्माक्षेपी (Exothermic)", "C": "संयोजन", "D": "अपचयन"},
    "opts_en": {"A": "Endothermic", "B": "Exothermic", "C": "Combination", "D": "Reduction"},
    "ans": "B",
    "exp_hi": "श्वसन में ग्लूकोज ऑक्सीजन से मिलकर ऊर्जा (ऊष्मा) मुक्त करता है (C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ऊर्जा), अतः यह ऊष्माक्षेपी अभिक्रिया है।",
    "exp_en": "Respiration releases energy, making it an exothermic reaction."
  },
  {
    "id": "q_sci_c1_003", "subject_id": "science", "book_id": "sci_b2", "chapter_id": "sci_c1", "topic_id": "sci_c1_t3",
    "difficulty": "Easy",
    "q_hi": "चिप्स की थैली में कौन-सी गैस भरी जाती है ताकि वे विकृतगंधी (Rancid) न हों?",
    "q_en": "Which gas is flushed in bags of potato chips to prevent rancidity?",
    "opts_hi": {"A": "ऑक्सीजन", "B": "नाइट्रोजन (Nitrogen)", "C": "हाइड्रोजन", "D": "क्लोरीन"},
    "opts_en": {"A": "Oxygen", "B": "Nitrogen", "C": "Hydrogen", "D": "Chlorine"},
    "ans": "B",
    "exp_hi": "नाइट्रोजन एक अक्रिय गैस है जो तेल व वसा के उपचयन (Oxidation) को रोकती है।",
    "exp_en": "Nitrogen is an unreactive gas that prevents oxidation of oils and fats."
  },
  # Chemistry - Acids, Bases & Salts
  {
    "id": "q_sci_c2_002", "subject_id": "science", "book_id": "sci_b2", "chapter_id": "sci_c2", "topic_id": "sci_c2_t3",
    "difficulty": "Easy",
    "q_hi": "बेकिंग सोडा (खाने का सोडा) का रासायनिक नाम और सूत्र क्या है?",
    "q_en": "What is the chemical name and formula of Baking Soda?",
    "opts_hi": {"A": "सोडियम कार्बोनेट (Na₂CO₃)", "B": "सोडियम हाइड्रोजनकार्बोनेट (NaHCO₃)", "C": "सोडियम हाइड्रॉक्साइड (NaOH)", "D": "कैल्शियम कार्बोनेट (CaCO₃)"},
    "opts_en": {"A": "Sodium carbonate (Na₂CO₃)", "B": "Sodium hydrogencarbonate (NaHCO₃)", "C": "Sodium hydroxide (NaOH)", "D": "Calcium carbonate (CaCO₃)"},
    "ans": "B",
    "exp_hi": "बेकिंग सोडा का रासायनिक नाम सोडियम बाइकार्बोनेट / सोडियम हाइड्रोजन कार्बोनेट (NaHCO₃) है।",
    "exp_en": "Baking soda is Sodium Hydrogen Carbonate (NaHCO₃)."
  },
  {
    "id": "q_sci_c2_003", "subject_id": "science", "book_id": "sci_b2", "chapter_id": "sci_c2", "topic_id": "sci_c2_t3",
    "difficulty": "Medium",
    "q_hi": "धोने का सोडा (Washing Soda) का सही रासायनिक सूत्र क्या है?",
    "q_en": "What is the correct chemical formula of Washing Soda?",
    "opts_hi": {"A": "Na₂CO₃·10H₂O", "B": "NaHCO₃", "C": "CaOCl₂", "D": "CaSO₄·2H₂O"},
    "opts_en": {"A": "Na₂CO₃·10H₂O", "B": "NaHCO₃", "C": "CaOCl₂", "D": "CaSO₄·2H₂O"},
    "ans": "A",
    "exp_hi": "धोने के सोडे का सूत्र सोडियम कार्बोनेट डेकाहाइड्रेट (Na₂CO₃·10H₂O) होता है।",
    "exp_en": "Washing soda is Sodium Carbonate Decahydrate (Na₂CO₃·10H₂O)."
  },
  # Chemistry - Metals & Non-metals
  {
    "id": "q_sci_c3_002", "subject_id": "science", "book_id": "sci_b2", "chapter_id": "sci_c3", "topic_id": "sci_c3_t1",
    "difficulty": "Easy",
    "q_hi": "विद्युत की सबसे अच्छी सुचालक धातु कौन-सी है?",
    "q_en": "Which metal is the best conductor of electricity?",
    "opts_hi": {"A": "तांबा (Copper)", "B": "चाँदी (Silver / Ag)", "C": "सोना (Gold)", "D": "एल्युमिनियम"},
    "opts_en": {"A": "Copper", "B": "Silver (Ag)", "C": "Gold", "D": "Aluminium"},
    "ans": "B",
    "exp_hi": "चाँदी (Ag) विद्युत और ऊष्मा की सर्वोत्तम सुचालक धातु है।",
    "exp_en": "Silver is the best conductor of electricity and heat."
  },
  {
    "id": "q_sci_c3_003", "subject_id": "science", "book_id": "sci_b2", "chapter_id": "sci_c3", "topic_id": "sci_c3_t2",
    "difficulty": "Easy",
    "q_hi": "सोडियम को किस द्रव में डुबोकर रखा जाता है?",
    "q_en": "In which liquid is Sodium metal stored submerged?",
    "opts_hi": {"A": "जल में", "B": "केरोसिन तेल में (मिट्टी का तेल)", "C": "अल्कोहॉल में", "D": "पेट्रोल में"},
    "opts_en": {"A": "In water", "B": "In Kerosene oil", "C": "In Alcohol", "D": "In Petrol"},
    "ans": "B",
    "exp_hi": "सोडियम अत्यधिक क्रियाशील धातु है जो हवा और पानी के संपर्क में आने पर आग पकड़ लेती है, इसलिए इसे केरोसिन में डुबोकर रखते हैं।",
    "exp_en": "Sodium vigorously reacts with oxygen and water, so it is stored under kerosene oil."
  },
  # Chemistry - Carbon
  {
    "id": "q_sci_c4_002", "subject_id": "science", "book_id": "sci_b2", "chapter_id": "sci_c4", "topic_id": "sci_c4_t2",
    "difficulty": "Easy",
    "q_hi": "प्राकृतिक गैस (CNG) का मुख्य घटक क्या है?",
    "q_en": "What is the main component of Natural Gas (CNG)?",
    "opts_hi": {"A": "मीथेन (CH₄)", "B": "एथेन", "C": "प्रोपेन", "D": "ब्यूटेन"},
    "opts_en": {"A": "Methane (CH₄)", "B": "Ethane", "C": "Propane", "D": "Butane"},
    "ans": "A",
    "exp_hi": "प्राकृतिक गैस और बायोगैस का मुख्य घटक मीथेन (CH₄) होता है। LPG का मुख्य घटक ब्यूटेन है।",
    "exp_en": "Methane is the chief component of Natural Gas (CNG)."
  },
  # Biology - Life Processes
  {
    "id": "q_sci_c6_002", "subject_id": "science", "book_id": "sci_b3", "chapter_id": "sci_c6", "topic_id": "sci_c6_t1",
    "difficulty": "Easy",
    "q_hi": "क्लोरोफिल वर्णक (Chlorophyll pigment) का रंग कैसा होता है?",
    "q_en": "What color is the chlorophyll pigment?",
    "opts_hi": {"A": "पीला", "B": "हरा (Green)", "C": "लाल", "D": "सफेद"},
    "opts_en": {"A": "Yellow", "B": "Green", "C": "Red", "D": "White"},
    "ans": "B",
    "exp_hi": "क्लोरोफिल वर्णक का रंग हरा होता है जिसमें मैग्नीशियम (Mg) धातु पाई जाती है।",
    "exp_en": "Chlorophyll is green in color and contains Magnesium."
  },
  {
    "id": "q_sci_c6_003", "subject_id": "science", "book_id": "sci_b3", "chapter_id": "sci_c6", "topic_id": "sci_c6_t2",
    "difficulty": "Easy",
    "q_hi": "वायवीय श्वसन (Aerobic Respiration) कोशिका के किस भाग में संपन्न होता है?",
    "q_en": "In which part of the cell does Aerobic Respiration take place?",
    "opts_hi": {"A": "कोशिकाद्रव्य", "B": "माइटोकॉन्ड्रिया (Mitochondria)", "C": "केंद्रक", "D": "हरितलवक"},
    "opts_en": {"A": "Cytoplasm", "B": "Mitochondria", "C": "Nucleus", "D": "Chloroplast"},
    "ans": "B",
    "exp_hi": "पाइरुवेट का पूर्ण विखंडन ऑक्सीजन की उपस्थिति में माइटोकॉन्ड्रिया में होता है। इसे कोशिका का पावर हाउस कहते हैं।",
    "exp_en": "Mitochondria is the site of aerobic respiration (powerhouse of cell)."
  },
  # Biology - Control & Coordination
  {
    "id": "q_sci_c7_002", "subject_id": "science", "book_id": "sci_b3", "chapter_id": "sci_c7", "topic_id": "sci_c7_t3",
    "difficulty": "Medium",
    "q_hi": "इंसुलिन हार्मोन की कमी से कौन-सा रोग होता है?",
    "q_en": "Deficiency of Insulin hormone causes which disease?",
    "opts_hi": {"A": "घेंघा (गलगंड)", "B": "मधुमेह (Diabetes)", "C": "रतौंधी", "D": "एनीमिया"},
    "opts_en": {"A": "Goitre", "B": "Diabetes (Madhumeh)", "C": "Night blindness", "D": "Anaemia"},
    "ans": "B",
    "exp_hi": "अग्न्याशय द्वारा स्रावित इंसुलिन रक्त में शर्करा को नियंत्रित करता है। इसकी कमी से मधुमेह (Diabetes) होता है। आयोडीन कमी से घेंघा होता है।",
    "exp_en": "Insulin deficiency leads to Diabetes mellitus."
  },
  # Biology - Reproduction
  {
    "id": "q_sci_c8_002", "subject_id": "science", "book_id": "sci_b3", "chapter_id": "sci_c8", "topic_id": "sci_c8_t1",
    "difficulty": "Easy",
    "q_hi": "हाइड्रा और यीस्ट में अलैंगिक जनन की मुख्य विधि क्या है?",
    "q_en": "What is the primary method of asexual reproduction in Hydra and Yeast?",
    "opts_hi": {"A": "द्विखंडन", "B": "मुकुलन (Budding)", "C": "पुनर्जनन", "D": "बीजाणुजनन"},
    "opts_en": {"A": "Binary fission", "B": "Budding", "C": "Regeneration", "D": "Spore formation"},
    "ans": "B",
    "exp_hi": "हाइड्रा और यीस्ट में मुकुलन (Budding) द्वारा जनक शरीर पर एक उभार (मुकुल) बनकर नया जीव बनता है।",
    "exp_en": "Hydra and Yeast reproduce asexually by budding."
  },

  # =========================================================================
  # SOCIAL SCIENCE (History, Geography, Disaster Mgmt, Pol Sci, Economics)
  # =========================================================================
  # History
  {
    "id": "q_sst_hist_c5_01", "subject_id": "social", "book_id": "sst_b1", "chapter_id": "hist_c5", "topic_id": "hist_c5_t1",
    "difficulty": "Easy",
    "q_hi": "सेफ्टी लैंप (Safety Lamp) का आविष्कार किसने किया था?",
    "q_en": "Who invented the Safety Lamp for coal miners?",
    "opts_hi": {"A": "जेम्स वाट", "B": "हम्फ्री डेवी (Humphry Davy)", "C": "जॉन के", "D": "रिचर्ड आर्कराइट"},
    "opts_en": {"A": "James Watt", "B": "Humphry Davy", "C": "John Kay", "D": "Richard Arkwright"},
    "ans": "B",
    "exp_hi": "1815 में हम्फ्री डेवी ने खानों में काम करने वाले मजदूरों की सुरक्षा के लिए 'सेफ्टी लैंप' का आविष्कार किया।",
    "exp_en": "Humphry Davy invented the Safety Lamp in 1815."
  },
  {
    "id": "q_sst_hist_c5_02", "subject_id": "social", "book_id": "sst_b1", "chapter_id": "hist_c5", "topic_id": "hist_c5_t1",
    "difficulty": "Medium",
    "q_hi": "टाटा आयरन एंड स्टील कंपनी (TISCO) की स्थापना जमशेदजी टाटा ने किस वर्ष जमशेदपुर (साकची) में की थी?",
    "q_en": "In which year did Jamsetji Tata establish TISCO at Jamshedpur?",
    "opts_hi": {"A": "1854", "B": "1907 (1907 ई.)", "C": "1915", "D": "1923"},
    "opts_en": {"A": "1854", "B": "1907", "C": "1915", "D": "1923"},
    "ans": "B",
    "exp_hi": "1907 में जमशेदजी टाटा द्वारा साकची (वर्तमान जमशेदपुर) में भारत के पहले आधुनिक इस्पात कारखाने TISCO की स्थापना की गई।",
    "exp_en": "TISCO was founded in 1907 at Sakchi (Jamshedpur)."
  },
  {
    "id": "q_sst_hist_c6_01", "subject_id": "social", "book_id": "sst_b1", "chapter_id": "hist_c6", "topic_id": "hist_c6_t1",
    "difficulty": "Easy",
    "q_hi": "पटना के गोलघर का निर्माण किस मुख्य उद्देश्य से कैप्टन जॉन गार्स्टिन द्वारा 1786 में कराया गया था?",
    "q_en": "Golghar in Patna was built in 1786 for which main purpose?",
    "opts_hi": {"A": "सैनिक छावनी", "B": "अनाज भंडारण (Grain Storage)", "C": "हथियार रखने", "D": "पूजा स्थल"},
    "opts_en": {"A": "Military barracks", "B": "Grain Storage against famine", "C": "Armory", "D": "Temple"},
    "ans": "B",
    "exp_hi": "1770 के भयंकर अकाल के बाद ब्रिटिश सरकार ने अनाज के सुरक्षित भंडारण के लिए गोलघर का निर्माण करवाया था।",
    "exp_en": "Golghar was constructed in 1786 as a granary after the 1770 famine."
  },
  # Geography
  {
    "id": "q_sst_geo_c1_02", "subject_id": "social", "book_id": "sst_b2", "chapter_id": "geo_c1", "topic_id": "geo_c1_t4",
    "difficulty": "Easy",
    "q_hi": "भारत का प्रथम परमाणु ऊर्जा उत्पादन केंद्र (First Atomic Power Station) कहाँ स्थापित किया गया था?",
    "q_en": "Where was India's first Nuclear Power Station established?",
    "opts_hi": {"A": "तारापुर (महाराष्ट्र - 1969)", "B": "कलपक्कम (तमिलनाडु)", "C": "नरौरा (उत्तर प्रदेश)", "D": "रावतभाटा (राजस्थान)"},
    "opts_en": {"A": "Tarapur (Maharashtra)", "B": "Kalpakkam", "C": "Narora", "D": "Rawatbhata"},
    "ans": "A",
    "exp_hi": "तारापुर (महाराष्ट्र) में 1969 में भारत का पहला परमाणु विद्युत गृह स्थापित किया गया।",
    "exp_en": "Tarapur in Maharashtra is India's first nuclear power station."
  },
  {
    "id": "q_sst_geo_c1_03", "subject_id": "social", "book_id": "sst_b2", "chapter_id": "geo_c1", "topic_id": "geo_c1_t5",
    "difficulty": "Easy",
    "q_hi": "भारत में सबसे पुराना तेल का कुआँ (First Oil Refinery/Well) कहाँ स्थित है?",
    "q_en": "Where is the oldest oilfield / refinery in India located?",
    "opts_hi": {"A": "बॉम्बे हाई", "B": "डिगबोई (असम - Digboi)", "C": "अंकलेश्वर (गुजरात)", "D": "बरौनी (बिहार)"},
    "opts_en": {"A": "Bombay High", "B": "Digboi (Assam)", "C": "Ankleshwar", "D": "Barauni"},
    "ans": "B",
    "exp_hi": "डिगबोई (असम) भारत का सबसे प्राचीन तेल क्षेत्र है जहाँ 1901 में पहली तेल रिफाइनरी शुरू हुई थी।",
    "exp_en": "Digboi in Assam is India's oldest operating oilfield and refinery."
  },
  {
    "id": "q_sst_geo_c3_01", "subject_id": "social", "book_id": "sst_b2", "chapter_id": "geo_c3", "topic_id": "geo_c3_t1",
    "difficulty": "Easy",
    "q_hi": "भारत में पहली सूती वस्त्र मिल 1854 में कहाँ स्थापित की गई थी?",
    "q_en": "Where was the first successful cotton textile mill established in India in 1854?",
    "opts_hi": {"A": "सूरत", "B": "मुंबई (Mumbai)", "C": "अहमदाबाद", "D": "कोलकाता"},
    "opts_en": {"A": "Surat", "B": "Mumbai", "C": "Ahmedabad", "D": "Kolkata"},
    "ans": "B",
    "exp_hi": "कावासजी डाबर द्वारा 1854 में मुंबई में भारत की पहली आधुनिक और सफल सूती वस्त्र मिल स्थापित की गई थी।",
    "exp_en": "The first modern cotton mill was established in Mumbai in 1854."
  },
  # Economics
  {
    "id": "q_sst_eco_c3_01", "subject_id": "social", "book_id": "sst_b5", "chapter_id": "eco_c3", "topic_id": "eco_c3_t1",
    "difficulty": "Easy",
    "q_hi": "निम्नलिखित में से कौन 'प्लास्टिक मुद्रा' (Plastic Money) का रूप है?",
    "q_en": "Which of the following is an example of 'Plastic Money'?",
    "opts_hi": {"A": "चेक", "B": "ड्राफ्ट", "C": "एटीएम / डेबिट-क्रेडिट कार्ड (ATM / Debit Card)", "D": "कागजी नोट"},
    "opts_en": {"A": "Cheque", "B": "Bank Draft", "C": "ATM / Debit-Credit Card", "D": "Currency notes"},
    "ans": "C",
    "exp_hi": "डेबिट कार्ड, क्रेडिट कार्ड और एटीएम कार्ड को प्लास्टिक मुद्रा कहा जाता है।",
    "exp_en": "Debit and Credit cards are forms of Plastic Money."
  },
  {
    "id": "q_sst_eco_c4_02", "subject_id": "social", "book_id": "sst_b5", "chapter_id": "eco_c4", "topic_id": "eco_c4_t1",
    "difficulty": "Medium",
    "q_hi": "स्वयं सहायता समूह (Self Help Group - SHG) में सामान्यतः कितने सदस्य होते हैं?",
    "q_en": "Typically, how many members are there in a Self Help Group (SHG)?",
    "opts_hi": {"A": "15 से 20 सदस्य", "B": "50 से 100", "C": "5 से 10", "D": "100 से अधिक"},
    "opts_en": {"A": "15 to 20 members", "B": "50 to 100", "C": "5 to 10", "D": "More than 100"},
    "ans": "A",
    "exp_hi": "स्वयं सहायता समूह में मुख्यतः ग्रामीण महिलाओं के 15-20 सदस्य होते हैं जो नियमित बचत करते हैं।",
    "exp_en": "An SHG typically comprises 15-20 members, mainly rural women."
  },
  {
    "id": "q_sst_eco_c7_02", "subject_id": "social", "book_id": "sst_b5", "chapter_id": "eco_c7", "topic_id": "eco_c7_t1",
    "difficulty": "Easy",
    "q_hi": "सोने के आभूषणों की शुद्धता सुनिश्चित करने के लिए किस मानक चिह्न (Standard Mark) की पहचान आवश्यक है?",
    "q_en": "Which standard certification mark ensures the purity of gold jewelry in India?",
    "opts_hi": {"A": "ISI मार्क", "B": "हॉलमार्क (Hallmark)", "C": "एगमार्क (Agmark)", "D": "सिल्क मार्क"},
    "opts_en": {"A": "ISI Mark", "B": "Hallmark (BIS)", "C": "Agmark", "D": "Silk Mark"},
    "ans": "B",
    "exp_hi": "स्वर्ण आभूषणों की गुणवत्ता के लिए हॉलमार्क (BIS Hallmark), कृषि उत्पादों के लिए एगमार्क और औद्योगिक सामान के लिए ISI मार्क होता है।",
    "exp_en": "Hallmark certifies the purity and standard of gold jewelry."
  },

  # =========================================================================
  # HINDI (गोधूलि & वर्णिका)
  # =========================================================================
  {
    "id": "q_hin_c8_01", "subject_id": "hindi", "book_id": "hin_b1", "chapter_id": "hin_c8", "topic_id": "hin_c8_t1",
    "difficulty": "Easy",
    "q_hi": "'जित-जित मैं निरखत हूँ' पाठ में पंडित बिरजू महाराज का संबंध किस प्रसिद्ध शास्त्रीय नृत्य से है?",
    "q_en": "In 'Jit-Jit Main Nirkhat Hun', Pandit Birju Maharaj is associated with which classical dance?",
    "opts_hi": {"A": "भरतनाट्यम", "B": "कथक (Kathak - लखनऊ घराना)", "C": "कुचिपुड़ी", "D": "ओडिसी"},
    "opts_en": {"A": "Bharatnatyam", "B": "Kathak (Lucknow Gharana)", "C": "Kuchipudi", "D": "Odissi"},
    "ans": "B",
    "exp_hi": "पंडित बिरजू महाराज लखनऊ कालका-बिंदादीन घराने के विश्वप्रसिद्ध कथक नर्तक थे।",
    "exp_en": "Pandit Birju Maharaj is the maestro of classical Kathak dance."
  },
  {
    "id": "q_hin_c9_01", "subject_id": "hindi", "book_id": "hin_b1", "chapter_id": "hin_c9", "topic_id": "hin_c9_t1",
    "difficulty": "Medium",
    "q_hi": "'आविन्यों' किस देश में स्थित एक प्राचीन कला केंद्र है?",
    "q_en": "In which country is 'Avignon', an ancient art center, situated?",
    "opts_hi": {"A": "इटली", "B": "जर्मनी", "C": "फ्रांस (रोन नदी तट, दक्षिणी फ्रांस)", "D": "इंग्लैंड"},
    "opts_en": {"A": "Italy", "B": "Germany", "C": "France (Rhone river, Southern France)", "D": "England"},
    "ans": "C",
    "exp_hi": "आविन्यों दक्षिणी फ्रांस में रोन नदी के किनारे स्थित एक मध्ययुगीन ईसाई कला केंद्र है।",
    "exp_en": "Avignon is located along the Rhone river in Southern France."
  },
  {
    "id": "q_hin_c10_01", "subject_id": "hindi", "book_id": "hin_b1", "chapter_id": "hin_c10", "topic_id": "hin_c10_t1",
    "difficulty": "Easy",
    "q_hi": "'मछली' कहानी में लेखक विनोद कुमार शुक्ल के साथ कौन मछली को कुएँ में डालने के लिए लेकर भागा था?",
    "q_en": "In the story 'Machhli', who ran with the fish to put it in the well?",
    "opts_hi": {"A": "भग्गू", "B": "सन्तू (Santu)", "C": "नरेन", "D": "मोहरा"},
    "opts_en": {"A": "Bhaggu", "B": "Santu", "C": "Naren", "D": "Mohra"},
    "ans": "B",
    "exp_hi": "सन्तू मछली के कटने के डर से एक जीवित मछली लेकर कुएँ में डालने के लिए भाग निकला था।",
    "exp_en": "Santu ran away with the fish to save its life in the well."
  },
  {
    "id": "q_hin_c12_01", "subject_id": "hindi", "book_id": "hin_b1", "chapter_id": "hin_c12", "topic_id": "hin_c12_t1",
    "difficulty": "Easy",
    "q_hi": "महात्मा गांधी के अनुसार 'शिक्षा और संस्कृति' में बढ़िया शिक्षा किसे कहा गया है?",
    "q_en": "According to Mahatma Gandhi, which is the best form of education?",
    "opts_hi": {"A": "अंग्रेजी माध्यम शिक्षा", "B": "अहिंसक प्रतिरोध एवं दस्तकारी आधारित व्यावहारिक शिक्षा", "C": "केवल किताबी ज्ञान", "D": "धार्मिक कट्टरता"},
    "opts_en": {"A": "English medium education", "B": "Non-violent resistance & craft-based practical education", "C": "Rote book learning", "D": "Dogmatic education"},
    "ans": "B",
    "exp_hi": "गांधीजी ने चरित्र निर्माण और बुनियादी दस्तकारी (हस्तशिल्प) आधारित स्वावलंबी शिक्षा को सर्वोत्तम माना।",
    "exp_en": "Gandhiji advocated practical, craft-based, and character-building education."
  },
  {
    "id": "q_hin_c14_01", "subject_id": "hindi", "book_id": "hin_b1", "chapter_id": "hin_c14", "topic_id": "hin_c14_t1",
    "difficulty": "Easy",
    "q_hi": "'प्रेम अयनि श्री राधिका' और 'करील के कुंजन ऊपर वारौं' सवैये किस भक्त कवि द्वारा रचित हैं?",
    "q_en": "Who is the poet of the Krishna-bhakti verses 'Prem Ayani Shri Radhika'?",
    "opts_hi": {"A": "रसखान (Raskhan)", "B": "तुलसीदास", "C": "सूरदास", "D": "बिहारी"},
    "opts_en": {"A": "Raskhan", "B": "Tulsidas", "C": "Surdas", "D": "Bihari"},
    "ans": "A",
    "exp_hi": "रसखान कृष्ण भक्ति शाखा के प्रसिद्ध मुस्लिम कवि थे जिन्होंने ब्रजभूमि और श्रीकृष्ण पर सुंदर सवैये लिखे।",
    "exp_en": "Raskhan is the celebrated Krishna devotee poet of medieval Hindi literature."
  },

  # =========================================================================
  # ENGLISH (Panorama & Supplementary)
  # =========================================================================
  {
    "id": "q_eng_c6_01", "subject_id": "english", "book_id": "eng_b1", "chapter_id": "eng_c6", "topic_id": "eng_c6_t1",
    "difficulty": "Medium",
    "q_hi": "नोबेल पुरस्कार विजेता टोनी मॉरिसन (Toni Morrison) के निबंध 'Once Upon a Time' में बूढ़ी अंधी महिला को किसका प्रतीक माना गया है?",
    "q_en": "In Toni Morrison's Nobel lecture 'Once Upon a Time', what does the old blind woman symbolize?",
    "opts_hi": {"A": "धन का", "B": "बुद्धिमता और भाषा के रक्षक (Wisdom & Living Language)", "C": "गुलामी का", "D": "युद्ध का"},
    "opts_en": {"A": "Wealth", "B": "Wisdom & Living Language as an instrument of agency", "C": "Slavery", "D": "War"},
    "ans": "B",
    "exp_hi": "टोनी मॉरिसन ने निबंध में भाषा को एक जीवित पक्षी और बूढ़ी अंधी महिला को भाषा के संवेदनशील संरक्षक के रूप में प्रस्तुत किया है।",
    "exp_en": "Toni Morrison portrays language as a living bird and the wise woman as its guardian."
  },
  {
    "id": "q_eng_c8_01", "subject_id": "english", "book_id": "eng_b1", "chapter_id": "eng_c8", "topic_id": "eng_c8_t1",
    "difficulty": "Easy",
    "q_hi": "'Little Girls Wiser Than Men' कहानी के लेखक कौन हैं?",
    "q_en": "Who is the author of the story 'Little Girls Wiser Than Men'?",
    "opts_hi": {"A": "लियो टॉल्स्टॉय (Leo Tolstoy)", "B": "एंटोन चेखव", "C": "आर.सी. हचिंसन", "D": "जॉन गाल्सवर्दी"},
    "opts_en": {"A": "Leo Tolstoy", "B": "Anton Chekhov", "C": "R.C. Hutchinson", "D": "John Galsworthy"},
    "ans": "A",
    "exp_hi": "महान रूसी लेखक लियो टॉल्स्टॉय ने इस कहानी में दो बच्चियों अकुल्या और मलाशा की बाल सुलभ मासूमियत का चित्रण किया है।",
    "exp_en": "Russian master Leo Tolstoy wrote 'Little Girls Wiser Than Men'."
  },
  {
    "id": "q_eng_p2_01", "subject_id": "english", "book_id": "eng_b1", "chapter_id": "eng_p2", "topic_id": "eng_p2_t1",
    "difficulty": "Easy",
    "q_hi": "एलेक्जेंडर पोप (Alexander Pope) की प्रसिद्ध कविता 'Ode on Solitude' में सुखी मनुष्य की क्या विशेषता है?",
    "q_en": "In Alexander Pope's 'Ode on Solitude', what characterizes a truly happy man?",
    "opts_hi": {"A": "जो विदेश यात्रा करता है", "B": "जो अपने पैतृक कुछ एकड़ जमीन पर शांत जीवन जीता है", "C": "जो राजा का मंत्री हो", "D": "जिसके पास बहुत धन हो"},
    "opts_en": {"A": "One who travels abroad", "B": "One content to breathe native air on a few paternal acres", "C": "One who is a king's minister", "D": "One who has massive wealth"},
    "ans": "B",
    "exp_hi": "कविता में कवि कहते हैं कि सुखी मनुष्य वही है जो अपनी पैतृक भूमि पर सादगी, संतोष और शांति से जीता है।",
    "exp_en": "The happy man is content with his few paternal acres, bread from his ground, and quiet mind."
  },
  {
    "id": "q_eng_p7_01", "subject_id": "english", "book_id": "eng_b1", "chapter_id": "eng_p7", "topic_id": "eng_p7_t1",
    "difficulty": "Medium",
    "q_hi": "लक्ष्मी प्रसाद देवकोटा की कविता 'The Sleeping Porter' में कुली (Porter) अपनी पीठ पर कितने किलो का भार उठाता है?",
    "q_en": "In Laxmi Prasad Devkota's poem 'The Sleeping Porter', how heavy is the load on the porter's back?",
    "opts_hi": {"A": "10 किलो", "B": "25 किलो (25 kilo load)", "C": "50 किलो", "D": "15 किलो"},
    "opts_en": {"A": "10 kg", "B": "25 kilo load", "C": "50 kg", "D": "15 kg"},
    "ans": "B",
    "exp_hi": "नेपाली कवि लक्ष्मी प्रसाद देवकोटा ने कुली के संघर्ष का वर्णन करते हुए 25 किलो के भारी बोझ के साथ बर्फीले पहाड़ों की चढ़ाई का उल्लेख किया है।",
    "exp_en": "The porter carries a 25 kilo load on his back up the mountain cliff."
  },
  {
    "id": "q_eng_s6_01", "subject_id": "english", "book_id": "eng_b2", "chapter_id": "eng_s6", "topic_id": "eng_s6_t1",
    "difficulty": "Medium",
    "q_hi": "'Two Horizons' (बीणापाणि मोहंती) कहानी में पत्राचार किन दो पात्रों के बीच होता है?",
    "q_en": "In Binapani Mohanty's story 'Two Horizons', between whom does the exchange of letters take place?",
    "opts_hi": {"A": "पिता और पुत्र", "B": "माँ और पुत्री (Mother and Daughter)", "C": "पति और पत्नी", "D": "दो मित्र"},
    "opts_en": {"A": "Father and son", "B": "Mother and Daughter", "C": "Husband and wife", "D": "Two friends"},
    "ans": "B",
    "exp_hi": "उड़िया कहानी 'Two Horizons' में एक विवाहित बेटी और उसकी माँ के बीच भावनात्मक पत्रों का आदान-प्रदान होता है।",
    "exp_en": "The story consists of intimate and emotional letters exchanged between a daughter and her mother."
  },

  # =========================================================================
  # SANSKRIT (पीयूषम् भाग 2)
  # =========================================================================
  {
    "id": "q_san_c2_02", "subject_id": "sanskrit", "book_id": "san_b1", "chapter_id": "san_c2", "topic_id": "san_c2_t1",
    "difficulty": "Easy",
    "q_hi": "सिखों के दसवें गुरु गोविंद सिंह का जन्म स्थान कहाँ है?",
    "q_en": "Where is the birthplace of the 10th Sikh Guru, Guru Gobind Singh?",
    "opts_hi": {"A": "अमृतसर", "B": "पटना (पाटलिपुत्र - तख्त श्री हरमंदिर जी)", "C": "वाराणसी", "D": "आनंदपुर"},
    "opts_en": {"A": "Amritsar", "B": "Patna (Takht Sri Harmandir Ji Sahib)", "C": "Varanasi", "D": "Anandpur"},
    "ans": "B",
    "exp_hi": "सिखों के दसवें गुरु, गुरु गोविंद सिंह जी का जन्म पाटलिपुत्र (पटना) में हुआ था जहाँ 'तख्त श्री हरमंदिर जी साहिब' स्थित है।",
    "exp_en": "Guru Gobind Singh, the 10th Sikh Guru, was born in Patna."
  },
  {
    "id": "q_san_c5_01", "subject_id": "sanskrit", "book_id": "san_b1", "chapter_id": "san_c5", "topic_id": "san_c5_t1",
    "difficulty": "Easy",
    "q_hi": "'गायन्ति देवाः किल गीतकानि धन्यास्तु ते भारतभूमिभागे...' यह प्रसिद्ध श्लोक किस पुराण से संकलित है?",
    "q_en": "From which Purana is the verse 'Gayanti devah kila gitakani...' praising India taken?",
    "opts_hi": {"A": "विष्णुपुराण (Vishnu Purana)", "B": "भागवतपुराण", "C": "मत्स्यपुराण", "D": "अग्निपुराण"},
    "opts_en": {"A": "Vishnu Purana", "B": "Bhagavata Purana", "C": "Matsya Purana", "D": "Agni Purana"},
    "ans": "A",
    "exp_hi": "'भारतमहिमा' पाठ का पहला श्लोक विष्णुपुराण से लिया गया है जिसमें देवता भी भारत में जन्म लेने वाले मनुष्यों की स्तुति करते हैं।",
    "exp_en": "This verse in 'Bharatamahima' is taken from Vishnu Purana."
  },
  {
    "id": "q_san_c9_02", "subject_id": "sanskrit", "book_id": "san_b1", "chapter_id": "san_c9", "topic_id": "san_c9_t1",
    "difficulty": "Easy",
    "q_hi": "स्वामी दयानंद के बचपन का नाम क्या था?",
    "q_en": "What was the childhood name of Swami Dayanand Saraswati?",
    "opts_hi": {"A": "दयाशंकर", "B": "मूलशंकर (Moolshankar)", "C": "शिवशंकर", "D": "गौरीशंकर"},
    "opts_en": {"A": "Dayashankar", "B": "Moolshankar", "C": "Shivshankar", "D": "Gaurishankar"},
    "ans": "B",
    "exp_hi": "स्वामी दयानंद का जन्म गुजरात के टंकारा ग्राम में हुआ था और उनके बचपन का नाम मूलशंकर था।",
    "exp_en": "Swami Dayanand's childhood name was Moolshankar."
  },
  {
    "id": "q_san_c10_01", "subject_id": "sanskrit", "book_id": "san_b1", "chapter_id": "san_c10", "topic_id": "san_c10_t1",
    "difficulty": "Medium",
    "q_hi": "'मन्दाकिनीवर्णनम्' पाठ महर्षि वाल्मीकि रचित रामायण के किस काण्ड से संकलित है?",
    "q_en": "From which Kand of Valmiki Ramayana is 'Mandakini Varnanam' compiled?",
    "opts_hi": {"A": "बालकाण्ड", "B": "अयोध्याकाण्ड (सर्ग 95)", "C": "अरण्यकाण्ड", "D": "किष्किन्धाकाण्ड"},
    "opts_en": {"A": "Bala Kanda", "B": "Ayodhya Kanda (Canto 95)", "C": "Aranya Kanda", "D": "Kishkindha Kanda"},
    "ans": "B",
    "exp_hi": "'मन्दाकिनीवर्णनम्' वाल्मीकि रामायण के अयोध्याकाण्ड के 95वें सर्ग से संकलित है जिसमें श्रीराम चित्रकूट में सीता को मंदाकिनी नदी दिखाते हैं।",
    "exp_en": "Mandakini Varnanam is taken from Ayodhya Kanda (Canto 95) of Valmiki Ramayana."
  }
]

# Randomize options function
def process_and_randomize(items):
    output = []
    keys = ['A', 'B', 'C', 'D']
    for item in items:
        orig_pairs = [
            {'key': 'A', 'hi': item['opts_hi']['A'], 'en': item['opts_en']['A']},
            {'key': 'B', 'hi': item['opts_hi']['B'], 'en': item['opts_en']['B']},
            {'key': 'C', 'hi': item['opts_hi']['C'], 'en': item['opts_en']['C']},
            {'key': 'D', 'hi': item['opts_hi']['D'], 'en': item['opts_en']['D']}
        ]
        random.shuffle(orig_pairs)
        
        new_opts_hi = {}
        new_opts_en = {}
        new_corr = 'A'
        
        for idx, pair in enumerate(orig_pairs):
            k = keys[idx]
            new_opts_hi[k] = pair['hi']
            new_opts_en[k] = pair['en']
            if pair['key'] == item['ans']:
                new_corr = k
                
        output.append({
            "id": item["id"],
            "board": "BSEB",
            "class": "10",
            "subject_id": item["subject_id"],
            "book_id": item["book_id"],
            "chapter_id": item["chapter_id"],
            "topic_id": item["topic_id"],
            "difficulty": item["difficulty"],
            "question": {
                "hi": item["q_hi"],
                "en": item["q_en"]
            },
            "options": {
                "hi": new_opts_hi,
                "en": new_opts_en
            },
            "correct_option": new_corr,
            "explanation": {
                "hi": item["exp_hi"],
                "en": item["exp_en"]
            }
        })
    return output

# Read current bank
with open(r"c:\Users\harsh\Desktop\test app\js\data\questionBank.js", "r", encoding="utf-8") as f:
    t = f.read()

pfx = "window.BSEB_QUESTION_BANK = "
raw = t[t.find(pfx) + len(pfx):].rstrip(";\n ")
cur_bank = json.loads(raw)

new_processed = process_and_randomize(all_data)

# Combine and deduplicate
combined = cur_bank + new_processed
seen_ids = set()
final_list = []
for q in combined:
    if q["id"] not in seen_ids:
        seen_ids.add(q["id"])
        final_list.append(q)

target = r"c:\Users\harsh\Desktop\test app\js\data\questionBank.js"
js_out = "/**\n * Bihar Board (BSEB) Class 10 Centralized Question Bank\n * Verified, unique MCQs across all subjects and chapters in Hindi & English\n */\n\nwindow.BSEB_QUESTION_BANK = " + json.dumps(final_list, ensure_ascii=False, indent=2) + ";\n"

with open(target, "w", encoding="utf-8") as f:
    f.write(js_out)

print(f"Generated and merged! Total questions in Question Bank now: {len(final_list)}")
