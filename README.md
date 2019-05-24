# My CI/CD Ready Repo

## Roles can be installed with:

  # Future this will be `install linuxfoundation.ci`
  #  which will contain all the other roles as dependencies
  #  and may be done as a post-run script for cookiecutter
  ansible-galaxy install -r requirements.yml --roles-path roles

## Individual roles can be tested with the following command:

  # In the future this will be molecule, or an ansible specific runner
  docker run --rm -it \
  -v $PWD:/app \
  -w /app \
  -e ANSIBLE_STDOUT_CALLBACK=unixy \
  -e WORKSPACE=/app \
  williamyeh/ansible:alpine3 \
  ansible-playbook -c local .playbooks/verify.yml


## Gitlab CI jobs can be verified with:

  gitlab-runner exec docker verify




# Java Toolchain

## Environment

- MAVEN_URL

...


# Docs Toolchain

## Environment

- RTD_PROJECT_NAME
    Project name on ReadTheDocs

- RTD_BUILD_URL
    URL endpoint for triggering new build

- RTD_TOKEN
    Token needed for triggering the RTD_BUILD_URL

