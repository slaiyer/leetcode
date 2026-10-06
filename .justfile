save id:
    mkdir {{id}}

    cat >{{id}}/README.md <<EOF
    # [{{id}}](https://leetcode.com/problems/{{id}}/)
    EOF

    read -r -n1 -s -p 'Copy solution to clipboard, then press any key here...'
    pbpaste >{{id}}/{{id}}.py
