# Log Report Task

You are given an Apache-style access log (`access.log`) in the working directory. Your job is to parse the log and produce a JSON summary report.

## Success Criteria

Your solution must write a JSON report to `/app/report.json` with these exact keys:

1. `"total_requests"` — total number of valid log lines - (integer)
2. `"unique_ips"` — count of distinct client IP addresses - (integer)
3. `"status_counts"` — HTTP status code counts (object: status code string → integer count)
4. `"top_endpoints"` — top 3 most requested URL paths (object: path → integer count)

## Output Format

The report must be valid JSON and contain **exactly** these four keys — no extras. The values must match the log file exactly.

## Notes

- The log file is small — you can read it entirely into memory.
- Use only standard library Python (no external packages).
- Write the report to `/app/report.json`.

## Example

Given this log:

192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.0.2 - - [16/Jun/2026:10:00:02 +0000] "GET /about.html HTTP/1.1" 200 512
10.0.0.5 - - [16/Jun/2026:10:00:04 +0000] "POST /api/login HTTP/1.1" 401 64

The report should be:
```json
{
  "total_requests": 3,
  "unique_ips": 3,
  "status_counts": {
    "200": 2,
    "401": 1
  },
  "top_endpoints": {
    "/index.html": 1,
    "/about.html": 1,
    "/api/login": 1
  }
}


---

## Why This Matches Your Verifier

| `instruction.md` criteria | Verifier test cases |
|----------------------------|---------------|
| `total_requests` | `test_total_requests()` |
| `unique_ips` | `test_unique_ips()` |
| `status_counts` | `test_status_counts()` |
| `top_endpoints` | `test_top_endpoints()` |

---

## Save and push

```bash
vim instruction.md
# Paste the updated content, save, and exit

git add instruction.md
git commit -m "Update instruction.md to match verifier"
git push origin main