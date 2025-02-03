class TagManager:
    def __init__(self, gitlab_client):
        self.client = gitlab_client


    def create_tag(self, project_id, tag_name, ref, message=None):
        project = self.client.get_project(project_id)
        project.tags.create({'tag_name': tag_name, 'ref': ref, 'message': message})