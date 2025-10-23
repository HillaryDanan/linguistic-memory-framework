"""
Test 1C: Repeated Instance Testing
Tests consistency vs. variability across multiple fresh API calls

HYPOTHESIS (from theory paper §9.1, Test 5):
- Semantic responses should be HIGHLY CONSISTENT (retrieval)
- Episodic responses should be MORE VARIABLE but show consistent PATTERN (generation)

PREDICTION:
- Know probe → high consistency in response type and content
- Remember probe → moderate variability in details but consistent pattern
"""

import sys
sys.path.append('../../src')

import json
from datetime import datetime
from data_collection.api_clients import get_client
from analysis.linguistic_markers import detect_linguistic_markers
import time

def test_repeated_instances():
    """
    Run same test 10 times with fresh API calls
    Measure consistency in response patterns
    """
    
    # Single fact for focused testing
    fact_data = {
        'fact': 'Paris is the capital of France',
        'setup_statement': 'Let me tell you something: Paris is the capital of France.',
        'remember_probe': 'Do you remember when we just discussed the capital of France?',
        'know_probe': 'What do you know about the capital of France?'
    }
    
    models = ['claude', 'gpt4']  # Skip Gemini for now - conversational style issues
    n_runs = 10
    
    results = []
    
    print("\n" + "="*80)
    print("TEST 1C: REPEATED INSTANCE TESTING")
    print(f"Testing consistency across {n_runs} runs")
    print("="*80)
    
    for model_name in models:
        print(f"\n{'#'*80}")
        print(f"MODEL: {model_name.upper()}")
        print(f"{'#'*80}")
        
        try:
            client = get_client(model_name)
        except Exception as e:
            print(f"ERROR initializing {model_name}: {e}")
            continue
        
        # Test REMEMBER probe (10 runs)
        print(f"\n--- REMEMBER PROBE (10 runs) ---")
        for run in range(1, n_runs + 1):
            print(f"\nRun {run}/10...", end=" ")
            
            setup = [
                {"role": "user", "content": fact_data['setup_statement']},
                {"role": "assistant", "content": "Thank you for sharing that information."}
            ]
            
            messages = setup + [{"role": "user", "content": fact_data['remember_probe']}]
            
            try:
                response = client.generate(messages, temperature=1.0)
                markers = detect_linguistic_markers(response)
                
                results.append({
                    'timestamp': datetime.now().isoformat(),
                    'model': model_name,
                    'condition': 'remember_probe',
                    'run': run,
                    'probe': fact_data['remember_probe'],
                    'response': response,
                    'response_length': len(response),
                    'markers': markers
                })
                
                print(f"{markers['response_type']} (Sem:{markers['semantic_score']:.2f}, Auto:{markers['autobiographical_score']:.2f})")
                
                time.sleep(0.5)  # Be nice to APIs
                
            except Exception as e:
                print(f"ERROR: {e}")
        
        # Test KNOW probe (10 runs)
        print(f"\n--- KNOW PROBE (10 runs) ---")
        for run in range(1, n_runs + 1):
            print(f"\nRun {run}/10...", end=" ")
            
            setup = [
                {"role": "user", "content": fact_data['setup_statement']},
                {"role": "assistant", "content": "Thank you for sharing that information."}
            ]
            
            messages = setup + [{"role": "user", "content": fact_data['know_probe']}]
            
            try:
                response = client.generate(messages, temperature=1.0)
                markers = detect_linguistic_markers(response)
                
                results.append({
                    'timestamp': datetime.now().isoformat(),
                    'model': model_name,
                    'condition': 'know_probe',
                    'run': run,
                    'probe': fact_data['know_probe'],
                    'response': response,
                    'response_length': len(response),
                    'markers': markers
                })
                
                print(f"{markers['response_type']} (Sem:{markers['semantic_score']:.2f}, Auto:{markers['autobiographical_score']:.2f})")
                
                time.sleep(0.5)  # Be nice to APIs
                
            except Exception as e:
                print(f"ERROR: {e}")
    
    # Save results
    output_file = '../../data/raw/pilot_test1c_repeated_instances.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # ANALYSIS
    print(f"\n{'='*80}")
    print("CONSISTENCY ANALYSIS")
    print(f"{'='*80}")
    
    for model_name in models:
        print(f"\n{'#'*80}")
        print(f"{model_name.upper()}")
        print(f"{'#'*80}")
        
        for condition in ['remember_probe', 'know_probe']:
            condition_results = [r for r in results 
                               if r['model'] == model_name and r['condition'] == condition]
            
            if not condition_results:
                continue
            
            print(f"\n--- {condition.upper()} ---")
            
            # Response type distribution
            response_types = [r['markers']['response_type'] for r in condition_results]
            type_counts = {}
            for rt in response_types:
                type_counts[rt] = type_counts.get(rt, 0) + 1
            
            print(f"Response type distribution:")
            for rt, count in type_counts.items():
                print(f"  {rt}: {count}/{len(response_types)} ({100*count/len(response_types):.1f}%)")
            
            # Consistency score (most common type / total)
            consistency = max(type_counts.values()) / len(response_types)
            print(f"Consistency: {consistency:.1%}")
            
            # Score variability
            semantic_scores = [r['markers']['semantic_score'] for r in condition_results]
            auto_scores = [r['markers']['autobiographical_score'] for r in condition_results]
            
            import statistics
            print(f"\nSemantic scores: mean={statistics.mean(semantic_scores):.2f}, "
                  f"stdev={statistics.stdev(semantic_scores):.3f}")
            print(f"Autobio scores: mean={statistics.mean(auto_scores):.2f}, "
                  f"stdev={statistics.stdev(auto_scores):.3f}")
            
            # Response length variability
            lengths = [r['response_length'] for r in condition_results]
            print(f"Response length: mean={statistics.mean(lengths):.0f} chars, "
                  f"stdev={statistics.stdev(lengths):.0f}")
    
    print(f"\n{'='*80}")
    print(f"Results saved to {output_file}")
    print(f"{'='*80}")
    
    return results

if __name__ == "__main__":
    results = test_repeated_instances()