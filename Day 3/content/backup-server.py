import shutil
import datetime
import os
# import schedule

SOURCE_PATH = os.environ.get("SOURCE_PATH")
DESTINATION_PATH = os.environ.get("DESTINATION_PATH")

def create_backup(source_path, destination_path):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = os.path.join(destination_path, f"backup_{date_time}")
    try:
        shutil.make_archive(backup_name, 'gztar', source_path)
        print(f"Backup created at {backup_name}.tar.gz")
    except Exception as e: 
        print(f"Backup failed: {e}")

source_path = SOURCE_PATH
destination_path = DESTINATION_PATH

# schedule.every(1).day.at("00:00").do(lambda: create_backup(source_path, destination_path))
create_backup(source_path, destination_path)