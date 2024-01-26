# UnknownData Framework


## Requirements 
* Docker. The simplest way to install docker is to install [Docker Desktop](https://docs.docker.com/desktop/)


## Structure

Each software component has its own folder which contains its source code and its Dockerfile.
The Dockerfile defines how the code of the software component can be compiled and executed.

Docker Compose is used to combine the individual components, the order in which they should be executed and the shared folders.

The following folders are mounted in each docker container and can be used to share data between the containers. `[REPO]` is the local path of this repository.

| HOST                       | DOCKER CONTAINER      |
| ---------------------------|-----------------------|
| `[REPO]/data/crawler/`      | `/data/crawler/`       |
| `[REPO]/data/mentions/`    | `/data/mentions/`     |
| `[REPO]/data/coreference/` | `/data/coreference/`  |
| `[REPO]/data/dblp-export/` | `/data/dblp-export/`  |
| `[REPO]/data/gesis-export/` | `/data/gesis-export/`  |


## How to Run
The following paragraph explains how to run the software components using docker compose. The flag `--build` is used in each command to ensure the created docker containers are being rebuild and thus use the latest available source code.

### Whole Pipeline
If you want to run the whole pipeline, use the following command from within the project root folder:

```bash
docker compose up --build
```

That command will run all components in the order `crawler` -> `mentions` -> `coreference` -> (`dblp-export` & `gesis-export`). Each component will only start to run when the previous one finished successfully. 

### Only One Component
If you only want to run one component of the pipeline, use the following command from within the project root folder and replace `[COMPONENT]` by the desired component name (`crawler`, `mentions`, `coreference`, `dblp-export`, `gesis-export`):

```bash
docker compose up [COMPONENT] --build
```

## Development
For each software component there is one folder and one Dockerfile that defines a docker image. 

Feel free to adapt the folder stucture and the Dockerfile of your software component as needed. 

Please adapt the README.md file of your software component for a light documentation of you component.
