## wxO Pro Code Demo for TXC 2025

### Steps to install the demo on your laptop's Developer Edition

🚨 NOTE that you will need to update the PATH of the two files in the `corporatepolicies.yaml` file to match where they are located on your computer.

existing path looks like this:

```text
/Users/danielbenner/IBM/python/txc2025/resources/relocation_policy_eligibility.md
```
change path so it is the FULL path to the file on your laptop.
```text
<full path>/txc2025/resources/relocation_policy_eligibility.md
```

Do the same for the other document return_to_the_office.md


You can test with this command to see if you got the paths correct. 
```text
orchestrate knowledge-bases import -f src/knowledge/corporatepolicies.yaml
```
### Now you can use the import script to load the demo

```text
insure you are in the txc2025 directory
pwd

orchestrate server start -e <.env path>

orchestrate env activate local

cd src

For bash shells
./import.sh

For powershells
import.ps1
```

