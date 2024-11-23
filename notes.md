# What Data Do We need?

- Age of manager
- Number of rookies
- Morale score???

## Batting

### Per-Player

- Age
- OPS +
- WAR
- OBP (On Base Percentage)
- Doubles/ At Bat
- Triples / At Bat
- Home Runs / At Bat
- Caught Stealing / Stolen Bases
- Strikeouts / At Bat
- Bats left handed / Total batters on team

## Pitching

### Per-Player

- Age
- ERA+
- Hits Allowed / Batters Faced
- Home Runs Allowed / Batters Faced
- Walks / Batters Faced
- Strikeouts / Batters Faced

# How the Model Works

We go through each player on the current year team, and find their stats from the prior year. If they don't have data from the prior year, we drop them. Next, we take the mean (weighted by At Bats/Batters Faced) and variance (weighted by At Bats/Batters Faced) of each of the batting and pitching stats listed above. This creates a set of features for each team. We feed all features into the model, and use binary classification to say if the home team (listed first) will win.
