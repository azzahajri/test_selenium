from selenium import webdriver

# Créer une nouvelle instance du navigateur Chrome
driver = webdriver.Chrome()

# Naviguer vers le site Web
driver.get("https://www.ma-calculatrice.fr/")

# Trouver le champ de saisie pour le premier nombre et saisir une valeur
first_number_input_element = driver.find_element("id", "cinq")
first_number_input_element.send_keys("5")

# Trouver le menu déroulant pour l'opération et cliquer sur l'option de soustraction
operation_dropdown_element = driver.find_element("id", "moins")
operation_dropdown_element.click()

# Trouver le champ de saisie pour le deuxième nombre et saisir une valeur
second_number_input_element = driver.find_element("id", "trois")
second_number_input_element.send_keys("3")



# Trouver le bouton pour effectuer le calcul et cliquer dessus
calculate_button_element = driver.find_element("id", "egale")
calculate_button_element.click()

# Trouver l'élément du résultat et vérifier qu'il affiche la bonne valeur
result_element = driver.find_element("id", "total")
expected_result = "2"  # Remplacez par le résultat attendu de la soustraction
assert result_element.text == expected_result

# Fermer le navigateur
driver.quit()
