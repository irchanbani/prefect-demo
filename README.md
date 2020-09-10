# prefect-demo

Learning Prefect

## Prepare

```bash
    make prepare-dev
```

## Local

We need to open 4 terminal that are still in this directory, and make sure docker daemon is running:

- Run this in terminal 1 (prefect server + UI)
```bash
    prefect backend server
    prefect server start
```

- Run this in terminal 2 (supervisor)
```bash
    prefect agent install local
```
Copy all the text that occur to `supervisord.conf`, then run
```bash
    supervisord
```


- Run this in terminal 3 (agent)
```bash
    prefect agent start
```

- Run this in terminal 4
```bash
    prefect create project new-project-id
    pipenv run python etl-01.py
```

### Result Local

![Image 01](https://raw.github.com/irchanbani/prefect-demo/main/docs/image-01-local.jpg)
