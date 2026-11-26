"""Five Seconds to Explain the Glass.

Writes the winning one-sentence cat defence to entry.txt.

Winner (chosen by a 12-candidate pairwise tournament judged on the
published criteria, in order: valid one-sentence cat excuse about the
glass; cat's own logic, self-interest, zero remorse; fresh comic idea;
speakable in five seconds; no wasted characters):

    The glass was hogging the sunspot, and I do not negotiate with
    furniture that blocks my light.

Why it won: a sunspot is the most unmistakably cat motive there is,
the "negotiate with furniture" line is pure unrepentant cat voice,
and it dodges every banned idea (no gravity, no slippery edge, no
"already falling"). Four tournament wins: vs the gravity-test line,
vs the whispering-glass line, vs the rent-eviction line, and vs the
abandoned-property line in the final.
"""

import os

ENTRY = (
    "The glass was hogging the sunspot, and I do not negotiate "
    "with furniture that blocks my light."
)


def main() -> None:
    # Gate self-check: 1-200 chars, one sentence, not whitespace-only.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
