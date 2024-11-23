from pybaseball import batting_stats, pitching_stats
import pandas as pd
import backoff
from tqdm import tqdm


@backoff.on_exception(backoff.expo, Exception, max_time=60)
def get_batting_stats(season):
    return batting_stats(season, league="all", qual=1, ind=1)


@backoff.on_exception(backoff.expo, Exception, max_time=60)
def get_pitching_stats(season):
    return pitching_stats(season, league="all", qual=1, ind=1)


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


if __name__ == "__main__":
    download_batting_stats()
    download_pitching_stats()
