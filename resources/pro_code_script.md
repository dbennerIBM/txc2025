# Pro Code script

## Preable (~5 min)

In this demonstration I will show you the “Pro Code” features of watsonx Orchestrate. These Pro Code feature are for creating, testing, and deploying AI agents. The two main tools for Pro Code are:

- The Agent Development Kit
- The Developer Edition

The Agent Development Kit, also called the ADK, is a python based CLI tool that enables AI Engineers to work with supporting AI agent solutions on all the watsonx Orchestrate environments, including SaaS deployments on IBM Cloud and AWS, on premises deployments, and even a local environment on your own laptop called the Developer Edition.

**_The ADK is where new features will show up first. Then those features will show up in the SaaS UI environments and finally in the on premises environments. And control of some capabilities is only available via the ADK, for example adjusting the chunk size and overlap for the built-in RAG._**

Show this link in a browser tab:
https://developer.watson-orchestrate.ibm.com/

The Developer Edition is a local watsonx Orchestrate environment that developers can run on their own laptops. Here is where the documentation is for setting this up on YOUR laptop.

Show this link a browser tab.
https://developer.watson-orchestrate.ibm.com/developer_edition/wxOde_overview

## The demo narrative (~10 min)

Walk through the entire “to-be” demo end to end
I want to first show you the story of what the AI agent is doing for our manager.

Let’s imagine you are a manager. You will be using your AI agent to promote an employee to a new role in a new city.

Show the picture of the 7 steps - Here is the overview of what our manager will do with the agent

1.  Get a list of his daily work items. Pick the employee promotion task
2.  Adjust employee’s pay
3.  Update the employee’s work location
4.  Qualify the employee’s pay adjustment
5.  Look up guidelines on pay adjustments
6.  Close work item
7.  Notify employee via email that she has been promoted to a new role in a new city

Now let’s see the demo in action

Run the steps in sequence

## Introduction to the Pro Code tools (~20 min)

Let’s now switch to the Pro Code tools and see how we created this experience for the manager

Let’s start with the source control for the AI agent solution we are deploying
https://github.com/dbennerIBM/txc2025/tree/master/src

How is this different from using the UI or low code/no code interface? (What the other group is doing)

We are using yaml files to define agents. Let’s look at one now.

Have the UI of the agent builder up on one side of the screen and the yaml spec file on the other as you go through the yaml elements.

**_With IBM’s watsonx Orchestrate you have tooling to create agents and also a platform to run them in as well._**

Open the ManagerSupportAgent.yaml file on GitHub.

**_Notice that we are able to control every aspect of the agent via yaml definition._**

Walk through some of the yaml spec

**_We can do the same with other key elements of watsonx Orchestrate AI agent solutions_** like:

- Knowledge bases (for working with the built-in RAG vector db, Milvus)
- Tools (which are OpenAPI spec AND python based tools)

Now let’s examine what the AI Engineer’s experience would be using these tools locally on their own laptops.

Switch to the VS Code view of the txc2025 repository

I’ve setup a virtual python environment for this AI agent project

```test
source .venv/bin/activate
```

Now I can use the Agent Development Kit CLI commands to work with my watsonx Orchestrate environments.

```text
orchestrate env list
```

Now let’s say I’ve been developing some Agents and I want to test them out locally on my laptop before I deploy them to my SaaS environment

```text
orchestrate server start -e .env
```

This is now starting the local wxO server to test the AI Agents.

Use the bash or powershell script to explain how the ADK helps to automate and tie in with your organizations DevOps processes.

```text
./src/import.sh
```

And then we can see our work with

```text
orchestrate chat start
```

Show that the tools, knowledge base, and agent have loaded into the Developer Edition Chat UI (or SaaS environment)
