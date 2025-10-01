## wxO Pro Code Demo for TXC 2025

### Steps to install the demo on your laptop's Developer Edition

```text
orchestrate env activate local

orchestrate tools import -f src/tools/adjustPay.py -k python -r src/tools/requirements.txt

orchestrate tools import -f src/tools/getWorkItems.py -k python -r src/tools/requirements.txt

orchestrate tools import -f src/tools/updateWorkLocation.py -k python -r src/tools/requirements.txt

orchestrate agents import -f src/agents/managerSupportAgent.yaml
```

🚨 NOTE that you will need to update the PATH of the two files in the corporatepolicies.yaml file to match where they are located on your computer.

```text
orchestrate knowledge-bases import -f src/knowledge/corporatepolicies.yaml
```

### Steps to uninstall the demo on your laptop's Developer Edition

```text
orchestrate agents remove --name manager_support_agent -k native
```
