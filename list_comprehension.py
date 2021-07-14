tenants_rent = {
	'Linda' : 1200,
	'Mike' : 1130,
	'Gina' : 2210,
	'Aldrin' : 2000,
	'Total_Rent' : 1200 + 1130 + 2210 + 2000,
	'Rent_Ledger': [1200, 1130, 2210, 2000],
	'Tenant_Names' : ['linda', 'mike', 'gina', 'aldrin']
}

print(tenants_rent['Total_Rent'])

#Iterate through the Rent Ledger for each Tenants rent per month: multiply by 12 months.
#Store the sum of the entire array in a variable.
one_year_rent = sum([i * 12 for i in tenants_rent['Rent_Ledger']])
print("Total cash for a year from rent: $" + str(one_year_rent))

#Iterate through the tenant name list in the tenants_rent dictionary.
#Capitalize each name of the tenant and store in a new list.
capitalized_names = [name.capitalize() for name in tenants_rent['Tenant_Names']]
print(capitalized_names)