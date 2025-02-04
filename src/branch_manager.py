class BranchManager:
    """Handles branch management operations in GitLab.

    This class provides methods to create and manage branches
    using a GitLab client.

    Attributes:
        client: An instance of the GitLab client used to interact
                with the GitLab API.
    """
    def __init__(self, gitlab_client):
        """Initializes the BranchManager with a GitLab client.

        Args:
            gitlab_client: A GitLab client instance to communicate with
                           the GitLab API.
        """
        self.client = gitlab_client

    def create_branch(self, project_id, branch_name, ref):
        """Creates a new branch in the specified GitLab project.
        
        Args:
            project_id (int): The ID of the GitLab project.
            branch_name (str): The name of the new branch.
            ref (str): The reference (commit SHA, branch, or tag)
                       from which the new branch will be created.

        Returns:
            None

        Raises:
            Exception: If branch creation fails.
        """
        project = self.client.get_project(project_id)
        project.branches.create({'branch': branch_name, 'ref': ref})