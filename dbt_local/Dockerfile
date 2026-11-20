FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m dbt
USER dbt
ENV PATH="/home/dbt/.local/bin:${PATH}"

# Create the project dir as the dbt user so it's writable, then use it as the workdir
RUN mkdir -p /home/dbt/project
WORKDIR /home/dbt/project

RUN pip install --no-cache-dir --user "dbt-core" "dbt-databricks==1.12.7"

# Now runs in a writable directory
# RUN dbt system install-drivers

COPY --chown=dbt:dbt . .
