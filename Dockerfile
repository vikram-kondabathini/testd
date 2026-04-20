ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-alpine
WORKDIR /app
# Copy the source code into the container.
COPY . /app
# RUN --mount=type=cache,target=/root/.cache/pip \
#     --mount=type=bind,source=requirements.txt,target=requirements.txt \
#     python -m pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# # Switch to the non-privileged user to run the application.
# USER appuser
# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
CMD python ./main.py
