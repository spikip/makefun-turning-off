"""Entry for the make.fun bounty "Have You Tried Turning It Off?".

The program writes a single funny line to /output/entry.txt. The line
is the hopeless tech support agent's cheerful first step: turning it
off and on again is step one of twelve, and the agent has already
forgotten step two. The humour is the agent's uselessness, never the
customer: the agent is cheerful, confident, and completely out of
ideas after the first one. The gate allows 1 to 199 characters of
UTF-8 text, so
the line is checked against that cap before it is written.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? Excellent \u2014 that "
    "was step one of twelve, and I have already forgotten step two."
)

MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
