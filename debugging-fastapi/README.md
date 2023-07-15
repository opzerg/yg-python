
# VSCode Debugging

``` json
"configurations": [
    {
        "name": "Python: Remote Attach",
        "type": "python",
        "request": "attach",
        "connect": {
            "host": "localhost",
            "port": 5678
        },
        "pathMappings": [
            {
                "localRoot": "${workspaceFolder}/src",
                "remoteRoot": "/app/src"
            }
        ],
        "justMyCode": true
    },
    {
        "name": "Python: FastAPI",
        "type": "python",
        "request": "launch",
        "module": "uvicorn",
        "args": [
            "src.main:app",
            "--reload",
            "--port",
            "8080"
        ],
        "jinja": true,
        "justMyCode": true
    }
]
```