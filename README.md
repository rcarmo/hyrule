# HyRule

This is a PoC for a [Hy][hy] REPL using [prompt_toolkit][pt]. Right now it requires a development snapshot for [Pygments][py] 2.0 (since that has the [Hy][hy] lexer)

Currently it supports:

- Readline editing
- Syntax highlight
- Keywords completion

Not supported yet:

- Multiline input
- `--spy`

[py]: http://pygments.org/
[hy]: http://hylang.org
[pt]: https://github.com/jonathanslenders/python-prompt-toolkit
