import pytest
from unittest.mock import Mock, patch
from src.gitlab_client import GitLabClient

class TestGitLabClient:
    def setup_method(self):
        self.url = "https://gitlab.com"
        self.token = "test-token"
        self.client = GitLabClient(self.url, self.token)


    @patch('gitlab.Gitlab')
    def test_initialization(self, mock_gitlab):
        GitLabClient(self.url, self.token)
        mock_gitlab.assert_called_once_with(self.url, private_token=self.token)


    @patch('gitlab.Gitlab')
    def test_get_project(self, mock_gitlab):
        mock_project = Mock()
        mock_gitlab.return_value.projects.get.return_value = mock_project

        client = GitLabClient(self.url, self.token)

        project_id = 123
        result = client.get_project(project_id)

        mock_gitlab.return_value.projects.get.assert_called_once_with(project_id)
        assert result == mock_project


    @patch('gitlab.Gitlab')
    def test_get_project_not_found(self, mock_gitlab):
        mock_gitlab.return_value.projects.get.side_effect = Exception("Project Not Found")

        client = GitLabClient(self.url, self.token)

        with pytest.raises(Exception, match="Project Not Found"):
            client.get_project(999)