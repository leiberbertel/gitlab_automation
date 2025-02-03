class BranchManager:
    def __init__(self, gitlab_client):
        self.client = gitlab_client


    def create_branch(self, project_id, branch_name, ref):
        project = self.client.get_project(project_id)
        project.branches.create({'branch': branch_name, 'ref': ref})