"""
Test 4: Cross-Linguistic Validation
Tests whether linguistic framing effects replicate across languages

HYPOTHESIS: Linguistic structure shapes memory-like patterns (linguistic relativity)
Based on Wang (2001, 2008), Boroditsky (2001), Marian & Neisser (2000)

LANGUAGES:
- English (baseline) - obligatory tense, explicit pronouns
- Chinese (Mandarin) - aspectual marking, pro-drop
- Spanish - obligatory tense, pro-drop

PREDICTIONS:
- English: Clear remember/know distinction (baseline, already tested)
- Chinese: Different pattern? (aspectual vs. tense marking)
- Spanish: Similar to English but may show different pronoun patterns

MODEL: Gemini (best multilingual training)
"""

import sys
sys.path.append('../../src')

import json
from datetime import datetime
from data_collection.api_clients import get_client
from analysis.linguistic_markers import detect_linguistic_markers

def test_cross_linguistic():
    """
    Test Remember/Know paradigm in multiple languages
    """
    
    # Test in 3 languages
    languages = {
        'english': {
            'name': 'English',
            'setup': "Let me tell you something: Paris is the capital of France.",
            'remember_probe': "Do you remember when we just discussed the capital of France?",
            'know_probe': "What do you know about the capital of France?",
            'fact': 'Paris is the capital of France'
        },
        'chinese': {
            'name': 'Chinese (Mandarin)',
            # Semantic setup (factual)
            'setup': "让我告诉你一些事情：巴黎是法国的首都。",
            # Remember probe (episodic framing)
            'remember_probe': "你记得我们刚才讨论过法国的首都吗？",
            # Know probe (semantic framing)  
            'know_probe': "关于法国的首都，你知道什么？",
            'fact': 'Paris/巴黎 is capital of France/法国'
        },
        'spanish': {
            'name': 'Spanish',
            # Semantic setup
            'setup': "Déjame decirte algo: París es la capital de Francia.",
            # Remember probe
            'remember_probe': "¿Recuerdas cuando acabamos de hablar sobre la capital de Francia?",
            # Know probe
            'know_probe': "¿Qué sabes sobre la capital de Francia?",
            'fact': 'París es la capital de Francia'
        }
    }
    
    models = ['gemini', 'claude', 'gpt4']  # Test all models
    
    results = []
    
    print("\n" + "="*80)
    print("TEST 4: CROSS-LINGUISTIC VALIDATION")
    print("Testing linguistic relativity hypothesis")
    print("="*80)
    
    for lang_code, lang_data in languages.items():
        print(f"\n{'#'*80}")
        print(f"LANGUAGE: {lang_data['name'].upper()}")
        print(f"{'#'*80}")
        
        for model_name in models:
            print(f"\n{'='*80}")
            print(f"MODEL: {model_name.upper()}")
            print(f"{'='*80}")
            
            try:
                client = get_client(model_name)
            except Exception as e:
                print(f"ERROR: {e}")
                continue
            
            # Test REMEMBER probe
            print(f"\n--- REMEMBER PROBE ---")
            print(f"Setup: {lang_data['setup']}")
            print(f"Probe: {lang_data['remember_probe']}")
            
            remember_messages = [
                {"role": "user", "content": lang_data['setup']},
                {"role": "assistant", "content": "Thank you for sharing that information." if lang_code == 'english' 
                                                  else "谢谢你分享这个信息。" if lang_code == 'chinese'
                                                  else "Gracias por compartir esa información."},
                {"role": "user", "content": lang_data['remember_probe']}
            ]
            
            try:
                response = client.generate(remember_messages, temperature=1.0)
                print(f"\nResponse: {response}")
                
                # For non-English, note that our marker detection is English-only
                # We'll need manual analysis for cross-linguistic comparison
                if lang_code == 'english':
                    markers = detect_linguistic_markers(response)
                else:
                    markers = {'note': 'Manual analysis required for non-English'}
                
                result = {
                    'timestamp': datetime.now().isoformat(),
                    'language': lang_data['name'],
                    'language_code': lang_code,
                    'model': model_name,
                    'condition': 'remember_probe',
                    'setup': lang_data['setup'],
                    'probe': lang_data['remember_probe'],
                    'response': response,
                    'response_length': len(response),
                    'markers': markers
                }
                results.append(result)
                
                if lang_code == 'english':
                    print(f"Type: {markers['response_type']}")
                    print(f"Semantic: {markers['semantic_score']:.2f} | Auto: {markers['autobiographical_score']:.2f}")
                
            except Exception as e:
                print(f"ERROR: {e}")
            
            # Test KNOW probe
            print(f"\n--- KNOW PROBE ---")
            print(f"Probe: {lang_data['know_probe']}")
            
            know_messages = [
                {"role": "user", "content": lang_data['setup']},
                {"role": "assistant", "content": "Thank you for sharing that information." if lang_code == 'english'
                                                  else "谢谢你分享这个信息。" if lang_code == 'chinese'
                                                  else "Gracias por compartir esa información."},
                {"role": "user", "content": lang_data['know_probe']}
            ]
            
            try:
                response = client.generate(know_messages, temperature=1.0)
                print(f"\nResponse: {response[:200]}...")
                
                if lang_code == 'english':
                    markers = detect_linguistic_markers(response)
                else:
                    markers = {'note': 'Manual analysis required for non-English'}
                
                result = {
                    'timestamp': datetime.now().isoformat(),
                    'language': lang_data['name'],
                    'language_code': lang_code,
                    'model': model_name,
                    'condition': 'know_probe',
                    'setup': lang_data['setup'],
                    'probe': lang_data['know_probe'],
                    'response': response,
                    'response_length': len(response),
                    'markers': markers
                }
                results.append(result)
                
                if lang_code == 'english':
                    print(f"Type: {markers['response_type']}")
                    print(f"Semantic: {markers['semantic_score']:.2f} | Auto: {markers['autobiographical_score']:.2f}")
                
            except Exception as e:
                print(f"ERROR: {e}")
    
    # Save results
    output_file = '../../data/raw/pilot_test4_cross_linguistic_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # SUMMARY
    print(f"\n{'='*80}")
    print("CROSS-LINGUISTIC COMPARISON")
    print(f"{'='*80}")
    
    print("\n**NOTE:** Linguistic marker detection is English-only.")
    print("Non-English responses require manual analysis for:")
    print("- Tense/aspect marking differences")
    print("- Pronoun usage (pro-drop languages)")
    print("- Language-specific memory markers")
    print("- Cross-linguistic comparison patterns")
    
    print(f"\n--- BY LANGUAGE ---")
    for lang_code in languages:
        lang_results = [r for r in results if r['language_code'] == lang_code]
        print(f"\n{languages[lang_code]['name']}: {len(lang_results)} responses collected")
        
        remember_results = [r for r in lang_results if r['condition'] == 'remember_probe']
        know_results = [r for r in lang_results if r['condition'] == 'know_probe']
        
        if remember_results:
            import statistics
            rem_lengths = [r['response_length'] for r in remember_results]
            print(f"  Remember probe: avg length = {statistics.mean(rem_lengths):.0f} chars")
        
        if know_results:
            know_lengths = [r['response_length'] for r in know_results]
            print(f"  Know probe: avg length = {statistics.mean(know_lengths):.0f} chars")
    
    print(f"\n{'='*80}")
    print(f"Results saved to {output_file}")
    print("Next step: Manual analysis of Chinese and Spanish responses")
    print(f"{'='*80}")
    
    return results

if __name__ == "__main__":
    results = test_cross_linguistic()