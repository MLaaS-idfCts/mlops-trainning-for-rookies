# Gitlab CI

### TODO:
- [quick start](https://docs.gitlab.com/ee/ci/quick_start/)
- [complex pipelines](https://docs.gitlab.com/ee/ci/quick_start/tutorial.html)

### Key Concepts:
- Configuration File
- Runner
- Job
- Stage
- Pipeline
- Artifacts
- Environments
- Dependecies

### Final Exercise:
Write a CICD pipeline using Gitlab CI that:
  - Builds the image from the docker file you wrote. (*Clue*: Use a build config).
    - The image's tag should be latest when commiting/merging to main branch.
    - The image's tag should be the name of the branch when commiting/merging to other branches.
  - Push the image to Quay.
    - This stage and the build stage should run only when commiting/merging branches and manually.
  - Deploy the application to Openshift.
    - The this stage should run only manually