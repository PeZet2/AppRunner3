call conda create -n app_runner_env_temp python==3.10 -y
call conda activate app_runner_env_temp
call pip install -r requirements.txt
call pip install auto-py-to-exe
call cd ..
call pyinstaller --noconfirm --onefile --console --add-data "src/lib;lib/" src/app_runner.py 
call rmdir /s /q build
call del /s /q app_runner.spec
call conda deactivate
call conda remove --name app_runner_env_temp --all -y