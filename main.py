import os
import argparse

a = os.popen("aws s3 ls s3://adhoc-sanchit/sampling_strategy/training_data_half_yolov5x/ --recursive").read()
with open("./list.txt", "w") as f:
    for i in a:
        f.write(a + "\n")

def walk_s3(s3_path):
    a = os.popen("aws s3 ls " + s3_path + " --recursive").read()
    return a

def walk_local(local_path):
    local_path_files_list = []
    for root, dirs, files in os.walk(local_path):
        for file in files:
            local_path_files_list.append(os.path.join(root, file))
    return local_path_files_list

def upload(from_path, to_path):
    
if __name__ = "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--from_path", type=str, default="s3://adhoc-sanchit/sampling_strategy/training_data_half_yolov5x/")
    parser.add_argument("--to_path", type=str, default="/home/ubuntu/data/")
    
    args = parser.parse_args()
    
    download = False
    upload = False
    if "s3://" in args.from_path:
        download = True
        files = walk_s3(args.from_path)
    
    if "s3://" in args.to_path:
        upload = True
        files = walk_local(args.from_path)
    
    
