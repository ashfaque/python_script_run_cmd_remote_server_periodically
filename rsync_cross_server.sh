
rsync \
    -avLr \
    --progress \
    -e "ssh -i /path/to/pvt_key" \
    /path/to/HOST/dir/dir_to_sync/* \    # This * here is really important.
    DESTINATION_SERVER_USERNAME@DESTINATION_IP_ADDRESS:/path/to/REMOTE/dir/dir_where_files_will_be_synced/



# 1. `-a` (or `--archive`):
#    - This option is used to archive files and directories while preserving their attributes, permissions, ownership, and timestamps. It's a combination of several other options, including `-rlptgoD`, which stands for:
#      - `-r` (or `--recursive`): Recursively copy directories and their contents.
#      - `-l` (or `--links`): Preserve symbolic links.
#      - `-p` (or `--perms`): Preserve permissions.
#      - `-t` (or `--times`): Preserve modification times.
#      - `-g` (or `--group`): Preserve group ownership.
#      - `-o` (or `--owner`): Preserve owner (superuser only).
#      - `-D`: Preserve special files and devices.

# 2. `-v` (or `--verbose`):
#    - This option enables verbose mode, which displays detailed information about the files being transferred. It provides feedback on the progress of the synchronization.

# 3. `-L` (or `--copy-links`):
#    - When this option is used, `rsync` follows symbolic links and copies the files they point to rather than copying the links themselves. This is useful to ensure that the content of symbolic links is synchronized.

# 4. `-r` (or `--recursive`):
#    - This option is included within the `-a` (archive) option, but it can also be used separately. It tells `rsync` to recursively copy directories and subdirectories, ensuring that all contents are synchronized.

