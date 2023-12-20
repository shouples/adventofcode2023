FROM mcr.microsoft.com/vscode/devcontainers/universal:1

USER root

# pyenv installation and setup
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"

# 2023-12-20: Python 3.8.5 is installed by default in the universal image
ENV PYTHON_VERSION=3.11.5
RUN pyenv install ${PYTHON_VERSION} && pyenv global ${PYTHON_VERSION}

# allow pyenv to install python versions
RUN chown -R "$USER:$USER" $PYENV_ROOT
USER $USER

# poetry installation and setup
# hadolint ignore=DL3013
RUN pip install poetry --no-cache-dir && \
    poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true
