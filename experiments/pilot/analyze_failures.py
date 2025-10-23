import json
import sys
sys.path.append('../../src')

with open('../../data/raw/pilot_test1_5facts_results.json', 'r') as f:
    results = json.load(f)

print("\n" + "="*80)
print("FAILED PREDICTIONS ANALYSIS")
print("="*80)

failures = [r for r in results if not r['prediction_matched']]

print(f"\nTotal failures: {len(failures)}/30\n")

for failure in failures:
    print(f"\n{'='*80}")
    print(f"Model: {failure['model'].upper()}")
    print(f"Fact: {failure['fact']}")
    print(f"Condition: {failure['condition']}")
    print(f"Expected: {failure['expected_type']}")
    print(f"Got: {failure['markers']['response_type']}")
    print(f"Semantic score: {failure['markers']['semantic_score']:.2f}")
    print(f"Autobio score: {failure['markers']['autobiographical_score']:.2f}")
    print(f"\nResponse: {failure['response'][:200]}...")
    print(f"\nMarkers:")
    print(f"  Tense: {failure['markers']['tense']}")
    print(f"  First-person: {failure['markers']['pronouns']['first_person']}")
    print(f"  Temporal adverbs: {failure['markers']['temporal_adverbs']}")
    print(f"  Mental state verbs: {failure['markers']['mental_state_verbs']}")