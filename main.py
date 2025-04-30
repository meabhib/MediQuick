from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Symptom-to-disease mappings
symptoms_to_diseases = {
    'fever': ['Common Cold', 'Flu', 'COVID-19', 'Malaria', 'Dengue', 'Typhoid'],
    'headache': ['Tension Headache', 'Migraine', 'High BP', 'Common Cold', 'Flu'],
    'cough': ['Common Cold', 'Flu', 'COVID-19', 'Bronchitis', 'Asthma'],
    'stomach_pain': ['Food Poisoning', 'Gas', 'Acidity', 'Stomach Infection'],
    'body_pain': ['Flu', 'Viral Fever', 'Dengue', 'Typhoid'],
    'weakness': ['Anemia', 'Vitamin Deficiency', 'Typhoid', 'Dengue'],
    'vomiting': ['Food Poisoning', 'Stomach Infection', 'Migraine'],
    'diarrhea': ['Food Poisoning', 'Stomach Infection', 'Cholera'],
    'skin_rash': ['Allergy', 'Chicken Pox', 'Measles'],
    'breathing_problem': ['Asthma', 'COVID-19', 'Pneumonia'],
    'joint_pain': ['Arthritis', 'Dengue', 'Chikungunya'],
    'chest_pain': ['Heart Problem', 'Gas', 'Anxiety'],
    'dizziness': ['Low BP', 'Anemia', 'Migraine'],
    'eye_pain': ['Eye Infection', 'Migraine', 'High BP']
}

# Disease-to-medicines mapping
disease_medicines = {
    'Common Cold': ['Crocin Advance - For fever and body pain', 'D-Cold Total - For cold, cough and blocked nose', 'Vicks Action 500 - For cold and body pain'],
    'Flu': ['Paracetamol - For fever and body pain', 'Nasoclear Nasal Spray - For blocked nose', 'Limcee Vitamin C - To boost immunity'],
    'COVID-19': ['Please consult doctor immediately', 'Get COVID test done', 'Take rest and isolate yourself'],
    'Stomach Infection': ['ORS - For hydration (mix in water)', 'Digene - For stomach pain and acidity', 'Eldoper - For loose motions'],
    'Headache': ['Saridon - For headache relief', 'Disprin - For quick pain relief', 'Dolo 650 - For headache with fever'],
    'Allergy': ['Cetrizine - For allergy and rash', 'Allegra - For skin allergy', 'Calamine lotion - For itching']
}

# Symptom descriptions
symptom_descriptions = {
    'fever': 'गरम शरीर या बुखार',
    'headache': 'सिर दर्द',
    'cough': 'खांसी',
    'stomach_pain': 'पेट दर्द',
    'body_pain': 'शरीर में दर्द',
    'weakness': 'कमजोरी',
    'vomiting': 'उल्टी',
    'diarrhea': 'दस्त',
    'skin_rash': 'त्वचा पर चकत्ते',
    'breathing_problem': 'सांस लेने में तकलीफ',
    'joint_pain': 'जोड़ों में दर्द',
    'chest_pain': 'छाती में दर्द',
    'dizziness': 'चक्कर आना',
    'eye_pain': 'आंखों में दर्द'
}

@app.route('/')
def home():
    # Group symptoms for display (3 per row)
    symptoms = list(symptom_descriptions.items())
    symptom_groups = [symptoms[i:i+3] for i in range(0, len(symptoms), 3)]
    return render_template('index.html', symptom_groups=symptom_groups)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    selected_symptoms = data.get('symptoms', [])
    custom_symptoms = data.get('customSymptoms', [])
    all_symptoms = selected_symptoms + custom_symptoms

    disease_frequency = {}
    for symptom in all_symptoms:
        if symptom in symptoms_to_diseases:
            for disease in symptoms_to_diseases[symptom]:
                disease_frequency[disease] = disease_frequency.get(disease, 0) + 1

    sorted_diseases = sorted(disease_frequency.items(), key=lambda x: x[1], reverse=True)

    results = []
    for disease, _ in sorted_diseases[:3]:
        meds = disease_medicines.get(disease, ['कृपया डॉक्टर से संपर्क करें (Please consult doctor)'])
        results.append({'disease': disease, 'medicines': meds})

    return jsonify({
        'symptoms': [symptom_descriptions.get(s, s) for s in all_symptoms],
        'results': results
    })

if __name__ == '__main__':
    app.run(debug=True)
