import pytest
from unittest.mock import Mock, patch
from src.branch_manager import BranchManager
class TestBranchManager:
    def setup_method(self):
        self.mock_client = Mock()
        self.branch_manager = BranchManager(self.mock_client)
        self.project_id = 123
        self.branch_name = "feature/test-branch"
        self.ref = "main"


    def test_create_branch_success(self):
        mock_project = Mock()
        self.mock_client.get_project.return_value = mock_project
        mock_project.branches.create.return_value = Mock()

        self.branch_manager.create_branch(self.project_id, self.branch_name, self.ref)

        self.mock_client.get_project.assert_called_once_with(self.project_id)
        mock_project.branches.create.assert_called_once_with({
            'branch': self.branch_name,
            'ref': self.ref
        })


    def test_create_branch_project_not_found(self):
        self.mock_client.get_project.side_effect = Exception("Project Not Found")

        with pytest.raises(Exception, match="Project Not Found"):
            self.branch_manager.create_branch(self.project_id, self.branch_name, self.ref)


    def test_create_branch_already_exists(self):
        mock_project = Mock()
        self.mock_client.get_project.return_value = mock_project
        mock_project.branches.create.side_effect = Exception("Branch already exists")

        with pytest.raises(Exception, match="Branch already exists"):
            self.branch_manager.create_branch(self.project_id, self.branch_name, self.ref)
