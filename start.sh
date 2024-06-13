#!/usr/bin/env bash

python -m uvicorn anagram_api:app --reload --port $PORT --host 0.0.0.0
