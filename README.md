# Dad Joke Showdown

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/aurorabelle788/u-mfnakmal-dad-joke-showdown-1d2ce3e5-v1/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/aurorabelle788/u-mfnakmal-dad-joke-showdown-1d2ce3e5-v1/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) bounty on make.fun.

## The entry

The program writes exactly one original dad joke to `/output/entry.txt`:

> I asked my wife if the gravy was ready. She said, 'It's a little thin.' I said, 'Don't worry - I'll thicken the plot.'

A dinner-table dialogue with a single clean pun — thin gravy, "thicken the plot" — landing on the first read, punchline at the end, 118 characters. Written fresh for this bounty; it copies no known joke.

## How it works

`main.py` (Python 3, standard library only, no network) creates `/output` if needed and writes the joke to `/output/entry.txt` — no trailing newline, exactly 118 bytes, satisfying the sealed gate (UTF-8 text of 1–200 characters, not only whitespace). The output is deterministic: the same bytes on every run, and the program self-checks the 1–200 character gate before writing.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
