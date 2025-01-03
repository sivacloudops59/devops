
pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        GITHUB_TOKEN = credentials('github-token') // Store the GitHub token in Jenkins credentials
        REPO_NAME = 'example-repo'
        BRANCH_NAME = 'main'
        OWNER = 'sivacloudops59'
    }
    stages {
        stage('Create Repository') {
            steps {
                script {
                    def repoPayload = """
                    {
                        "name": "${REPO_NAME}",
                        "private": true,
                        "description": "Repository created by Jenkins"
                    }
                    """
                    sh """
                    curl -X POST \
                        -H "Authorization: token ${GITHUB_TOKEN}" \
                        -H "Content-Type: application/json" \
                        -d '${repoPayload}' \
                        ${GITHUB_API_URL}/user/repos
                    """
                }
            }
        }
        stage('Create Branch') {
            steps {
                script {
                    sh """
                    git clone https://github.com/${OWNER}/${REPO_NAME}.git
                    cd ${REPO_NAME}
                    git checkout -b ${BRANCH_NAME}
                    git push origin ${BRANCH_NAME}
                    """
                }
            }
        }
        stage('Protect Branch') {
            steps {
                script {
                    def protectionPayload = """
                    {
                        "required_status_checks": {
                            "strict": true,
                            "contexts": []
                        },
                        "enforce_admins": true,
                        "required_pull_request_reviews": {
                            "dismiss_stale_reviews": true,
                            "require_code_owner_reviews": true
                        },
                        "restrictions": null
                    }
                    """
                    sh """
                    curl -X PUT \
                        -H "Authorization: token ${GITHUB_TOKEN}" \
                        -H "Content-Type: application/json" \
                        -d '${protectionPayload}' \
                        ${GITHUB_API_URL}/repos/${OWNER}/${REPO_NAME}/branches/${BRANCH_NAME}/protection
                    """
                }
            }
        }
    }
    post {
        success {
            echo "Repository, branch, and branch protection successfully created."
        }
        failure {
            echo "Failed to set up GitHub repository or branch protection."
        }
    }
}
