conda create -n app_runner_env_temp python==3.10 -y
conda activate app_runner_env_temp
pip install -r requirements.txt
cd ..
pyinstaller --onefile app_runner.py
rmdir /s /q build
del /s /q app_runner.spec
conda deactivate
conda remove --name app_runner_env_temp --all -y