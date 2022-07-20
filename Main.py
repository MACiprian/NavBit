import subprocess

path = r'D:\GitShit\NavBit'
tasks = ['AudioRecorder.py', 'ScreenRecorder.py', 'WebNavBot.py']
task_processes = [
    subprocess.Popen(r'python %s\%s' % (path, task), shell=True)
    for task
    in tasks
]
for task in task_processes:
    task.wait()
