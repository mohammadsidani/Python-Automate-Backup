import os
import shutil
import datetime
import schedule
import time

source_dir = ""
backup_dir = ""

def copy_folder_to_dir(source, dest):
    today=datetime.date.today()
    backup_dir=os.path.join(dest,str(today))
    
    try:
        shutil.copytree(source, backup_dir)
        print("Folder copied successfully to: {backup_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")
        
schedule.every().day.at("00:00").do(lambda:
    copy_folder_to_dir(source_dir, backup_dir))

while True:
    schedule.run_pending()
    time.sleep(60)