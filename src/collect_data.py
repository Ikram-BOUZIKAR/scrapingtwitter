collect_data.py
---------------
Collect tweets/posts using Twarc2 (Twitter API v2) via CLI calls.

This script does NOT contain any API keys.
Keys must be provided via environment variables or a local .env file
(never commit secrets to GitHub).
"""

import subprocess
from pathlib import Path


def run_cmd(cmd: list[str]) -> None:
    """Run a shell command safely and raise if it fails."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed:\n{' '.join(cmd)}\n\nSTDERR:\n{result.stderr}"
        )


def twarc2_search_archive(
    query: str,
    start_time: str,
    end_time: str,
    output_path: str,
) -> None:
    """
    Run an archive search with twarc2 and save results in JSONL.

    Example:
        twarc2 search --archive --start-time 2021-11-01 --end-time 2022-01-01 "query" out.jsonl
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "twarc2",
        "search",
        "--archive",
        "--start-time",
        start_time,
        "--end-time",
        end_time,
        query,
    ]

    # Redirect output to file (works cross-platform via python)
    with open(output_path, "w", encoding="utf-8") as f:
        result = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"twarc2 failed:\n{result.stderr}")


if __name__ == "__main__":
    # Example queries (edit as needed)
    twarc2_search_archive(
        query='(#justicepouradama) lang:fr',
        start_time="2021-11-01",
        end_time="2022-01-01",
        output_path="data/sample/justicepouradama_2021-11_2022-01.jsonl",
    )
