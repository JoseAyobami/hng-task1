from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import crud, schemas

router = APIRouter(prefix="/strings", tags=["strings"])


@router.post("/", status_code=201, response_model=schemas.StringResponse)
def create_string(body: schemas.StringCreate):
	if not isinstance(body.value, str):
		raise HTTPException(status_code=422, detail="value must be a string")
	if body.value == "":
		raise HTTPException(status_code=400, detail="value cannot be empty")
	try:
		entry = crud.create_string(body.value)
	except KeyError:
		raise HTTPException(status_code=409, detail="String already exists")
	return entry


@router.get("/{string_value}", response_model=schemas.StringResponse)
def get_string(string_value: str):
	entry = crud.get_by_value(string_value)
	if not entry:
		raise HTTPException(status_code=404, detail="String not found")
	return entry


@router.get("/", response_model=dict)
def list_strings(
	is_palindrome: Optional[bool] = Query(None),
	min_length: Optional[int] = Query(None, ge=0),
	max_length: Optional[int] = Query(None, ge=0),
	word_count: Optional[int] = Query(None, ge=0),
	contains_character: Optional[str] = Query(None, min_length=1, max_length=1),
):
	filters = {
		"is_palindrome": is_palindrome,
		"min_length": min_length,
		"max_length": max_length,
		"word_count": word_count,
		"contains_character": contains_character,
	}
	data = crud.get_all(filters)
	return {"data": data, "count": len(data), "filters_applied": {k: v for k, v in filters.items() if v is not None}}


@router.get("/filter-by-natural-language", response_model=schemas.NaturalLanguageResult)
def natural_language_filter(query: str):
	# Very small heuristic parser for a couple of example phrases
	q = query.lower().strip()
	parsed = {}
	if "single word" in q:
		parsed["word_count"] = 1
	if "palindrom" in q:
		parsed["is_palindrome"] = True
	if "longer than" in q:
		# extract number after phrase
		import re

		m = re.search(r"longer than\s+(\d+)", q)
		if m:
			parsed["min_length"] = int(m.group(1)) + 1
	if "contain" in q or "containing" in q:
		# look for single letters mentioned
		for ch in "abcdefghijklmnopqrstuvwxyz":
			if f"{ch}" in q:
				parsed["contains_character"] = ch
				break

	if not parsed:
		raise HTTPException(status_code=400, detail="Unable to parse natural language query")

	data = crud.get_all(parsed)
	interpreted = {"original": query, "parsed_filters": parsed}
	return {"data": data, "count": len(data), "interpreted_query": interpreted}


@router.delete("/{string_value}", status_code=204)
def delete_string(string_value: str):
	try:
		crud.delete_by_value(string_value)
	except KeyError:
		raise HTTPException(status_code=404, detail="String not found")
	return None
