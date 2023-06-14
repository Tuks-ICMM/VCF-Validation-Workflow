# %%
from json import load
from os.path import abspath, dirname, join

with open(join("config", "config.json"), "r", encoding="UTF-8") as file_content:
    config = load(file_content)

PBS_Headers = [
    "#!/usr/bin/env bash",
    "#PBS -q long",
    "#PBS -l walltime=900:00:00",
    "#PBS -l nodes=1:ppn=2",
    "#PBS -N Snakemake",
]

PBS_Body = [
    "module load python-3.11.3",
    f"cd {dirname(abspath(__file__))};",
    f"source {dirname(abspath(__file__))}/venv/bin/activate",
    "snakemake --profile config/PBS-Torque-Profile --use-envmodules",
]

if "environment" in config:
    if "email" in config["environment"]:
        if "condition" in config["environment"]["email"]:
            EMAIL_CONDITIONS = "#PBS -k "
            for condition in config["environment"]["email"]["conditions"]:
                EMAIL_CONDITIONS += condition
            PBS_Headers.append(EMAIL_CONDITIONS)
        if "address" in config["environment"]["email"]:
            PBS_Headers.append("#PBS -M " + config["environment"]["email"]["address"])


with open("run.sh", "w", encoding="UTF-8") as file:
    file.writelines("\n".join(PBS_Headers + PBS_Body))

# %%
