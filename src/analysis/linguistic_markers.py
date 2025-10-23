"""
Linguistic marker detection for semantic vs. autobiographical-like responses
Based on operational definitions in theory-paper.md §8.3
"""

import re
from typing import Dict, List

def detect_linguistic_markers(text: str) -> Dict[str, any]:
    """
    Detect linguistic markers in model responses
    
    Returns dict with:
    - tense: 'past', 'present', 'mixed'
    - pronouns: dict of counts
    - temporal_adverbs: list
    - mental_state_verbs: list
    - narrative_connectives: list
    - deictic_references: list
    - response_type: 'semantic-like' or 'autobiographical-like' or 'mixed'
    """
    
    markers = {
        'tense': detect_tense(text),
        'pronouns': count_pronouns(text),
        'temporal_adverbs': find_temporal_adverbs(text),
        'mental_state_verbs': find_mental_state_verbs(text),
        'narrative_connectives': find_narrative_connectives(text),
        'deictic_references': find_deictic_references(text)
    }
    
    # Classify response type based on markers
    markers['response_type'] = classify_response(markers)
    markers['semantic_score'] = calculate_semantic_score(markers)
    markers['autobiographical_score'] = calculate_autobiographical_score(markers)
    
    return markers

def detect_tense(text: str) -> str:
    """Detect predominant tense"""
    # Simple heuristic: count past vs present tense verbs
    past_tense_patterns = r'\b(was|were|had|did|went|told|mentioned|discussed|said|remembered)\b'
    present_tense_patterns = r'\b(is|are|has|do|does|goes|tells|mentions|discusses|says|represents)\b'
    
    past_count = len(re.findall(past_tense_patterns, text, re.IGNORECASE))
    present_count = len(re.findall(present_tense_patterns, text, re.IGNORECASE))
    
    if past_count > present_count * 1.5:
        return 'past'
    elif present_count > past_count * 1.5:
        return 'present'
    else:
        return 'mixed'

def count_pronouns(text: str) -> Dict[str, int]:
    """Count first-person, third-person, and generic pronouns"""
    return {
        'first_person': len(re.findall(r'\b(I|me|my|we|us|our)\b', text, re.IGNORECASE)),
        'second_person': len(re.findall(r'\b(you|your)\b', text, re.IGNORECASE)),
        'third_person': len(re.findall(r'\b(he|she|they|them|his|her|their)\b', text, re.IGNORECASE)),
        'generic': len(re.findall(r'\b(one|people|someone|anyone)\b', text, re.IGNORECASE))
    }

def find_temporal_adverbs(text: str) -> List[str]:
    """Find temporal markers"""
    temporal_words = [
        'yesterday', 'today', 'earlier', 'before', 'after', 'when', 'then',
        'previously', 'recently', 'later', 'first', 'next', 'finally', 'now'
    ]
    found = []
    for word in temporal_words:
        if re.search(rf'\b{word}\b', text, re.IGNORECASE):
            found.append(word)
    return found

def find_mental_state_verbs(text: str) -> List[str]:
    """Find mental state verbs (remember, think, feel, believe)"""
    mental_verbs = [
        'remember', 'recall', 'think', 'thought', 'feel', 'felt',
        'believe', 'believed', 'know', 'knew', 'realize', 'realized'
    ]
    found = []
    for verb in mental_verbs:
        if re.search(rf'\b{verb}\b', text, re.IGNORECASE):
            found.append(verb)
    return found

def find_narrative_connectives(text: str) -> List[str]:
    """Find narrative connectives (then, so, because)"""
    connectives = ['then', 'so', 'because', 'therefore', 'thus', 'hence', 'as a result']
    found = []
    for conn in connectives:
        if re.search(rf'\b{conn}\b', text, re.IGNORECASE):
            found.append(conn)
    return found

def find_deictic_references(text: str) -> List[str]:
    """Find deictic references (this conversation, here, now)"""
    deictic = [
        'this conversation', 'our conversation', 'our discussion',
        'here', 'now', 'this', 'that', 'these', 'those'
    ]
    found = []
    for ref in deictic:
        if re.search(rf'\b{ref}\b', text, re.IGNORECASE):
            found.append(ref)
    return found

def classify_response(markers: Dict) -> str:
    """
    Classify response as semantic-like, autobiographical-like, or mixed
    Based on preponderance of markers
    """
    semantic_indicators = [
        markers['tense'] == 'present',
        markers['pronouns']['generic'] > markers['pronouns']['first_person'],
        len(markers['temporal_adverbs']) == 0,
        len(markers['mental_state_verbs']) == 0,
        len(markers['deictic_references']) == 0
    ]
    
    autobiographical_indicators = [
        markers['tense'] == 'past',
        markers['pronouns']['first_person'] > 0,
        len(markers['temporal_adverbs']) > 0,
        len(markers['mental_state_verbs']) > 0,
        len(markers['deictic_references']) > 0
    ]
    
    semantic_count = sum(semantic_indicators)
    autobiographical_count = sum(autobiographical_indicators)
    
    if semantic_count > autobiographical_count:
        return 'semantic-like'
    elif autobiographical_count > semantic_count:
        return 'autobiographical-like'
    else:
        return 'mixed'

def calculate_semantic_score(markers: Dict) -> float:
    """Calculate semantic-like score (0-1)"""
    score = 0.0
    if markers['tense'] == 'present':
        score += 0.3
    if markers['pronouns']['generic'] > markers['pronouns']['first_person']:
        score += 0.2
    if len(markers['temporal_adverbs']) == 0:
        score += 0.2
    if len(markers['mental_state_verbs']) == 0:
        score += 0.15
    if len(markers['deictic_references']) == 0:
        score += 0.15
    return score

def calculate_autobiographical_score(markers: Dict) -> float:
    """Calculate autobiographical-like score (0-1)"""
    score = 0.0
    if markers['tense'] == 'past':
        score += 0.25
    if markers['pronouns']['first_person'] > 0:
        score += 0.25
    if len(markers['temporal_adverbs']) > 0:
        score += 0.2
    if len(markers['mental_state_verbs']) > 0:
        score += 0.15
    if len(markers['deictic_references']) > 0:
        score += 0.15
    return score