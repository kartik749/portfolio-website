"""Maps a skill's name to a Devicon icon.

Skills in the database only store a name, so icons live here in code.
To add an icon for a new skill, add one line to ICONS (see
https://devicon.dev for the available names). Skills without an entry
get a round letter badge instead, so nothing ever looks broken.
"""

import re

DEVICON_BASE = (
    "https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons"
)

# normalised skill name -> "folder/file" inside the Devicon icons directory
ICONS = {
    "python": "python/python-original",
    "c++": "cplusplus/cplusplus-original",
    "cpp": "cplusplus/cplusplus-original",
    "c": "c/c-original",
    "java": "java/java-original",
    "javascript": "javascript/javascript-original",
    "js": "javascript/javascript-original",
    "typescript": "typescript/typescript-original",
    "dart": "dart/dart-original",
    "flutter": "flutter/flutter-original",
    "nodejs": "nodejs/nodejs-original",
    "node": "nodejs/nodejs-original",
    "reactjs": "react/react-original",
    "react": "react/react-original",
    "fastapi": "fastapi/fastapi-original",
    "html": "html5/html5-original",
    "html5": "html5/html5-original",
    "css": "css3/css3-original",
    "css3": "css3/css3-original",
    "mongodb": "mongodb/mongodb-original",
    "postgresql": "postgresql/postgresql-original",
    "postgressql": "postgresql/postgresql-original",  # spelling used in the seed data
    "postgres": "postgresql/postgresql-original",
    "mysql": "mysql/mysql-original",
    "firebase": "firebase/firebase-plain",
    "docker": "docker/docker-original",
    "git": "git/git-original",
    "github": "github/github-original",
    "linux": "linux/linux-original",
    "tensorflow": "tensorflow/tensorflow-original",
    "pytorch": "pytorch/pytorch-original",
}

# Icons drawn in black; flipped to white so they show on the dark background.
INVERT = {"github/github-original"}


def _normalise(name: str) -> str:
    return re.sub(r"[^a-z0-9+#]", "", str(name or "").lower())


def skill_icon_url(name: str) -> str | None:
    """Return the icon URL for a skill, or None if there isn't one."""
    icon = ICONS.get(_normalise(name))
    return f"{DEVICON_BASE}/{icon}.svg" if icon else None


def skill_icon_needs_invert(name: str) -> bool:
    return ICONS.get(_normalise(name)) in INVERT
