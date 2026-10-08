start id:
    #!/usr/bin/env bash
    mkdir -p {{id}}

    cat >{{id}}/README.md <<EOF
    # [{{id}}](https://leetcode.com/problems/{{id}}/)
    EOF

    touch {{id}}/{{id}}.py

save id:
    read -r -n1 -s -p 'Copy solution to clipboard, then press any key here...'
    pbpaste >{{id}}/{{id}}.py
