# ============================================================
# AgriSakha - Disease Information Service
# Multilingual: English / Marathi / Hindi
# ============================================================


# ------------------------------------------------------------
# Class Name Normalization
# ------------------------------------------------------------

def normalize_class_name(name):
    return (
        name.strip()
        .lower()
        .replace("_", "")
        .replace(" ", "")
        .replace("-", "")
    )


# ------------------------------------------------------------
# Disease Information
# ------------------------------------------------------------

DISEASE_INFO = {

    # ========================================================
    # RICE
    # ========================================================

    "Rice_Healthy": {

        "en": {
            "crop": "Rice",
            "disease": "Healthy",
            "symptoms": "The leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain balanced nutrition, proper irrigation, good field sanitation, and regular crop monitoring.",
            "next_steps": "Continue regular monitoring and maintain proper crop management practices."
        },

        "mr": {
            "crop": "तांदूळ",
            "disease": "निरोगी",
            "symptoms": "पान निरोगी दिसते. त्याचा हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "संतुलित पोषण, योग्य सिंचन, शेताची स्वच्छता आणि नियमित पीक निरीक्षण ठेवा.",
            "next_steps": "नियमित निरीक्षण सुरू ठेवा आणि योग्य पीक व्यवस्थापन पद्धतींचा अवलंब करा."
        },

        "hi": {
            "crop": "चावल",
            "disease": "स्वस्थ",
            "symptoms": "पत्ता स्वस्थ दिखाई देता है। इसका हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "संतुलित पोषण, उचित सिंचाई, खेत की स्वच्छता और नियमित फसल निरीक्षण बनाए रखें।",
            "next_steps": "नियमित निगरानी जारी रखें और उचित फसल प्रबंधन अपनाएं।"
        }
    },


    "Rice_Brown_Spot": {

        "en": {
            "crop": "Rice",
            "disease": "Brown Spot",
            "symptoms": "Brown to reddish-brown spots may appear on leaves and can enlarge as the disease develops.",
            "prevention": "Maintain balanced crop nutrition, avoid prolonged plant stress, and use healthy planting material.",
            "next_steps": "Inspect nearby plants for similar symptoms and consult a local agricultural expert if symptoms are spreading."
        },

        "mr": {
            "crop": "तांदूळ",
            "disease": "तपकिरी डाग",
            "symptoms": "पानांवर तपकिरी ते लालसर-तपकिरी डाग दिसू शकतात आणि रोग वाढल्यास ते मोठे होऊ शकतात.",
            "prevention": "पिकाला संतुलित पोषण द्या, झाडावर दीर्घकाळ ताण येऊ देऊ नका आणि निरोगी लागवड साहित्य वापरा.",
            "next_steps": "आजूबाजूच्या झाडांवर अशीच लक्षणे आहेत का ते तपासा. लक्षणे वाढत असल्यास स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "चावल",
            "disease": "भूरा धब्बा",
            "symptoms": "पत्तियों पर भूरे से लाल-भूरे धब्बे दिखाई दे सकते हैं और बीमारी बढ़ने पर ये बड़े हो सकते हैं।",
            "prevention": "फसल को संतुलित पोषण दें, पौधे पर लंबे समय तक तनाव न आने दें और स्वस्थ रोपण सामग्री का उपयोग करें।",
            "next_steps": "आसपास के पौधों में समान लक्षणों की जांच करें। लक्षण फैल रहे हों तो स्थानीय कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Rice_Leaf_Blast": {

        "en": {
            "crop": "Rice",
            "disease": "Leaf Blast",
            "symptoms": "Spindle-shaped or diamond-shaped lesions may appear on leaves, often with gray centers and darker margins.",
            "prevention": "Avoid excessive nitrogen application, maintain balanced nutrition, and monitor the crop regularly.",
            "next_steps": "Inspect the crop for spreading lesions and consult an agricultural expert for appropriate management."
        },

        "mr": {
            "crop": "तांदूळ",
            "disease": "पानावरील ब्लास्ट",
            "symptoms": "पानांवर लांबट किंवा हिऱ्यासारखे डाग दिसू शकतात. या डागांचा मध्यभाग राखाडी आणि कडा गडद असू शकतात.",
            "prevention": "अति नत्राचा वापर टाळा, संतुलित पोषण द्या आणि पिकाचे नियमित निरीक्षण करा.",
            "next_steps": "डाग वाढत आहेत का ते तपासा आणि योग्य व्यवस्थापनासाठी कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "चावल",
            "disease": "पत्ती ब्लास्ट",
            "symptoms": "पत्तियों पर लंबे या हीरे के आकार के धब्बे दिखाई दे सकते हैं। इनके बीच का भाग धूसर और किनारे गहरे हो सकते हैं।",
            "prevention": "अत्यधिक नाइट्रोजन का उपयोग न करें, संतुलित पोषण दें और फसल की नियमित निगरानी करें।",
            "next_steps": "धब्बे फैल रहे हैं या नहीं इसकी जांच करें और उचित प्रबंधन के लिए कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    # ========================================================
    # MAIZE
    # ========================================================

    "Maize_Healthy": {

        "en": {
            "crop": "Maize",
            "disease": "Healthy",
            "symptoms": "The leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain proper irrigation, balanced nutrition, field sanitation, and regular crop monitoring.",
            "next_steps": "Continue monitoring the crop and maintain good agricultural practices."
        },

        "mr": {
            "crop": "मका",
            "disease": "निरोगी",
            "symptoms": "पान निरोगी दिसते. हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "योग्य सिंचन, संतुलित पोषण, शेताची स्वच्छता आणि नियमित पीक निरीक्षण ठेवा.",
            "next_steps": "पिकाचे निरीक्षण सुरू ठेवा आणि चांगल्या कृषी पद्धतींचा अवलंब करा."
        },

        "hi": {
            "crop": "मक्का",
            "disease": "स्वस्थ",
            "symptoms": "पत्ता स्वस्थ दिखाई देता है। हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "उचित सिंचाई, संतुलित पोषण, खेत की स्वच्छता और नियमित फसल निगरानी बनाए रखें।",
            "next_steps": "फसल की निगरानी जारी रखें और अच्छी कृषि पद्धतियों को अपनाएं।"
        }
    },


    "Maize_Leaf_Spot": {

        "en": {
            "crop": "Maize",
            "disease": "Leaf Spot",
            "symptoms": "Small to elongated brown or grayish spots may develop on maize leaves and may increase in size over time.",
            "prevention": "Maintain field sanitation, avoid excessive plant stress, and monitor leaves regularly.",
            "next_steps": "Check nearby plants for similar spots and consult an agricultural expert if the condition spreads."
        },

        "mr": {
            "crop": "मका",
            "disease": "पानावरील डाग",
            "symptoms": "मक्याच्या पानांवर लहान ते लांबट तपकिरी किंवा राखाडी डाग दिसू शकतात आणि कालांतराने ते वाढू शकतात.",
            "prevention": "शेताची स्वच्छता ठेवा, झाडावर जास्त ताण येऊ देऊ नका आणि पानांचे नियमित निरीक्षण करा.",
            "next_steps": "आजूबाजूच्या झाडांवरही असे डाग आहेत का ते तपासा. स्थिती वाढत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "मक्का",
            "disease": "पत्ती धब्बा",
            "symptoms": "मक्के की पत्तियों पर छोटे से लंबे भूरे या धूसर धब्बे दिखाई दे सकते हैं और समय के साथ बढ़ सकते हैं।",
            "prevention": "खेत की स्वच्छता बनाए रखें, पौधे पर अत्यधिक तनाव न आने दें और पत्तियों की नियमित निगरानी करें।",
            "next_steps": "आसपास के पौधों में भी ऐसे धब्बों की जांच करें। स्थिति फैल रही हो तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Maize_Streak_Virus": {

        "en": {
            "crop": "Maize",
            "disease": "Streak Virus",
            "symptoms": "Light-colored streaks or lines may appear along maize leaves, sometimes accompanied by reduced plant growth.",
            "prevention": "Use healthy planting material, control insect vectors where appropriate, and monitor plants regularly.",
            "next_steps": "Inspect nearby plants for similar streaking and seek agricultural advice if symptoms are spreading."
        },

        "mr": {
            "crop": "मका",
            "disease": "स्ट्रीक विषाणू",
            "symptoms": "मक्याच्या पानांवर फिकट रंगाचे पट्टे किंवा रेषा दिसू शकतात. काही वेळा झाडाची वाढ कमी होऊ शकते.",
            "prevention": "निरोगी लागवड साहित्य वापरा, आवश्यकतेनुसार कीटक वाहकांचे नियंत्रण करा आणि झाडांचे नियमित निरीक्षण करा.",
            "next_steps": "आजूबाजूच्या झाडांवर अशीच लक्षणे आहेत का ते तपासा आणि लक्षणे वाढत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "मक्का",
            "disease": "स्ट्रीक वायरस",
            "symptoms": "मक्के की पत्तियों पर हल्के रंग की धारियां या रेखाएं दिखाई दे सकती हैं। कभी-कभी पौधे की वृद्धि भी कम हो सकती है।",
            "prevention": "स्वस्थ रोपण सामग्री का उपयोग करें, आवश्यकता के अनुसार कीट वाहकों को नियंत्रित करें और पौधों की नियमित निगरानी करें।",
            "next_steps": "आसपास के पौधों में समान लक्षणों की जांच करें और लक्षण फैल रहे हों तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    # ========================================================
    # SOYABEAN
    # ========================================================

    "Soyabean_Healthy": {

        "en": {
            "crop": "Soyabean",
            "disease": "Healthy",
            "symptoms": "The leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain balanced nutrition, appropriate irrigation, good field sanitation, and regular monitoring.",
            "next_steps": "Continue regular crop monitoring and maintain healthy crop management practices."
        },

        "mr": {
            "crop": "सोयाबीन",
            "disease": "निरोगी",
            "symptoms": "पान निरोगी दिसते. हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "संतुलित पोषण, योग्य सिंचन, शेताची स्वच्छता आणि नियमित निरीक्षण ठेवा.",
            "next_steps": "पिकाचे नियमित निरीक्षण सुरू ठेवा आणि निरोगी पीक व्यवस्थापन पद्धतींचा अवलंब करा."
        },

        "hi": {
            "crop": "सोयाबीन",
            "disease": "स्वस्थ",
            "symptoms": "पत्ता स्वस्थ दिखाई देता है। हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "संतुलित पोषण, उचित सिंचाई, खेत की स्वच्छता और नियमित निगरानी बनाए रखें।",
            "next_steps": "फसल की नियमित निगरानी जारी रखें और स्वस्थ फसल प्रबंधन अपनाएं।"
        }
    },


    "Soyabean_Caterpillar": {

        "en": {
            "crop": "Soyabean",
            "disease": "Caterpillar Damage",
            "symptoms": "Irregular holes, missing leaf tissue, or feeding damage may appear on soybean leaves.",
            "prevention": "Regularly inspect leaves for caterpillars and maintain appropriate integrated pest management practices.",
            "next_steps": "Inspect affected plants closely and consult an agricultural expert if pest damage is increasing."
        },

        "mr": {
            "crop": "सोयाबीन",
            "disease": "अळीमुळे नुकसान",
            "symptoms": "सोयाबीनच्या पानांवर अनियमित छिद्रे, पानांचा काही भाग खाल्लेला किंवा कुरतडल्याची लक्षणे दिसू शकतात.",
            "prevention": "पानांवर अळ्यांची नियमित तपासणी करा आणि योग्य एकात्मिक कीड व्यवस्थापन पद्धतींचा अवलंब करा.",
            "next_steps": "प्रभावित झाडांची काळजीपूर्वक तपासणी करा. किडीचे नुकसान वाढत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "सोयाबीन",
            "disease": "इल्ली से नुकसान",
            "symptoms": "सोयाबीन की पत्तियों पर अनियमित छेद, पत्ती का खाया हुआ भाग या कुतरने के लक्षण दिखाई दे सकते हैं।",
            "prevention": "पत्तियों पर इल्ली की नियमित जांच करें और उचित एकीकृत कीट प्रबंधन अपनाएं।",
            "next_steps": "प्रभावित पौधों की सावधानी से जांच करें। कीट का नुकसान बढ़ रहा हो तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Soyabean_Diabrotica_speciosa": {

        "en": {
            "crop": "Soyabean",
            "disease": "Diabrotica speciosa Damage",
            "symptoms": "Feeding damage may appear as holes or irregular areas of tissue loss on soybean leaves.",
            "prevention": "Monitor plants regularly for beetles and maintain appropriate pest management practices.",
            "next_steps": "Inspect affected plants and consult an agricultural expert if insect damage continues to increase."
        },

        "mr": {
            "crop": "सोयाबीन",
            "disease": "Diabrotica speciosa मुळे नुकसान",
            "symptoms": "सोयाबीनच्या पानांवर छिद्रे किंवा पानांचा काही भाग खाल्ल्यामुळे अनियमित नुकसान दिसू शकते.",
            "prevention": "झाडांवर भुंग्यांचे नियमित निरीक्षण करा आणि योग्य कीड व्यवस्थापन पद्धतींचा अवलंब करा.",
            "next_steps": "प्रभावित झाडांची तपासणी करा. किडीचे नुकसान वाढत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "सोयाबीन",
            "disease": "Diabrotica speciosa से नुकसान",
            "symptoms": "सोयाबीन की पत्तियों पर छेद या पत्तियों का कुछ हिस्सा खाए जाने के कारण अनियमित नुकसान दिखाई दे सकता है।",
            "prevention": "पौधों पर भृंगों की नियमित निगरानी करें और उचित कीट प्रबंधन अपनाएं।",
            "next_steps": "प्रभावित पौधों की जांच करें। कीट का नुकसान बढ़ रहा हो तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    # ========================================================
    # WHEAT
    # ========================================================

    "Wheat_Healthy": {

        "en": {
            "crop": "Wheat",
            "disease": "Healthy",
            "symptoms": "The leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain balanced nutrition, appropriate irrigation, field sanitation, and regular monitoring.",
            "next_steps": "Continue regular crop monitoring and maintain proper crop management."
        },

        "mr": {
            "crop": "गहू",
            "disease": "निरोगी",
            "symptoms": "पान निरोगी दिसते. हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "संतुलित पोषण, योग्य सिंचन, शेताची स्वच्छता आणि नियमित निरीक्षण ठेवा.",
            "next_steps": "पिकाचे नियमित निरीक्षण सुरू ठेवा आणि योग्य पीक व्यवस्थापन करा."
        },

        "hi": {
            "crop": "गेहूं",
            "disease": "स्वस्थ",
            "symptoms": "पत्ता स्वस्थ दिखाई देता है। हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "संतुलित पोषण, उचित सिंचाई, खेत की स्वच्छता और नियमित निगरानी बनाए रखें।",
            "next_steps": "फसल की नियमित निगरानी जारी रखें और उचित फसल प्रबंधन करें।"
        }
    },


    "Wheat_Brown_Rust": {

        "en": {
            "crop": "Wheat",
            "disease": "Brown Rust",
            "symptoms": "Small orange-brown to reddish-brown rust-colored pustules may appear on wheat leaves.",
            "prevention": "Use healthy seed, monitor the crop regularly, and maintain appropriate field management.",
            "next_steps": "Inspect the crop for increasing rust symptoms and consult an agricultural expert for management guidance."
        },

        "mr": {
            "crop": "गहू",
            "disease": "तपकिरी गेरू",
            "symptoms": "गव्हाच्या पानांवर लहान नारिंगी-तपकिरी ते लालसर-तपकिरी गंजासारखे ठिपके दिसू शकतात.",
            "prevention": "निरोगी बियाणे वापरा, पिकाचे नियमित निरीक्षण करा आणि योग्य शेत व्यवस्थापन ठेवा.",
            "next_steps": "गंजाची लक्षणे वाढत आहेत का ते तपासा आणि व्यवस्थापनासाठी कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "गेहूं",
            "disease": "भूरा रतुआ",
            "symptoms": "गेहूं की पत्तियों पर छोटे नारंगी-भूरे से लाल-भूरे रंग के जंग जैसे दाने दिखाई दे सकते हैं।",
            "prevention": "स्वस्थ बीज का उपयोग करें, फसल की नियमित निगरानी करें और उचित खेत प्रबंधन बनाए रखें।",
            "next_steps": "रतुआ के लक्षण बढ़ रहे हैं या नहीं इसकी जांच करें और प्रबंधन के लिए कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Wheat_Yellow_Rust": {

        "en": {
            "crop": "Wheat",
            "disease": "Yellow Rust",
            "symptoms": "Yellow to orange-yellow rust-colored stripes or pustules may appear along wheat leaves.",
            "prevention": "Use healthy seed, monitor the crop frequently, and maintain suitable field conditions.",
            "next_steps": "Check whether yellow rust symptoms are spreading and consult an agricultural expert if necessary."
        },

        "mr": {
            "crop": "गहू",
            "disease": "पिवळा गेरू",
            "symptoms": "गव्हाच्या पानांवर पिवळ्या ते नारिंगी-पिवळ्या रंगाचे गंजासारखे पट्टे किंवा ठिपके दिसू शकतात.",
            "prevention": "निरोगी बियाणे वापरा, पिकाचे वारंवार निरीक्षण करा आणि योग्य शेत परिस्थिती ठेवा.",
            "next_steps": "पिवळ्या गंजाची लक्षणे पसरत आहेत का ते तपासा आणि आवश्यक असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "गेहूं",
            "disease": "पीला रतुआ",
            "symptoms": "गेहूं की पत्तियों पर पीले से नारंगी-पीले रंग की जंग जैसी धारियां या दाने दिखाई दे सकते हैं।",
            "prevention": "स्वस्थ बीज का उपयोग करें, फसल की नियमित निगरानी करें और उचित खेत परिस्थितियां बनाए रखें।",
            "next_steps": "पीले रतुआ के लक्षण फैल रहे हैं या नहीं इसकी जांच करें और आवश्यकता होने पर कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    # ========================================================
    # GROUNDNUT
    # ========================================================

    "Groundnut_Healthy_Leaf": {

        "en": {
            "crop": "Groundnut",
            "disease": "Healthy Leaf",
            "symptoms": "The leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain balanced nutrition, proper irrigation, good field sanitation, and regular monitoring.",
            "next_steps": "Continue regular crop monitoring and maintain good crop management."
        },

        "mr": {
            "crop": "भुईमूग",
            "disease": "निरोगी पान",
            "symptoms": "पान निरोगी दिसते. हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "संतुलित पोषण, योग्य सिंचन, शेताची स्वच्छता आणि नियमित निरीक्षण ठेवा.",
            "next_steps": "पिकाचे नियमित निरीक्षण सुरू ठेवा आणि चांगले पीक व्यवस्थापन करा."
        },

        "hi": {
            "crop": "मूंगफली",
            "disease": "स्वस्थ पत्ती",
            "symptoms": "पत्ता स्वस्थ दिखाई देता है। हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "संतुलित पोषण, उचित सिंचाई, खेत की स्वच्छता और नियमित निगरानी बनाए रखें।",
            "next_steps": "फसल की नियमित निगरानी जारी रखें और अच्छा फसल प्रबंधन अपनाएं।"
        }
    },


    "Groundnut_Leaf_Spot": {

        "en": {
            "crop": "Groundnut",
            "disease": "Leaf Spot",
            "symptoms": "Dark brown or blackish spots may appear on groundnut leaves and may increase as the condition develops.",
            "prevention": "Maintain field sanitation, avoid prolonged leaf wetness where possible, and monitor the crop regularly.",
            "next_steps": "Inspect nearby plants for similar spots and consult an agricultural expert if symptoms spread."
        },

        "mr": {
            "crop": "भुईमूग",
            "disease": "पानावरील डाग",
            "symptoms": "भुईमुगाच्या पानांवर गडद तपकिरी किंवा काळसर डाग दिसू शकतात आणि स्थिती वाढल्यास ते अधिक पसरू शकतात.",
            "prevention": "शेताची स्वच्छता ठेवा, शक्य असल्यास पानांवर दीर्घकाळ ओलावा राहू देऊ नका आणि पिकाचे नियमित निरीक्षण करा.",
            "next_steps": "आजूबाजूच्या झाडांवर असेच डाग आहेत का ते तपासा. लक्षणे पसरत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "मूंगफली",
            "disease": "पत्ती धब्बा",
            "symptoms": "मूंगफली की पत्तियों पर गहरे भूरे या काले धब्बे दिखाई दे सकते हैं और स्थिति बढ़ने पर फैल सकते हैं।",
            "prevention": "खेत की स्वच्छता बनाए रखें, जहां संभव हो पत्तियों पर लंबे समय तक नमी न रहने दें और फसल की नियमित निगरानी करें।",
            "next_steps": "आसपास के पौधों में समान धब्बों की जांच करें। लक्षण फैल रहे हों तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Groundnut_Nutrition_Deficiency": {

        "en": {
            "crop": "Groundnut",
            "disease": "Nutrition Deficiency",
            "symptoms": "Leaves may show abnormal yellowing, discoloration, or reduced healthy green coloration associated with nutritional stress.",
            "prevention": "Maintain balanced soil fertility and use soil testing to guide appropriate nutrient management.",
            "next_steps": "Check soil and crop nutrition conditions and consult an agricultural expert before applying corrective nutrients."
        },

        "mr": {
            "crop": "भुईमूग",
            "disease": "पोषणाची कमतरता",
            "symptoms": "पानांवर असामान्य पिवळेपणा, रंग बदलणे किंवा हिरवा रंग कमी होणे यांसारखी पोषण ताणाची लक्षणे दिसू शकतात.",
            "prevention": "जमिनीची सुपीकता संतुलित ठेवा आणि योग्य पोषण व्यवस्थापनासाठी माती परीक्षणाचा उपयोग करा.",
            "next_steps": "माती आणि पिकाच्या पोषणाची स्थिती तपासा. सुधारात्मक पोषक द्रव्ये देण्यापूर्वी कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "मूंगफली",
            "disease": "पोषक तत्वों की कमी",
            "symptoms": "पत्तियों में असामान्य पीलापन, रंग में बदलाव या हरे रंग में कमी जैसे पोषण संबंधी तनाव के लक्षण दिखाई दे सकते हैं।",
            "prevention": "मिट्टी की उर्वरता संतुलित रखें और उचित पोषण प्रबंधन के लिए मिट्टी परीक्षण का उपयोग करें।",
            "next_steps": "मिट्टी और फसल की पोषण स्थिति की जांच करें। सुधारात्मक पोषक तत्व देने से पहले कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    # ========================================================
    # POTATO
    # ========================================================

    "Potato_Healthy": {

        "en": {
            "crop": "Potato",
            "disease": "Healthy",
            "symptoms": "The leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain balanced nutrition, appropriate irrigation, field sanitation, and regular monitoring.",
            "next_steps": "Continue monitoring the crop and maintain proper crop management."
        },

        "mr": {
            "crop": "बटाटा",
            "disease": "निरोगी",
            "symptoms": "पान निरोगी दिसते. हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "संतुलित पोषण, योग्य सिंचन, शेताची स्वच्छता आणि नियमित निरीक्षण ठेवा.",
            "next_steps": "पिकाचे निरीक्षण सुरू ठेवा आणि योग्य पीक व्यवस्थापन करा."
        },

        "hi": {
            "crop": "आलू",
            "disease": "स्वस्थ",
            "symptoms": "पत्ता स्वस्थ दिखाई देता है। हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "संतुलित पोषण, उचित सिंचाई, खेत की स्वच्छता और नियमित निगरानी बनाए रखें।",
            "next_steps": "फसल की निगरानी जारी रखें और उचित फसल प्रबंधन करें।"
        }
    },


    "Potato_Early_Blight": {

        "en": {
            "crop": "Potato",
            "disease": "Early Blight",
            "symptoms": "Dark brown spots with concentric ring patterns may appear on potato leaves.",
            "prevention": "Maintain good field sanitation, avoid prolonged leaf wetness, and provide balanced crop nutrition.",
            "next_steps": "Inspect nearby plants for similar lesions and consult an agricultural expert if symptoms are spreading."
        },

        "mr": {
            "crop": "बटाटा",
            "disease": "अर्ली ब्लाइट",
            "symptoms": "बटाट्याच्या पानांवर गडद तपकिरी डाग दिसू शकतात. या डागांमध्ये वर्तुळाकार पट्ट्यांसारखी रचना असू शकते.",
            "prevention": "शेताची स्वच्छता ठेवा, पानांवर दीर्घकाळ ओलावा राहू देऊ नका आणि संतुलित पोषण द्या.",
            "next_steps": "आजूबाजूच्या झाडांवर अशीच लक्षणे आहेत का ते तपासा. लक्षणे पसरत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "आलू",
            "disease": "अर्ली ब्लाइट",
            "symptoms": "आलू की पत्तियों पर गहरे भूरे धब्बे दिखाई दे सकते हैं। इन धब्बों में गोलाकार छल्ले जैसी संरचना हो सकती है।",
            "prevention": "खेत की स्वच्छता बनाए रखें, पत्तियों पर लंबे समय तक नमी न रहने दें और संतुलित पोषण दें।",
            "next_steps": "आसपास के पौधों में समान लक्षणों की जांच करें। लक्षण फैल रहे हों तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Potato_Late_Blight": {

        "en": {
            "crop": "Potato",
            "disease": "Late Blight",
            "symptoms": "Dark water-soaked or irregular brown lesions may appear on leaves and can expand rapidly under favorable conditions.",
            "prevention": "Maintain good field sanitation, avoid excessive leaf wetness, and monitor the crop frequently.",
            "next_steps": "Inspect the crop carefully for spreading lesions and consult an agricultural expert for appropriate management."
        },

        "mr": {
            "crop": "बटाटा",
            "disease": "लेट ब्लाइट",
            "symptoms": "पानांवर गडद, पाण्याने भिजल्यासारखे किंवा अनियमित तपकिरी डाग दिसू शकतात आणि योग्य परिस्थितीत ते वेगाने वाढू शकतात.",
            "prevention": "शेताची स्वच्छता ठेवा, पानांवर जास्त ओलावा राहू देऊ नका आणि पिकाचे वारंवार निरीक्षण करा.",
            "next_steps": "पिकावर पसरत असलेल्या डागांची काळजीपूर्वक तपासणी करा आणि योग्य व्यवस्थापनासाठी कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "आलू",
            "disease": "लेट ब्लाइट",
            "symptoms": "पत्तियों पर गहरे, पानी से भीगे हुए जैसे या अनियमित भूरे धब्बे दिखाई दे सकते हैं और अनुकूल परिस्थितियों में तेजी से फैल सकते हैं।",
            "prevention": "खेत की स्वच्छता बनाए रखें, पत्तियों पर अत्यधिक नमी न रहने दें और फसल की नियमित निगरानी करें।",
            "next_steps": "फसल में फैल रहे धब्बों की सावधानी से जांच करें और उचित प्रबंधन के लिए कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    # ========================================================
    # TOMATO
    # ========================================================

    "Tomato_Healthy": {

        "en": {
            "crop": "Tomato",
            "disease": "Healthy",
            "symptoms": "The leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain balanced nutrition, proper irrigation, field sanitation, and regular monitoring.",
            "next_steps": "Continue regular crop monitoring and maintain healthy crop management practices."
        },

        "mr": {
            "crop": "टोमॅटो",
            "disease": "निरोगी",
            "symptoms": "पान निरोगी दिसते. हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "संतुलित पोषण, योग्य सिंचन, शेताची स्वच्छता आणि नियमित निरीक्षण ठेवा.",
            "next_steps": "पिकाचे नियमित निरीक्षण सुरू ठेवा आणि निरोगी पीक व्यवस्थापन करा."
        },

        "hi": {
            "crop": "टमाटर",
            "disease": "स्वस्थ",
            "symptoms": "पत्ता स्वस्थ दिखाई देता है। हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "संतुलित पोषण, उचित सिंचाई, खेत की स्वच्छता और नियमित निगरानी बनाए रखें।",
            "next_steps": "फसल की नियमित निगरानी जारी रखें और स्वस्थ फसल प्रबंधन अपनाएं।"
        }
    },


    "Tomato_Leaf_Blight": {

        "en": {
            "crop": "Tomato",
            "disease": "Leaf Blight",
            "symptoms": "Brown or dark lesions may appear on tomato leaves and can expand as the condition develops.",
            "prevention": "Maintain good field sanitation, avoid prolonged leaf wetness, and provide adequate crop spacing.",
            "next_steps": "Inspect nearby plants for similar symptoms and consult an agricultural expert if the condition spreads."
        },

        "mr": {
            "crop": "टोमॅटो",
            "disease": "पानावरील ब्लाइट",
            "symptoms": "टोमॅटोच्या पानांवर तपकिरी किंवा गडद डाग दिसू शकतात आणि स्थिती वाढल्यास ते मोठे होऊ शकतात.",
            "prevention": "शेताची स्वच्छता ठेवा, पानांवर दीर्घकाळ ओलावा राहू देऊ नका आणि झाडांमध्ये योग्य अंतर ठेवा.",
            "next_steps": "आजूबाजूच्या झाडांवर अशीच लक्षणे आहेत का ते तपासा. स्थिती पसरत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "टमाटर",
            "disease": "पत्ती ब्लाइट",
            "symptoms": "टमाटर की पत्तियों पर भूरे या गहरे धब्बे दिखाई दे सकते हैं और स्थिति बढ़ने पर ये बड़े हो सकते हैं।",
            "prevention": "खेत की स्वच्छता बनाए रखें, पत्तियों पर लंबे समय तक नमी न रहने दें और पौधों के बीच उचित दूरी रखें।",
            "next_steps": "आसपास के पौधों में समान लक्षणों की जांच करें। स्थिति फैल रही हो तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Tomato_Septoria_Leaf_Spot": {

        "en": {
            "crop": "Tomato",
            "disease": "Septoria Leaf Spot",
            "symptoms": "Small circular spots with darker margins may appear on tomato leaves and can increase in number as the condition progresses.",
            "prevention": "Maintain field sanitation, avoid overhead watering where possible, and remove severely affected plant material appropriately.",
            "next_steps": "Inspect lower and nearby leaves for additional spots and consult an agricultural expert if symptoms continue spreading."
        },

        "mr": {
            "crop": "टोमॅटो",
            "disease": "सेप्टोरिया पानावरील डाग",
            "symptoms": "टोमॅटोच्या पानांवर गडद कडा असलेले लहान गोलाकार डाग दिसू शकतात आणि स्थिती वाढल्यास त्यांची संख्या वाढू शकते.",
            "prevention": "शेताची स्वच्छता ठेवा, शक्य असल्यास वरून पाणी देणे टाळा आणि जास्त प्रभावित झाडांचा भाग योग्य पद्धतीने काढा.",
            "next_steps": "खालच्या आणि आजूबाजूच्या पानांवर आणखी डाग आहेत का ते तपासा. लक्षणे पसरत राहिल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "टमाटर",
            "disease": "सेप्टोरिया पत्ती धब्बा",
            "symptoms": "टमाटर की पत्तियों पर गहरे किनारों वाले छोटे गोल धब्बे दिखाई दे सकते हैं और स्थिति बढ़ने पर इनकी संख्या बढ़ सकती है।",
            "prevention": "खेत की स्वच्छता बनाए रखें, जहां संभव हो ऊपर से पानी देने से बचें और अधिक प्रभावित पौधों के हिस्सों को उचित तरीके से हटाएं।",
            "next_steps": "नीचे और आसपास की पत्तियों में अतिरिक्त धब्बों की जांच करें। लक्षण फैलते रहें तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    # ========================================================
    # COTTON
    # ========================================================

    "Cotton_Healthy_Leaf": {

        "en": {
            "crop": "Cotton",
            "disease": "Healthy Leaf",
            "symptoms": "The cotton leaf appears healthy with normal green coloration and no major visible disease symptoms.",
            "prevention": "Maintain balanced nutrition, appropriate irrigation, field sanitation, and regular crop monitoring.",
            "next_steps": "Continue regular monitoring and maintain healthy crop management practices."
        },

        "mr": {
            "crop": "कापूस",
            "disease": "निरोगी पान",
            "symptoms": "कापसाचे पान निरोगी दिसते. हिरवा रंग सामान्य असून रोगाची कोणतीही मोठी लक्षणे दिसत नाहीत.",
            "prevention": "संतुलित पोषण, योग्य सिंचन, शेताची स्वच्छता आणि नियमित पीक निरीक्षण ठेवा.",
            "next_steps": "नियमित निरीक्षण सुरू ठेवा आणि निरोगी पीक व्यवस्थापन करा."
        },

        "hi": {
            "crop": "कपास",
            "disease": "स्वस्थ पत्ती",
            "symptoms": "कपास की पत्ती स्वस्थ दिखाई देती है। हरा रंग सामान्य है और बीमारी के कोई प्रमुख लक्षण दिखाई नहीं देते।",
            "prevention": "संतुलित पोषण, उचित सिंचाई, खेत की स्वच्छता और नियमित फसल निगरानी बनाए रखें।",
            "next_steps": "नियमित निगरानी जारी रखें और स्वस्थ फसल प्रबंधन अपनाएं।"
        }
    },


    "Cotton_Bacterial_Blight": {

        "en": {
            "crop": "Cotton",
            "disease": "Bacterial Blight",
            "symptoms": "Water-soaked or angular dark lesions may appear on cotton leaves and may develop into larger damaged areas.",
            "prevention": "Use healthy planting material, maintain field sanitation, and avoid unnecessary leaf wetness.",
            "next_steps": "Inspect nearby plants for similar symptoms and consult an agricultural expert if symptoms spread."
        },

        "mr": {
            "crop": "कापूस",
            "disease": "बॅक्टेरियल ब्लाइट",
            "symptoms": "कापसाच्या पानांवर पाण्याने भिजल्यासारखे किंवा कोनीय गडद डाग दिसू शकतात आणि ते मोठ्या खराब झालेल्या भागात बदलू शकतात.",
            "prevention": "निरोगी लागवड साहित्य वापरा, शेताची स्वच्छता ठेवा आणि अनावश्यक पानांचा ओलावा टाळा.",
            "next_steps": "आजूबाजूच्या झाडांवर अशीच लक्षणे आहेत का ते तपासा. लक्षणे पसरत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "कपास",
            "disease": "बैक्टीरियल ब्लाइट",
            "symptoms": "कपास की पत्तियों पर पानी से भीगे हुए जैसे या कोणीय गहरे धब्बे दिखाई दे सकते हैं और ये बड़े क्षतिग्रस्त क्षेत्रों में बदल सकते हैं।",
            "prevention": "स्वस्थ रोपण सामग्री का उपयोग करें, खेत की स्वच्छता बनाए रखें और अनावश्यक पत्ती नमी से बचें।",
            "next_steps": "आसपास के पौधों में समान लक्षणों की जांच करें। लक्षण फैल रहे हों तो कृषि विशेषज्ञ से सलाह लें।"
        }
    },


    "Cotton_Curl_Virus": {

        "en": {
            "crop": "Cotton",
            "disease": "Curl Virus",
            "symptoms": "Cotton leaves may curl, become distorted, and show changes in normal leaf growth.",
            "prevention": "Use healthy planting material, monitor insect vectors, and regularly inspect new growth.",
            "next_steps": "Inspect affected plants and nearby plants for similar symptoms and seek agricultural advice if symptoms increase."
        },

        "mr": {
            "crop": "कापूस",
            "disease": "कर्ल विषाणू",
            "symptoms": "कापसाची पाने वाकडी किंवा विकृत होऊ शकतात आणि पानांच्या सामान्य वाढीत बदल दिसू शकतो.",
            "prevention": "निरोगी लागवड साहित्य वापरा, कीटक वाहकांचे निरीक्षण करा आणि नवीन वाढीचे नियमित निरीक्षण करा.",
            "next_steps": "प्रभावित आणि आजूबाजूच्या झाडांवर अशीच लक्षणे आहेत का ते तपासा. लक्षणे वाढत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या."
        },

        "hi": {
            "crop": "कपास",
            "disease": "कर्ल वायरस",
            "symptoms": "कपास की पत्तियां मुड़ या विकृत हो सकती हैं और पत्तियों की सामान्य वृद्धि में बदलाव दिखाई दे सकता है।",
            "prevention": "स्वस्थ रोपण सामग्री का उपयोग करें, कीट वाहकों की निगरानी करें और नई वृद्धि का नियमित निरीक्षण करें।",
            "next_steps": "प्रभावित और आसपास के पौधों में समान लक्षणों की जांच करें। लक्षण बढ़ रहे हों तो कृषि विशेषज्ञ से सलाह लें।"
        }
    }
}


# ------------------------------------------------------------
# Risk Level
#
# The typical impact of each condition if it is left untreated.
# This describes the condition in general, NOT how bad the
# photographed leaf is, so the UI labels it "Risk level".
# Values: none | low | moderate | high
# ------------------------------------------------------------

RISK_LEVELS = {
    "Rice_Healthy": "none",
    "Rice_Brown_Spot": "moderate",
    "Rice_Leaf_Blast": "high",

    "Maize_Healthy": "none",
    "Maize_Leaf_Spot": "moderate",
    "Maize_Streak_Virus": "high",

    "Soyabean_Healthy": "none",
    "Soyabean_Caterpillar": "moderate",
    "Soyabean_Diabrotica_speciosa": "moderate",

    "Wheat_Healthy": "none",
    "Wheat_Brown_Rust": "high",
    "Wheat_Yellow_Rust": "high",

    "Groundnut_Healthy_Leaf": "none",
    "Groundnut_Leaf_Spot": "moderate",
    "Groundnut_Nutrition_Deficiency": "low",

    "Potato_Healthy": "none",
    "Potato_Early_Blight": "moderate",
    "Potato_Late_Blight": "high",

    "Tomato_Healthy": "none",
    "Tomato_Leaf_Blight": "moderate",
    "Tomato_Septoria_Leaf_Spot": "moderate",

    "Cotton_Healthy_Leaf": "none",
    "Cotton_Bacterial_Blight": "high",
    "Cotton_Curl_Virus": "high",
}


# ------------------------------------------------------------
# Unknown Class Fallback (localized)
# ------------------------------------------------------------

UNKNOWN_INFO = {

    "en": {
        "crop": "Unknown",
        "symptoms": "Information is not available for this prediction.",
        "prevention": "Please consult a local agricultural expert.",
        "next_steps": "Consider getting the crop inspected by an agricultural professional."
    },

    "mr": {
        "crop": "अज्ञात",
        "symptoms": "या निकालासाठी माहिती उपलब्ध नाही.",
        "prevention": "कृपया स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या.",
        "next_steps": "पिकाची तपासणी कृषी तज्ज्ञांकडून करून घेण्याचा विचार करा."
    },

    "hi": {
        "crop": "अज्ञात",
        "symptoms": "इस परिणाम के लिए जानकारी उपलब्ध नहीं है।",
        "prevention": "कृपया स्थानीय कृषि विशेषज्ञ से सलाह लें।",
        "next_steps": "फसल की जांच किसी कृषि विशेषज्ञ से करवाने पर विचार करें।"
    }
}


SUPPORTED_LANGUAGES = ("en", "mr", "hi")


# ------------------------------------------------------------
# Lookup Table
# Built once at import time instead of looping on every request.
# ------------------------------------------------------------

_CLASS_LOOKUP = {
    normalize_class_name(class_name): class_name
    for class_name in DISEASE_INFO
}


def count_conditions():
    return len(DISEASE_INFO)


# ------------------------------------------------------------
# Get Disease Information
# ------------------------------------------------------------

def get_disease_info(predicted_class, language="en"):
    """
    Returns a dict with: crop, disease, symptoms, prevention,
    next_steps, risk ("none" | "low" | "moderate" | "high" | "unknown")
    and key (the canonical class id, or the raw prediction if unknown).
    """

    if language not in SUPPORTED_LANGUAGES:
        language = "en"

    class_key = _CLASS_LOOKUP.get(
        normalize_class_name(predicted_class)
    )

    # Unknown class fallback — now respects the selected language
    if class_key is None:

        information = dict(UNKNOWN_INFO[language])

        information["disease"] = predicted_class
        information["risk"] = "unknown"
        information["key"] = predicted_class

        return information


    # Copy so callers can never mutate the shared DISEASE_INFO data
    information = dict(DISEASE_INFO[class_key][language])

    information["risk"] = RISK_LEVELS.get(class_key, "unknown")
    information["key"] = class_key

    return information