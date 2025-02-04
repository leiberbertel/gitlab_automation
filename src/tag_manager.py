class TagManager:
    """Handles tag management operations in GitLab.

    This class provides methods to create and manage tags using
    a GitLab client.

    Attributes:
        client (GitLabClient): An instance of GitLabClient used to interact
                               with the GitLab API.
    """

    def __init__(self, gitlab_client):
        """Initializes the TagManager with a GitLab client.

        Args:
            gitlab_client (GitLabClient): A GitLab client instance to interact
                                          with the GitLab API.
        """
        self.client = gitlab_client

    def create_tag(self, project_id, tag_name, ref, message=None):
        """Creates a new tag in the specified GitLab project.

        Args:
            project_id (int): The ID of the GitLab project.
            tag_name (str): The name of the new tag.
            ref (str): The reference (commit SHA, branch, or tag)
                       from which the new tag will be created.
            message (str, optional): A message associated with the tag.

        Returns:
            None

        Raises:
            gitlab.exceptions.GitlabCreateError: If the tag creation fails.
        """
        project = self.client.get_project(project_id)
        project.tags.create({'tag_name': tag_name, 'ref': ref, 'message': message})