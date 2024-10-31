import cobra


model = cobra.io.read_sbml_model("/home/lukasu/Desktop/24-WS-ComputationSystemsBiology/Exercise_1-01_eColiCore/e_coli_core.xml")

print(len(model.reactions))
print(len(model.metabolites))
print(len(model.genes))

# for i in range(0, len(model.reactions)):
#     print(model.reactions[i])

print(model.summary())
model.reactions.get_by_any(5)
