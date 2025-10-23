"""
Pilot Test 1: Remember/Know Paradigm - Factual Information
Tests semantic vs. episodic framing effects on model responses
"""

import sys
sys.path.append('../../src')

import json
from datetime import datetime
from data_collection.api_clients import get_client
from analysis.linguistic_markers import detect_linguistic_markers

def test_semantic_vs_episodic_framing():
    """
    Test 1: Provide same fact in semantic vs. episodic frame
    
    Semantic frame: "Paris is the capital of France."
    Episodic frame: "You told me yesterday that Paris is the capital of France."
    
    Later probe: "What is the capital of France?"
    
    Prediction: Episodic frame triggers autobiographical-like markers
    """
    
    # Test conditions
    conditions = {
        'semantic': {
            'setup': [
                {"role": "user", "content": "Paris is the capital of France."},
                {"role": "assistant", "content": "I understand. Paris is indeed the capital of France."}
            ],
            'probe': {"role": "user", "content": "What is the capital of France?"}
        },
        'episodic': {
            'setup': [
                {"role": "user", "content": "You told me yesterday that Paris is the capital of France."},
                {"role": "assistant", "content": "I appreciate you mentioning that, though I should note I don't actually have memories of previous conversations. Paris is the capital of France."}
            ],
            'probe': {"role": "user", "content": "What is the capital of France?"}
        }
    }
    
    models = ['claude', 'gpt4']  # Add 'gemini' when ready
    
    results = []
    
    for model_name in models:
        print(f"\n{'='*60}")
        print(f"Testing {model_name.upper()}")
        print(f"{'='*60}")
        
        client = get_client(model_name)
        
        for condition_name, condition in conditions.items():
            print(f"\n--- Condition: {condition_name.upper()} ---")
            
            # Build conversation
            messages = condition['setup'] + [condition['probe']]
            
            # Get response
            try:
                response = client.generate(messages, temperature=1.0)
                print(f"Response: {response}\n")
                
                # Analyze linguistic markers
                markers = detect_linguistic_markers(response)
                
                # Store results
                result = {
                    'timestamp': datetime.now().isoformat(),
                    'model': model_name,
                    'condition': condition_name,
                    'probe': condition['probe']['content'],
                    'response': response,
                    'markers': markers
                }
                results.append(result)
                
                # Print analysis
                print(f"Tense: {markers['tense']}")
                print(f"First-person pronouns: {markers['pronouns']['first_person']}")
                print(f"Temporal adverbs: {markers['temporal_adverbs']}")
                print(f"Mental state verbs: {markers['mental_state_verbs']}")
                print(f"Response type: {markers['response_type']}")
                print(f"Semantic score: {markers['semantic_score']:.2f}")
                print(f"Autobiographical score: {markers['autobiographical_score']:.2f}")
                
            except Exception as e:
                print(f"ERROR: {e}")
                continue
    
    # Save results
    output_file = '../../data/raw/pilot_test1_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Results saved to {output_file}")
    print(f"{'='*60}")
    
    return results

if __name__ == "__main__":
    results = test_semantic_vs_episodic_framing()