"""Check whether each project in projects.json still calls Google's Custom Search JSON API.

Run from this folder:

    python3 check.py

For each project it fetches the file from the default branch on GitHub and looks
for the pattern at the recorded line. It changes nothing and needs no token.
"""

import datetime
import json
import urllib.error
import urllib.request

RAW = "https://raw.githubusercontent.com/{repository}/{default_branch}/{path}"


def fetch_lines(project):
    url = RAW.format(**project)
    request = urllib.request.Request(url, headers={"User-Agent": "cse-shutdown-check"})
    try:
        with urllib.request.urlopen(request, timeout=30) as reply:
            return reply.read().decode("utf-8", errors="replace").splitlines()
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def status(project, lines):
    if lines is None:
        return "file not found", False
    recorded = project["line"]
    pattern = project["pattern"]
    if recorded <= len(lines) and pattern in lines[recorded - 1]:
        return f"still there at line {recorded}", True
    for number, text in enumerate(lines, start=1):
        if pattern in text:
            return f"moved to line {number}", True
    return "gone from the file", False


def main():
    with open("projects.json", encoding="utf-8") as handle:
        projects = json.load(handle)
    width = max(len(p["repository"]) for p in projects)
    holding = 0
    for project in projects:
        result, holds = status(project, fetch_lines(project))
        holding += holds
        print(f"{project['repository']:<{width}}  {result}")
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    print(f"\n{holding} of {len(projects)} projects still hold Google's address. Checked {today} (UTC).")


if __name__ == "__main__":
    main()
