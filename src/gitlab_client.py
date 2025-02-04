import gitlab

class GitLabClient:
    """A client to interact with the GitLab API.
    
    This class provides methods to connect to a GitLab instance
    and retrieve project information.
    
    Attributes:
        gl (gitlab.Gitlab): An authenticated GitLab client instance.
    """

    def __init__(self, url, private_token):
        """Initializes the GitLab client.
        
        Args:
            url (str): The GitLab instance URL.
            private_token (str): The private token for authentication.
        """
        self.gl = gitlab.Gitlab(url, private_token=private_token)

    def get_project(self, project_id):
        """Retrieves a project from GitLab by its ID.
        
        Args:
            project_id (int): The ID of the GitLab project.
        
        Returns:
            gitlab.v4.objects.Project: The requested project instance.
        
        Raises:
            gitlab.exceptions.GitlabGetError: If the project is not found or
                                              the request fails.
        """
        return self.gl.projects.get(project_id)