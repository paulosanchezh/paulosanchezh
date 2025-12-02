import requests
import datetime

USERNAME = "paulosanchezh"

# Obtener stats desde GitHub API
repos = requests.get(f"https://api.github.com/users/{USERNAME}/repos").json()
num_repos = len(repos)

commits = requests.get(
    f"https://api.github.com/search/commits?q=author:{USERNAME}",
    headers={"Accept": "application/vnd.github.cloak-preview"}
).json()["total_count"]

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

svg = f"""
<svg width="530" height="220" xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" fill="#0a0f24"/>
  <text x="20" y="40" fill="#00eaff" font-size="26">📊 Dashboard — {USERNAME}</text>

  <text x="20" y="90" fill="#ff00ff" font-size="20">
      • Repos públicos: {num_repos}
  </text>

  <text x="20" y="130" fill="#aaff00" font-size="20">
      • Commits totales: {commits}
  </text>

  <text x="20" y="175" fill="#888" font-size="14">
      Última actualización: {today}
  </text>

</svg>
"""

with open("assets/dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg)
