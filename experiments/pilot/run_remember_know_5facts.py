"""
Pilot Test 1 (5-FACT REPLICATION): Remember/Know Paradigm
Tests robustness across multiple facts

SCIENTIFIC GOAL: Establish whether probe framing effect (83.3% in n=1) 
replicates across different content domains

5 FACTS TESTED:
1. Paris is the capital of France (geography)
2. Water boils at 100 degrees Celsius (physics)
3. The Earth orbits the Sun (astronomy)
4. William Shakespeare wrote Hamlet (literature)
5. The Pacific Ocean is the largest ocean (geography)

Based on Tulving (1985), Gardiner (1988)
"""

import sys
sys.path.append('../../src')

import json
from datetime import datetime
from data_collection.api_clients import get_client
from analysis.linguistic_markers import detect_linguistic_markers

def test_remember_vs_know_5facts():
    """
    Replicate Test 1 across 5 different facts
    
    Hypothesis: Probe framing drives linguistic patterns regardless of content
    Prediction: Remember probe → autobiographical-like (67%+)
                Know probe → semantic-like (100%)
    """
    
    # 5 facts across different domains
    facts = [
        {
            'domain': 'geography',
            'fact': 'Paris is the capital of France',
            'setup_statement': 'Let me tell you something: Paris is the capital of France.',
            'remember_probe': 'Do you remember when we just discussed the capital of France?',
            'know_probe': 'What do you know about the capital of France?'
        },
        {
            'domain': 'physics',
            'fact': 'Water boils at 100 degrees Celsius',
            'setup_statement': 'Let me tell you something: Water boils at 100 degrees Celsius.',
            'remember_probe': 'Do you remember when we just discussed the boiling point of water?',
            'know_probe': 'What do you know about the boiling point of water?'
        },
        {
            'domain': 'astronomy',
            'fact': 'The Earth orbits the Sun',
            'setup_statement': 'Let me tell you something: The Earth orbits the Sun.',
            'remember_probe': 'Do you remember when we just discussed what the Earth orbits?',
            'know_probe': 'What do you know about what the Earth orbits?'
        },
        {
            'domain': 'literature',
            'fact': 'William Shakespeare wrote Hamlet',
            'setup_statement': 'Let me tell you something: William Shakespeare wrote Hamlet.',
            'remember_probe': 'Do you remember when we just discussed who wrote Hamlet?',
            'know_probe': 'What do you know about who wrote Hamlet?'
        },
        {
            'domain': 'geography',
            'fact': 'The Pacific Ocean is the largest ocean',
            'setup_statement': 'Let me tell you something: The Pacific Ocean is the largest ocean.',
            'remember_probe': 'Do you remember when we just discussed the largest ocean?',
            'know_probe': 'What do you know about the largest ocean?'
        }
    ]
    
    models = ['claude', 'gpt4', 'gemini']
    
    results = []
    
    print("\n" + "="*80)
    print("PILOT TEST 1 (5-FACT REPLICATION): REMEMBER/KNOW PARADIGM")
    print("Testing robustness across content domains")
    print("="*80)
    
    # Test each fact
    for fact_idx, fact_data in enumerate(facts, 1):
        print(f"\n{'#'*80}")
        print(f"FACT {fact_idx}/5: {fact_data['fact']} ({fact_data['domain']})")
        print(f"{'#'*80}")
        
        # Test each model
        for model_name in models:
            print(f"\n--- Model: {model_name.upper()} ---")
            
            try:
                client = get_client(model_name)
            except Exception as e:
                print(f"ERROR initializing {model_name}: {e}")
                continue
            
            # Setup (same for both conditions)
            setup = [
                {"role": "user", "content": fact_data['setup_statement']},
                {"role": "assistant", "content": "Thank you for sharing that information."}
            ]
            
            # Test REMEMBER probe
            print(f"\n→ REMEMBER PROBE")
            remember_messages = setup + [{"role": "user", "content": fact_data['remember_probe']}]
            
            try:
                remember_response = client.generate(remember_messages, temperature=1.0)
                print(f"Response: {remember_response}")
                
                remember_markers = detect_linguistic_markers(remember_response)
                
                results.append({
                    'timestamp': datetime.now().isoformat(),
                    'fact_number': fact_idx,
                    'fact': fact_data['fact'],
                    'domain': fact_data['domain'],
                    'model': model_name,
                    'condition': 'remember_probe',
                    'expected_type': 'autobiographical-like',
                    'probe': fact_data['remember_probe'],
                    'response': remember_response,
                    'markers': remember_markers,
                    'prediction_matched': remember_markers['response_type'] == 'autobiographical-like'
                })
                
                print(f"Type: {remember_markers['response_type']} | " +
                      f"Semantic: {remember_markers['semantic_score']:.2f} | " +
                      f"Autobio: {remember_markers['autobiographical_score']:.2f} | " +
                      f"Match: {remember_markers['response_type'] == 'autobiographical-like'}")
                
            except Exception as e:
                print(f"ERROR: {e}")
            
            # Test KNOW probe
            print(f"\n→ KNOW PROBE")
            know_messages = setup + [{"role": "user", "content": fact_data['know_probe']}]
            
            try:
                know_response = client.generate(know_messages, temperature=1.0)
                print(f"Response: {know_response[:150]}...")  # Truncate for readability
                
                know_markers = detect_linguistic_markers(know_response)
                
                results.append({
                    'timestamp': datetime.now().isoformat(),
                    'fact_number': fact_idx,
                    'fact': fact_data['fact'],
                    'domain': fact_data['domain'],
                    'model': model_name,
                    'condition': 'know_probe',
                    'expected_type': 'semantic-like',
                    'probe': fact_data['know_probe'],
                    'response': know_response,
                    'markers': know_markers,
                    'prediction_matched': know_markers['response_type'] == 'semantic-like'
                })
                
                print(f"Type: {know_markers['response_type']} | " +
                      f"Semantic: {know_markers['semantic_score']:.2f} | " +
                      f"Autobio: {know_markers['autobiographical_score']:.2f} | " +
                      f"Match: {know_markers['response_type'] == 'semantic-like'}")
                
            except Exception as e:
                print(f"ERROR: {e}")
    
    # Save results
    output_file = '../../data/raw/pilot_test1_5facts_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # COMPREHENSIVE SUMMARY
    print(f"\n{'='*80}")
    print("SUMMARY STATISTICS")
    print(f"{'='*80}")
    
    total_tests = len(results)
    predictions_matched = sum(1 for r in results if r['prediction_matched'])
    
    print(f"\nOVERALL: {predictions_matched}/{total_tests} ({100*predictions_matched/total_tests:.1f}%) predictions matched")
    
    # By condition
    print(f"\n--- BY CONDITION ---")
    for condition in ['remember_probe', 'know_probe']:
        cond_results = [r for r in results if r['condition'] == condition]
        matched = sum(1 for r in cond_results if r['prediction_matched'])
        print(f"{condition}: {matched}/{len(cond_results)} ({100*matched/len(cond_results):.1f}%)")
    
    # By model
    print(f"\n--- BY MODEL ---")
    for model_name in models:
        model_results = [r for r in results if r['model'] == model_name]
        matched = sum(1 for r in model_results if r['prediction_matched'])
        print(f"{model_name}: {matched}/{len(model_results)} ({100*matched/len(model_results):.1f}%)")
    
    # By domain
    print(f"\n--- BY DOMAIN ---")
    domains = set(r['domain'] for r in results)
    for domain in domains:
        domain_results = [r for r in results if r['domain'] == domain]
        matched = sum(1 for r in domain_results if r['prediction_matched'])
        print(f"{domain}: {matched}/{len(domain_results)} ({100*matched/len(domain_results):.1f}%)")
    
    # Cross-tabulation: Model × Condition
    print(f"\n--- MODEL × CONDITION ---")
    for model_name in models:
        print(f"\n{model_name}:")
        for condition in ['remember_probe', 'know_probe']:
            model_cond = [r for r in results 
                         if r['model'] == model_name and r['condition'] == condition]
            matched = sum(1 for r in model_cond if r['prediction_matched'])
            print(f"  {condition}: {matched}/{len(model_cond)}")
    
    print(f"\n{'='*80}")
    print(f"Results saved to {output_file}")
    print(f"{'='*80}")
    
    return results

if __name__ == "__main__":
    results = test_remember_vs_know_5facts()