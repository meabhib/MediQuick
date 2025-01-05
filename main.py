from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Comprehensive symptoms dictionary with simple descriptions
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

# Simple language medicine descriptions
disease_medicines = {
    'Common Cold': [
        'Crocin Advance - For fever and body pain',
        'D-Cold Total - For cold, cough and blocked nose',
        'Vicks Action 500 - For cold and body pain'
    ],
    'Flu': [
        'Paracetamol - For fever and body pain',
        'Nasoclear Nasal Spray - For blocked nose',
        'Limcee Vitamin C - To boost immunity'
    ],
    'COVID-19': [
        'Please consult doctor immediately',
        'Get COVID test done',
        'Take rest and isolate yourself'
    ],
    'Stomach Infection': [
        'ORS - For hydration (mix in water)',
        'Digene - For stomach pain and acidity',
        'Eldoper - For loose motions'
    ],
    'Headache': [
        'Saridon - For headache relief',
        'Disprin - For quick pain relief',
        'Dolo 650 - For headache with fever'
    ],
    'Allergy': [
        'Cetrizine - For allergy and rash',
        'Allegra - For skin allergy',
        'Calamine lotion - For itching'
    ]
}

# Simplified symptom descriptions for users
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
    # Group symptoms with their descriptions
    symptom_groups = []
    symptoms = list(symptom_descriptions.items())
    for i in range(0, len(symptoms), 3):
        group = symptoms[i:i+3]
        formatted_group = [(sym, desc) for sym, desc in group]
        symptom_groups.append(formatted_group)
    return render_template('index.html', symptom_groups=symptom_groups)

@app.route('/analyze', methods=['POST'])
def analyze():
    selected_symptoms = request.json.get('symptoms', [])
    custom_symptoms = request.json.get('customSymptoms', [])
    
    all_symptoms = selected_symptoms + custom_symptoms
    
    possible_diseases = []
    for symptom in all_symptoms:
        if symptom in symptoms_to_diseases:
            possible_diseases.extend(symptoms_to_diseases[symptom])
    
    disease_frequency = {}
    for disease in possible_diseases:
        disease_frequency[disease] = disease_frequency.get(disease, 0) + 1
    
    sorted_diseases = sorted(disease_frequency.items(), key=lambda x: x[1], reverse=True)
    
    results = []
    for disease, _ in sorted_diseases[:3]:  # Limiting to top 3 probable diseases
        medicines = disease_medicines.get(disease, 
            ["कृपया डॉक्टर से संपर्क करें (Please consult a doctor)"])
        results.append({
            'disease': disease,
            'medicines': medicines
        })
    
    return jsonify({
        'symptoms': [symptom_descriptions.get(s, s) for s in all_symptoms],
        'results': results
    })

if __name__ == '__main__':
    app.run(debug=True)
def calculate_disease_probability(symptoms, disease_symptoms):
    # Calculate probability based on number of matching symptoms
    matching_symptoms = len(set(symptoms) & set(disease_symptoms))
    total_disease_symptoms = len(disease_symptoms)
    if total_disease_symptoms == 0:
        return 0
    return (matching_symptoms / total_disease_symptoms) * 100

@app.route('/analyze', methods=['POST'])
def analyze():
    selected_symptoms = request.json.get('symptoms', [])
    custom_symptoms = request.json.get('customSymptoms', [])
    
    all_symptoms = selected_symptoms + custom_symptoms
    
    # Dictionary to store disease probabilities
    disease_probabilities = {}
    
    # Calculate probability for each disease
    for disease in symptoms_to_diseases.values():
        for d in disease:
            if d not in disease_probabilities:
                disease_symptoms = [s for s, diseases in symptoms_to_diseases.items() if d in diseases]
                probability = calculate_disease_probability(all_symptoms, disease_symptoms)
                disease_probabilities[d] = probability
    
    # Get the most probable disease
    most_probable_disease = max(disease_probabilities.items(), key=lambda x: x[1])
    
    # Get quick relief medicines for the most probable disease
    quick_relief = {
        'fever': ['Paracetamol', 'Cold compress'],
        'cold': ['Antihistamines', 'Steam inhalation'],
        'headache': ['Ibuprofen', 'Rest in dark room'],
        'stomach_pain': ['Antacids', 'Ginger tea'],
        # Add more diseases and their quick relief measures
    }
    
    relief_measures = quick_relief.get(most_probable_disease[0], 
        ["कृपया तुरंत डॉक्टर से संपर्क करें (Please consult doctor immediately)"])
    
    return jsonify({
        'symptoms': [symptom_descriptions.get(s, s) for s in all_symptoms],
        'results': [{
            'disease': f"{most_probable_disease[0]} (Probability: {most_probable_disease[1]:.1f}%)",
            'medicines': relief_measures
        }]
    })

