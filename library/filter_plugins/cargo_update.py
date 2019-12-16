# Adapted from
# https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/filter/core.py
from __future__ import absolute_import, division, print_function

import sys

# Python 2/3 compatability.
IS_PY3 = sys.version_info[0] == 3
if IS_PY3:
    Text = str
    Bytes = bytes
else:
    Text = unicode  # type: ignore  # noqa
    Bytes = str  # type: ignore
__metaclass__ = type


if "doctest" in sys.modules:
    TEST_DATA = """   Updating registry 'https://github.com/rust-lang/crates.io-index'

Package        Installed  Latest   Needs update
just           v0.4.4     v0.5.3   Yes
bat            v0.12.1    v0.12.1  No
bingrep        v0.8.1     v0.8.1   No
cargo-deps     v1.3.0     v1.3.0   No
cargo-edit     v0.4.2     v0.4.2   No
cargo-make     v0.24.2    v0.24.2  No
cargo-release  v0.13.0    v0.13.0  No
cargo-tree     v0.27.0    v0.27.0  No
cargo-update   v2.5.0     v2.5.0   No
cargo-watch    v7.3.0     v7.3.0   No
exa            v0.9.0     v0.9.0   No
find-files     v0.1.8     v0.1.8   No
fselect        v0.6.7     v0.6.7   No
funzzy         v0.3.3     v0.3.3   No
fw             v2.2.2     v2.2.2   No
hx             v0.2.1     v0.2.1   No
hyperfine      v1.9.0     v1.9.0   No
latexdef       v0.4.2     v0.4.2   No
lsd            v0.16.0    v0.16.0  No
ripgrep        v11.0.2    v11.0.2  No
ruplacer       v0.4.1     v0.4.1   No
sd             v0.6.5     v0.6.5   No
skim           v0.6.9     v0.6.9   No
tokei          v10.1.0    v10.1.0  No
xsv            v0.13.0    v0.13.0  No
"""

EXPECTED_TABLE_HEADER = "Package        Installed  Latest   Needs update"


def cargo_update_planned(lines):
    # type: (list) -> list
    in_table = False
    ret = []
    for line in lines:
        line = line.strip()
        if in_table:
            if not line:
                # We don't simply 'break' because the --git option will list
                # multiple tables.
                in_table = False
            split = line.split()
            if len(split) < 4:
                continue
            crate, installed, latest, to_update = line.split()
            if to_update == "Yes":
                ret.append({"crate": crate, "installed": installed, "latest": latest})
        else:
            if line == EXPECTED_TABLE_HEADER:
                in_table = True
    return ret


class FilterModule(object):
    def filters(self):
        return {
            "cargo_update_planned": cargo_update_planned,
        }
