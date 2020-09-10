from prefect import Flow, task
from datetime import timedelta
from prefect.schedules import IntervalSchedule

@task
def hello_world():
    print("hello world!")
    return "Hello Prefect"

@task
def prefect_say(s:str):
    print(s)

schedule = IntervalSchedule(interval=timedelta(minutes=2))

with Flow("hello-flow", schedule) as flow:
    r = hello_world()
    s2 = prefect_say(r)

# flow.run()
flow.register(project_name="new-project-id")
flow.run_agent()
