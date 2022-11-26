#!/bin/bash

#SBATCH --time=24:00:00
#SBATCH --job-name=Road_Damage_Detection
#SBATCH --output=Road_Damage_Detection.out
#SBATCH --error=Road_Damage_Detection.err
#SBATCH --partition=CPUQ
#SBATCH --gres=gpu:1
#SBATCH --constraint=V100
#SBATCH --account=iv-imt
#SBATCH --nodes=1
#SBATCH --mail-user=mdaaz@stud.ntnu.no

python yolov5/train.py --data yolov5/data/road.yaml --cfg yolov5/models/yolov5x_road.yaml --weights runs/exp4/weights/last.pt --batch-size 16 --epochs 100
