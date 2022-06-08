# Challenge 4
## Team 2 and the Fifth Element
aka we have an invisible friend
## Goal
The objective of this challenge is to pick up relationships between structural elements to describe which ones are supporting or are supported by which ones.
The input is a collection of IFC files to be collated in one project.
The output will consist in a graph that can answer to queries cross models and provide details on the construction elements and their structural relationships with each other, and in a collated IFC file that is enriched with the data contained in the generated ontology.
## Tool Features
The tool uses Python and Java scripts to open, collate and analyse the IFC files containing the structural elements, build the links between said elements, export them to a graph for queries and write back the enriched model into a new IFC file.
The tool uses the following existing libraries:
- [OpenCascade](https://dev.opencascade.org/)
- [IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
- [IFCtoRDF](https://github.com/pipauwel/IFCtoRDF)
- [IFCtoLBD](https://github.com/pipauwel/IFCtoLBD)

## Advantages over existing tools
The tool is only based on open source software and libraries. So no initial costs are required to test, familiarise with or deploy the tool, and plenty of documentation is available for the users.
The tool is light and simple, can be run on desktop or dockerised for cloud use.
The tool reads open formats and returns open formats.
The tool can be used as base for other routines or to inform decisions. Some examples of real world applications:
- Support to Structural Engineers: links between structural elements are not necessarily present in the chosen design software and this tool can extrapolate new information from an existing structural model to inform design decisions or further automated operations.
- Fault detections assessment: if a fault is detected (manually or via ML) in an existing building, the information can be transferred automatically to an Ifc element in the BIM model and all the structural elements connected to the damaged one can be queried and identified for further inspection.
- Count and analysis of typical joints: an accurate assessment of the most common joints between instances of classes of structural elements can simplify the design of the structural joints, leading to reduced fees and human errors in the design and the construction phase.
## Usage

## Next steps

## Team
