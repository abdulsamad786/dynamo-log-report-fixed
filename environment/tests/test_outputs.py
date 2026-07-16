import json
import pytest
from pathlib import Path
from collections import Counter

REPORT = Path("/app/report.json")
LOG = Path("/app/access.log")

def test_report_exists():
    """Criterion 1: report.json must exist."""
    assert REPORT.exists(), "no report.json found"

def test_report_is_json():
    """Criterion 1: must be valid JSON (not just a text file)."""
    with open(REPORT) as f:
        json.load(f)

def test_report_has_keys():
    """Criteria 1-4: check all required fields are present."""
    with open(REPORT) as f:
        data = json.load(f)

    required = {"total_requests", "unique_ips", "status_counts", "top_endpoints"}
    missing = required - set(data.keys())
    assert not missing, f"missing keys: {missing}"

def test_total_requests():
    """Criterion 1: total_requests must match log line count."""
    with open(REPORT) as f:
        data = json.load(f)
    with open(LOG) as f:
        lines = sum(1 for l in f if l.strip())
    assert data["total_requests"] == lines, f"expected {lines}, got {data['total_requests']}"

def test_unique_ips():
    """Criterion 2: unique_ips must match distinct IPs in log."""
    with open(REPORT) as f:
        data = json.load(f)
    with open(LOG) as f:
        ips = {l.strip().split()[0] for l in f if l.strip()}
    assert data["unique_ips"] == len(ips), f"expected {len(ips)}, got {data['unique_ips']}"

def test_status_counts():
    """Criterion 3: status_counts must match log status codes."""
    with open(REPORT) as f:
        data = json.load(f)
    with open(LOG) as f:
        counts = Counter()
        for l in f:
            parts = l.strip().split()
            if len(parts) > 5 and parts[5].isdigit():
                counts[parts[5]] += 1
    assert data["status_counts"] == dict(counts), "status_counts mismatch"

def test_top_endpoints():
    """Criterion 4: top_endpoints must match top 3 URL paths."""
    with open(REPORT) as f:
        data = json.load(f)
    with open(LOG) as f:
        endpoints = Counter()
        for l in f:
            l = l.strip()
            if not l:
                continue
            start = l.find('"') + 1
            end = l.find('"', start)
            req = l[start:end]
            path = req.split()[1]
            endpoints[path] += 1
    expected = dict(endpoints.most_common(3))
    assert data["top_endpoints"] == expected, "top_endpoints mismatch"