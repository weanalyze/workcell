FROM public.ecr.aws/lambda/python:3.8

# Using poetry to manage dependencies
RUN pip install --upgrade pip && pip install poetry
# Copy workcell project folder to build
COPY --chown=user:group ../.. /var/workcell
# Build python package by poetry
RUN cd /var/workcell && poetry build 
RUN pip install /var/workcell/dist/*.whl
# Remove workcell project folder
RUN rm -rf /var/workcell