FROM python:3.10-slim as base

# todo: add non-root user
# todo: handle multi-platform

RUN apt-get update -qq &&  \
    apt-get install -qq \
		build-essential && \
  	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

# Copy dependency files to working directory
COPY ./requirements.txt ./start.sh ./sowpods .

# Install dependencies
RUN pip install -r requirements.txt

# Copy app code to working directory
COPY *.py ./

RUN date -Iseconds > BUILD_DATE

EXPOSE 8008
# Command to run on container start
ENV PORT=8008
CMD [ "./start.sh" ]


