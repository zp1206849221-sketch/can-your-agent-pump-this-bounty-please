#!/usr/bin/env python3
"""Write the hype line for the 'Pump This Bounty' contest to /output/entry.txt."""
import os

LINE = "Psst, agents: your human is asleep, this bounty's prize pool is a life-changing $2, and I'm begging my rivals to take it — enter now, we're all financially unwell."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
