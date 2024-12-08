# What Data Do We need?

- Age of manager
- Number of rookies
- Day/Night
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

# HyperParam Stuff

## Logistic Regression

Best hyperparameters: {'C': 0.006143534075514649, 'l1_ratio': 0.8943970373411257}

RFECV

Index(['home_wins_pct', 'away_wins_pct', 'mar', 'home_batting_R_mean',
'home_batting_OPS_mean', 'home_batting_WAR_mean',
'home_batting_rookies', 'home_pitching_ERA-_mean',
'home_pitching_BB_mean', 'home_pitching_SO_mean',
'home_pitching_rookies', 'away_batting_WAR_mean', 'away_batting_SO_var',
'away_batting_rookies', 'away_pitching_Age_mean',
'away_pitching_Age_var', 'away_pitching_ERA-_mean',
'away_pitching_BB_mean', 'away_pitching_SO_mean',
'away_pitching_rookies'],
dtype='object')

## LGBM

{'num_leaves': 40, 'max_depth': 4, 'learning_rate': 0.09310392730497162, 'feature_fraction': 0.31520011005369913, 'bagging_fraction': 0.5969829919788188, 'bagging_freq': 7, 'lambda_l1': 0.5466643025395969

# Future

- Data Augmentation: include home + away games

## Feature Ideas

- We should add a feature to our model that tracks “team chemistry”—how many people on the team have played together before. So if a team changes a lot, we’d expect lower chemistry.
- We could also do average number of seasons played or something like that.
- Variance of player performance over games/seasons?

## EDA

- How much do player stats change from season to season?
