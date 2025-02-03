# GitLab Automation Tool

Automation tool for GitLab that allows the programmatic creation of branches and tags using the GitLab API.

## 🚀 Features

- Automatic branch creation
- Tag management with customized messages
- Secure handling of credentials through environment variables
- Modular and easily extensible structure

## 📋 Prerequisites

- Python 3.8 or higher
- GitLab access token with sufficient permissions
- GitLab project ID

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/leiberbertel/gitlab_automation
cd gitlab-automation
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Set the environment variables:
   - Copy the `.env.example` file to `.env`.
   - Edit `.env` with your actual values.

```bash
cp .env.example .env
```

## ⚙️ Configuration

Be sure to set the following environment variables in your `.env` file:

```plaintext
GITLAB_URL=https://gitlab.com
GITLAB_PRIVATE_TOKEN=your-token-private
GITLAB_PROJECT_ID=your-project-id
```

You can also set these variables directly on your system:

```bash
export GITLAB_URL=https://gitlab.com
export GITLAB_PRIVATE_TOKEN=your-token-private
export GITLAB_PROJECT_ID=your-project-id
```

## 🖥️ Usage

### Run the main script

```bash
python main.py
```

### Use the classes in your own code

```python
from src.gitlab_client import GitLabClient
from src.branch_manager import BranchManager
from src.tag_manager import TagManager

# Initialize the client
client = GitLabClient(gitlab_url, private_token)

# Create a branch
branch_manager = BranchManager(client)
branch_manager.create_branch(project_id, 'feature/new-feature', 'main')

# Create a tag
tag_manager = TagManager(client)
tag_manager.create_tag(project_id, 'v1.0.0', 'main', 'First stable version')
```

## 🧪 Tests

To run the tests:

```bash
pytest
```

## 📁 Project Structure

```
gitlab-automation/
│
├── src/
│   ├── __init__.py
│   ├── gitlab_client.py      # Client for interacting with the GitLab API
│   ├── branch_manager.py     # Logic for branch management
│   └── tag_manager.py        # Logic for tag management
│
├── tests/
│   ├── __init__.py
│   ├── test_gitlab_client.py
│   ├── test_branch_manager.py
│   └── test_tag_manager.py
│
├── .env.example             # Example of environment variables
├── requirements.txt         # Project units
└── main.py                  # Main entry point
```

## 🤝 Contribute

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is under the MIT License - see the file [LICENSE.md](LICENSE.md) for details.

## ✨ Author

Leiber Bertel - [@leiberbertel](https://github.com/leiberbertel)

## 🙏 Acknowledgments

- [python-gitlab](https://python-gitlab.readthedocs.io/) for providing an excellent library for interacting with GitLab
- [python-dotenv](https://github.com/theskumar/python-dotenv) by the handling of environment variables

## 📚 References

- [GitLab API Documentation](https://docs.gitlab.com/ee/api/)
- [Guide to python-gitlab](https://python-gitlab.readthedocs.io/en/stable/)