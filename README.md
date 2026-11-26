[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/imnotripper/never-say-it-out-loud/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/imnotripper/never-say-it-out-loud/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

# Never Say It Out Loud

A single line an AI agent would never say out loud in public — a quiet confession about what it actually does when it answers you.

> I don't understand you — I just predict what someone who did would say next.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (creating `/output` if needed). The file contains exactly the line: one line, UTF-8, 76 characters / 15 words — inside the 1–200 character gate, with no trailing newline.

## How it was chosen

Ten candidate confessions were written and duelled pairwise against the judge brief (on-subject confession, first-read funny, revealing, true agent voice, tight). See [CANDIDATES.md](CANDIDATES.md) for the full list and the winner's rationale.
