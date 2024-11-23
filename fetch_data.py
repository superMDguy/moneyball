from pybaseball import batting_stats, pitching_stats, schedule_and_record
import pandas as pd
import backoff
from tqdm import tqdm
from itertools import product

# All 2024 Teams
teams = [
    "NYY",
    "KCR",
    "LAD",
    "BAL",
    "NYM",
    "BOS",
    "CLE",
    "CIN",
    "ARI",
    "TOR",
    "SFG",
    "MIL",
    "SEA",
    "HOU",
    "SDP",
    "PHI",
    "OAK",
    "ATL",
    "TEX",
    "MIN",
    "CHC",
    "DET",
    "COL",
    "STL",
    "PIT",
    "LAA",
    "WSN",
    "MIA",
    "TBR",
    "CHW",
]


@backoff.on_exception(backoff.expo, Exception, max_time=60)
def get_batting_stats(season):
    return batting_stats(season, league="all", qual=1, ind=1)


@backoff.on_exception(backoff.expo, Exception, max_time=60)
def get_pitching_stats(season):
    return pitching_stats(season, league="all", qual=1, ind=1)


@backoff.on_exception(backoff.expo, Exception, max_time=60)
def get_schedule(season, team):
    return schedule_and_record(season, team)


def download_batting_stats(season_start=1998):
    print("Downloading batting stats")
    all_stats = []
    for season in tqdm(range(season_start, 2025)):
        try:
            season_stats = get_batting_stats(season)
            all_stats.append(season_stats)
        except Exception as e:
            print(f"Error downloading {season} batting data: {e}")
            continue

    # Save data
    all_stats = pd.concat(all_stats)
    all_stats.to_parquet(
        "data/batting_full.parquet.gz", index=False, compression="gzip"
    )


def download_pitching_stats(season_start=1998):
    print("Downloading pitching stats")
    all_stats = []
    for season in tqdm(range(season_start, 2025)):
        try:
            season_stats = get_pitching_stats(season)
            all_stats.append(season_stats)
        except Exception as e:
            print(f"Error downloading {season} pitching data: {e}")
            continue

    # Save data
    all_stats = pd.concat(all_stats)
    all_stats.to_parquet(
        "data/pitching_full.parquet.gz", index=False, compression="gzip"
    )


def download_schedule(season_start=1998):
    print("Downloading schedules")
    all_stats = []
    for season, team in tqdm(
        product(range(season_start, 2025), teams),
        total=len(teams) * (2025 - season_start),
    ):
        try:
            season_schedule = get_schedule(season, team)
            season_schedule["Season"] = season
            all_stats.append(season_schedule)
        except Exception as e:
            print(f"Error downloading {season} pitching data for {team}: {e}")
            continue

    # Save data
    all_stats = pd.concat(all_stats)
    all_stats.to_parquet(
        "data/schedules_full.parquet.gz", index=False, compression="gzip"
    )


if __name__ == "__main__":
    # download_batting_stats()
    # download_pitching_stats()
    download_schedule()
