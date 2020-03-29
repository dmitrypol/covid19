FROM python:3.6.8

ENV app_name=covid19
ENV home_dir=/opt/${app_name}/
RUN mkdir -p ${home_dir}
WORKDIR ${home_dir}

RUN pip install --upgrade pip && pip install pipenv 
COPY Pipfile* ./
RUN pipenv install --system --dev && rm -rf /root/.cache/pip
COPY ./ ./

RUN APP_ENV=test pytest tests/* --cov=app
RUN pylint app/

EXPOSE 5000
ENTRYPOINT ["devops/entrypoint.sh"]