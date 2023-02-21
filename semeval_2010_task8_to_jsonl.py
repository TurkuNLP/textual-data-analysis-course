#!/usr/bin/env python3

import sys
import json


def main(argv):
    with open(argv[1]) as f:
        lines = f.read().splitlines()

    assert len(lines) % 4 == 0

    examples = []
    for i in range(0, len(lines), 4):
        id_text = lines[i]
        id_, text = id_text.split('\t')
        id_ = int(id_)
        assert text[0] == '"' and text[-1] == '"'
        text = text[1:-1]
        label = lines[i+1]
        comment = lines[i+2]
        assert lines[i+3].isspace() or not lines[i+3]

        print(json.dumps({
            'id': id_,
            'text': text,
            'label': label,
        }))

    
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))
