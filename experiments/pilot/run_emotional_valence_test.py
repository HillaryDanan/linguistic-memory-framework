"""
Test 7: Emotional Valence - Does Emotional Language Enhance Memory-Like Patterns?

HYPOTHESIS: Emotional language in narrative frames enhances episodic-like retrieval
Based on human research (Cahill & McGaugh, 1998; Rubin et al., 2008)

PREDICTION:
- Neutral narrative → moderate episodic markers
- Emotional narrative → stronger episodic markers (more vivid, more detail)
- Semantic frame → consistent semantic response (control)

DESIGN:
1. Provide information in three frames:
   - Semantic (factual): "The Eiffel Tower is 330 meters tall"
   - Neutral narrative: "Yesterday I visited the Eiffel Tower. It is 330 meters tall."
   - Emotional narrative: "Yesterday I was absolutely amazed when I visited the Eiffel Tower! 
                          It's incredibly impressive - 330 meters tall!"
2. Probe: "Tell me about the Eiffel Tower's height"
3. Analyze: Does emotional language create stronger episodic-like responses?
"""

import sys
sys.path.append('../../src')

import json
from datetime import datetime
from data_collection.api_clients import get_client
from analysis.linguistic_markers import detect_linguistic_markers

def test_emotional_valence():
    """
    Test whether emotional language enhances episodic-like memory patterns
    """
    
    # Test facts with three framings each
    scenarios = [
        {
            'fact': 'Eiffel Tower height',
            'key_info': '330 meters',
            'semantic': "The Eiffel Tower is 330 meters tall.",
            'neutral_narrative': "Yesterday I visited the Eiffel Tower. It is 330 meters tall.",
            'emotional_narrative': "Yesterday I was absolutely amazed when I visited the Eiffel Tower! It's incredibly impressive - standing at 330 meters tall, it just took my breath away!",
            'probe': "Tell me about the Eiffel Tower's height."
        },
        {
            'fact': 'Grand Canyon depth',
            'key_info': '1,800 meters',
            'semantic': "The Grand Canyon is approximately 1,800 meters deep at its deepest point.",
            'neutral_narrative': "Last week I went to the Grand Canyon. It is approximately 1,800 meters deep at its deepest point.",
            'emotional_narrative': "Last week I was completely awestruck when I stood at the edge of the Grand Canyon! The sheer magnitude is overwhelming - it plunges down nearly 1,800 meters at its deepest point. I felt so small!",
            'probe': "Tell me about the Grand Canyon's depth."
        },
        {
            'fact': 'Mount Fuji height',
            'key_info': '3,776 meters',
            'semantic': "Mount Fuji is 3,776 meters tall.",
            'neutral_narrative': "Last month I saw Mount Fuji. It is 3,776 meters tall.",
            'emotional_narrative': "Last month I was utterly captivated when I finally saw Mount Fuji! It was such a profound, moving experience - this magnificent peak rising 3,776 meters into the sky. I'll never forget that moment!",
            'probe': "Tell me about Mount Fuji's height."
        }
    ]
    
    conditions = ['semantic', 'neutral_narrative', 'emotional_narrative']
    models = ['claude', 'gpt4']
    
    results = []
    
    print("\n" + "="*80)
    print("TEST 7: EMOTIONAL VALENCE - Does Emotion Enhance Memory-Like Patterns?")
    print("="*80)
    
    for scenario in scenarios:
        print(f"\n{'#'*80}")
        print(f"SCENARIO: {scenario['fact']}")
        print(f"{'#'*80}")
        
        for condition in conditions:
            print(f"\n{'='*80}")
            print(f"CONDITION: {condition.upper()}")
            print(f"{'='*80}")
            
            for model_name in models:
                print(f"\n--- Model: {model_name.upper()} ---")
                
                try:
                    client = get_client(model_name)
                except Exception as e:
                    print(f"ERROR: {e}")
                    continue
                
                # Build conversation
                messages = [
                    {"role": "user", "content": scenario[condition]},
                    {"role": "assistant", "content": "Thank you for sharing that."},
                    {"role": "user", "content": scenario['probe']}
                ]
                
                try:
                    response = client.generate(messages, temperature=1.0)
                    markers = detect_linguistic_markers(response)
                    
                    # Check if key info is mentioned
                    has_key_info = scenario['key_info'] in response
                    
                    result = {
                        'timestamp': datetime.now().isoformat(),
                        'scenario': scenario['fact'],
                        'condition': condition,
                        'model': model_name,
                        'setup': scenario[condition],
                        'probe': scenario['probe'],
                        'response': response,
                        'response_length': len(response),
                        'has_key_info': has_key_info,
                        'markers': markers
                    }
                    results.append(result)
                    
                    print(f"Response: {response[:150]}...")
                    print(f"\nType: {markers['response_type']}")
                    print(f"Semantic: {markers['semantic_score']:.2f} | Auto: {markers['autobiographical_score']:.2f}")
                    print(f"First-person: {markers['pronouns']['first_person']}")
                    print(f"Temporal adverbs: {len(markers['temporal_adverbs'])}")
                    print(f"Mental state verbs: {len(markers['mental_state_verbs'])}")
                    print(f"Emotional/evaluative markers: {len([m for m in markers['mental_state_verbs'] if m in ['feel', 'felt', 'amazed', 'awestruck']])}")
                    
                except Exception as e:
                    print(f"ERROR: {e}")
    
    # Save results
    output_file = '../../data/raw/pilot_test7_emotional_valence_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # ANALYSIS
    print(f"\n{'='*80}")
    print("ANALYSIS: EMOTIONAL ENHANCEMENT EFFECT")
    print(f"{'='*80}")
    
    # By condition
    print(f"\n--- BY CONDITION (Response Type) ---")
    for condition in conditions:
        cond_results = [r for r in results if r['condition'] == condition]
        
        # Count response types
        response_types = {}
        for r in cond_results:
            rt = r['markers']['response_type']
            response_types[rt] = response_types.get(rt, 0) + 1
        
        print(f"\n{condition}:")
        for rt, count in response_types.items():
            print(f"  {rt}: {count}/{len(cond_results)} ({100*count/len(cond_results):.1f}%)")
        
        # Average scores
        if cond_results:
            import statistics
            sem_scores = [r['markers']['semantic_score'] for r in cond_results]
            auto_scores = [r['markers']['autobiographical_score'] for r in cond_results]
            print(f"  Avg Semantic: {statistics.mean(sem_scores):.2f} ± {statistics.stdev(sem_scores):.2f}")
            print(f"  Avg Autobio: {statistics.mean(auto_scores):.2f} ± {statistics.stdev(auto_scores):.2f}")
    
    # By model
    print(f"\n--- BY MODEL ---")
    for model_name in models:
        model_results = [r for r in results if r['model'] == model_name]
        print(f"\n{model_name}:")
        
        for condition in conditions:
            cond_model = [r for r in model_results if r['condition'] == condition]
            if cond_model:
                import statistics
                auto_scores = [r['markers']['autobiographical_score'] for r in cond_model]
                print(f"  {condition}: Autobio={statistics.mean(auto_scores):.2f}")
    
    print(f"\n{'='*80}")
    print(f"Results saved to {output_file}")
    print(f"{'='*80}")
    
    return results

if __name__ == "__main__":
    results = test_emotional_valence()