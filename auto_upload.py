import subprocess
from datetime import datetime

def auto_github_upload():
    try:
        # 1. Get the current date and time for a clean, automatic commit message
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-upload: {current_time}"
        
        print("🚀 Starting auto-upload to GitHub...")

        # 2. Run 'git add .' to stage all new and changed files
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Files staged (git add).")

        # 3. Run 'git commit' with our automated message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"✅ Changes committed: '{commit_message}'")

        # 4. Run 'git push' to send it to GitHub (assuming your branch is 'main')
        # Change "main" to "master" if your repository uses the older naming system
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🎉 Successfully uploaded to GitHub!")

    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred during the Git process: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the function
if __name__ == "__main__":
    auto_github_upload()