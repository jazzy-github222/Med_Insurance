# DISCLAIMERS!!!
# ----------------------------------------
# SEX = 0, then female
# SEX = 1, then male
# SMOKER = 0, then non-smoker
# SMOKER = 1, then smoker


# INITIAL INSURANCE PREMIUMS
# -----------------------------------------

# Create the initial variables below
age = 28
smoker = 0 
sex = 0 
num_of_children = 3
bmi = 26.2

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Print the statement
print("This person's insurance cost is $" + str(insurance_cost) + " dollars.")


# 4 YEARS LATER INSURANCE PREMIUMS (AGE FACTOR)
# --------------------------------------------

# Add 4 and keep counting age variable
age += 4

# Calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance 
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Write a print statement
print("The change in the cost of insurance after increasing the age by 4 years is $" + str(change_in_insurance_cost) + " dollars.")


# HIGHER BMI INSURANCE PREMIUMS (BMI FACTOR)
# -------------------------------------------

# Reset age to 28
age = 28

# Add 3.1 to the BMI and keep counting
bmi += 3.1

# Calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance 
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Write a print statement
print("The change in estimated insurance cost after increasing BMI by 3.1 is $" + str(change_in_insurance_cost) + " dollars.")


# INSURANCE PREMIUMS FOR MALE (SEX FACTOR)
# -----------------------------------------

# Reset BMI to original
bmi = 26.2

# Change the sex to a male
sex = 1

# Calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance 
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Write a print statement
print("The change in estimated cost for being a male instead of female is $" + str(change_in_insurance_cost) + " dollars.")


# INSURANCE PREMIUMS FOR SMOKER (SMOKER FACTOR)
# -----------------------------------------

# Keep smoker status as smoker
smoker = 1

# Calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance 
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Write a print statement
print("The change in estimated cost for being a smoker is $" + str(change_in_insurance_cost) + " dollars.")


# INSURANCE PREMIUMS FOR NON-SMOKER FAMILY (FAMILY FACTOR)
# --------------------------------------------------------

# Assign the number of children
num_of_children = 4

# Keep smoker status as non-smoker
smoker = 0

# Calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance 
change_in_insurance_cost = new_insurance_cost - insurance_cost

# Write a print statement
print("The change in estimated cost of 4 childrens comes to $" + str(change_in_insurance_cost) + " dollars.")