from locust import HttpLocust, TaskSet, task


class UserTasks(TaskSet):

    @task
    def index(self):
        response = self.client.get("/")
        print("Response content:", response.text)


class WebsiteUser(HttpLocust):
    task_set = UserTasks
    min_wait = 5000
    max_wait = 15000
