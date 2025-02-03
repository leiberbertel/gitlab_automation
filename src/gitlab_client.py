import gitlab

class GitLabClient:
    def __init__(self, url, private_token):
        self.gl = gitlab.Gitlab(url, private_token=private_token)


    def get_project(self, project_id):
        return self.gl.projects.get(project_id)