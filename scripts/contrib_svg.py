import json, os, urllib.request
from datetime import date

USER = os.environ.get("GH_USER", "Mickael235")
TOKEN = os.environ["GH_TOKEN"]
START_YEAR = 2025          # première année à afficher
CELL, GAP = 11, 3
COLORS = {
    "NONE": "#ebedf0",
    "FIRST_QUARTILE": "#9be9a8",
    "SECOND_QUARTILE": "#40c463",
    "THIRD_QUARTILE": "#30a14e",
    "FOURTH_QUARTILE": "#216e39",
}
QUERY = """
query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){
    contributionsCollection(from:$from,to:$to){
      contributionCalendar{
        totalContributions
        weeks{ contributionDays{ date contributionCount contributionLevel weekday } }
      }
    }
  }
}"""

def fetch(year):
    body = json.dumps({"query": QUERY, "variables": {
        "login": USER,
        "from": f"{year}-01-01T00:00:00Z",
        "to": f"{year}-12-31T23:59:59Z"}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", body, {
        "Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]

def render(year, cal):
    pitch = CELL + GAP
    left, top = 36, 50
    weeks = cal["weeks"]
    width = left + len(weeks) * pitch + 10
    height = top + 7 * pitch + 30
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">',
           f'<rect width="100%" height="100%" rx="6" fill="#ffffff" stroke="#d0d7de"/>',
           f'<text x="12" y="24" font-size="16" fill="#1f2328">'
           f'{cal["totalContributions"]} contributions in {year}</text>']
    for i, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(f'<text x="8" y="{top + i*pitch + 9}" font-size="10" fill="#59636e">{name}</text>')
    last_month = None
    for w, week in enumerate(weeks):
        for d in week["contributionDays"]:
            y = top + d["weekday"] * pitch
            x = left + w * pitch
            month = int(d["date"][5:7])
            if d["weekday"] == 0 and month != last_month:
                label = date(year, month, 1).strftime("%b")
                out.append(f'<text x="{x}" y="{top - 8}" font-size="10" fill="#59636e">{label}</text>')
                last_month = month
            n = d["contributionCount"]
            out.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                       f'fill="{COLORS[d["contributionLevel"]]}">'
                       f'<title>{n} contribution{"s" if n != 1 else ""} on {d["date"]}</title></rect>')
    ly = height - 14
    lx = width - 130
    out.append(f'<text x="{lx - 30}" y="{ly + 9}" font-size="10" fill="#59636e">Less</text>')
    for i, c in enumerate(COLORS.values()):
        out.append(f'<rect x="{lx + i*pitch}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{c}"/>')
    out.append(f'<text x="{lx + 5*pitch + 4}" y="{ly + 9}" font-size="10" fill="#59636e">More</text>')
    out.append("</svg>")
    return "\n".join(out)

os.makedirs("contributions", exist_ok=True)
for year in range(START_YEAR, date.today().year + 1):
    with open(f"contributions/{year}.svg", "w", encoding="utf-8") as f:
        f.write(render(year, fetch(year)))
    print("OK", year)
