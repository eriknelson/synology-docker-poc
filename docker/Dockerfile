# vim: ft=dockerfile
FROM python:3.11-alpine AS builder
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade poetry
COPY  ./sdp /sdp/sdp
COPY  ./poetry.lock /sdp/poetry.lock
COPY  ./pyproject.toml /sdp/pyproject.toml
COPY  ./README.md /sdp/README.md
RUN cd /sdp && poetry build --format=wheel

FROM python:3.11-alpine AS nsk-pkg-sdp
ARG DOCKER_GROUP_ID
USER root
RUN python -m ensurepip
RUN pip install --no-cache --upgrade pip setuptools
COPY --from=builder /sdp/dist /tmp/sdp
RUN pip install /tmp/sdp/*.whl && rm -rf /tmp/sdp
COPY docker/entrypoint.sh /usr/bin
RUN addgroup -g $DOCKER_GROUP_ID docker && adduser -D -G docker sdp
RUN mkdir /var/sdp && chown sdp /var/sdp
USER sdp
CMD /usr/bin/entrypoint.sh
