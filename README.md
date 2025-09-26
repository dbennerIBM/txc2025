## wxO Pro Code Demo for TXC 2025

### Steps to install the demo on your laptop's Developer Edition

```text
orchestrate env activate local

orchestrate tools import -f src/tools/adjustPay.py -k python -r src/tools/requirements.txt

orchestrate tools import -f src/tools/getWorkItems.py -k python -r src/tools/requirements.txt

orchestrate tools import -f src/tools/updateWorkLocation.py -k python -r src/tools/requirements.txt

orchestrate agents import -f src/agents/managerSupportAgent.yaml

orchestrate knowledge-bases import -f src/knowledge/corporatepolicies.yaml

```
