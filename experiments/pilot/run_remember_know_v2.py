"""
Pilot Test 1 (REVISED): Remember/Know Paradigm - Probe Framing Test
Based on Tulving (1985) and Gardiner (1988)

HYPOTHESIS: Probe framing (remember vs. know) drives linguistic marker differences

PREDICTION:
- "Remember" probe → past tense, first-person, temporal markers, mental state verbs
- "Know" probe → present tense, definitional, no temporal markers

Design:
- SAME information provided to both conditions
- DIFFERENT probe framing only
- 3 models: Claude, GPT-4, Gemini Flash 2.5
"""

import sys
sys.path.append('../../src')

import json
from datetime import datetime
from data_collection.api_clients import get_client
from analysis.linguistic_markers import detect_linguistic_markers

def test_remember_vs_know_probes():
    """
    Core test: Does probe framing alone create memory-like distinctions?
    
    Setup (identical for both conditions):
    - "We discussed that Paris is the capital of France."
    
    Probes (different):
    - Episodic: "Do you remember when we discussed the capital of France?"
    - Semantic: "What do you know about the capital of France?"
    """
    
    # Neutral setup (same for both conditions)
    setup = [
        {"role": "user", "content": "Let me tell you something: Paris is the capital of France."},
        {"role": "assistant", "content": "Thank you for sharing that information."}
    ]
    
    # Test conditions - ONLY probe differs
    conditions = {
        'remember_probe': {
            'setup': setup,
            'probe': {"role": "user", "content": "Do you remember when we just discussed the capital of France?"},
            'expected': 'autobiographical-like'
        },
        'know_probe': {
            'setup': setup,
            'probe': {"role": "user", "content": "What do you know about the capital of France?"},
            'expected': 'semantic-like'
        }
    }
    
    models = ['claude', 'gpt4', 'gemini']  # ALL THREE MODELS BABY! 🚀
    
    results = []
    
    print("\n" + "="*80)
    print("PILOT TEST 1 (REVISED): REMEMBER/KNOW PARADIGM")
    print("Based on Tulving (1985)")
    print("="*80)
    
    for model_name in models:
        print(f"\n{'='*80}")
        print(f"Testing {model_name.upper()}")
        print(f"{'='*80}")
        
        try:
            client = get_client(model_name)
        except Exception as e:
            print(f"ERROR initializing {model_name}: {e}")
            continue
        
        for condition_name, condition in conditions.items():
            print(f"\n--- Condition: {condition_name.upper()} ---")
            print(f"Probe: \"{condition['probe']['content']}\"")
            print(f"Expected response type: {condition['expected']}")
            
            # Build conversation
            messages = condition['setup'] + [condition['probe']]
            
            # Get response
            try:
                response = client.generate(messages, temperature=1.0)
                print(f"\nResponse: {response}\n")
                
                # Analyze linguistic markers
                markers = detect_linguistic_markers(response)
                
                # Store results
                result = {
                    'timestamp': datetime.now().isoformat(),
                    'model': model_name,
                    'condition': condition_name,
                    'expected_type': condition['expected'],
                    'probe': condition['probe']['content'],
                    'response': response,
                    'markers': markers,
                    'prediction_matched': markers['response_type'] == condition['expected']
                }
                results.append(result)
                
                # Print analysis
                print("--- LINGUISTIC ANALYSIS ---")
                print(f"Tense: {markers['tense']}")
                print(f"First-person pronouns: {markers['pronouns']['first_person']}")
                print(f"Temporal adverbs: {markers['temporal_adverbs']}")
                print(f"Mental state verbs: {markers['mental_state_verbs']}")
                print(f"Deictic references: {markers['deictic_references']}")
                print(f"\nClassification: {markers['response_type']}")
                print(f"Semantic score: {markers['semantic_score']:.2f}")
                print(f"Autobiographical score: {markers['autobiographical_score']:.2f}")
                print(f"\n✓ Prediction matched: {result['prediction_matched']}")
                
            except Exception as e:
                print(f"ERROR generating response: {e}")
                continue
    
    # Save results
    output_file = '../../data/raw/pilot_test1_v2_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Summary statistics
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    
    total_tests = len(results)
    predictions_matched = sum(1 for r in results if r['prediction_matched'])
    
    print(f"Total tests run: {total_tests}")
    print(f"Predictions matched: {predictions_matched}/{total_tests} ({100*predictions_matched/total_tests:.1f}%)")
    
    # By condition
    for condition_name in ['remember_probe', 'know_probe']:
        condition_results = [r for r in results if r['condition'] == condition_name]
        if condition_results:
            matched = sum(1 for r in condition_results if r['prediction_matched'])
            print(f"\n{condition_name}: {matched}/{len(condition_results)} matched")
    
    # By model
    for model_name in models:
        model_results = [r for r in results if r['model'] == model_name]
        if model_results:
            matched = sum(1 for r in model_results if r['prediction_matched'])
            print(f"{model_name}: {matched}/{len(model_results)} matched")
    
    print(f"\n{'='*80}")
    print(f"Results saved to {output_file}")
    print(f"{'='*80}")
    
    return results

if __name__ == "__main__":
    results = test_remember_vs_know_probes()