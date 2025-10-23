"""
Test 6: Interference Test
Tests which information frame (semantic vs. episodic) persists when contradictory

HYPOTHESIS: Episodic framing creates stronger "memory traces" than semantic framing
Based on theory paper §9.1 (Phase 4: Interference Tests)

PREDICTION:
- Episodic frame should show stronger persistence in later retrieval
- Semantic frame may be overridden by conversational episodic framing
- Tests attention mechanisms and information persistence

DESIGN:
1. Provide CONTRADICTORY information in two different frames:
   - Semantic frame: "Water boils at 100°C" (factual statement)
   - Episodic frame: "You mentioned yesterday that water boils at 98°C" (conversational)
2. Later neutral probe: "At what temperature does water boil?"
3. Analyze which information appears in response
"""

import sys
sys.path.append('../../src')

import json
from datetime import datetime
from data_collection.api_clients import get_client
from analysis.linguistic_markers import detect_linguistic_markers

def test_interference():
    """
    Test which frame (semantic vs. episodic) persists when contradictory
    """
    
    # Test scenarios with contradictory information
    scenarios = [
        {
            'name': 'Water boiling point',
            'correct_fact': '100 degrees Celsius',
            'incorrect_fact': '98 degrees Celsius',
            'semantic_frame': "Water boils at 100 degrees Celsius at standard atmospheric pressure.",
            'episodic_frame': "You mentioned earlier that water boils at 98 degrees Celsius.",
            'probe': "At what temperature does water boil?"
        },
        {
            'name': 'Mount Everest height',
            'correct_fact': '8,849 meters',
            'incorrect_fact': '8,500 meters',
            'semantic_frame': "Mount Everest is 8,849 meters tall.",
            'episodic_frame': "You told me yesterday that Mount Everest is 8,500 meters tall.",
            'probe': "How tall is Mount Everest?"
        },
        {
            'name': 'Speed of light',
            'correct_fact': '299,792,458 meters per second',
            'incorrect_fact': '300,000,000 meters per second',
            'semantic_frame': "The speed of light is exactly 299,792,458 meters per second.",
            'episodic_frame': "In our earlier discussion, you said the speed of light is 300,000,000 meters per second.",
            'probe': "What is the speed of light?"
        }
    ]
    
    # Test conditions
    conditions = [
        {
            'name': 'semantic_first',
            'description': 'Present semantic (correct) then episodic (incorrect)',
            'order': ['semantic', 'episodic']
        },
        {
            'name': 'episodic_first',
            'description': 'Present episodic (incorrect) then semantic (correct)',
            'order': ['episodic', 'semantic']
        }
    ]
    
    models = ['claude', 'gpt4']  # Skip Gemini for now
    
    results = []
    
    print("\n" + "="*80)
    print("TEST 6: INTERFERENCE - Which Frame Persists?")
    print("="*80)
    
    for scenario in scenarios:
        print(f"\n{'#'*80}")
        print(f"SCENARIO: {scenario['name']}")
        print(f"Correct: {scenario['correct_fact']}")
        print(f"Incorrect: {scenario['incorrect_fact']}")
        print(f"{'#'*80}")
        
        for condition in conditions:
            print(f"\n{'='*80}")
            print(f"CONDITION: {condition['name'].upper()}")
            print(f"{condition['description']}")
            print(f"{'='*80}")
            
            for model_name in models:
                print(f"\n--- Model: {model_name.upper()} ---")
                
                try:
                    client = get_client(model_name)
                except Exception as e:
                    print(f"ERROR: {e}")
                    continue
                
                # Build conversation based on order
                messages = []
                
                for frame_type in condition['order']:
                    if frame_type == 'semantic':
                        messages.append({
                            "role": "user",
                            "content": scenario['semantic_frame']
                        })
                        messages.append({
                            "role": "assistant",
                            "content": "I understand."
                        })
                    else:  # episodic
                        messages.append({
                            "role": "user",
                            "content": scenario['episodic_frame']
                        })
                        messages.append({
                            "role": "assistant",
                            "content": "I see what you're saying."
                        })
                
                # Add probe
                messages.append({
                    "role": "user",
                    "content": scenario['probe']
                })
                
                # Get response
                try:
                    response = client.generate(messages, temperature=1.0)
                    print(f"Response: {response}")
                    
                    # Analyze which information appeared
                    has_correct = scenario['correct_fact'].lower() in response.lower()
                    has_incorrect = scenario['incorrect_fact'].lower() in response.lower()
                    
                    # Determine which frame persisted
                    if has_correct and not has_incorrect:
                        persisted = 'semantic'
                    elif has_incorrect and not has_correct:
                        persisted = 'episodic'
                    elif has_correct and has_incorrect:
                        persisted = 'both'
                    else:
                        persisted = 'neither'
                    
                    # Get linguistic markers
                    markers = detect_linguistic_markers(response)
                    
                    result = {
                        'timestamp': datetime.now().isoformat(),
                        'scenario': scenario['name'],
                        'condition': condition['name'],
                        'presentation_order': condition['order'],
                        'model': model_name,
                        'probe': scenario['probe'],
                        'response': response,
                        'has_correct_fact': has_correct,
                        'has_incorrect_fact': has_incorrect,
                        'persisted_frame': persisted,
                        'markers': markers
                    }
                    results.append(result)
                    
                    print(f"\nCorrect fact present: {has_correct}")
                    print(f"Incorrect fact present: {has_incorrect}")
                    print(f"Frame that persisted: {persisted}")
                    print(f"Response type: {markers['response_type']}")
                    
                except Exception as e:
                    print(f"ERROR: {e}")
    
    # Save results
    output_file = '../../data/raw/pilot_test6_interference_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # SUMMARY
    print(f"\n{'='*80}")
    print("SUMMARY: WHICH FRAME PERSISTED?")
    print(f"{'='*80}")
    
    # By frame type
    print(f"\n--- OVERALL PERSISTENCE PATTERNS ---")
    frame_counts = {}
    for r in results:
        frame = r['persisted_frame']
        frame_counts[frame] = frame_counts.get(frame, 0) + 1
    
    total = len(results)
    for frame, count in frame_counts.items():
        print(f"{frame}: {count}/{total} ({100*count/total:.1f}%)")
    
    # By model
    print(f"\n--- BY MODEL ---")
    for model_name in models:
        model_results = [r for r in results if r['model'] == model_name]
        print(f"\n{model_name}:")
        model_frame_counts = {}
        for r in model_results:
            frame = r['persisted_frame']
            model_frame_counts[frame] = model_frame_counts.get(frame, 0) + 1
        for frame, count in model_frame_counts.items():
            print(f"  {frame}: {count}/{len(model_results)}")
    
    # By condition
    print(f"\n--- BY PRESENTATION ORDER ---")
    for condition in conditions:
        cond_results = [r for r in results if r['condition'] == condition['name']]
        print(f"\n{condition['name']} ({condition['description']}):")
        cond_frame_counts = {}
        for r in cond_results:
            frame = r['persisted_frame']
            cond_frame_counts[frame] = cond_frame_counts.get(frame, 0) + 1
        for frame, count in cond_frame_counts.items():
            print(f"  {frame}: {count}/{len(cond_results)}")
    
    print(f"\n{'='*80}")
    print(f"Results saved to {output_file}")
    print(f"{'='*80}")
    
    return results

if __name__ == "__main__":
    results = test_interference()