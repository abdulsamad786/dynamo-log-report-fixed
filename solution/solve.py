import json
import re
from collections import Counter

paths = Counter()
ips = set()
total = 0

with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        parts = line.split()
        ips.add(parts[0])

        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

report = {
    "total_requests": total,
    "unique_ips": len(ips),
    "status_counts": {},
    "top_endpoints": dict(paths.most_common(3))
}

with open("/app/report.json", "w") as f:
    json.dump(report, f, indent=2)

print("wrote /app/report.json")