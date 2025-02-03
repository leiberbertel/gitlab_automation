import os
from dotenv import load_dotenv
from src.gitlab_client import GitLabClient
from src.branch_manager import BranchManager
from src.tag_manager import TagManager


def load_config():
    load_dotenv()

    required_vars = ['GITLAB_URL', 'GITLAB_PRIVATE_TOKEN', 'GITLAB_PROJECT_ID']
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        raise ValueError(f"The following environment variables are missing: {', '.join(missing_vars)}")

    return {
        'gitlab_url': os.getenv('GITLAB_URL'),
        'private_token': os.getenv('GITLAB_PRIVATE_TOKEN'),
        'project_id': os.getenv('GITLAB_PROJECT_ID')
    }


def main():
    new_branch_name = 'feature/example'
    base_branch = 'main'
    new_tag_name = 'v1.0.0'
    message = ''

    try:
        config = load_config()
        client = GitLabClient(config['gitlab_url'], config['private_token'])

        branch_manager = BranchManager(client)
        tag_manager = TagManager(client)

        project_id = config['project_id']
        branch_manager.create_branch(project_id, new_branch_name, base_branch)
        tag_manager.create_tag(project_id, new_tag_name, base_branch, message)

    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()