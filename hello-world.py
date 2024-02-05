from prefect import flow,task


@task
def my_name():
    name = 'Shangeeth'
    return name


@task
def my_age():
    age = 25
    return age



@flow
def hello():
    name = my_name()
    age = my_age()
    print(f"Hi I am {name}, {age} of age")

if __name__ == "__main__":
    hello()


