import pytest
from unittest.mock import Mock, patch
from src.tag_manager import TagManager

class TestTagManager:
    def setup_method(self):
        self.mock_client = Mock()
        self.tag_manager = TagManager(self.mock_client)
        self.project_id = 123
        self.tag_name = "v1.0.0"
        self.ref = "main"
        self.message = "Test tag"


    def test_create_tag_success(self):
        mock_project = Mock()
        self.mock_client.get_project.return_value = mock_project
        mock_project.tags.create.return_value = Mock()

        self.tag_manager.create_tag(
            self.project_id,
            self.tag_name,
            self.ref,
            self.message
        )

        self.mock_client.get_project.assert_called_once_with(self.project_id)
        mock_project.tags.create.assert_called_once_with({
            'tag_name': self.tag_name,
            'ref': self.ref,
            'message': self.message
        })


    def test_create_tag_without_message(self):
        mock_project = Mock()
        self.mock_client.get_project.return_value = mock_project
        mock_project.tags.create.return_value = Mock()

        self.tag_manager.create_tag(self.project_id, self.tag_name, self.ref)

        mock_project.tags.create.assert_called_once_with({
            'tag_name': self.tag_name,
            'ref': self.ref,
            'message': None
        })


    def test_create_tag_project_not_found(self):
        self.mock_client.get_project.side_effect = Exception("Project Not Found")

        with pytest.raises(Exception, match="Project Not Found"):
            self.tag_manager.create_tag(self.project_id, self.tag_name, self.ref)


    def test_create_tag_already_exists(self):
        mock_project = Mock()
        self.mock_client.get_project.return_value = mock_project
        mock_project.tags.create.side_effect = Exception("Tag already exists")

        with pytest.raises(Exception, match="Tag already exists"):
            self.tag_manager.create_tag(self.project_id, self.tag_name, self.ref)