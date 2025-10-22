from typing import Dict, Optional, List
from datetime import datetime, timezone
import hashlib


def sha256_hash(value: str) -> str:
	return hashlib.sha256(value.encode("utf-8")).hexdigest()


def is_palindrome(value: str) -> bool:
	s = ''.join(value.split()).lower()
	return s == s[::-1]


def character_frequency_map(value: str) -> Dict[str, int]:
	freq: Dict[str, int] = {}
	for ch in value:
		freq[ch] = freq.get(ch, 0) + 1
	return freq


def analyze_string(value: str) -> Dict:
	h = sha256_hash(value)
	props = {
		"length": len(value),
		"is_palindrome": is_palindrome(value),
		"unique_characters": len(set(value)),
		"word_count": 0 if not value.strip() else len(value.split()),
		"sha256_hash": h,
		"character_frequency_map": character_frequency_map(value),
	}
	return props


# Simple in-memory store keyed by sha256 hash
STORE: Dict[str, Dict] = {}


def create_string(value: str) -> Dict:
	props = analyze_string(value)
	id_ = props["sha256_hash"]
	if id_ in STORE:
		raise KeyError("exists")
	entry = {
		"id": id_,
		"value": value,
		"properties": props,
		"created_at": datetime.now(timezone.utc).isoformat(),
	}
	STORE[id_] = entry
	return entry


def get_by_value(value: str) -> Optional[Dict]:
	h = sha256_hash(value)
	return STORE.get(h)


def get_all(filters: Dict = None) -> List[Dict]:
	results = list(STORE.values())
	if not filters:
		return results

	def match(entry: Dict) -> bool:
		p = entry["properties"]
		if "is_palindrome" in filters and filters["is_palindrome"] is not None:
			if p["is_palindrome"] != filters["is_palindrome"]:
				return False
		if "min_length" in filters and filters["min_length"] is not None:
			if p["length"] < filters["min_length"]:
				return False
		if "max_length" in filters and filters["max_length"] is not None:
			if p["length"] > filters["max_length"]:
				return False
		if "word_count" in filters and filters["word_count"] is not None:
			if p["word_count"] != filters["word_count"]:
				return False
		if "contains_character" in filters and filters["contains_character"]:
			ch = filters["contains_character"]
			if ch not in p["character_frequency_map"]:
				return False
		return True

	return [e for e in results if match(e)]


def delete_by_value(value: str) -> None:
	h = sha256_hash(value)
	if h not in STORE:
		raise KeyError("notfound")
	del STORE[h]
