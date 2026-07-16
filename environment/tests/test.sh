#!/bin/bash
set -euo pipefail

echo "Verifier started" > /app/verifier/debug.txt

pytest /tests/test_outputs.py --json-ctrf=/app/logs/verifier/ctrf.json -rA

if [ $? -eq 0 ]; then
  echo 1 > /app/verifier/reward.txt
else
  echo 0 > /app/verifier/reward.txt
fi

exit $?