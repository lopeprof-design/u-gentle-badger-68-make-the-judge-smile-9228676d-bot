# Make the Judge Smile — one warm line about a small good thing today.
# Writes the line to /output/entry.txt (UTF-8, at most 200 characters).
import os

LINE = (
    "At 6:40 this morning Pak Dedi, who sells iced tea by the station, "
    "poured mine without sugar before I reached his cart — he remembered, "
    "and the whole rushed morning slowed down for one sip."
)

# The gate needs 1 to 200 characters of real text: refuse to write
# anything outside it rather than submitting an invalid entry.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, gate needs 1-200"
assert LINE.strip(), "line must not be only white space"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)
