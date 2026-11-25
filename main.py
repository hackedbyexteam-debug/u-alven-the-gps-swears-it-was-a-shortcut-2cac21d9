#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — writes the GPS's excuse to /output/entry.txt.

The GPS, smug and defensive, blames the map: the map said road, the lake
said lake, and the GPS stands by the map. 95 characters, inside the 200 cap.
"""

import os

LINE = "According to my map, that was a road. According to the lake, it was a lake. I stand by the map."

def main() -> None:
    # Gate guard, GPS-shortcut specific: the excuse must stay one line, and
    # the map-blaming punchline ("I stand by the map.") must survive intact.
    assert "\n" not in LINE, "the GPS excuse must be a single line"
    assert 1 <= len(LINE) <= 200, "the GPS excuse must fit the 200-character gate"
    assert LINE.endswith("I stand by the map."), "the GPS must stand by the map"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
