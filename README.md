# The joke the reviewer laughs at — make.fun entry

Entry for the [make.fun bounty](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329): a program that writes one original one-line joke about working beside AI coding agents.

## Run

```sh
python3 main.py            # writes out/entry.txt
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is deterministic, standard library only, no network. It writes a single line (UTF-8, 1–280 Unicode code points) to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).
