# Local recovery backup

Verified pre-simplification backup: `_backups/before_simplification_20261116_164503/project_backup.zip`.

The archive contains the entire starting repository, including uncommitted and untracked work and Git history. Its adjacent `inventory.json` records every original file size and SHA-256; every archived file was read back and checked. `affected_files.json` lists removals and renames.

To recover files, extract the ZIP into a new empty folder, verify against the inventory, and copy back only the files needed. This avoids overwriting current work. No restore has been run. The backup directory is excluded from Git.
