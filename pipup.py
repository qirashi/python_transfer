import subprocess as sbp
import json

for pkg in json.loads(sbp.run(["pip", "list", "-o", "--format=json"], capture_output=True, text=True).stdout):
    sbp.run(["pip", "install", "-U", pkg['name']])

sbp.run(["python", "-m", "pip", "install", "-U", "pip"])